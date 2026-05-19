
#Creando una funcion de 3 Parametros
def frase(nombre,apellido,adjetivo):
    return F"Hola {nombre} {apellido}, eres muy {adjetivo}"

frase_resultante = frase("Esteban", "Botto", "capo")
print(frase_resultante)

#Utilizando keyword arguments: se pueden alterar el orden aqui e igual saldra con el mismo order previamente establecido
frase_resultante = frase(adjetivo = "capo", nombre = "Esteban", apellido = "Botto")
print(frase_resultante)

#Agregando a la misma funcion un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo = "tonto"):           #Adjetivo es la variable opcional pero le estamos dando un valor por defecto

    return f"Hola{nombre} {apellido}, eres muy {adjetivo}"
frase_resultante = frase("Esteban, Botto")
print(frase_resultante)