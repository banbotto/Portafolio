
#Creando una funcion que nos devuelva los numeros primos entre el 0 y el que pidamos

#Crear una funcion que verifique si un numero es primo
def es_primo(num):                       
    for i in range(2,num-1):             #verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese numero -1 
        if num%i==0: return False        #si es divisible por alguno retornamos false y termina el bucle
    return True

resultado = es_primo(7)
print(resultado)


#Creando funcion que retorne una lista con todos los primos
def primos_hasta(num):
    primos = []                                  #creamos la lista
    for i in range(2,num+1):                   
        resultado = es_primo(i)                  #verificamos si el valor es primo 
        if resultado == True: primos.append(i)   #en caso de que sea lo agregamos a la lista
    return primos                                #devolvemos la lista

resultado = primos_hasta(98)                     #creamos el resultado llamando a la funcion y lo mostramos
print(resultado)
