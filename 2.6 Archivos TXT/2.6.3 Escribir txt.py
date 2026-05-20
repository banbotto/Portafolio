
#Sobreescribiendo texto en un archivo: write para escribir en un archivo, si el archivo ya existe se sobreescribe su contenido 
#"w" es el modo de apertura para escribir, si el archivo no existe se crea uno nuevo, si ya existe se borra su contenido y se escribe el nuevo texto
with open ("archivos\\texto_de_esteban.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola, este es un nuevo texto que se ha escrito en el archivo.")
    
    archivo.write("\nAsi se escribe una nueva linea que se agrega al archivo.")

#Agregando dos lineas con writelines
archivo.writelines(["\nEsta es la primera linea que se agrega al archivo.", "\nEsta es la segunda linea que se agrega al archivo."])

