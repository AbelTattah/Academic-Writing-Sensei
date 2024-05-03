# Importing flask from the flask library
from flask import Flask,render_template,request,jsonify
# Importing the main from the main folder
from main import main
# Import Json
import json
# Import gevent
from gevent.pywsgi import WSGIServer
from flask_cors import CORS

john = main.Kofi()

app  = Flask(__name__)

CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sensei',methods=['POST'])
def start_chat():
    question = request.json
    print(question)
    response = john.ask_question(question['question'])
    return jsonify({"answer":response})

@app.route('/askgpt',methods=['POST'])
def gpt():
    prompt = request.json
    print(prompt)
    response = john.chat_completion(prompt["messages"])
    return jsonify({"answer":response})


if __name__ == '__main__':
    # Running the server
    server = WSGIServer(('', 3000), app)
    server.serve_forever()
