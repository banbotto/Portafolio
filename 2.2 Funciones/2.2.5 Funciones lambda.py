
#Funciones lambda: son funciones anonimas, sin nombre y reutilizables
funcion = lambda x : expresion

#Creando una funcion lambda para multiplicar por 2
multiplicar_por_dos = lambda x : x*2 
    print(multiplicar_por_dos(5))          #Da como resultado 10 porque 5 x 2 = 10

#Es lo mismo que hacer esto sin que sea anonimo (lambda)
Def multiplicar_por_dos(x):
    return x*2


#Creando una funcion comun que diga los numeros que son par o no
numeros = [1,2,3,4,5,6,7,8,9,10]

def es_par (num):
    if(num%2==0):
        return True
 
#Usando filter con una funcion comun   
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))    #Resultado = [2,4,6,8,10]

#Creando misma funcion comun pero con lambda: Todo mas simplificado
numeros_pares = filter(lambda numero:numero%2 == 0, numeros)    #Resultado mucho mas simplificado
print(list(numeros_pares))    
                            