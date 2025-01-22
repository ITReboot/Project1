import os
from github_api import GitHubAPI



if __name__ == "__main__":
    token = os.getenv('USER_GITHUB_TOKEN')
    print("token")
    github = GitHubAPI(token)

    
    github.print_user_details()
