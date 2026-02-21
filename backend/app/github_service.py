import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

def get_pr_files(owner: str, repo: str, pr_number: int):
    token = os.getenv("GITHUB_TOKEN")
    g = Github(token)

    repository = g.get_repo(f"{owner}/{repo}")
    pull_request = repository.get_pull(pr_number)

    files_data = []

    for file in pull_request.get_files():
        if file.filename.endswith(".py"):
            file_content = repository.get_contents(
                file.filename,
                ref=pull_request.head.sha
            )
            decoded_content = file_content.decoded_content.decode("utf-8")

            files_data.append({
                "filename": file.filename,
                "code": decoded_content
            })

    return files_data

def post_pr_comment(owner: str, repo: str, pr_number: int, comment: str):
    token = os.getenv("GITHUB_TOKEN")
    g = Github(token)

    repository = g.get_repo(f"{owner}/{repo}")
    pull_request = repository.get_pull(pr_number)

    pull_request.create_issue_comment(comment)