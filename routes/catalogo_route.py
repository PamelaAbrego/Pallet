from flask import redirect, render_template, request, session, url_for
from funciones import Funciones
from logic.catalogos_logic import CatalogoLogic
import bcrypt
import requests
import pywhatkit

class Catalogo:
    @staticmethod
    def configure_routes(app):
        @app.route("/catalogo", methods=["GET", "POST"])

        def catologo():
            if request.method == "GET":
                Funciones().moveBdCatalogo()
                datos = Funciones().getAllCatalogoSinEnviar()
                return render_template("catalogo.html", data=datos)
            elif request.method == "POST":
                
                return render_template("catalogo.html", data=datos)