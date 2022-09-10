from flask import Flask, render_template

#Testing Branching

app = Flask(__name__)

#the view section to show the HTML page
@app.route("/")
def welcome():
    return render_template("main.html")

if __name__ == '__main__':
   app.run()