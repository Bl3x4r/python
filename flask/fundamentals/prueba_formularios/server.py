from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# nuestra ruta de índice manejará la representación de nuestro formulari
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    print('Got Post info')
    print(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)