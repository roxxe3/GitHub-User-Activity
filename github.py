import requests
import json



# Define the API endpoint
url = 'https://api.github.com/users/kamranahmedse/events'

event_types = {
    "CommitCommentEvent",
    "CreateEvent",
    "DeleteEvent",
    "ForkEvent",
    "GollumEvent",
    "IssueCommentEvent",
    "IssuesEvent",
    "MemberEvent",
    "PublicEvent",
    "PullRequestEvent",
    "PullRequestReviewEvent",
    "PullRequestReviewCommentEvent",
    "PushEvent",
    "ReleaseEvent",
    "SponsorshipEvent",
    "WatchEvent"
}

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print the type of the event
    for event in data:
        if event["payload"]["action"]:
            print(f"{event["payload"]["action"]} {event['type']} in {event["repo"]["name"]}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")