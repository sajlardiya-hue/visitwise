from flask import Flask, render_template, request
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    today = date.today().strftime("%A, %B %-d").upper()
    return render_template("home.html")

@app.route("/prep")
def prep():
    return render_template("prep.html")

@app.route("/summary", methods=["POST"])
def summary():
    return render_template("summary.html", d=request.form)

if __name__ == "__main__":
    app.run(debug=True)