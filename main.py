from github_api import GitHubAPI

if __name__ == "__main__":
    token = "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"  
    github = GitHubAPI(token)


    github.print_user_details()

