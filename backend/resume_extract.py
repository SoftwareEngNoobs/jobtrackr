"""
This file contains a function to extract text from a pdf file. 
This is used for providing text versions of the resumes the user 
has uploaded to their account to Ollama for generating cover letters 
and providing resume suggestions.
"""

import PyPDF2


def extract_text_from_pdf(pdf_path):
    """
    Extracts and returns the text in the pdf at the given path.
    """
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text
