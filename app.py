"""
A simple Flask web application that provides number addition functionality.
"""

from flask import Flask, jsonify

app = Flask(__name__)

def add_numbers(a, b):
    """
    Adds two numbers and returns the result.
    """
    return a + b

@app.route('/')
def home():
    """Home endpoint that returns a welcome message."""
    return jsonify({"message": "Welcome to the adding service!"})

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    """Endpoint that adds two numbers."""
    result = add_numbers(a, b)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
