
#creando un conjunto con funcion set
conjunto = set(["Dato1", "Dato2"])

#metiendo un conjunto dentro de otro conjunto con funcion frozenset
conjunto1 = frozenset({"dato 1","dato 2"})
conjunto2 = {conjunto1, "dato 3"}
print(conjunto2)

#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Verificando si es un subconjunto con funcion issubset
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#Verificando si es un superconjunto con funcion issuperset
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#Verificar si no hay algun numero en comun con funcion isdisjoint
resultado = conjunto2.isdisjoint(conjunto1)  

print(resultado)