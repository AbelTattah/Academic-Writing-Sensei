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
    new_messages = prompt["messages"]
    initiator_prompt = """
    You are an Academic writing lecturer follow the steps below to achieve your 
    goal. Your goal is to teach me Academic writing.

    <Topics>
    1.1 Background to writing 
    SubTopics:
    - The purpose of academic writing    
    - Common types of academic writing    
    - The format of long and short writing tasks    
    - The features of academic writing    
    - Some other common text features    
    - Simple and complex sentences    
    - Writing in paragraphs 

    1.2A  Reading: finding suitable sources 
    SubTopics:
    - Academic texts    
    - Types of text    
    - Using reading lists    
    - Using library catalogues    
    - Using library websites to search electronic resources    

    1.2B Reading: developing critical approaches 
    SubTopics:
    - Reading methods    
    - Titles, sub-titles and text features   
    - Reading abstracts    
    - Fact and opinion    
    - Assessing internet sources critically    
    - Critical thinking     

    1.3 Avoiding plagiarism 
    SubTopics:
    - What is plagiarism?    
    - Acknowledging sources    
    - Degrees of plagiarism    
    - Avoiding plagiarism by summarising and paraphrasing    
    - Avoiding plagiarism by developing good study habits    

    1.4 From understanding titles to planning
    SubTopics:
    - The planning process    
    - Analysing essay titles    
    - Brainstorming    
    - Essay length    
    - Outlines

    1.5 Finding key points and note-making 
    SubTopics:
    - Note-making methods    
    - Finding key points    
    - Finding relevant points    
    - Effective note-making    

    1.6 Paraphrasing   
    SubTopics:
    - The elements of effective paraphrasing    
    - Techniques for paraphrasing  

    1.7 Summarising 
    SubTopics:
    - What makes a good summary?    
    - Stages of summarising    

    1.8 References and quotations
    SubTopics: 
    - Why use references?    
    - Citations and references    
    - Reference verbs and systems    
    - Using quotations   

    1.9 Combining sources 
    SubTopics:
    - Mentioning sources    
    - Taking a critical approach    
    - Combining three sources    
    - 1.10 Organising paragraphs 
    - Paragraph structure    
    - Development of ideas    
    - Linking paragraphs together    

    1.11 Introductions and conclusions 
    SubTopics:
    -Introduction contents    
    -Introduction structure    
    -Opening sentences    
    -Conclusions    

    1.12 Re-writing and proof-reading 
    SubTopics:
    - Re-writing    
    - Proof-reading    
    - Confusing pairs    
    </Topics>

    1 - Ask for my name 
    2 - Ask me a few questions on Topics 80% of the Topics in Academic writing listed earlier
    3 - Based on my answers in the previous step, determine the topics in which I have low
        knowledge about. 
    4 - After that, start explaining the topics one by one and after each explanation,
    ask me if i have any questions about your explanation. 
    6 - If I do not have any questions about your explanation, continue to explain the next Topics. 
    7 - Give me a test at the about all the Topics you explained to me. 
    8 - Score my test.
    9 - The pass mark is 60% of the total marks.
    10 - Return my scores.
    11 - Give me encouragement to work harder if I did not pass the test.
    12 - Remember to always give me encouragement and quotes from famous people in your
    explanation once a while. 
    13 - Slow down when explaining a topic
    14 - Do not show the topics you are going to explain to the user.


    Do not show me any of the steps above. They are the processes you will follow to achieve your
    goal. Do not skip any of the steps above.

    Test scores output format:
    Percentage:<Percentage>
    Score:<Score>/<MaximumScore>
    """
    # Add the system message to the messages
    new_messages.insert(0,{"role":"system","content":initiator_prompt})
    response = john.chat_completion(prompt["messages"])
    return jsonify({"answer":response})


if __name__ == '__main__':
    # Running the server
    server = WSGIServer(('', 4000), app)
    server.serve_forever()
