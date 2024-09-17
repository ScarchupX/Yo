lista_10_estudiantes=[19,22,19,24,20,25,26,24,25,24]

#parte a)ordena la lista y encuentra la edad maxima y minima
lista_10_estudiantes.sort()  #esto ordena de menor a mayor profesor
print(f"ordenando seria{lista_10_estudiantes}")
edad_minima=lista_10_estudiantes[0]
edad_maxima=lista_10_estudiantes[len(lista_10_estudiantes)-1]
print(f"la edad minima  es {edad_minima} y la edad mas alta es {edad_maxima}")

#paret b) añade nuevamente la edad minima y maxima a la lista

lista_10_estudiantes.append(19)
lista_10_estudiantes.append(26)

print(lista_10_estudiantes)
print()

#parte c) encuentra la edad mediana si el numero de elmentos es par toma los dos del medio y divide
lista_10_estudiantes=[19,22,19,24,20,25,26,24,25,24]
    #primero ordenamos nuyvamente
lista_10_estudiantes.sort()
    #listo
num_de_elementos=len(lista_10_estudiantes)
    #como es par tomaremos el elemento 5 y 6
quinto_elemento=lista_10_estudiantes[4]
sexto_elemento=lista_10_estudiantes[5]

mediana=(quinto_elemento+sexto_elemento)/2
print(mediana)
print()
#Parte d) encuentra la edad promedio(suma todo y divide por su numero)
lista_10_estudiantes=[19,22,19,24,20,25,26,24,25,24]
num_alumnos=len(lista_10_estudiantes)
print(sum(lista_10_estudiantes)/num_alumnos)
#Parte e) encontra rango de edades

lista_10_estudiantes=[19,22,19,24,20,25,26,24,25,24]
lista_10_estudiantes.sort()
edad_minima=lista_10_estudiantes[0]
edad_maxima=lista_10_estudiantes[len(lista_10_estudiantes)-1]

rango_edades=edad_maxima-edad_minima

print(rango_edades)






