primera_lista=[1,2,3,4,5,6,7,8,9,10]
segunda_lista=[5,6,7,8,9,10,11,12,13,14,15]
tercera_lista=[10,11,12,13,14,15,16,17,18,19,20]

#parte a)   ♥5transformar a conjunto
lista_total=primera_lista+segunda_lista+tercera_lista
lista_total=set(lista_total)
print(lista_total)
#parte b) encontrar el conjutno que intersectan en las 3 listas
primera_lista=set(primera_lista)
segunda_lista=set(segunda_lista)
tercera_lista=set(tercera_lista)

conjunto_de_intersecciones=primera_lista.intersection(segunda_lista).intersection(tercera_lista)
print(conjunto_de_intersecciones)
print()

#parte c) encontrar el conjunto de todos los numeros que estan en al menos una lista
valores_unicos_conjuntos_parte1=primera_lista.symmetric_difference(segunda_lista)
valores_unicos_conjuntos_parte_total=valores_unicos_conjuntos_parte1.symmetric_difference(tercera_lista)
print(valores_unicos_conjuntos_parte_total)

#parte d) encontrar el conjunto de todos los numeros presentes en la primera lista pero no en la ultima
set_diferencia=primera_lista-tercera_lista
print(set_diferencia)
print()
#parte e) convierte los conjuntos obetenidos en tuplas y suma el primer y ultimo elemento de cada tupla
primera_lista=tuple(primera_lista)
segunda_lista=tuple(segunda_lista)
tercera_lista=tuple(tercera_lista)

primer_elemento_primera_lista=primera_lista[0]
ultimo_elemento_primera_lista=primera_lista[len(primera_lista)-1]
primer_elemtno_segunda_lista=segunda_lista[0]
ultimo_elemento_segunda_lista=segunda_lista[len(segunda_lista)-1]
primer_elemento_tercera_lista=tercera_lista[0]
ultimo_elemento_tercera_lista=tercera_lista[len(tercera_lista)-1]

print(f"la suma del primer y ultimo elemento de la primera lista es {primer_elemento_primera_lista+ultimo_elemento_primera_lista}\n y de la segunda lista es {primer_elemtno_segunda_lista+ultimo_elemento_segunda_lista}\n y de la tercera lista es {primer_elemento_tercera_lista+ultimo_elemento_tercera_lista}")















