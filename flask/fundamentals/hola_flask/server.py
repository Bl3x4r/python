from flask import Flask, render_template  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return render_template("index.html")  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/dojo')
def success():
    return "Dojo"

@app.route('/say/<string:nombre>')
def hello(nombre):
    return f"Hello {nombre}"

@app.route('/hello')
def mensaje2():
    return render_template("hello.html",frase="Hola",numero_veces=5)


@app.route('/hello/<string:banana>/<int:num>')
def mensaje(banana,num):
    return render_template("hello.html",banana=banana, num= num)

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración