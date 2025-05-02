import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


from google import genai

from PyQt5.QtWidgets import QApplication, QMainWindow

import django


client = genai.Client(api_key=API_KEY)

content = str(input("Ruby-Chan: "))

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents = f"You are a maths tutor, only answer and explain maths questions. {content}"
)

print(response.text)