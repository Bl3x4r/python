from flask_app.controllers import controlador_dojos, controlador_ninja
from flask import redirect
from flask_app import app

@app.route("/")
def main():
    return redirect("/dojos")
if __name__ == "__main__":
    app.run(debug = True)