
#Usando la funcion read_csv de pandas para leer un archivo csv y mostrar su contenido

import pandas as pd
archivo = pd.read_csv("archivos\\datos.cvs")
print(archivo)

#obteniendo una columna especifica del archivo csv
df = pd.read_csv("archivos\\datos.cvs")
print(df["nombre_columna"])

#obteniendo varias columnas especificas del archivo csv
df = pd.read_csv("archivos\\datos.cvs", names =["columna1", "columna2", "columna3"])
print(df[["columna1", "columna2", "columna3"]])

#Slicing de dataframe
cadena = "0123456789"
print(cadena[0:5])  #muestra los caracteres desde el indice 0 hasta el 4

#Ordenando el dataframe por una columna especifica (Edad)
df_ordenado_por_edad = df.sort_values(by = "Edad")
print(df_ordenado_por_edad)

#Ordenando el dataframe por una columna especifica (Edad) de forma descendente/inverso
df_ordenado_por_edad_descendente = df.sort_values(by = "Edad", ascending = False)
print(df_ordenado_por_edad_descendente)   #Viene configurado por defecto en True, es decir, ordena de forma ascendente

#concatenar 2 dataframes
df1 = pd.DataFrame({"columna1": [1, 2, 3], "columna2": ["a", "b", "c"]})
df2 = pd.DataFrame({"columna1": [4, 5, 6], "columna2": ["d", "e", "f"]})
df_concatenado = pd.concat([df1, df2])
print(df_concatenado)   

#Acceder a la primera fila del dataframe con head()
primera_fila = df.head(1)   #el encabezado del dataframe es 0
print(primera_fila)

#Accediendo a las primeras 5 filas del dataframe con head()
primeras_cinco_filas = df.head(5)
print(primeras_cinco_filas)

#Accediendo a las ultimas 5 filas del dataframe con tail()
ultimas_cinco_filas = df.tail(5)  #el encabezado del dataframe es -1
print(ultimas_cinco_filas)

#Accediendo a la cantidad de filas y columnas del dataframe con shape
cantidad_filas_columnas = df.shape
print(cantidad_filas_columnas)  

#Acceder a la cantidad de filas
cantidad_filas = df.shape[0]
print(cantidad_filas)

#Acceder a la cantidad de columnas
cantidad_columnas = df.shape[1]
print(cantidad_columnas)

#Accediendo cantidad filas y columnas desempaquetando
cantidad_filas, cantidad_columnas = df.shape
print(cantidad_filas)

#Obteniendo data estadistica del dataframe
estadistica = df.describe()
print(estadistica)

#Accediendo a un elemento especifico del dataframe con loc
elemento_especifico = df.loc[0, "columna1"]  #Accediendo al elemento de la fila 0 y la columna "columna1"
print(elemento_especifico)

#Accediendo a un elemento especifico del dataframe con iloc
elemento_especifico = df.iloc[2, 3]  #Accediendo al elemento de la fila 2 y la columna 3
print(elemento_especifico)

#Accediendo a todas las filas de una columna especifica con loc
columna_especifica = df.loc[:, "columna1"]  #Donde : indica que queremos todas las filas de la columna "columna1"
print(columna_especifica)   

#Accediendo a todas las filas de una columna especifica con iloc
columna_especifica = df.iloc[:, 1]  #Donde : indica que queremos todas las filas de la columna 1
print(columna_especifica)   

#Accediendo a todas las columnas de una fila especifica con loc
fila_especifica = df.loc[0, :]  #Donde : indica que queremos todas las columnas de la fila 0
print(fila_especifica)

#Accediendo a todas las columnas de una fila especifica con iloc
fila_especifica = df.iloc[0, :]  #Donde : indica que queremos todas las columnas de la fila 0
print(fila_especifica)  

#Accediendo a filas con variable mayor que 30 (Edad > 30)
filas_mayores_30 = df[df["Edad"] > 30]
print(filas_mayores_30) 
