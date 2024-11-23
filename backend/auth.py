"""
This file contains the functionality for user authentication for 
JobTrackr. There are functions to register a new user, login an 
existing user, and logout a currently logged in user.
"""

from bson.objectid import ObjectId
from flask import request, session, jsonify
from pymongo import ReturnDocument
import bcrypt
import json


def register(UserRecords):
    '''
    Registers a new user into the system.
    ```
    Request:
    {
        firstName: string,
        lastName: string,
        email: string,
        password: string,
        confirmPassword: string
    }
    Response:
    {
        status: 200
        data: Success message

        status: 400
        data: Error message

    }
    ```
    '''

    try:
        req = request.get_json()
        name = {"firstName": req["firstName"], "lastName": req["lastName"]}
        email = req["email"]
        password = req["password"]
        confirmPassword = req["confirmPassword"]

        email_found = UserRecords.find_one({"email": email})
        if email_found:
            return jsonify({'error': "This email already exists in database"}), 400
        if password != confirmPassword:
            return jsonify({'error': "Passwords should match!"}), 400

        else:
            hashed = bcrypt.hashpw(
                confirmPassword.encode("utf-8"), bcrypt.gensalt())
            user_input = {"name": name, "email": email, "password": hashed}
            UserRecords.insert_one(user_input)
            return jsonify({'message': 'Login successful'}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': "Something went wrong"}), 400


def login(UserRecords):
    '''
    Attempts to login a user with the provided email and password.
    ```
    Request:
    {
        email: string,
        password: string
    }
    Response:
    {
        status: 200
        data: Success message

        status: 400
        data: Error message

    }
    ```
    '''

    try:
        req = request.get_json()
        email = req["email"]
        password = req["password"]
        email_found = UserRecords.find_one({"email": email})
        if email_found:
            passwordcheck = email_found["password"]
            if bcrypt.checkpw(password.encode("utf-8"), passwordcheck):
                return jsonify({'message': 'Login successful'}), 200
            else:
                if "email" in session:
                    return jsonify({'message': 'Login successful'}), 200
                return jsonify({'error': "Wrong password"}), 400
        else:
            return jsonify({'error': "Email not found"}), 400
    except Exception as e:
        print(e)
        return jsonify({'error': "Something went wrong"}), 400


def logout():
    '''
    Logs out the current user from the system.
    ```
    Request:
    {

    }
    Response:
    {
        data: message (Success)

    }
    ```
    '''

    return jsonify({'message': 'Logout successful'}), 200


def create_profile(UserProfiles):
    '''
    Creates the profile of the user. 
    Request: 
    {
     email: string, 
     first_name: string,
     last_name: string, 
     city: string,
     state: string,
     country: string,
     education: json,
     work_ex: json,
     skills: list,
    }
    '''
    try:
        data = request.get_json()
        email_found = UserProfiles.find_one({"email": data["email"]})
        if email_found:
            return jsonify({'error': "This email already exists in database"}), 400
        else:
            insert_result = UserProfiles.insert_one(data)
            return jsonify({'message': "Profile created succesfully", 'id': f'{insert_result.inserted_id}'}), 201
    except Exception as e:
        print(e)
        return jsonify({'message': "Error while creating the profile"}), 500

def view_profile(UserProfiles):
    '''
        Returns user profile of the user, if it exists. 
        Request: 
        { 
            user_id :  string
        }
        Response: 
        {
            email: string, 
            first_name: string,
            last_name: string, 
            city: string,
            state: string,
            country: string,
            education: json,
            work_ex: json,
            skills: list,
        }
    '''
    try:
        id = request.args.get("user_id")
        object_id = ObjectId(id)
        result = UserProfiles.find_one(object_id)
        #print('is anything even printing')
        print(type(result), result)
        result['_id'] = str(result['_id'])
        return jsonify({'message': 'Profile found', 'profile':result}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': "Error while viewing the profile"}), 500