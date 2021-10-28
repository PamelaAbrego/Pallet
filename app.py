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
    return render_template("main.html")


if __name__ == "__main__":
    app.run(debug=True)