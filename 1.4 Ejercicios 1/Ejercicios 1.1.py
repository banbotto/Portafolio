
#Promedio de Duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5


#Diferencias de Duración
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000// otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100


#Diferencias de Crudos (Videos sin editar)
crudo_promedio = 5
crudo_dalto = 3.5


#Calculando el porcentaje de tiempo vacío removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10 


#Mostrando Diferencias de Duracion (Ejercicio A)

print("El curso de Dalto dura:")
print(f' - {diferencia_con_min}% menos que el más rápido')
print(f' - {diferencia_con_max}% menos que el más lento')
print(f' - {diferencia_con_promedio}% menos que el promedio')
print("-------------")

#Mostrando la Cantidad de Espacios vacios que se remueven (Ejercicio B)
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {diferencia_con_promedio}% de tiempo vacio')
print("-------------")

#Mostrando las diferencias si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio *1000 // dalto_curso /100} horas de otros cursos')
print("-------------")