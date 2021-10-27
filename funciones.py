import pandas as pd
from logic.personalizados_logic import PersonalizadosLogic

class Funciones():
    def __init__(self):
        self.url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTyj9XZujJrqeRlIafFoeIhQ5JrDcRybioZy5PVV7Z5ZoB9m-JOYPchfG-hEnE62XjLg4zO78aFfj4j/pub?output=csv"
        self.df = pd.read_csv(self.url)

    def moveBdPersonalizados(self):
        df = self.df
        datos = []
        if len(df.loc[:,'Nombre']) != len(PersonalizadosLogic().getAllPersonalizados()):
            i =0
            while i <= len(df.loc[:,'Nombre'])-1:
                if df.loc[:,'Producto'][i] == "Personalizado":
                    personalizado = [df.loc[:,'Marca temporal'][i],df.loc[:,'Nombre'][i],df.loc[:,'Correo'][i],df.loc[:,'Celular'][i], df.loc[:,'Descripción'][i]]
                datos.append(personalizado)
                i = i+1
            n= len(PersonalizadosLogic().getAllPersonalizados())
            while n <= i-1:
                PersonalizadosLogic().insertPersonalizado(datos[n][0],datos[n][1], datos[n][2], datos[n][3], datos[n][4])
                n = n+1
        return 1

    def getAllPersonalizadosSinEnviar(self):
        datos = PersonalizadosLogic().getAllPersonalizadosSinEnviar()
        return datos

    def getAllPersonalizadosEnviados(self):
        datos = PersonalizadosLogic().getAllPersonalizadosEnviados()
        return datos


    def getAllCompras(self):
        df = self.df
        datos = []
        i=0
        articulo = []
        cantidad = []
        while i <= len(df.loc[:,'Nombre']) -1:
            if not pd.isna(df['Artículo Hogar'][i]):
                articulo.append(df.loc[:,'Artículo Hogar'][i])
                cantidad.append(df.loc[:,'Cantidad Hogar'][i])
            if not pd.isna(df['Artículo Cocina'][i]):
                articulo.append(df.loc[:,'Artículo Cocina'][i])
                cantidad.append(df.loc[:,'Cantidad Cocina'][i])
            if not pd.isna(df['Artículo Baño'][i]):
                articulo.append(df.loc[:,'Artículo Baño'][i])
                cantidad.append(df.loc[:,'Cantidad Baño'][i])
            if not pd.isna(df['Artículo Jardín'][i]):
                articulo.append(df.loc[:,'Artículo Jardín'][i])
                cantidad.append(df.loc[:,'Cantidad Jardín'][i])
            i=i+1
        i =0
        while i <= len(df.loc[:,'Nombre'])-1:
            compra = [df.loc[:,'Marca temporal'][i],df.loc[:,'Nombre'][i],df.loc[:,'Correo'][i],df.loc[:,'Celular'][i], df.loc[:,'Categoría'][i], articulo[i], cantidad[i]]
            datos.append(compra)
            i = i+1
        return datos

    def getAllPersonalizados(self):
        df = self.df
        i =0
        datos = []
        while i <= len(df.loc[:,'Nombre'])-1:
            pedido = [df.loc[:,'Marca temporal'][i],df.loc[:,'Nombre'][i],df.loc[:,'Correo'][i],df.loc[:,'Celular'][i], df.loc[:,'Descripción'][i]]
            datos.append(pedido)
            i = i+1
        return datos


    def mensajeEnviado(self, datos):
        celulares = []
        i=0
        while i <= len(self.df.loc[:,'ID'])-1:
            celulares.append(self.df.loc[:,'Celular'][i])
            i = i+1
        
        if celular in celulares:
            return True
        else:
            return False
