import requests

owner = "abillakanti"  
repo_name = "automateInfra"  

#  URL to access the GitHub 
url = f"https://api.github.com/repos/{owner}/{repo_name}"

# Send a GET request to the GitHub API
response = requests.get(url)

if response.status_code == 200:
    repo_data = response.json()
    # Print some details about the repository
    print(f"Repository: {repo_data['name']}")
    print(f"Description: {repo_data['description']}")

else:
    print(f"Failed to fetch repository. Status code: {response.status_code}")
