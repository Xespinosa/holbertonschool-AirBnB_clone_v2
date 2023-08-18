#!/usr/bin/python3
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """prompt for the HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """prompt for the HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_cool():
    """variable text"""
    text = text.replace('_', "")
    return f"C {text}"


@app.route('/python/<text>', strict_slashes=False, default='is cool')
def python_cool():
    """python variable text"""
    text = text.replace('_', "")
    return f"Python {text}"


@app.route('/number/<n>', strict_slashes=False)
def numbers(n):
    """variable numbers"""
    if type(n) is int:
        return f"Python {n}"
    else:
        raise TypeError


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
