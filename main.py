import os
import sys

def main():
    try:
        from dotenv import load_dotenv
        from google import genai
    except (ValueError, ModuleNotFoundError):
        sys.exit("Please install dependencies => pip install -r requirements.txt")

    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    if not API_KEY:
        sys.exit("API_KEY not found in environment variables.")

    client = genai.Client(api_key=API_KEY)

    username = input("Name: ").strip().title()
    character = input("Who do you want to chat with?: ").strip().title()

    print(f"Hello {username}, welcome to {character} chat!\n")
    print("Type 'stop()' to end the chat.")
    print("AI response may not be accurate, please do not share any private information.\n")

    while True:
        content = input(f"{username}: ").strip()
        if content.lower() == "stop()":
            sys.exit(f"Goodbye {username}, have a great day!")
        if not content:
            print("Please enter a message.")
            continue
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=f"You are a {character}, please be kind and do not mention anything private: {content}"
            )
            print(f"{character}: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
