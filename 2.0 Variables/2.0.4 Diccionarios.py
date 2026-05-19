
#creando diccionarios con dict()
diccionario = dict(nombre="Esteban",apellido="Botto")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Botto","Munoz"]):"jajaja"}

#creando diccionarios con funcion fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con funcion fromkeys() valor por defecto: "jajaja"
diccionario = dict.fromkeys(["nombre","apellido"],"jajaja")

print(diccionario)