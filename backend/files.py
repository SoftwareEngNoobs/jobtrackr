"""
This file handles the functionality for using AWS S3 for storing 
resume files in the cloud. There are functions for uploading files, 
viewing files, deleting files, downloading files, and scraping text 
content from the pdf file. These functions are all within the context 
of the current user.
"""

import io
from bson import ObjectId
from flask import request, jsonify, send_file, after_this_request
from pymongo import ReturnDocument
import boto3
import re
import os
from dotenv import load_dotenv
from resume_extract import extract_text_from_pdf

load_dotenv()

s3 = boto3.client('s3', aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID', ""),
                  aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY', ""))

bucket_name = "job-tracker-resume-upload"


def upload_file(UserRecords, Files):
    
    '''
    Uploads a file to the system for the given user using AWS S3.
    ```
    Request:
    {
        email: string,
        start: string,
        file: file,
        end: string,
        filename: string
        
    }
    Response:
    {
        status: 200
        data: Success message
        
        status: 500
        data: Error message
        
    }
    ```
    '''
    
    try:
        file = request.files['file']
        email = str(request.files['email'].read())
        start = email.find("'")
        end = email.rfind("'")
        email = email[start+1:end].strip()
        email_found = UserRecords.find_one({"email": email})
        if email_found:
            _id = str(email_found["_id"])
        else:
            return jsonify({'error': "Email not found"}), 500
        if file:
            filename = _id+"--;--"+file.filename
            file.save(filename)
            s3.upload_file(
                Bucket=bucket_name,
                Filename=filename,
                Key=filename
            )
            Files.insert_one({
                "email": email,
                "filename": filename,
            })
            os.remove(filename)
            return jsonify({"message": "File Uploaded Successfully"}), 200
        else:
            return jsonify({'error': "Found Empty File"}), 500
    except:
        return jsonify({'error': "Something went wrong"}), 500


def view_files(Files):
    
    '''
    Retrieves the files for the given user that were uploaded to AWS S3.
    ```
    Request:
    {
        email: string  
    }
    Response:
    {
        status: 200
        data: Success message
        
        status: 500
        data: Error message
        
    }
    ```
    '''
    
    try:
        if request:
            email = request.args.get("email")
            out = Files.find({"email": email})
            if out:
                files = []
                for i in out:
                    i['filename'] = i['filename']
                    i['_id'] = str(i['_id'])
                    files.append(i)
                if files:
                    return jsonify({'message': 'Files found', 'files': files}), 200
                else:
                    return jsonify({'message': 'No Files found', 'files': files}), 200
            else:
                return jsonify({'message': 'Email Doesnt Exist'}), 400
    except Exception as e:
        print(e)
        return jsonify({'error': "Something went wrong"}), 500

def get_pdf_info(file_req_name, Files, email):
    """
    Helper function to extract the values from a pdf
    in the AWS S3 bucket.
    """
    try:
        if request:
                file = Files.find_one({"filename": file_req_name})
                if not str(file["filename"]).endswith(".pdf"):
                    return ""
                if file:
                    if file["email"] == email:
                        s3.download_file(
                            bucket_name, file["filename"], file_req_name.split("--;--")[1])
                        output = extract_text_from_pdf(file_req_name.split("--;--")[1])
                        os.remove(file_req_name.split("--;--")[1])
                        return output
    except Exception:
        return ""

def download_file(Files):
    
    '''
    Downloads the given file to the client machine from AWS S3.
    ```
    Request:
    {
         
    }
    Response:
    {
        status: 200
        data: Success message
        
        status: 500
        data: Error message
        
        status: 501
        data: Authorization required
        
    }
    ```
    '''
    
    try:
        if request:
            req = request.get_json()
            file = Files.find_one({"filename": req["filename"]})
            if file:
                if file["email"] == req["email"]:
                    s3.download_file(
                        bucket_name, file["filename"], req["filename"].split("--;--")[1])

                    with open(req["filename"].split("--;--")[1], "rb") as f:
                        file_output = f.read()

                    os.remove(req["filename"].split("--;--")[1])
                    return send_file(io.BytesIO(file_output), 
                                     as_attachment=True, 
                                     download_name=req["filename"].split("--;--")[1])
                else:
                    return jsonify({'message': 'You are not authorized to view this file'}), 501

            return jsonify({'message': 'Files found'}), 200
    except Exception:
        return jsonify({'error': 'Something went wrong'}), 500


def delete_file(Files):
    
    '''
    Deletes a file from the system for the given user from AWS S3.
    ```
    Request:
    { 
    }
    Response:
    {
        status: 200
        data: Success message
        
        status: 500
        data: Error message
        
    }
    ```
    '''
    
    try:
        if request:
            req = request.get_json()
            df = Files.find_one_and_delete({"filename": req["filename"]})
            if df == None:
                return jsonify({"error": "No such Job ID found for this user's email"}), 500
            else:
                try:
                    s3.delete_object(Bucket=bucket_name, Key=req["filename"])
                except:
                    pass
                return jsonify({"message": "File Deleted Successfully"}), 200
    except Exception:
        return jsonify({'error': 'Something went wrong'}), 500
