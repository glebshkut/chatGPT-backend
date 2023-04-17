import os
# import openai
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])


@app.route('/chat-completion', methods=['POST'])
def chat_completion():
    data = request.get_json()
    prompt = data['prompt']
    apiKey = data.get("apiKey")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {apiKey}",
    }

    messages = [
        {"role": "system", "content": "You are a helpful assistant."}, *prompt]

    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "max_tokens": 1000,
        "temperature": 0.5,
    }

    response = requests.post(
        "https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    response_data = response.json()

    print('response', response_data)

    return jsonify({"result": response_data["choices"][0]["message"]})


if __name__ == '__main__':
    app.run(port=5000, debug=True)
