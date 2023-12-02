from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

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