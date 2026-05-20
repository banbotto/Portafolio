
#Agregando texto a un archivo: write para escribir en un archivo, si el archivo ya existe se sobreescribe su contenido, pero si se abre el archivo en modo "a" (append) se agrega el nuevo texto al final del archivo sin borrar su contenido
#Usamos un bucle for para agregar varias lineas al archivo, cada linea se agrega con un salto de linea al final de cada linea para que se escriban en lineas separadas

with open ("archivos\\texto_de_esteban.txt", "a", encoding="utf-8") as archivo: 
    
    for i in range(5):
        archivo.write(f"Esta es la linea {i+1} que se agrega al archivo\n.")
        
