import aiohttp
import asyncio

async def generate_response(prompt):
    url = 'http://localhost:3000/text'  # Replace with the actual URL of the Flask application

    payload = {
        'prompt': prompt
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=payload) as response:
                response.raise_for_status()
                data = await response.json()
                generated_text = data.get('generated_text')
                return generated_text
    except aiohttp.ClientError as e:
        print(f"Error occurred: {e}")
        return None
      
prompt = """

User: Hi there?
Bot:
"""

response = asyncio.run(generate_response(prompt))

print (response)
