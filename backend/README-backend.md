# Backend Local Development Setup

### Installation

Clone the repository (if you haven't already)

```
git clone https://github.com/jayrajmulani/se-group1-project2.git
```

Open a new terminal inside the backend directory.

`se-group1-project2\backend`

Create a virtual environment called `venv`

```
python -m venv venv
```

For Windows - Activate the virtual environment

```
venv\Scripts\activate.bat
```

For Mac OS - Activate the virtual environment

```
source venv/bin/activate
```

For bash/linux - Activate the virtual environment

```
source venv/bin/activate
```
Install MongoDB
Create a database in MongoDB with the name localhost:27017
![image](https://github.com/user-attachments/assets/b9b004c2-8d59-4d5b-ac44-d2e9dd6c99ba)

Install Ollama
Download it from this link: [ollama download](https://ollama.com/download) 
```
ollama serve
ollama pull llama3.2
```
Create the .env file by copying the .env.example file in the root directory (place it in the root directory)
```
AWS_ACCESS_KEY_ID="<id>"
AWS_SECRET_ACCESS_KEY="<access key>"
MONGO_DB_CONNECTION="mongodb://localhost:27017/"
APP_SECRET_KEY="testing"
DATABASE_TYPE="development"
```
Create an access key id and a secret access key to access the AWS S3 Bucket for the env file
![image](https://github.com/user-attachments/assets/afacf5b3-56cc-4dcf-8e17-ca2244bfedfc)
![image](https://github.com/user-attachments/assets/06afd005-d0eb-4468-8392-9bc721cc6ec4)
![image](https://github.com/user-attachments/assets/a2a45ceb-6217-4abe-8650-d809ec6b046c)
![image](https://github.com/user-attachments/assets/11206c06-8647-4436-84cd-f7b4b43911e3)
![image](https://github.com/user-attachments/assets/abddbf73-9715-4ac5-94f6-e6e405f130c3)
* Copy over the access key id and the secret access key to your env file

Install required packages for the Flask server

```
pip install -r requirements.txt
```

The flask server runs in [http://localhost:8000](http://localhost:8000)

### Start the server in development mode

Run the flask server.

```
python app.py
```

### Backend Test

Run this command to test the backend APIs

```
python backend\tests.py
```
