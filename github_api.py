# github_api.py
import requests
from dotenv import load_dotenv
import os

class GitHubAPI:
    def __init__(self):
        
        # Load environment variables from the .env file
        load_dotenv()

        # Get the token from the environment variable
        self.token = os.getenv('USER_GITHUB_TOKEN')

        if not self.token:
            raise ValueError("GitHub token is missing in the environment variables.")

        self.base_url = "https://api.github.com/"
        self.headers = {
            "Authorization": f"token {self.token}"
        }

    def fetch_user_details(self):
        url = f"{self.base_url}user"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch user data. Status code: {response.status_code}")
            return None

    def print_user_details(self):
        user_data = self.fetch_user_details()
        print(user_data)
        #print(type(user_data))
        if user_data:
            print(f"User: {user_data['login']}")
            print(f"Name: {user_data['name']}")
            print(f"Public Repos: {user_data['public_repos']}")
        else:
            print("Could not retrieve user details.")
