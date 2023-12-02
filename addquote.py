from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)


@app.route("/addquote", methods = ["GET", "POST"])
def add_quote():
    return render_template("addquote.html")
