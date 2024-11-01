"""
This file includes Prompt Engineering Tests for evaluting the method 
of prompting and system prompt to use for generating cover letters. 
The output of the generated test files are located in the 
cv_test_output folder.
"""

from backend.app import app
import ollama_connect
from unittest.main import main
import bcrypt
from bson import ObjectId
from flask import app
import unittest
import sys
import os
import inspect
import json

from pymongo import MongoClient

currentdir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
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


def cv_test(self, prompt_file, resume_file, job_file, example_files=[]):
    """
    Master template for Cover Letter Prompt Engineering Tests.

    Takes the prompt, resume, job description, and example files if provided, 
    reads in the content from the files in the sample_data file, and runs the 
    given test. The output is in the cv_test_output folder.
    """
    # Set up the flask client
    tester = app.test_client(self)
    email = "dhrumilshah1234@gmail.com"
    urlToSend = f"/generate_cv"

    # Read in the sample data files
    prompt_path = os.path.join("sample_data", "system_prompts", prompt_file)
    system_prompt = import_file(prompt_path)
    resume_path = os.path.join("sample_data", "sample_resumes", resume_file)
    resume = import_file(resume_path)
    job_desc_path = os.path.join(
        "sample_data", "sample_job_descriptions", job_file)
    job_desc = import_file(job_desc_path)

    # Adjust the System Prompt and Example Files
    ollama_connect.system_prompt_cv = system_prompt
    ollama_connect.example_files.clear()
    example_files_content = []
    for example in example_files:
        example_path = os.path.join(
            "sample_data", "sample_cover_letters", example)
        example_content = import_file(example_path)
        example_files_content.append(example_content)
    ollama_connect.example_files = example_files_content
    filename = prompt_file[:-4] + "_" + \
        resume_file[:-4] + "_" + job_file[:-4] + ".txt"

    # Send the request
    req = {
        "email": email,
        "resume": resume,
        "job_desc": job_desc
    }
    response = tester.post(urlToSend, json=req)
    statuscode = response.status_code
    self.assertEqual(statuscode, 200)

    # Print the results to a file with the name of the test
    response_json = json.loads(response.data)
    cover_letter = response_json['letter']
    output_path = os.path.join("cv_test_output", filename)
    if not os.path.exists(os.path.join("cv_test_output")):
        os.mkdir(os.path.join("cv_test_output"))
    export_file(output_path, cover_letter)


# File to use for the One Shot Prompt Engineering Tests
one_shot_examples = ["entry_level_software_engineer.txt"]

# Files to use for the Few Shot Prompt Engineering Tests
few_shot_examples = [
    "entry_level_software_engineer.txt",
    "experienced_software_engineer.txt",
    "junior_software_engineer.txt"
]


class FlaskTest(unittest.TestCase):
    def test_zero_shot_Charles_Lenovo(self):
        cv_test(self, "cv_zero_shot.txt",
                "charles_mcturland.txt", "lenovo.txt")

    def test_zero_shot_Cynthia_Fidelity(self):
        cv_test(self, "cv_zero_shot.txt", "cynthia_dwayne.txt", "fidelity.txt")

    def test_zero_shot_Ava_RedHat(self):
        cv_test(self, "cv_zero_shot.txt", "ava_johnson.txt", "redhat.txt")

    def test_zero_shot_Charles_EpicGames(self):
        cv_test(self, "cv_zero_shot.txt",
                "charles_mcturland.txt", "epicgames.txt")

    def test_zero_shot_Ava_Apple(self):
        cv_test(self, "cv_zero_shot.txt", "ava_johnson.txt", "apple.txt")

    def test_one_shot_Charles_Lenovo(self):
        cv_test(self, "cv_one_shot.txt", "charles_mcturland.txt",
                "lenovo.txt", one_shot_examples)

    def test_one_shot_Cynthia_Fidelity(self):
        cv_test(self, "cv_one_shot.txt", "cynthia_dwayne.txt",
                "fidelity.txt", one_shot_examples)

    def test_one_shot_Ava_RedHat(self):
        cv_test(self, "cv_one_shot.txt", "ava_johnson.txt",
                "redhat.txt", one_shot_examples)

    def test_one_shot_Charles_EpicGames(self):
        cv_test(self, "cv_one_shot.txt", "charles_mcturland.txt",
                "epicgames.txt", one_shot_examples)

    def test_one_shot_Ava_Apple(self):
        cv_test(self, "cv_one_shot.txt", "ava_johnson.txt",
                "apple.txt", one_shot_examples)

    def test_one_shot_long_Charles_Lenovo(self):
        cv_test(self, "cv_one_shot_long.txt", "charles_mcturland.txt",
                "lenovo.txt", one_shot_examples)

    def test_one_shot_long_Cynthia_Fidelity(self):
        cv_test(self, "cv_one_shot_long.txt", "cynthia_dwayne.txt",
                "fidelity.txt", one_shot_examples)

    def test_one_shot_long_Ava_RedHat(self):
        cv_test(self, "cv_one_shot_long.txt", "ava_johnson.txt",
                "redhat.txt", one_shot_examples)

    def test_one_shot_long_Charles_EpicGames(self):
        cv_test(self, "cv_one_shot_long.txt", "charles_mcturland.txt",
                "epicgames.txt", one_shot_examples)

    def test_one_shot_long_Ava_Apple(self):
        cv_test(self, "cv_one_shot_long.txt", "ava_johnson.txt",
                "apple.txt", one_shot_examples)

    def test_few_shot_Charles_Lenovo(self):
        cv_test(self, "cv_few_shot.txt", "charles_mcturland.txt",
                "lenovo.txt", few_shot_examples)

    def test_few_shot_Cynthia_Fidelity(self):
        cv_test(self, "cv_few_shot.txt", "cynthia_dwayne.txt",
                "fidelity.txt", few_shot_examples)

    def test_few_shot_Ava_RedHat(self):
        cv_test(self, "cv_few_shot.txt", "ava_johnson.txt",
                "redhat.txt", few_shot_examples)

    def test_few_shot_Charles_EpicGames(self):
        cv_test(self, "cv_few_shot.txt", "charles_mcturland.txt",
                "epicgames.txt", few_shot_examples)

    def test_few_shot_Ava_Apple(self):
        cv_test(self, "cv_few_shot.txt", "ava_johnson.txt",
                "apple.txt", few_shot_examples)


if __name__ == "__main__":
    unittest.main()
