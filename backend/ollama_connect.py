from flask import request, jsonify
from langchain_ollama import ChatOllama
llm = ChatOllama(
    model="llama3.2",
    temperature=0,
)

system_prompt = """
You are a helpful assistant that writes a cover letter from a resume and a job description.
Only respond with the cover letter and nothing else.
"""

example_files = []

def generate_cv(resume, job_desc, context = ""):
    """
    Generates a cover letter from a resume and a job description.
    ```
    Request:
    {
        resume: string,  
        job_desc: string
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
                ("system",system_prompt,),
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
        job_desc: string
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
                (
                    "system",
                    "You are a helpful assistant that provides resume suggestions to tailor a resume to the job description.",
                ),
                ("human", "Resume: " + resume),
                ("human", "Job Description: " + job_desc),
            ]
            msg = llm.invoke(messages)
            response = msg.content
            return jsonify({'message': "Successfully Created Resume Suggestions", 'suggestions': response}), 200

    except Exception as e:
        return jsonify({'error': "Something went wrong"}), 400
