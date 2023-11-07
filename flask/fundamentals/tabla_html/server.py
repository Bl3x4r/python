from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def tabla():
    info_usuarios = [
        {'nombre' : 'Michael', 'apellido' : 'Choi'},
        {'nombre' : 'John', 'apellido' : 'Supsupin'},
        {'nombre' : 'Mark', 'apellido' : 'Guillen'},
        {'nombre' : 'KB', 'apellido' : 'Tonel'}
    ]
    return render_template("index.html" ,usuarios = info_usuarios)

if __name__ == '__main__':
    app.run(debug=True)
