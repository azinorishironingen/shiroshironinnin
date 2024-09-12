from flask import Flask
from flask import render_template
app=Flask(__name__)
@app.route("/")
def top():
    return render_template("top.html")

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/edit")
def edit():
    return render_template("edit.html")

app.run(debug=True)