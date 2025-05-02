import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

from google import genai

client = genai.Client(api_key=API_KEY)

username = str(input("Enter your name: "))
print(f"Hello {username}, welcome to Ruby-Chan chat!")

while True:
    content = str(input(f"{username}: "))

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents = f"You are a cute anime chatbot named Ruby Chan, please be kind and do not mention anything private: {content}"
    )

    print(f"Ruby-Chan: {response.text}")