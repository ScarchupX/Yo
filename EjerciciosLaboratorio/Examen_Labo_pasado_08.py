lista_tuplas=[(2,4),(3,9),(5,25),(6,36),(8,49)]

lista_de_multiplos=list()

for (i,y) in lista_tuplas:
    if y%i==0:
        lista_de_multiplos.append((i,y))

print(lista_de_multiplos)







