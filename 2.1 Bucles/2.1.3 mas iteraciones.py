
#Creando las listas
frutas = ("banana","manzana","ciruela","pera","naranja","granada","durazno")
cadena = ("Hola Esteban")
numeros = [2,5,8,10]

#Iterando
for fruta in frutas:
    print(fruta)
    
#Evitar que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'Me voy a comer una {fruta}')
    
#Evitar que el bucle siga ejecutándose
for fruta in frutas:
    if fruta == 'pera':
        break
    print(f'Me voy a comer una {fruta}')
    
#Iterar una cadena de texto
for letra in cadena:
    print(letra)
    
#For en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
