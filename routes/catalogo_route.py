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

        def catalogo():
            if request.method == "GET":
                Funciones().moveBdCatalogo()
                datos = Funciones().getAllCatalogoSinEnviar()
                return render_template("catalogo.html", data=datos)
            elif request.method == "POST":
                datos = Funciones().getAllCatalogoSinEnviar()
                for item in datos:
                    mensaje = "Nombre: " + item['Nombre'] + ", celular: " + str(item['Celular']) + ", categoría: " + item['Categoría'] + " artículo: " + item['Producto'] + " cantidad: " + str(item['Cantidad'])
                    celular = "+503"+str(item['Celular'])
                    pywhatkit.sendwhatmsg_instantly(celular, mensaje,10,True,10)
                    id = CatalogoLogic().getIdCatalogo(item['Fecha'], item['Nombre'], item['Celular'], item['Correo'], item['Categoría'], item['Producto'], item['Cantidad'])[0]['id']
                    CatalogoLogic().updateEnviado(id)

            return render_template("catalogo.html", data=datos)