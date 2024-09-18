numeros=[2,3,5,10,15,20,25]

lista_multiplos=[]
for numero in numeros:
    contador_de_multiplos=0
    for numero2 in numeros:
        if numero!=numero2 and numero%numero2==0:
            contador_de_multiplos+=1
    if contador_de_multiplos>=2:
        lista_multiplos.append(numero)
        
print(lista_multiplos)
