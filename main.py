# main_script.py

from github_api import GitHubAPI

# Example usage
if __name__ == "__main__":
    github = GitHubAPI()

    # Fetch and print user details
    github.print_user_details()
