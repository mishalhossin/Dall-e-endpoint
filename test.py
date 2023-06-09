import aiohttp
import asyncio

url = 'http://localhost:3000/text'  # Replace with the actual URL of the Flask application

async def generate_response(prompt):
    async with aiohttp.ClientSession() as session:
        data = {'prompt': prompt}
        async with session.post(url, json=data) as response:
            if response.status == 200:
                result = await response.json()
                generated_text = result.get('generated_text')
                return generated_text
            else:
                return None

# Example usage
async def main():
    prompt = """
User: Hi there?
Bot:
"""
    generated_text = await generate_response(prompt)
    if generated_text:
        print(generated_text)
    else:
        print('Error generating response')

asyncio.run(main())
