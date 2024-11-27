This project fetches and displays recent GitHub events for a specified user. It uses the GitHub API to retrieve the events and prints information about each event to the console.

project url : https://roadmap.sh/projects/github-user-activity

## Features

- Fetches recent GitHub events for a specified user.
- Displays information about different types of events, including:
  - Push events (number of commits pushed)
  - Issues events (issue actions)
  - Watch events (repository starred)
  - Pull request events
  - Issue comment events
  - Pull request review comment events
  - Pull request review events
  - Branch creation events

## Prerequisites

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/github-user-activity.git
    cd github-user-activity
    ```

2. Install the required dependencies:
    ```sh
    pip install requests
    ```

## Usage

1. Run the script with a GitHub username as an argument:
    ```sh
    python github.py <username>
    ```

    Replace `<username>` with the GitHub username you want to fetch events for.

## Example

```sh
python github.py kamranahmedse