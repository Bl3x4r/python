from app_flask import app
from flask import render_template, redirect, session, request, session
import random

contador = 0


@app.route("/")
def inicio():
    if session["contador"] == 0:
        session["your_gold"] = 0
        session["place"] = 0
        session["gold"] = 0
        session["contador"] = aumentar_contador(session["contador"])
    
    print("Este es el lugar",session["place"])
    return render_template("index.html")

def aumentar_contador(contador):
    contador+=1
    return contador


@app.route("/procesar_dinero/<int:lugar>", methods=["POST"])
def procesar_dinero(lugar):
    if lugar == 1:
        session["gold"] = random.randint(10,20)
        session["your_gold"] += session["gold"]
        print("Cantidad ganada, granja",session["gold"])
        session["place"] = "Farm"
    if lugar == 2:
        session["gold"] = random.randint(5,10)
        session["your_gold"] += session["gold"]
        print("Cantidad ganada Cueva",session["gold"])
        session["place"] = "Cave"
    if lugar == 3:
        session["gold"] = random.randint(2,5)
        session["your_gold"] += session["gold"]
        print("Cantidad ganada Casa",session["gold"])
        session["place"] = "House"
    if lugar == 4:
        session["gold"] = random.randint(-50,50)
        session["your_gold"] += session["gold"]
        if session["gold"] < 0:
            print("Cantidad perdida Casino",session["gold"])
        else:
            print("Cantidad ganada Casino",session["gold"])
        session["place"] = "casino"
    session["contador"] = aumentar_contador(session["contador"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)