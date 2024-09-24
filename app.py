from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from database import Ajinori
app=Flask(__name__)
@app.route("/")
def top():
    ajinories = Ajinori.select()
    return render_template("top.html",ajinories=ajinories)

@app.route("/add")
def add():
    return render_template("add.html")

@app.route("/edit/<id>")
def edit(id):
    ajinori = Ajinori.get(id=id)
    print(ajinori.name)
    return render_template("edit.html",ajinori=ajinori)

@app.route("/new-ajinori",methods=["POST"])
def new():
    print(request.form["ajinori"])
    Ajinori.create(name=request.form["ajinori"])
    return redirect("/add")
app.run(debug=True)