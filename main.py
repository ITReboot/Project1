from github_api import GitHubAPI

if __name__ == "__main__":
    token = os.getenv('User_GITHUB_TOKEN')
    github = GitHubAPI(token)

    
    github.print_user_details()
