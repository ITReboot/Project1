import os
from github_api import GitHubAPI



if __name__ == "__main__":
  
    github = GitHubAPI()

    
    github.print_user_details()
