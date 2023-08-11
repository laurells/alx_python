"""
Script: 1-hbtn_header.py
This script defines a function to fetch and display the value of the X-Request-Id header from a URL's response.
"""

import requests
import sys

def fetch_x_request_id(url):
    """
    Fetches the value of the X-Request-Id header from the response of a given URL.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        str: The value of the X-Request-Id header if found, or None if not found.
    """
    # Send a GET request to the provided URL
    response = requests.get(url)
    
    # Get the value of the X-Request-Id header from the response
    x_request_id = response.headers.get('X-Request-Id')
    return x_request_id

if __name__ == '__main__':
    """
    Main entry point of the script.
    """
    # Check the number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python 1-hbtn_header.py <URL>")
        sys.exit(1)

    # Get the URL from the command-line argument
    url = sys.argv[1]
    
    # Fetch the X-Request-Id value using the fetch_x_request_id function
    x_request_id = fetch_x_request_id(url)

    # Print the X-Request-Id value if found, or a message if not found
    if x_request_id:
        print(x_request_id)
    else:
        print()
