from flask import Flask, request, render_template
import sqlite3
# import logging

# logging.basicConfig(level=logging.DEBUG)

# Initializing application
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quote", methods=["POST"])
def gen_quote_fn():
    
    # Creating sqlite connection to the database
    conn = sqlite3.connect("animequotes.db")
    c = conn.cursor()
    random_quote_cursor = c.execute("select character, quote from quotes ORDER BY RANDOM() limit 1;")
    
    # Fetching untupled character & quote from the database table quotes
    character, quote = random_quote_cursor.fetchall()[0]
    
    # Closing the connection
    conn.close()
    return render_template("quote.html", my_character = character, my_quote = quote)

@app.route("/addquote", methods = ["GET", "POST"])
def add_quote():
    return render_template("addquote.html")

@app.route("/quote_add_response", methods = ["POST"])
def quote_response():
    character = request.form.get("character")
    quote = request.form.get("quote")
    if not (character and quote):
        return render_template("quote_add_failure.html")
    try:
        conn = sqlite3.connect("animequotes.db")
        c = conn.cursor()
        c.execute("BEGIN TRANSACTION")
        c.execute("INSERT into quotes (character, quote) VALUES (?, ?)", (character, quote))
        conn.commit()
        conn.close()
        return render_template("quote_add_success.html")
    except sqlite3.IntegrityError:
        return render_template("quote_add_failure.html")
    
@app.route("/all_quotes", methods = ["GET", "POST"])
def display_all_quotes():
    conn = sqlite3.connect("animequotes.db")
    c = conn.cursor()
    all_quotes_cursor = c.execute("select character, quote from quotes")
    all_quotes = all_quotes_cursor.fetchall()
    conn.close()
    return render_template("all_quotes.html", quotes_list = all_quotes)