from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.hamburguesa import Hamburguesa

@app.route("/")
def hamburguesa():
    return render_template("index.html")

