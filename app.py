from flask import Flask, render_template, jsonify

import json

app = Flask(__name__)


def load_db():
    with open("sample_db.json") as f:
        return json.load(f)


db = load_db()


#the view section to show the HTML page
@app.route("/")
def welcome():
    entries = db
    return render_template("main.html", entries=entries)
