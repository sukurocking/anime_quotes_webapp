from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

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