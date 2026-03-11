import os

from dotenv import load_dotenv


def main():
    print("Hello from langchain-course!")
    print("Loading environment variables from .env file...")
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("API_KEY loaded successfully!")
    else:
        print("API_KEY not found. Please check your .env file.")


if __name__ == "__main__":
    main()
