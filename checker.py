import openai
import json

def check_api_key(api_key):
    openai.api_key = api_key
    try:
        openai.Completion.create(model="gpt-3.5-turbo", prompt="Hello", max_tokens=5)
        return True
    except openai.error.AuthenticationError:
        return False

def reorder_api_keys():
    with open('unique_keys.json') as f:
        keys = json.load(f)
    
    working_keys = []
    invalid_keys = []
    
    for key_name, key_value in keys.items():
        if check_api_key(key_value):
            working_keys.append((key_name, key_value))
        else:
            invalid_keys.append((key_name, key_value))
    
    ordered_keys = working_keys + invalid_keys
    
    working_unique_keys = {key[0]: key[1] for key in ordered_keys}
    
    with open('working_unique_keys.json', 'w') as f:
        json.dump(working_unique_keys, f, indent=4)

reorder_api_keys()
