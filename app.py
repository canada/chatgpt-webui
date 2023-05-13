from flask import Flask, request, jsonify
from openai import ChatCompletion
from dotenv import load_dotenv
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    load_dotenv()  # take environment variables from .env.

    data = request.get_json()
    message = data['message']

    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    response = llm([HumanMessage(content=message)]).content
    return jsonify({"answer": response})

if __name__ == '__main__':
    app.run(debug=True)

