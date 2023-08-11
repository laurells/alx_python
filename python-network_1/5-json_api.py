import requests
import sys

def search_user_by_letter(letter):
    """
    Sends a POST request to the given URL with the letter as a parameter.

    Args:
        letter (str): The letter to search for.

    Returns:
        dict: The JSON response content parsed into a dictionary.
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}
    response = requests.post(url, data=payload)
    
    try:
        response_json = response.json()
        return response_json
    except ValueError as e:
        return None

if __name__ == '__main__':
    """
    Main entry point of the script.
    """
    # Get the letter from the command-line argument
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    
    # Send the POST request and get the JSON response content
    response_json = search_user_by_letter(letter)

    # Check if the JSON response is valid and not empty
    if response_json is None:
        print("No response or invalid JSON")
    elif isinstance(response_json, dict) and response_json:
        user_id = response_json.get('id')
        user_name = response_json.get('name')
        print(f"[{user_id}] {user_name}")
    elif isinstance(response_json, dict):
        print("No result")
    else:
        print("Not a valid JSON")
