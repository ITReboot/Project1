from github_api import GitHubAPI

if __name__ == "__main__":
    token = "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"  # Replace with your GitHub token
    github = GitHubAPI(token)


    github.print_user_details()

