"""
This file handles the functionality for generating cover letters 
and providing resume suggestions using Ollama. The system prompts used 
for each of these tasks are at the top of the file using the 
system_prompt_cv and system_prompt_suggest variables. 

The model being used by Ollama can be changed by adjusting the model 
variable in the ChatOllama instantion of the llm variable at the top 
of the file.
"""

from flask import request, jsonify
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
)

system_prompt_cv = """
You are a helpful assistant that writes a cover letter from a resume and a job description.
Only respond with the cover letter and nothing else.
"""

system_prompt_suggest = """
You are a helpful assistant that generates suggestions for a resume from a resume and a job description.
You have also been provided a sample output.
Only respond with the suggestions and nothing else.
"""

example_files = []

example_files_suggest = [
    """Here are a few Suggestions

1. Experience:
- Replace Passive Voice Phrases with Active Voice Phrases
- Emphasize Python Usage within Job Descriptions
- Discuss Soft skills like talking to customers and leadership opportunities

2. Skills:
- Reorganize Skills to state Python and Java first since they are on the job description
- State Key skills related with Leadership such as coordinination and teamwork

3. Projects:
- Break Descriptions into small bullet points
- Provide a link to the project if possible
- Create a digital portfolio to showoff Projects"""
]

def generate_cv(resume, job_desc, context = ""):
    """
    Generates a cover letter from a resume and a job description. 
    The resume content is extracted from a pdf in the application, 
    which is taken from the file tag in the request. In testing, the 
    resume tag is used to pass in the sample resume. Context is also 
    used as a user input to guide the generation.
    ```
    Request:
    {
        resume: string,  
        job_desc: string,
        file: string,
        context: string
    }
    Response:
    {
        status: boolean
        data: message (Success / Error message as per status)
        
    }
    ```
    """
    try:
        if request:
            messages = [
                ("system",system_prompt_cv,),
                ("human", "Resume: " + resume),
                ("human", "Additional Requests and Context: " + context),
                ("human", "Job Description: " + job_desc),
            ]

            for f in example_files:
                messages.append(("human", "Example Cover Letter: " + f))

            msg = llm.invoke(messages)
            response = msg.content
            return jsonify({'message': "Cover Letter Generated Successfully", 'letter': response}), 200

    except Exception:
        return jsonify({'error': "Something went wrong"}), 400
    
def resume_suggest(resume, job_desc):
    """
    Reviews a resume and provides suggestions to tailor it for a job description.
    ```
    Request:
    {
        resume: string,  
        job_desc: string,
        file: string
    }
    Response:
    {
        status: boolean
        data: message (Success / Error message as per status)
        
    }
    ```
    """
    try:
        if request:
            messages = [
                ("system",system_prompt_suggest,),
                ("human", "Resume: " + resume),
                ("human", "Job Description: " + job_desc),
            ]

            for f in example_files_suggest:
                messages.append(("human", "Example Resume Suggestions: " + f))

            msg = llm.invoke(messages)
            response = msg.content
            return jsonify({'message': "Successfully Created Resume Suggestions", 'suggestions': response}), 200

    except Exception as e:
        return jsonify({'error': "Something went wrong"}), 400
