oracion="the cat in the hat is in the house"
oracion_lista=oracion.split(" ") #ya es una lista ['the', 'cat', 'in', 'the', 'hat', 'is', 'in', 'the', 'house']
oracion_lista=set(oracion_lista) #aqui es conjunto #{'the', 'in', 'house', 'is', 'cat', 'hat'}

elementos_unicos_lista=list(oracion_lista)


oracion_lista=oracion.split(" ") #ya es una lista ['the', 'cat', 'in', 'the', 'hat', 'is', 'in', 'the', 'house']
elementos_repetidos_conjunto={}
elementos_repetidos_conjunto=set(elementos_repetidos_conjunto)

for i in oracion_lista:
    if i not in elementos_unicos_lista:
        elementos_unicos_lista.append(i)
    if oracion.count(i)>1:
        elementos_repetidos_conjunto.add(i)

final_lfin=(elementos_unicos_lista, elementos_repetidos_conjunto)

print(final_lfin) 
























