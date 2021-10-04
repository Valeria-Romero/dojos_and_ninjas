from datetime import datetime
from flask import render_template, request, session, redirect
from dojos_and_ninjas_app import app
from dojos_and_ninjas_app.models.Dojo import Dojo
from dojos_and_ninjas_app.models.Ninja import Ninja

@app.route("/ninjas", methods=['GET'])
def show_add_ninja_form():
    dojos = Dojo.get_all_dojos()
    return render_template("new_ninja.html", dojos=dojos)

@app.route("/ninjas/add", methods=['POST', 'GET'])
def add_ninja():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    dojo_id = request.form['dojos_id']
    created_at = datetime
    updated_at = datetime

    new_ninja = Ninja(id, first_name, last_name, age, dojo_id, created_at, updated_at)
    result = Ninja.add_new_ninja(new_ninja)

    return redirect ("/dojos")