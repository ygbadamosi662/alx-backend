#!/usr/bin/env python3
"""
    Basic flask setup
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    The index/home page
    Returns:
        str: renders the template for display
    """
    return render_template('./0-index.html')


if __name__ == "__main__":
    app.run()
