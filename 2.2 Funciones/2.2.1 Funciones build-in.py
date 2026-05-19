
numeros = {4,7,1,12,20,42}

#Encontrando el numero mayor de una lista con la funcion max
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#Encontrando el numero menor de una lista con la funcion min
numero_mas_pequeno = min(numeros)
print(numero_mas_pequeno) 

#Redondeando a 6 Decimales con la funcion round
numero = round(12.345678,2)
print(numero)

#El sistema te retorna un False cuando encuentra un 0, vacio, False, None con la funcion booleana
resultado_bool = bool(0)
print(resultado_bool)

#Retorna True si todos los valores son verdaderos con la funcion all
resultado_all = all([10,"true",[344,23]])
print(resultado_all)

#Suma todos los valores iterables con la funcion sum
suma_total = sum(numeros)
print(suma_total)