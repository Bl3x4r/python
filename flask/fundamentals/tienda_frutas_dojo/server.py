from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    total = int(request.form['strawberry']) + int(request.form['raspberry'])+ int(request.form['apple'])
    print('Cobrando a '+ request.form['first_name'] + ' ' + request.form['last_name']+ ' por ' + str(total) + ' Frutas.')#se puede apreciar que al recargar la pagina, vuelve a hacer un cobro al mismo usuario
    print(request.form)
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    