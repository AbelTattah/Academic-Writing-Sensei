## Introduction

This is a simple chatbot web application that teaches you academic writing in an interactive way.

Click here to try the application [Academic Writing](https://academic-writing-sensei-1.onrender.com)

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
The command above will create a virtual environment that you can use to manage your projects
dependencies or libraries indepedently from globally installed libraries on your system.

#### Using the virtual environment :
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

🎉🎉

6. Create a file with .env extension, copy and past the environment variable below in 
the application

```
OPENAI_API_KEY = "your openai api-key "
```

You need an openai account to obtain an API key.


## Contribution

1. Fork or clone this repo.
2. Make changes.
3. Creat a pull request
4. Review
5. Merging 🎉


All suggestions are completely welcome at abeltattahh@gmail.com

Happy hacking ✌


