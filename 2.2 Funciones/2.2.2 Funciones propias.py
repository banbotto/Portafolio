
#Creando funciones propias

#Para crear tu propia funcion simple debes colocar antes el indicador Def
def saludar():
    print("Hola Esteban te mando un saludo")
    
saludar()

#Crear una funcion con una variable
def saludar(nombre):
    print(f"Hola {nombre}, mi amigo ¿como estas?")
    
saludar("Esteban")

#Crear una funcion con varias variables: usando if, elif, else, .lower para identificar las minusculas en las variables y los dos puntos despues del else
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "Reina"
    elif (sexo == "hombre"):
        adjetivo = "Rey"
    else:
        adjetivo = "sexo neutro"
    print(f"Hola {nombre}, mi {adjetivo} ¿como estas?")
        
saludar("Camila","mujer")

#Crear una funcion que nos regrese valores: donde int hace que el sistema tome el caracter escogido en la variable: "98" -> "9"
def crear_contraseña_random(num):
    listado = "abcdfghij"
    num_entero = str(num)
    num = int(num_entero[0])    
    c1 = num - 2
    c2 = num - 4
    c3 = num - 5
    contraseña = f"{listado[c1]}{listado[c2]}{listado[c3]}{num * 2}"
    print(contraseña)

crear_contraseña_random(98)

#Guardar valores creados y volverlos a usar en una funcion que nos regresa valores
#EXPLICACION DETALLADA de esta funcion
                             
def crear_contraseña_random(num):
    listado = "abcdfghij"    #aca se crean caracteres aleatorios
    num_entero = str(num)    #aca se convierte el numero recibido a texto (string) porque los numeros enteros no pueden separarse por posiciones pero los strings si pueden usar indices como [0], [1], [2]
    num = int(num_entero[0]) #aca se toma el primer caracter del string: "98"[0]->"9" luego int convierte el texto a numero "9"-> 9 y al final el valor original de num es reemplazado por 9
    c1 = num - 2             #En estas 3 se crean variables para luego buscar letras dentro del string "listado" segun las determinadas maneras en que se busquen dichas posiciones del string
    c2 = num - 4
    c3 = num - 5
    contraseña = f"{listado[c1]}{listado[c2]}{listado[c3]}{num * 2}" #se calcula todo segun los parametros establecidos
    return(contraseña)       #return devuelve el valor creado para poder guardarlo y reutilizarlo posteriormente fuera de la funcion

password = crear_contraseña_random(0)        #aca se vuelve a usar la ultima funcion para usarla y guardarla dentro de la variable password
frase = f"Tu nueva contraseña es:{password}" #aca se establecen los nuevos parametros de la nueva funcion donde la ultima funcion se encuentra dentro de variable password
print(frase)                                 #aca se corre el resultado final

#Este ejercicio es complejo y rebuscado pero hay que acostumbrarse al enredo jejejeje

#Crear una funcion que nos regrese varios valores

def crear_contraseña_random(num):
    listado = "abcdfghij"    
    num_entero = str(num)   
    num = int(num_entero[0])
    c1 = num - 2             
    c2 = num - 4
    c3 = num - 5
    contraseña = f"{listado[c1]}{listado[c2]}{listado[c3]}{num * 2}"
    return contraseña,num      #Ahora guarda y devuelve la contraseña creada y el numero utilizado

#Desempaquetando la funcion
password,primer_numero = crear_contraseña_random(0) #Si entra "0" la funcion devuelve 0 de primer valor: password = igf0 y segundo valor: primer_numero = 0 porque esta Desempaquetado y se optimiza el proceso

#Mostrando varios resultados obtenidos
print(f"Tu contraseña nueva es: {password}")
print(f"El numero utilizado para crearla fue: {primer_numero}") 