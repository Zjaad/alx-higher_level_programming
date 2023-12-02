import requests
from sys import argv
"""Takes 2 arguments in order to solve this challenge. task n10."""
if __name__ == '__main__':
    if len(argv) != 3:
        print("Usage: python script.py owner repository")
    else:
        owner = argv[1]
        repository = argv[2]
        link = f'https://api.github.com/repos/{owner}/{repository}/commits'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        try:
            r = requests.get(link)
            r.raise_for_status()
            commit = r.json()
            for c in commit[:10]:
                sha = c.get('sha')
                author = c.get('commit', {}).get('author', {}).get('name', 'Unknown')
                print(f"{sha}: {author}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
