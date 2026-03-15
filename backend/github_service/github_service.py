import os
from github import Github
from dotenv import load_dotenv
import requests

load_dotenv()
GITHUB_API = "https://api.github.com"

import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

# create github client using token
def get_github_client():

    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise Exception("GITHUB_TOKEN not found in environment variables")

    return Github(token)


# fetch Python files from a PR
def get_pr_files(owner: str, repo: str, pr_number: int):

    g = get_github_client()

    repository = g.get_repo(f"{owner}/{repo}")
    pull_request = repository.get_pull(pr_number)

    files_data = []

    for file in pull_request.get_files():

        # only analyze python files
        if file.filename.endswith(".py"):

            file_content = repository.get_contents(
                file.filename,
                ref=pull_request.head.sha
            )

            decoded_content = file_content.decoded_content.decode("utf-8")

            files_data.append({
                "filename": file.filename,
                "code": decoded_content,
                "changes": file.changes,
                "additions": file.additions,
                "deletions": file.deletions
            })

    return files_data


# post a comment to the PR
def post_pr_comment(owner: str, repo: str, pr_number: int, comment: str):

    g = get_github_client()

    repository = g.get_repo(f"{owner}/{repo}")
    pull_request = repository.get_pull(pr_number)

    pull_request.create_issue_comment(comment)


# fetch PR files using github api
def fetch_pr_files(owner, repo, pr_number):
    url = f"{GITHUB_API}/repos/{owner}/{repo}/pulls/{pr_number}/files"
    response = requests.get(url)

    return response.json()