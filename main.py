import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


from google import genai

client = genai.Client(api_key=API_KEY)

content = str(input("Ruby-Chan: "))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents = content,
)

print(response.text)