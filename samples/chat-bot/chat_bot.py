import os
import argparse
from openai import OpenAI

class ChatBot:
    def __init__(self, api_key, model="gpt-3.5-turbo"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def chat(self, system_content, user_content):
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": user_content}
            ]
        )
        return completion.choices[0].message

def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple ChatBot")
    parser.add_argument("--model", type=str, default="gpt-3.5-turbo", choices=["gpt-3.5-turbo", "gpt-4-turbo"], help="Model to use")
    parser.add_argument("--system", type=str, default="You are a poetic assistant, skilled in explaining complex programming concepts with creative flair.", help="System content")
    parser.add_argument("--user", type=str, default=None, help="User content")
    parser.add_argument("--user-file", type=str, default="assets/user-content.txt", help="Path to a file containing user content")
    return parser.parse_args()

def load_user_content(file_path):
    if not file_path:
        return None
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("User content file not found.")
        return None

if __name__ == "__main__":
    args = parse_arguments()
    user_content = args.user
    if user_content is None:
        user_file='assets/user-content.txt'
        user_content = load_user_content(args.user_file)
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        chatbot = ChatBot(api_key, model=args.model)
        response = chatbot.chat(args.system, user_content)
        print(response.content)
    else:
        print("Please provide your OpenAI API key.")
