import requests
import sys

def send_post_request(url, email):
    """
    Sends a POST request to the provided URL with the email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to send as a parameter.

    Returns:
        str: The response content of the POST request.
    """
    # Prepare the data payload with the email parameter
    payload = {'email': email}
    
    # Send a POST request to the provided URL with the payload
    response = requests.post(url, data=payload)
    
    # Return the response content
    return response.text

if __name__ == '__main__':
    """
    Main entry point of the script.
    """
    # Get the URL and email from the command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Send the POST request and get the response content
    response_content = send_post_request(url, email)
    
    # Print the response content
    print(response_content)
