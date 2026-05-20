
#Abriendo el archivo con with open
with open("archivos\\texto_de_esteban.txt", encoding="utf-8") as archivo:
    print(archivo.read())
    
    #Leemos el contenido
    contenido = archivo.read()
    
    #Mostrando el contenido
    print(contenido)
    
#No es necesario cerrar el archivo al usar with open