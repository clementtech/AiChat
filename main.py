import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

from google import genai
import sys

client = genai.Client(api_key=API_KEY)

username = str(input("Enter your name: ")).title()
character = str(input("Who do you want to chat with?: ")).title()
print(f"Hello {username}, welcome to {character} chat!")



while True:
    content = str(input(f"{username}: "))

    if content.lower() == "stop":
        sys.exit(f"Goodbye {username}, have a great day!")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents = f"You are a {character}, please be kind and do not mention anything private: {content}"
    )

    print(f"{character}: {response.text}")