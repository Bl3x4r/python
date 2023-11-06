from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def tablero_inicial():
    return render_template("index.html",columna = 8, fila= 8,col_1="red",col_2="black")

@app.route("/<int:fila>")
def tablero_fila(fila):
    return render_template("index.html", columna = 8, fila=fila,col_1="red",col_2="black")

@app.route("/<int:fila>/<int:columna>")
def tablero_columna(fila,columna):
    return render_template("index.html", fila=fila,columna=columna, col_1="yellow",col_2="fuchsia")

@app.route("/<int:fila>/<int:columna>/<string:col_1>/<string:col_2>")
def tablero_completo(fila,columna, col_1, col_2):
    return render_template("index.html", fila=fila, columna=columna, col_1=col_1,col_2=col_2)

if __name__=="__main__":
    app.run(debug = True)