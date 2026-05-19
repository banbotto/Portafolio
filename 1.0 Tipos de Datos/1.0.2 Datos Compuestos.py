
#Creando una lista (se pueden modificar sus elementos)
lista = ["Esteban Botto", "Soy Esteban", True, 1.75]
print(lista[0])

#Creando una tupla (no se pueden modificar sus elementos)
tupla = ("Esteban Botto", "Soy Esteban", True, 1.75)
print(tupla[0])

#Esto es válido
lista[3] = "Pedro"

#Esto no
#tupla[3] = "Pedro"

#Creando un conjunto (set) (no se accede a los elementos por índice, no almacena datos duplicados)
conjunto = {"Esteban Botto", "Soy Esteban", True, 1.75} 

#print(conjunto[3]) no puede acceder al elemento

#Creando un diccionario (la estructura es key : value y se separa con comas)
dicccionario = {
    "nombre" : "Esteban Botto",
    "canal" : "Soy Esteban",
    "está_emocionado" : True,
    "altura" : 1.75,
    "dato_duplicado" : "Soy Esteban"
}

print(dicccionario["canal"])