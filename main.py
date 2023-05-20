import os
from datetime import datetime
import openai
import logging
from flask import Flask, request, jsonify
import requests
import random

env_variable_names = [
  "OPENAI_API_KEY_1",
  "OPENAI_API_KEY_2",
  "OPENAI_API_KEY_3",
  "OPENAI_API_KEY_4",
  "OPENAI_API_KEY_5",
  "OPENAI_API_KEY_6",
  "OPENAI_API_KEY_7",
  "OPENAI_API_KEY_8",
  "OPENAI_API_KEY_9",
  "OPENAI_API_KEY_10",
  "OPENAI_API_KEY_11",
  "OPENAI_API_KEY_12",
  "OPENAI_API_KEY_13",
  "OPENAI_API_KEY_14",
  "OPENAI_API_KEY_15",
  "OPENAI_API_KEY_16",
  "OPENAI_API_KEY_17",
  "OPENAI_API_KEY_18",
  "OPENAI_API_KEY_19",
  "OPENAI_API_KEY_20",
  "OPENAI_API_KEY_21",
  "OPENAI_API_KEY_22",
  "OPENAI_API_KEY_23",
  "OPENAI_API_KEY_24",
  "OPENAI_API_KEY_25",
  "OPENAI_API_KEY_26",
  "OPENAI_API_KEY_27",
  "OPENAI_API_KEY_28",
  "OPENAI_API_KEY_29",
  "OPENAI_API_KEY_30"
]


def get_key():
    selected_variable_name = random.choice(env_variable_names)
    api_key = os.getenv(selected_variable_name)
    return api_key

def generate_image(prompt):
    openai.api_key = get_key()
    print(f"Generating : {prompt}")
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=4,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
    except openai.error.InvalidRequestError as e:
        print(f"Invalid request error: {e}")
        image_url = "https://cdn.discordapp.com/attachments/1025493152301326356/1109451078942081114/DIGITAL_LAVENDER_VIRTUAL_EVENT_VIRTUAL_BACKGROUND.jpg"
    except Exception as e:
        print(f"Error occurred: {e}")
        image_url = "https://cdn.discordapp.com/attachments/1025493152301326356/1109446996449820794/ai.png"

    return image_url

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    data = request.get_json()
    prompt = data.get('prompt')
    if prompt:
        image_url = generate_image(prompt)
        response = {'image_url': image_url}
        return jsonify(response), 200
    return jsonify({'error': 'Invalid request'}), 400

@app.route('/', methods=['GET'])
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Centered Rounded Box with Header and Shadow</title>
    <style>
      body {
        background-color: #333;
      }
    
      .container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
      }
    
      .rounded-box {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        background-color: #f0f0f0;
        border-radius: 20px;
        padding: 20px;
        width: 300px;
        height: 150px;
        text-align: center;
        box-shadow: 0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23);
      }
    
      h2 {
        margin-bottom: 10px;
      }
    </style>
    </head>
    <body>
    <div class="container">
      <div class="rounded-box">
        <h2>Howdy! Welcome to the endpoint</h2>
        The requested URL does not permit this method.
        Please use POST instead. For example: "prompt": "image of a cute dog"
      </div>
    </div>
    </body>
    </html>
    '''
  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
