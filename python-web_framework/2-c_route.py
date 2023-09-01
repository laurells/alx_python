# Import the Flask class and escape function from the Flask module
from flask import Flask, escape

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

# Define a route for "/c/<text>" and allow trailing slashes
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """
    This function handles the "/c/<text>" route and responds with "C " followed by the value of the text variable.

    Args:
        text (str): The text provided in the URL.

    Returns:
        str: A message containing "C " followed by the formatted text.

    Example:
        For "/c/this_is_cool", it returns "C this is cool".
    """
    # Replace underscores with spaces in the text
    formatted_text = escape(text.replace('_', ' '))
    return 'C {}'.format(formatted_text)

# Run the Flask application when this script is executed directly
if __name__ == '__main__':
    # Start the Flask development server
    app.run(host='0.0.0.0', port=5000)

