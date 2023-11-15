from flask_app.controllers import controlador_dojos, controlador_ninja
from flask import render_template
from flask_app import app

if __name__ == "__main__":
    app.run(debug = True)