from flask import render_template,request, redirect, session
from dojos_and_ninjas_app import app
from dojos_and_ninjas_app.models.Dojo import Dojo 
from dojos_and_ninjas_app.models.Ninja import Ninja
from datetime import datetime

@app.route("/dojos", methods=['GET'])
def showDojos():
    dojos = Dojo.get_all_dojos()
    return render_template("dojos.html", dojos=dojos)

@app.route("/dojos/add", methods=['POST'])
def addDojo():
    name = request.form['dojo_name']
    created_at = datetime
    updated_at = datetime

    newDojo = Dojo(id,name,created_at,updated_at)
    result = Dojo.add_dojo(newDojo)
    return redirect("/dojos")

@app.route("/dojos/<id>", methods=['GET'])
def show_dojo_information(id):
    dojos = Dojo.get_dojo(id)
    ninjas = Ninja.get_all_ninjas(id)
    return render_template("dojos_information.html", ninjas=ninjas, dojos=dojos)

