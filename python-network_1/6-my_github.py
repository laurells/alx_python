import requests
import sys

def fetch_user_id(username, token):
    """
    Fetches the user ID from GitHub API using Basic Authentication.

    Args:
        username (str): Your GitHub username.
        token (str): Your personal access token.

    Returns:
        int: Your user ID.
    """
    url = f"https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    user_info = response.json()
    return user_info.get('id')

if __name__ == '__main__':
    """
    Main entry point of the script.
    """
    username = sys.argv[1]
    token = sys.argv[2]
    
    user_id = fetch_user_id(username, token)
    print("Your GitHub user ID:", user_id)
