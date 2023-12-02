from flask import Flask, request, render_template
import sqlite3
# import logging

# logging.basicConfig(level=logging.DEBUG)

# Initializing application
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

