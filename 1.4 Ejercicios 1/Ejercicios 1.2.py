frase = input("Dime una frase y te calculo cuanto tardas en decirla:  ")
palabras_palabras = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f' Dijiste {cantidad_de_palabras} palabras, y tardaste {cantidad_de_palabras/2} segundos en decirlo')
print(f' Dalto lo diria en {cantidad_de_palabras* 100 // 2 *1.3 / 100} segundos')
if cantidad_de_palabras > 120:
    print("Para, tampoco te pedi la biblia")
