"""
This module contains functions for flask framework.
"""
# Import the Flask class from the Flask module
from flask import Flask

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route for the root URL ("/") and allow trailing slashes
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function handles the root URL ("/") and responds with "Hello HBNB!".

    Returns:
        str: A greeting message.
    """
    return 'Hello HBNB!'

# Define a route for "/hbnb" and allow trailing slashes
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function handles the "/hbnb" route and responds with "HBNB".

    Returns:
        str: A message indicating "HBNB".
    """
    return 'HBNB'

# Run the Flask application when this script is executed directly
if __name__ == '__main__':
    # Start the Flask development server
    app.run(host='0.0.0.0', port=5000)
