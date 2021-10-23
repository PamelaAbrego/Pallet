from flask import Flask, request, render_template, session, redirect, url_for
from funciones import Funciones
import pywhatkit

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        datos = Funciones().getAllCompras()
        return render_template("form.html", data=datos)
    elif request.method == "POST":
        datos = Funciones().getAllCompras()
        nombre = request.form["nombre"]
        cel = request.form["celular"]
        celular = "+503"+str(cel)
        categoria = request.form["categoria"]
        articulo = request.form["articulo"]
        cantidad = request.form["cantidad"]
        mensaje = "Nombre: " + nombre + " , celular: " + celular + " , categoria: " + categoria + " , articulo: " + articulo + " , cantidad: " + cantidad
        pywhatkit.sendwhatmsg_instantly(celular, mensaje,10,True,10
        )
        return render_template("form.html", data=datos)


if __name__ == "__main__":
    app.run(debug=True)