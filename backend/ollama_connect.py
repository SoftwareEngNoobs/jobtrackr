"""
This file handles the functionality for generating cover letters
and providing resume suggestions using Ollama. The system prompts used
for each of these tasks are at the top of the file using the
system_prompt_cv and system_prompt_suggest variables.

The model being used by Ollama can be changed by adjusting the model
variable in the ChatOllama instantiation of the llm variable at the top
of the file.
"""

from flask import request, jsonify
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
)

system_prompt_cv = """
You are a helpful assistant that writes a cover letter from a resume
and a job description. Only respond with the cover letter and nothing
else.
"""

system_prompt_suggest = """
You are a helpful assistant that generates suggestions for a resume
from a resume and a job description. You have also been provided a
sample output. Only respond with the suggestions and nothing else.
"""

system_prompt_ats_score = """
You are a helpful assistant that compares the skills in a resume and a
job description. Extract relevant skills from both the resume and the
job description, compare them, and calculate a score based on how many
skills match.

Follow these steps:
1. Extract skills from the resume and the job description.
2. Compare the extracted skills.
3. Calculate the ATS score using this formula:
   Score (%) = (Number of Matched Skills / Total Skills in Job Description) * 100

Respond with a JSON output in this format:
{
  "extracted_resume_skills": ["skill1", "skill2", "..."],
  "extracted_job_skills": ["skillA", "skillB", "..."],
  "matched_skills": ["skill1", "skill2", "..."],
  "missing_skills": ["skill3", "..."],
  "ats_score": "XX%"
}
"""

example_files = []

example_files_suggest = [
    """
Here are a few Suggestions:

1. Experience:
- Replace Passive Voice Phrases with Active Voice Phrases.
- Emphasize Python Usage within Job Descriptions.
- Discuss Soft Skills like customer communication and leadership
opportunities.

2. Skills:
- Reorganize Skills to state Python and Java first since they are on
the job description.
- State Key Skills related to Leadership, such as coordination and
teamwork.

3. Projects:
- Break Descriptions into smaller bullet points.
- Provide a link to the project if possible.
- Create a digital portfolio to showcase projects.
"""
]


def generate_ats_score(resume, job_desc):
    """
    Generates an ATS score by comparing skills in a resume and job
    description.
    """
    try:
        ats_score_messages = [
            ("system", system_prompt_ats_score),
            ("human", "Resume: " + resume),
            ("human", "Job Description: " + job_desc),
        ]
        ats_msg = llm.invoke(ats_score_messages)
        ats_result = ats_msg.content
        return ats_result
    except Exception as e:
        return jsonify({'error': f"Something went wrong: {str(e)}"}), 400


def generate_cv(resume, job_desc, context=""):
    """
    Generates a cover letter from a resume and a job description.
    """
    try:
        if request:
            messages = [
                ("system", system_prompt_cv),
                ("human", "Resume: " + resume),
                ("human", "Additional Requests and Context: " + context),
                ("human", "Job Description: " + job_desc),
            ]

            for f in example_files:
                messages.append(("human", "Example Cover Letter: " + f))

            msg = llm.invoke(messages)
            response = msg.content
            return jsonify({
                'message': "Cover Letter Generated Successfully",
                'letter': response
            }), 200
    except Exception:
        return jsonify({'error': "Something went wrong"}), 400


def resume_suggest(resume, job_desc):
    """
    Reviews a resume and provides suggestions to tailor it for a job
    description. Includes ATS score, matched skills, and missing skills.
    """
    try:
        if request:
            # Generate suggestions using LLM
            suggestion_messages = [
                ("system", system_prompt_suggest),
                ("human", "Resume: " + resume),
                ("human", "Job Description: " + job_desc),
            ]
            for f in example_files_suggest:
                suggestion_messages.append(
                    ("human", "Example Resume Suggestions: " + f))

            suggestion_msg = llm.invoke(suggestion_messages)
            suggestions = suggestion_msg.content

            # Generate ATS score using ats_score logic
            ats_result = generate_ats_score(resume, job_desc)

            # Return combined response
            return jsonify({
                "message": "Successfully Created Resume Suggestions",
                "suggestions": suggestions,
                "ats_content": ats_result
            }), 200
    except Exception as e:
        return jsonify({'error': f"Something went wrong: {str(e)}"}), 400
