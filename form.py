import pandas as pd
import pywhatkit

# pywhatkit.sendwhatmsg("+50375477081", "Hola",24,20,3) 
#pywhatkit.sendwhatmsg_instantly("+50371809799", "Hola",5,True,10)

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS-pbxp9Zx1lscyogsyNQU3TjLsqQTrrF1Is-YYHzzYEr-spE061aGMFFQ1s5Su-_NQtqh9yBJlNW_F/pub?gid=630035512&single=true&output=csv"
df = pd.read_csv(url)

print(df.loc[:,'Categoría'][0])

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
#x = df.loc[:,'ID']

print(articulo)
print(cantidad)
#print(len(x))

datos = []

i =0
# while i <= len(x)-1:
#    compra = [df.loc[:,'ID'][i],df.loc[:,'Marca temporal'][i],df.loc[:,'Pregunta 1'][i],df.loc[:,'Pregunta 2'][i]]
#    datos.append(compra)
#    i = i+1

#print(datos)

#cprint(df['Pregunta 1'][1])

#cprint(df['Pregunta 1'].value_counts())




#cprint(df.at[0,'Pregunta 1'])
