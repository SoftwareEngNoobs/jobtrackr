from unittest.main import main
import os, json
import ollama_connect
import unittest

def import_file(path):
    with open(path, 'r') as f:
        file_content = f.read()
    return file_content

def export_file(path, content):
    with open(path, 'w') as f:
        f.write(content)

def cv_test(prompt_file, resume_file, job_file, example_files = []):
    prompt_path = os.path.join("sample_data", "system_prompts", prompt_file)
    system_prompt = import_file(prompt_path)
    resume_path = os.path.join("sample_data", "sample_resumes", resume_file)
    resume = import_file(resume_path)
    job_desc_path = os.path.join("sample_data", "sample_job_descriptions", job_file)
    job_desc = import_file(job_desc_path)

    ollama_connect.system_prompt = system_prompt
    ollama_connect.example_files.clear()
    example_files_content = []
    for example in example_files:
        example_path = os.path.join("sample_data", "sample_cover_letters", example)
        example_content = import_file(example_path)
        example_files_content.append(example_content)
    ollama_connect.example_files = example_files_content
    try:
        response = ollama_connect.generate_cv(resume, job_desc)
        response_json = json.loads(response)
        cover_letter = response_json['letter']
        filename = prompt_file[:-4] + "_" + resume_file[:-4] + "_" + job_file[:-4] + ".txt"
        output_path = os.path.join("cv_test_output", filename)
        export_file(output_path, cover_letter)
    except Exception:
        assert False, "Failed test: " + filename

one_shot_examples = ["entry_level_software_engineer.txt"]
few_shot_examples = [
    "entry_level_software_engineer.txt", 
    "experienced_software_engineer.txt", 
    "junior_software_engineer.txt"
]

class FlaskTest(unittest.TestCase):

    def test_zero_shot_Charles_Lenovo(self):
        cv_test("cv_zero_shot.txt", "charles_mcturland.txt", "lenovo.txt")

    def test_zero_shot_Cynthia_Fidelity(self):
        cv_test("cv_zero_shot.txt", "cynthia_dwayne.txt", "fidelity.txt")
    
    def test_zero_shot_Ava_RedHat(self):
        cv_test("cv_zero_shot.txt", "ava_johnson.txt", "redhat.txt")
    
    def test_zero_shot_Charles_EpicGames(self):
        cv_test("cv_zero_shot.txt", "charles_mcturland.txt", "epicgames.txt")
    
    def test_zero_shot_Ava_Apple(self):
        cv_test("cv_zero_shot.txt", "ava_johnson.txt", "apple.txt")
    
    def test_one_shot_Charles_Lenovo(self):
        cv_test("cv_one_shot.txt", "charles_mcturland.txt", "lenovo.txt", one_shot_examples)
    
    def test_one_shot_Cynthia_Fidelity(self):
        cv_test("cv_one_shot.txt", "cynthia_dwayne.txt", "fidelity.txt", one_shot_examples)
    
    def test_one_shot_Ava_RedHat(self):
        cv_test("cv_one_shot.txt", "ava_johnson.txt", "redhat.txt", one_shot_examples)
    
    def test_one_shot_Charles_EpicGames(self):
        cv_test("cv_one_shot.txt", "charles_mcturland.txt", "epicgames.txt", one_shot_examples)
    
    def test_one_shot_Ava_Apple(self):
        cv_test("cv_one_shot.txt", "ava_johnson.txt", "apple.txt", one_shot_examples)
    
    def test_one_shot_long_Charles_Lenovo(self):
        cv_test("cv_one_shot_long.txt", "charles_mcturland.txt", "lenovo.txt", one_shot_examples)
    
    def test_one_shot_long_Cynthia_Fidelity(self):
        cv_test("cv_one_shot_long.txt", "cynthia_dwayne.txt", "fidelity.txt", one_shot_examples)
    
    def test_one_shot_long_Ava_RedHat(self):
        cv_test("cv_one_shot_long.txt", "ava_johnson.txt", "redhat.txt", one_shot_examples)
    
    def test_one_shot_long_Charles_EpicGames(self):
        cv_test("cv_one_shot_long.txt", "charles_mcturland.txt", "epicgames.txt", one_shot_examples)
    
    def test_one_shot_long_Ava_Apple(self):
        cv_test("cv_one_shot_long.txt", "ava_johnson.txt", "apple.txt", one_shot_examples)
    
    def test_few_shot_Charles_Lenovo(self):
        cv_test("cv_few_shot.txt", "charles_mcturland.txt", "lenovo.txt", few_shot_examples)
    
    def test_few_shot_Cynthia_Fidelity(self):
        cv_test("cv_few_shot.txt", "cynthia_dwayne.txt", "fidelity.txt", few_shot_examples)
    
    def test_few_shot_Ava_RedHat(self):
        cv_test("cv_few_shot.txt", "ava_johnson.txt", "redhat.txt", few_shot_examples)
    
    def test_few_shot_Charles_EpicGames(self):
        cv_test("cv_few_shot.txt", "charles_mcturland.txt", "epicgames.txt", few_shot_examples)
    
    def test_few_shot_Ava_Apple(self):
        cv_test("cv_few_shot.txt", "ava_johnson.txt", "apple.txt", few_shot_examples)
    
if __name__=="__main__":
    unittest.main()
