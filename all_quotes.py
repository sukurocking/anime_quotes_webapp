from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/all_quotes", methods = ["GET", "POST"])
def display_all_quotes():
    conn = sqlite3.connect("animequotes.db")
    c = conn.cursor()
    all_quotes_cursor = c.execute("select character, quote from quotes")
    all_quotes = all_quotes_cursor.fetchall()
    conn.close()
    return render_template("all_quotes.html", quotes_list = all_quotes)