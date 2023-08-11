import requests

# Define the URL to fetch
url = 'https://alu-intranet.hbtn.io/status'

# Send a GET request to the URL
response = requests.get(url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Get the content of the response
    content = response.text

    # Print information about the response content
    print("Body response:")
    print("\t- type:", type(content))  # Display the type of the content
    print("\t- content:", content)      # Display the actual content
else:
    # Print a failure message along with the status code
    print("Failed to fetch the URL. Status code:", response.status_code)
