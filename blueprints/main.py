from flask import Blueprint, render_template
import os

# Define main Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():

    # Serve the minified index.html
    return render_template('index.html')