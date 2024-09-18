tupla_lista=[(2,4),(3,1),(5,2),(6,8),(7,5)]

lista_tupla_segundo_mayor=list()
for i in tupla_lista:
    if i[1]>i[0]:
        lista_tupla_segundo_mayor.append(i)

print(lista_tupla_segundo_mayor)