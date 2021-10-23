import pandas as pd

class Funciones():
    def __init__(self):
        self.url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS-pbxp9Zx1lscyogsyNQU3TjLsqQTrrF1Is-YYHzzYEr-spE061aGMFFQ1s5Su-_NQtqh9yBJlNW_F/pub?gid=630035512&single=true&output=csv"
        self.df = pd.read_csv(self.url)

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

    def mensajeEnviado(self, celular):
        celulares = []
        i=0
        while i <= len(self.df.loc[:,'ID'])-1:
            celulares.append(self.df.loc[:,'Celular'][i])
            i = i+1
        
        if celular in celulares:
            return True
        else:
            return False