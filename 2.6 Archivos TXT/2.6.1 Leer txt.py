
#Leer texto de un archivo: usando open para abrir un archivo con una codificacion universal (utf-8)
archivo = open ("archivos\\texto_de_esteban.txt",encoding="utf-8")
print(archivo.read())                                               #y read para leerlo 

#Leer una sola linea del texto
linea_1 = archivo.readline(1)
print(linea_1)

#Leer linea por linea
Lineas= archivo.readlines()
print(Lineas)

#cerrar el archivo
arhivo.close(archivo)