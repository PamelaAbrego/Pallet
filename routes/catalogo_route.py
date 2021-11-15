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
                envio = request.form["envio"]
                if envio == "todos":
                    datos = Funciones().getAllCatalogoSinEnviar()
                    for item in datos:
                        mensaje = "Hola " + item['Nombre'] + "🧡! Te saluda Andrea del equipo de Pallet & Home Decor✨. Te confirmamos tu orden del producto " + item['Producto'] + " y una cantidad de " + str(item['Cantidad']) + " artículo(s)." 
                        celular = "+503"+str(item['Celular'])
                        pywhatkit.sendwhatmsg_instantly(celular, mensaje,10,True,10)
                        id = CatalogoLogic().getIdCatalogo(item['Fecha'], item['Nombre'], item['Celular'], item['Correo'], item['Categoría'], item['Producto'], item['Cantidad'])[0]['id']
                        CatalogoLogic().updateEnviado(id)
                    redirect("http://127.0.0.1:5000/")
                    return render_template("main.html")
                if envio == "uno":
                    fecha = request.form["fecha"]
                    nombre = request.form["nombre"]
                    correo = request.form["correo"]
                    cel = request.form["celular"]
                    celular = "+503"+str(cel)
                    categoria = request.form["categoria"]
                    producto = request.form["articulo"]
                    cantidad = request.form["cantidad"]

                    mensaje = "Hola " +nombre + "🧡! Te saluda Andrea del equipo de Pallet & Home Decor✨. Te confirmamos tu orden del producto " + producto + " y una cantidad de " + cantidad + " artículo(s)." 
                    pywhatkit.sendwhatmsg_instantly(celular, mensaje,10,True,10)
                    id = CatalogoLogic().getIdCatalogo(fecha, nombre, cel, correo, categoria, producto, int(cantidad))[0]['id']
                    CatalogoLogic().updateEnviado(id)
                    redirect("http://127.0.0.1:5000/")
                    return render_template("main.html")
                return render_template("main.html")




