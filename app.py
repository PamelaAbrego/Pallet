from flask import Flask, request, render_template, session, redirect, url_for
from flask_cors import CORS, cross_origin
from funciones import Funciones
import pywhatkit
from datetime import datetime
from logic.catalogos_logic import CatalogoLogic
from routes.personalizados_route import Personalizados
from routes.personalizadosEnviados_route import PersonalizadosEnviados
from routes.catalogo_route import Catalogo
from routes.catalogoEnviados_route import CatalogoEnviados

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
Personalizados.configure_routes(app)
PersonalizadosEnviados.configure_routes(app)
Catalogo.configure_routes(app)
CatalogoEnviados.configure_routes(app)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        # datos = Funciones().getAllCompras()
        # return render_template("form.html", data=datos)
        return render_template("main.html", datos = [])
    elif request.method == "POST":
        datos = Funciones().getAllCompras()
        nombre = request.form["nombre"]
        cel = request.form["celular"]
        celular = "+503"+str(cel)
        categoria = request.form["categoria"]
        articulo = request.form["articulo"]
        cantidad = request.form["cantidad"]
        data = request.form["data"]
        
        datos = Funciones().getAllCompras()
        for item in datos:
            print(item)
            mensaje = "Nombre: " + item[1] + ", celular: " + str(item[3]) + ", categoría: " + item[4] + " artículo: " + item[5] + " cantidad: " + str(item[6])
            celular = "+503"+str(item[3])
            # mensaje = "Nombre: " + nombre + " , celular: " + celular + " , categoria: " + categoria + " , articulo: " + articulo + " , cantidad: " + cantidad
            pywhatkit.sendwhatmsg_instantly(celular, mensaje,10,True,10)
            
        return render_template("main.html", data=datos)

def desaprobados():
    return render_template("desaprobados.html")

def index_materiales():
    return render_template("personalizados.html")

if __name__ == "__main__":
    app.run(debug=True)