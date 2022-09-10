from flask import Flask

app = Flask(__name__)

#the view section to show the HTML page
@app.route("/")
def welcome():
    return "Welcome to my APP"
