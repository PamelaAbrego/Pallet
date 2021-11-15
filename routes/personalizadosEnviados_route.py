from flask import redirect, render_template, request, session, url_for
from funciones import Funciones
from logic.personalizados_logic import PersonalizadosLogic
import bcrypt
import requests
import pywhatkit

class PersonalizadosEnviados:
    @staticmethod
    def configure_routes(app):
        @app.route("/personalizadosEnviados", methods=["GET", "POST"])

        def personalizadosEnviados():
            if request.method == "GET":
                Funciones().moveBdPersonalizados()
                datos = Funciones().getAllPersonalizadosEnviados()
                
                return render_template("personalizadosEnviados.html", datos=datos)
            elif request.method == "POST":
                Funciones().moveBdPersonalizados()
                datos = Funciones().getAllPersonalizadosSinEnviar()
                return render_template("personalizados.html", datos=datos)