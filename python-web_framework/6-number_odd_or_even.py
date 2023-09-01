"""
This module contains functions for flask framework.
"""
# Import the Flask class, escape function, and render_template function from the Flask module
from flask import Flask, escape, render_template

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
def c_with_text(text="is_cool"):
    """
    This function handles the "/c/<text>" route and responds with "C " followed by the value of the text variable.

    Args:
        text (str, optional): The text provided in the URL. Defaults to "is_cool".

    Returns:
        str: A message containing "C " followed by the formatted text.

    Example:
        For "/c/this_is_cool", it returns "C this is cool".
    """
    # Replace underscores with spaces in the text
    formatted_text = escape(text.replace('_', ' '))
    return 'C {}'.format(formatted_text)

# Define a route for "/python/<text>" and allow trailing slashes
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text="is_cool"):
    """
    This function handles the "/python/<text>" route and responds with "Python " followed by the value of the text variable.

    Args:
        text (str, optional): The text provided in the URL. Defaults to "is_cool".

    Returns:
        str: A message containing "Python " followed by the formatted text.

    Example:
        For "/python/this_is_cool", it returns "Python this is cool".
    """
    # Replace underscores with spaces in the text
    formatted_text = escape(text.replace('_', ' '))
    return 'Python {}'.format(formatted_text)

# Define a route for "/number/<int:n>" and allow trailing slashes
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    This function handles the "/number/<n>" route and responds with a message indicating whether "n" is a number.

    Args:
        n (int): The integer provided in the URL.

    Returns:
        str: A message indicating whether "n" is a number.
    """
    if isinstance(n, int):
        return '{} is a number'.format(n)
    else:
        return 'Not Found', 404

# Define a route for "/number_template/<int:n>" and allow trailing slashes
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    This function handles the "/number_template/<n>" route and responds with an HTML page displaying "Number: n".

    Args:
        n (int): The integer provided in the URL.

    Returns:
        str: An HTML page with "Number: n" inside the <h1> tag.
    """
    if isinstance(n, int):
        return render_template('number_template.html', number=n)
    else:
        return 'Not Found', 404

# Define a route for "/number_odd_or_even/<int:n>" and allow trailing slashes
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    This function handles the "/number_odd_or_even/<n>" route and responds with an HTML page indicating whether "n" is even or odd.

    Args:
        n (int): The integer provided in the URL.

    Returns:
        str: An HTML page with "Number: n is even|odd" inside the <h1> tag.
    """
    if isinstance(n, int):
        if n % 2 == 0:
            return render_template('number_odd_even_template.html', number=n, result='even')
        else:
            return render_template('number_odd_even_template.html', number=n, result='odd')
    else:
        return 'Not Found', 404

# Run the Flask application when this script is executed directly
if __name__ == '__main__':
    # Start the Flask development server, listening on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
