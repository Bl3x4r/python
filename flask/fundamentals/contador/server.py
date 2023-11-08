from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route("/")
def num_vistas_raiz():
    if "contador" not in session:
        session["contador"] = 0
    else:
        session["contador"] += 1
    return render_template("index.html")

@app.route("/agregar_dos")
def agregar():
    session["contador"] += 1
    return redirect('/')

@app.route('/reiniciar')
def reiniciar():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug =True)