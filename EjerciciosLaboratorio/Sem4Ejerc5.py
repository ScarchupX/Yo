frase_contar=str(input("inserte frase a contar: "))

vocales_fras="aeiouAEIOU"

contador_vocales=0

for i in frase_contar:
    if i in vocales_fras:
        contador_vocales+=1
        
print(contador_vocales)


 