from github_api import GitHubAPI

if __name__ == "__main__":
    token = "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"  
    github = GitHubAPI(token)
    github.print_user_details()

