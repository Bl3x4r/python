from flask_app import app, render_template, request, redirect

from flask_app.models.user import User

@app.route("/")
def index():
    return redirect("/usuarios")

@app.route("/usuarios")
def mostrar():
    return render_template("mostrar.html", usuarios = User.get_all())

@app.route("/usuarios/nuevo")
def nuevo():
    return render_template("crear.html")


@app.route("/usuarios/crear", methods=["POST"])
def crear():
    User.save(request.form)
    return redirect("/usuarios")

if __name__ == "__main__":
    app.run(debug = True)