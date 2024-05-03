# Academic Writing Sensei 

This is a simple chatbot that teaches you academic writing

## Introduction

The primary goal of this chatbot is to be able to teach a subject like academic 
writing in an interactive way.

This software aims to help in studies

The Langchain python library is used to create a chatbot that is able to answer questions based on 
data. This chatbot combines the power of the openai GPT-3.5 turbo LLM and some other techniques to create
enable it to give accurate answers.

The data used in this chatbot is obtained from an Academic writing Textbook.


## Technologies languages used

This program is mainly in python.
It utilizes [Langchain](https://python.langchain.com/docs/get_started/introduction/) for integrating AI functionality

- flask
- Langchain
- openai

## Installation
Make sure you have git and python 3.1.0 installed on your system.

1. Run this command in a terminal with your preferred directory as current working directory

```
git clone -b main https://github.com/AbelTattah/Academic-Writing-Sensei.git
```

2. Navigate into the folder containing the cloned repository

```
cd Academic writing Sensei
```

3. This step is optional: Create a virtual environment

In the root of the cloned repository's folder run

```
python3 -m venv .venv
```
The command above will create a vitual environment that you can use to manage your projects
dependencies or libraries indepedently from globally installed libraries on your system.

Using the virtual environment :
Depending on your system run

Windows
```
.venv/Script/activate
```

Linux
```
.venv/bin/scripts/activate
```

4. Install required libraries
Run 

```
pip install -r requirements.txt
```

5. Start
Run

```
python3 index.py
```

An instance of a flask server will be running on your system.
In order to actually use the endpoints or routes in this application on your machine,
contact the owner of this repo.
🎉🎉

6. Create a file with .env extension, copy and past the environment variable below in 
the application

```
OPENAI_API_KEY = "your openai api-key "
```

You might need an openai account to create an openai api key and even
make any meaningful contribution to this project.

## Routes

1. (/)  Main or home route

- Methods : GET
- Request Body: None
- Response: HTML homepage of this application
- This route will be soon removed.

2. (/chat)  Chat page route

- Methods : GET
- Request Body: None
- Response: HTML chat page of this application.
- This route will also be removed soon due to architectural changes

3. (/sensei) Ask questions About Academic writing

- Methods: POST
- Request Body:  
            content-Type : application/json
            example: {
                "question":"What is Academic writing"
            }
- Response: 
            Status: 200
            content-Type: application/json
            example: {
                "answer":"Academic writing is ...."
            }

4. (/askgpt) Ask questions About Academic writing

- Methods: POST
- Request Body:  
            content-Type : application/json
            example: {
                "question":"What is Academic writing"
            }
- Response: 
            Status: 200
            content-Type: application/json
            example: {
                "answer":"Academic writing is ...."
            }

## Usage

- Example:
To ask a question about academic writing,
make send a post request to this application url throught the /sensei route

- Method: POST
- Request Body:  
            content-Type : application/json
            example: {
                "question":"What is Academic writing"
            }
- Response: 
            Status: 200
            content-Type: application/json
            example: {
                "answer":"Academic writing is ...."
            }


## Troubleshooting

1. Not getting response from /sensei of /askgpt endpoints
ask:
Ask the owner of the repo for an openai api key or create an openai account

2. Cannot connect to application:
Check your IP address and the port number of this application.

The current setting is

```
# Running the server
    server = WSGIServer(('ipaddress',port), app)
```
Enter your current IP address and preferred port number

or if you are accessing the hosted version of this application

Check whether the url is correct or ask the owner of this repo for the url.

## Contribution

1. Fork or clone this repo.
2. Make changes.
3. Creat a pull request
4. Review
5. Merging 🎉


All suggestions are completely welcome at tattahabelk@gmail.com

Happy hacking ✌

