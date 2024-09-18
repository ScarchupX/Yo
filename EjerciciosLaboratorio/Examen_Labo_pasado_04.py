number_list=[1,2,3,4,5,6,7,8,9]

lista_dobles=[]

for numero in number_list:
    if numero/2 in number_list:
        lista_dobles.append(numero)
    
print(lista_dobles)