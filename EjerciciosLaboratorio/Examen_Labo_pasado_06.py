numbers=[1,2,3,4,5,6,7,8,9,10,11]

lista_pares=list()
lista_impares=list()

for i in numbers:
    if i%2==0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

final_tupla=(lista_pares, lista_impares)

print(final_tupla)















