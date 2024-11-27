import requests
import sys


if len(sys.argv) < 2:
    print("Usage: python github.py <username>")
    sys.exit(1)

username = sys.argv[1]

# Define the API endpoint
url = f'https://api.github.com/users/{username}/events'


response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    for event in data:
        event_type = event['type']
        repo_name = event['repo']['name']
        
        if event_type == "PushEvent":
            print(f"Pushed {event['payload']['size']} commit(s) to {repo_name}")
        elif event_type == "IssuesEvent":
            print(f"{event['payload']['action'].capitalize()} an issue in {repo_name}")
        elif event_type == "WatchEvent":
            print(f"Starred {repo_name}")
        elif event_type == "PullRequestEvent":
            print(f"PullRequest in {repo_name}")
        elif event_type == "IssueCommentEvent":
            print(f"IssueComment in {repo_name}")
        elif event_type == "PullRequestReviewCommentEvent":
            print(f"PullRequestReviewComment in {repo_name}")
        elif event_type == "PullRequestReviewEvent":
            print(f"PullRequestReview in {repo_name}")
        elif event_type == "CreateEvent" and event['payload']['ref_type'] == 'branch':
            print(f"Created branch in {repo_name}")
        else:
            action = event.get('payload', {}).get('action', 'performed an action on')
            print(f"{action.capitalize()} {event_type} in {repo_name}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")