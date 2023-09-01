from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    # Replace underscores with spaces in the text
    formatted_text = escape(text.replace('_', ' '))
    return 'C {}'.format(formatted_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
