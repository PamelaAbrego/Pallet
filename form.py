import pandas as pd
import pywhatkit

# pywhatkit.sendwhatmsg("+50375477081", "Hola",24,20,3) 
#pywhatkit.sendwhatmsg_instantly("+50371809799", "Hola",5,True,10)
from datetime import datetime
print(datetime.today())

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTyj9XZujJrqeRlIafFoeIhQ5JrDcRybioZy5PVV7Z5ZoB9m-JOYPchfG-hEnE62XjLg4zO78aFfj4j/pub?output=csv"
df = pd.read_csv(url)

print(df)
print(df.loc[:,'Marca temporal'])
print(len(df.isna('Artículo Hogar')))

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
