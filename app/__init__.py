import os
from flask import Flask

# Initialize application
app = Flask(__name__)


@app.route('/')
def top_apps():
    return 'top_apps'
