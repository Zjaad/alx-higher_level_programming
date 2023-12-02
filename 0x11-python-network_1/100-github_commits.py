#!/usr/bin/python3
""" takes 2 arguments in order to solve this challenge. task n10."""
from sys import argv
import requests
if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <repository owner>")
    else:
        repository = argv[1]
        owner = argv[2]
        link = f"https://api.github.com/repos/{owner}/{repository}/commits"
        
        try:
            r = requests.get(link)
            r.raise_for_status()
            commits = r.json()
            for c in range(10):
                sha = commits[c].get("sha")
                author = commits[c].get("commit").get("author").get("name")
                print(f"{sha}: {author}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        except IndexError:
            print("Less than 10 commits available.")
