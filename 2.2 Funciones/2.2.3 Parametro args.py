
#Forma no optima de sumar valores
def suma(a,b):               
    return a + b             #Este metodo acepta solo valores fijos: a y b, es simple pero limitado    

resultado = suma(5,3)
print(resultado)


#Utilizando el parametro args #Args permite que se agreguen mas valores después, sino siempre se esperara una cantidad fija
def suma(*numeros):
    return sum(numeros)      #El * acepta valores sueltos ilimitados, solo funciona si los valores estan separados por comas 
    
resultado = suma(4,5,6,7,8) 
print(resultado)


#Forma optima de sumar valores
def suma(numeros):           
    return sum([*numeros])   #EL [*] acepta cualquier coleccion iterable (listas,tuplas,set) pero ya no acepta valores separados

resultado2 = suma({5,3,9,10,20,4})
