"""
This is the main file for the backend. This is the file that is run
when starting up the backend for JobTrackr. It contains all the API
routes for the application.
"""

from flask import Flask, jsonify, request, after_this_request
from pymongo import MongoClient
from flask_cors import CORS
import auth
import applications
import questions
import files
import ollama_connect
import jd_scraper_workday
import os
import time
from files import get_pdf_info
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('APP_SECRET_KEY', "")
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

db1 = os.getenv('MONGO_DB_CONNECTION', "mongodb://localhost:27017/")
db2 = "?retryWrites=true&w=majority"
db = db1 + db2
client = MongoClient(db, tlsAllowInvalidCertificates=True)
db = client.get_database(os.getenv('DATABASE_TYPE', "development"))
UserRecords = db.register
Applications = db.Applications
UserProfiles = db.Profiles
Questions = db.QA
Files = db.file


@app.route("/")
def hello():
    '''
    ```
    Welcome Page
    ```
    '''

    return "Hello, Track your job on :3000"


@app.route("/register", methods=["post"])
def register():
    '''
    ```
    Register if you do not already have an account
    ```
    '''

    return auth.register(UserRecords)


@app.route("/login", methods=["POST"])
def login():
    '''
    ```
    Login to get to the dashboard to access various functions
    ```
    '''

    return auth.login(UserRecords)


@app.route("/logout", methods=["POST", "GET"])
def logout():
    '''
    ```
    Log out of your account
    ```
    '''

    return auth.logout()


@app.route("/view_applications", methods=["GET"])
def view_applications():
    '''
    ```
    View applications associated with the selected email ID
    ```
    '''

    return applications.view_applications(Applications)


@app.route("/view_questions", methods=["GET"])
def view_questions():
    '''
    ```
    View questions associated with the selected email ID
    ```
    '''

    return questions.view_questions(Questions)


@app.route("/add_application", methods=["POST"])
def add_application():
    '''
    ```
    Add application to an account with selected email ID.
    ```
    '''

    return applications.add_application(Applications)


@app.route("/add_question", methods=["POST"])
def add_question():
    '''
    ```
    Add question to a profile with selected email ID.
    ```
    '''

    return questions.add_question(Questions)


@app.route("/delete_application", methods=["POST"])
def delete_application():
    '''
    ```
    Delete application associated with selected email.
    ```
    '''

    return applications.delete_application(Applications)


@app.route("/delete_question", methods=["POST"])
def delete_question():
    '''
    ```
    Delete question to a profile with selected email.
    ```
    '''

    return questions.delete_question(Questions)


@app.route("/modify_application", methods=["POST"])
def modify_application():
    '''
    ```
    Modify application.
    ```
    '''

    return applications.modify_application(Applications)


@app.route("/modify_question", methods=["POST"])
def modify_question():
    '''
    ```
    Modify question to a profile with selected email ID.
    ```
    '''

    return questions.modify_question(Questions)


@app.route("/create_profile", methods=["post"])
def create_profile():
    '''
    ```
    Creating profile
    ```
    '''

    return auth.create_profile(UserProfiles)


@app.route("/view_profile", methods=["GET"])
def view_profile():
    '''
    ```
    View profile
    ```
    '''

    return auth.view_profile(UserProfiles)


@app.route("/modify_profile", methods=["POST"])
def modify_profile():
    '''
    ```
    Modify profile
    ```
    '''

    return auth.modify_profile(UserProfiles)


@app.route("/clear_profile", methods=["POST"])
def clear_profile():
    '''
    ```
    View profile
    ```
    '''

    return auth.clear_profile(UserProfiles, UserRecords)


@app.route("/upload_file", methods=["GET", "POST"])
def upload_file():
    '''
    ```
    Uploads file to Amazon S3 bucket
    ```
    '''

    return files.upload_file(UserRecords, Files)


@app.route("/view_files", methods=["GET"])
def view_files():
    '''
    ```
    View your files directly from cloud
    ```
    '''

    return files.view_files(Files)


@app.route("/download_file", methods=["POST"])
def download_file():
    '''
    ```
    View your files directly from cloud
    ```
    '''
    return files.download_file(Files)


@app.route("/delete_file", methods=["POST"])
def delete_file():
    '''
    ```
    Delete one's files from cloud storage
    ```
    '''

    return files.delete_file(Files)


@app.route("/generate_cv", methods=["POST"])
def generate_cv():
    '''
    ```
    Generates a Cover Letter from a resume and job description
    ```
    '''
    req = request.get_json()
    resume = (
        get_pdf_info(req["file"], Files, req["email"])
        if "file" in req and len(req["file"]) > 0
        else ""
    )
    if resume == "":
        resume = (
            req["resume"]
            if "resume" in req and len(req["resume"]) > 0
            else ""
        )
    job_desc = req["job_desc"] if "job_desc" in req.keys() else ""
    context = (
        req["context"]
        if "context" in req.keys() and len(req["context"]) > 0
        else ""
    )

    return ollama_connect.generate_cv(resume, job_desc, context)


@app.route("/resume_suggest", methods=["POST"])
def resume_suggest():
    '''
    ```
    Provides suggestions for a resume to tailor it to a job description
    ```
    '''
    req = request.get_json()
    resume = (
        get_pdf_info(req["file"], Files, req["email"])
        if "file" in req and len(req["file"]) > 0
        else ""
    )
    job_desc = req["job_desc"] if "job_desc" in req.keys() else ""
    return ollama_connect.resume_suggest(resume, job_desc)

@app.route('/get_job_description', methods=['POST'])
def get_job_description():
    data = request.json
    job_url = data.get('url', '')
    if not job_url:
        return jsonify({"error": "URL parameter is required"}), 400
    try:
        description = jd_scraper_workday.get_job_description(job_url)
        return jsonify({"description": description})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
