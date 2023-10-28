from flask import Flask, request, render_template
import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)

# Initializing application
app = Flask(__name__)

# Connecting to database


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quote", methods=["POST"])
def gen_quote_fn():
    conn = sqlite3.connect("animequotes.db")
    c = conn.cursor()
    random_quote_cursor = c.execute("select character, quote from quotes ORDER BY RANDOM() limit 1;")
    character, quote = random_quote_cursor.fetchall()[0]
    logging.debug(character)
    conn.close()
    return render_template("quote.html", my_character = character, my_quote = quote)