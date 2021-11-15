from flask import redirect, render_template, request, session, url_for
from funciones import Funciones
from logic.personalizados_logic import PersonalizadosLogic
import bcrypt
import requests
import pywhatkit

class Personalizados:
    @staticmethod
    def configure_routes(app):
        @app.route("/personalizados", methods=["GET", "POST"])

        def personalizados():
            if request.method == "GET":
                Funciones().moveBdPersonalizados()
                datos = Funciones().getAllPersonalizadosSinEnviar()
                redirect("http://127.0.0.1:5000/")
                return render_template("personalizados.html", datos=datos)
            elif request.method == "POST":
                fecha = request.form["fecha"]
                nombre = request.form["nombre"]
                correo = request.form["correo"]
                cel = request.form["celular"]
                celular = "+503"+str(cel)
                descripcion = request.form["descripcion"]

                mensaje = "Nombre: " + nombre + ", celular: " + celular + ", descripción: " + descripcion
                pywhatkit.sendwhatmsg_instantly(celular, mensaje,10,True,10)

                Funciones().moveBdPersonalizados()
                datos = Funciones().getAllPersonalizadosSinEnviar()

                id = PersonalizadosLogic().getIdPersonalizado(fecha, nombre, cel, correo, descripcion)[0]['id']
                PersonalizadosLogic().updateEnviado(id)
                redirect("http://127.0.0.1:5000/")
                return render_template("personalizados.html", datos=datos)