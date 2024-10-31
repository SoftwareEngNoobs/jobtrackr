import ollama_connect
from unittest.main import main
import bcrypt
from bson import ObjectId
from flask import app
import unittest
import sys, os, inspect
import json

from pymongo import MongoClient

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from backend.app import app
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

def import_file(path):
    with open(path, mode='r', encoding='utf-8') as f:
        file_content = f.read()
    return file_content

def export_file(path, content):
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(content)

def suggestions_test(self, prompt_file, resume_file, job_file, example_files = []):
    # Set up the flask client
    tester = app.test_client(self)
    email = "dhrumilshah1234@gmail.com"
    urlToSend = f"/suggestions"
    
    # Read in the sample data files
    prompt_path = os.path.join("sample_data", "system_prompts", prompt_file)
    system_prompt = import_file(prompt_path)
    resume_path = os.path.join("sample_data", "sample_resumes", resume_file)
    resume = import_file(resume_path)
    job_desc_path = os.path.join("sample_data", "sample_job_descriptions", job_file)
    job_desc = import_file(job_desc_path)

    # Adjust the System Prompt and Example Files
    ollama_connect.system_prompt_cv = system_prompt
    ollama_connect.example_files.clear()
    example_files_content = []
    for example in example_files:
        example_path = os.path.join("sample_data", "sample_cover_letters", example)
        example_content = import_file(example_path)
        example_files_content.append(example_content)
    ollama_connect.example_files = example_files_content
    filename = prompt_file[:-4] + "_" + resume_file[:-4] + "_" + job_file[:-4] + ".txt"
    
    # Send the request
    req = {
        "email": email,
        "resume": resume,
        "job_desc": job_desc
    }
    response = tester.post(urlToSend, json = req)
    statuscode = response.status_code
    self.assertEqual(statuscode, 200)

    # Print the results to a file with the name of the test
    response_json = json.loads(response.data)
    cover_letter = response_json['suggestions']
    output_path = os.path.join("cv_test_output", filename)
    export_file(output_path, cover_letter)


# one_shot_examples = ["entry_level_software_engineer.txt"]
# few_shot_examples = [
#     "entry_level_software_engineer.txt", 
#     "experienced_software_engineer.txt", 
#     "junior_software_engineer.txt"
# ]

class FlaskTest(unittest.TestCase):
    def test_zero_shot_Charles_Lenovo(self):
        suggestions_test(self, )