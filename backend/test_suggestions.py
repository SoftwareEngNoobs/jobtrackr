"""
This file contains Prompt Engineering tests for evaluating possible 
system prompts and methods of prompt engineering for providing resume 
suggestions. The test output files are located in the 
suggestions_test_output folder.
"""

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
    """
    Imports and returns the text content from a file at the given path.
    """
    with open(path, mode='r', encoding='utf-8') as f:
        file_content = f.read()
    return file_content

def export_file(path, content):
    """
    Creates and exports the provided content into the file at the given path.
    """
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(content)

def suggestions_test(self, prompt_file, resume_file, job_file, example_files = []):
    """
    Master template for Resume Suggestion Prompt Engineering Tests.
    
    Takes the prompt, resume, job description, and example files if provided, 
    reads in the content from the files in the sample_data file, and runs the 
    given test. The output is in the suggestions_test_output folder.
    """
    # Set up the flask client
    tester = app.test_client(self)
    email = "dhrumilshah1234@gmail.com"
    urlToSend = f"/resume_suggest"
    
    # Read in the sample data files
    prompt_path = os.path.join("sample_data", "system_prompts", prompt_file)
    system_prompt = import_file(prompt_path)
    resume_path = os.path.join("sample_data", "sample_resumes", resume_file)
    resume = import_file(resume_path)
    job_desc_path = os.path.join("sample_data", "sample_job_descriptions", job_file)
    job_desc = import_file(job_desc_path)

    # Adjust the System Prompt and Example Files
    ollama_connect.system_prompt_suggest = system_prompt
    ollama_connect.example_files.clear()
    example_files_content = []
    for example in example_files:
        example_path = os.path.join("sample_data", "sample_resume_suggestions", example)
        example_content = import_file(example_path)
        example_files_content.append(example_content)
    ollama_connect.example_files_suggest = example_files_content
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
    suggestions = response_json['suggestions']
    output_path = os.path.join("suggestions_test_output", filename)
    if not os.path.exists(os.path.join("suggestions_test_output")):
        os.mkdir(os.path.join("suggestions_test_output"))
    export_file(output_path, suggestions)

# File to use for the One Shot Prompt Engineering Tests
one_shot_examples = ["resume_suggestion.txt"]

class FlaskTest(unittest.TestCase):
   
    def test_zero_shot_Cynthia_Lenovo(self):
        suggestions_test(self, "suggestion_zero_shot.txt", "cynthia_dwayne.txt", "lenovo.txt")

    def test_zero_shot_Ava_EpicGames(self):
        suggestions_test(self, "suggestion_zero_shot.txt", "ava_johnson.txt", "epicgames.txt")

    def test_zero_shot_Charles_Fidelity(self):
        suggestions_test(self, "suggestion_zero_shot.txt", "charles_mcturland.txt", "fidelity.txt")

    def test_zero_shot_Cynthia_RedHat(self):
         suggestions_test(self, "suggestion_zero_shot.txt", "cynthia_dwayne.txt", "redhat.txt")

    def test_zero_shot_Charles_Apple(self):
        suggestions_test(self, "suggestion_zero_shot.txt", "charles_mcturland.txt", "apple.txt")

    def test_one_shot_Cynthia_Lenovo(self):
        suggestions_test(self, "suggestion_one_shot.txt", "cynthia_dwayne.txt", "lenovo.txt", one_shot_examples)

    def test_one_shot_Ava_EpicGames(self):
        suggestions_test(self, "suggestion_one_shot.txt", "ava_johnson.txt", "epicgames.txt", one_shot_examples)

    def test_one_shot_Charles_Fidelity(self):
        suggestions_test(self, "suggestion_one_shot.txt", "charles_mcturland.txt", "fidelity.txt", one_shot_examples)

    def test_one_shot_Cynthia_RedHat(self):
         suggestions_test(self, "suggestion_one_shot.txt", "cynthia_dwayne.txt", "redhat.txt", one_shot_examples)

    def test_one_shot_Charles_Apple(self):
        suggestions_test(self, "suggestion_one_shot.txt", "charles_mcturland.txt", "apple.txt", one_shot_examples)

    def test_one_shot_long_Cynthia_Lenovo(self):
        suggestions_test(self, "suggestion_one_shot_long.txt", "cynthia_dwayne.txt", "lenovo.txt", one_shot_examples)

    def test_one_shot_long_Ava_EpicGames(self):
        suggestions_test(self, "suggestion_one_shot_long.txt", "ava_johnson.txt", "epicgames.txt", one_shot_examples)

    def test_one_shot_long_Charles_Fidelity(self):
        suggestions_test(self, "suggestion_one_shot_long.txt", "charles_mcturland.txt", "fidelity.txt", one_shot_examples)

    def test_one_shot_long_Cynthia_RedHat(self):
         suggestions_test(self, "suggestion_one_shot_long.txt", "cynthia_dwayne.txt", "redhat.txt", one_shot_examples)

    def test_one_shot_long_Charles_Apple(self):
        suggestions_test(self, "suggestion_one_shot_long.txt", "charles_mcturland.txt", "apple.txt", one_shot_examples)

if __name__=="__main__":
    unittest.main()
