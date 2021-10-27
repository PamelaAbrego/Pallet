import pandas as pd
from logic.personalizados_logic import PersonalizadosLogic
from logic.catalogos_logic import CatalogoLogic

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

    def moveBdCatalogo(self):
        df = self.df
        datos = []
        if len(df.loc[:,'Nombre']) != len(CatalogoLogic().getAllCatalogo()):
            i = 0
            datos = []
            articulo = []
            cantidad = []
            while i <= len(df.loc[:,'Nombre'])-1:
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
                else:
                    articulo.append(0)
                    cantidad.append(0)
                i=i+1
            i =0
            m=0
            while i <= len(df.loc[:,'Nombre'])-1:
                catalogo = []
                if df.loc[:,'Producto'][i] == "Catálogo":
                    m=m+1
                    catalogo = [df.loc[:,'Marca temporal'][i],df.loc[:,'Nombre'][i],df.loc[:,'Correo'][i],df.loc[:,'Celular'][i], df.loc[:,'Categoría'][i], articulo[i], cantidad[i]]
                    datos.append(catalogo)
                i = i+1
            n= len(CatalogoLogic().getAllCatalogo())
            while n <= m-1:
                CatalogoLogic().insertCatalogo(datos[n][0],datos[n][1],datos[n][2], datos[n][3], datos[n][4], datos[n][5], datos[n][6])
                n = n+1
        return 1

    def getAllCatalogoSinEnviar(self):
        datos = CatalogoLogic().getAllCatalogoSinEnviar()
        return datos

    def getAllCatalogoEnviados(self):
        datos = CatalogoLogic().getAllCatalogoEnviados()
        return datos




