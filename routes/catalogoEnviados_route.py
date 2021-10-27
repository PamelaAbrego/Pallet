from flask import redirect, render_template, request, session, url_for
from funciones import Funciones
from logic.catalogos_logic import CatalogoLogic
import bcrypt
import requests
import pywhatkit

class CatalogoEnviados:
    @staticmethod
    def configure_routes(app):
        @app.route("/catalogoEnviados", methods=["GET", "POST"])

        def catologoEnviados():
            if request.method == "GET":
                Funciones().moveBdCatalogo()
                datos = Funciones().getAllCatalogoEnviados()
                return render_template("catalogoEnviados.html", data=datos)
            elif request.method == "POST":
                return render_template("catalogoEnviados.html", data=datos)