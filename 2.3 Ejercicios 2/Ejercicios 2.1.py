
#Hoy falto el profesor de clases y los 7 chicos se organizaron para hacer la suya, uno de los chicos va a ser el profesor y otro su asistente
#(A) Pedir el nombre y la edad de los compañeros que vinieron a clase y ordenar los datos de menor a mayor.
#(B) El mayor es el profesor y el menor es el asistente: ¿Quien es quien

#(A)
def obtener_compañeros(cantidad_de_compañeros):              #Funcion para obtener al asistente y al profesor segun la edad
    compañeros = []                                          #Creando la lista de los compañeros
    for i in range(cantidad_de_compañeros):                  #Ejecutando un for para pedir informacion de cada compañero
        nombre = input ("ingrese el nombre del compañero: ")
        edad = int (input ("ingrese la edad del compañero: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)                         #Agregando informacion a la lista
    compañeros.sort(key=lambda x:x[1])                       #Ordenandolos de menor a mayor segun su edad
    asistente = compañeros [0][0]                            #Compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    profesor = compañeros [-1][0]                            #Para definir al asistente y al profesor.
    return asistente, profesor                               #Retornamos una tupla

asistene, profesor = obtener_compañeros(5)                   #Desempaquetamos lo que nos retorna la funcion

print(f"El profesor es: {profesor} y su asistente es: {asistente}")   #Mostrando el resultado

#Todos los conceptos aprendidos previamente estan en este ejercicio.