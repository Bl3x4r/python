from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def inicial():
    if "num_rand" not in session:
        session["num_rand"] = random.randint(1,100)
    return render_template("index.html")

@app.route('/adivinar', methods=['POST'])
def adivinar():
    session["adiv"] = int(request.form["adivinar"])
    print(session['num_rand'])
    return redirect('/')

@app.route('/reiniciar')
def reiniciar():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug =True)