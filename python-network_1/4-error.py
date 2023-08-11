import requests
import sys

def fetch_and_display_response(url):
    """
    Fetches the response from the provided URL and displays the body.

    Args:
        url (str): The URL to send the GET request to.
    """
    response = requests.get(url)
    status_code = response.status_code
    content = response.text

    # Display the body of the response
    print(content)

    # Check if the HTTP status code is greater than or equal to 400
    if status_code >= 400:
        print("Error code:", status_code)

if __name__ == '__main__':
    """
    Main entry point of the script.
    """
    url = sys.argv[1]
    fetch_and_display_response(url)
