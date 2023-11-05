from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route("/play")
def fun():
    return render_template("index.html",cantidad=3,color="blue")

@app.route("/play/<int:cantidad>")
def fun_2(cantidad):
    return render_template("index.html", cantidad = cantidad,color="blueviolet")

@app.route("/play/<int:cantidad>/<string:color>")
def fun_3(cantidad,color):
    return render_template("index.html",cantidad=cantidad, color=color)

if __name__=="__main__":
    app.run(debug=True)