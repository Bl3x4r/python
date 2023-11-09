from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Don't let them know"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process",methods=['POST'])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['city'] = request.form['city']
    session['language'] = request.form['language']
    session['com'] = request.form['com']
    return redirect("/result")

@app.route("/result")
def show_result():
    return render_template("user.html")


if __name__ == "__main__":
    app.run(debug =True)