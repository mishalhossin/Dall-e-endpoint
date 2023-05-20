# Dall-e-endpoint

This repository contains a Flask application that generates images based on prompts using the OpenAI Image API. The application accepts HTTP POST requests with a JSON payload containing a prompt. It then generates an image based on the prompt and returns the image URL in the response.

## Getting Started

To run the application locally, follow the steps below:

1. Clone this repository to your local machine.

2. Install the required dependencies by running the following command:
```
pip install openai flask requests
```
3. Make sure to replace `API_KEY`'s with your actual OpenAI API key in .env
```
OPENAI_API_KEY_1=
OPENAI_API_KEY_2=
OPENAI_API_KEY_3=

...

OPENAI_API_KEY_30=
```
4. Start the Flask application by running the following command:
main.py
