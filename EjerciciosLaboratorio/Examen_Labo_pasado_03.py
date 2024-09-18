lista__de_palabras=['apple', 'banana', 'pear', 'mango']
lista_abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

lista_de_Abecedario_no_presentes=lista_abecedario.copy()
for elemento in lista__de_palabras:
    for letra in elemento:
        if letra in lista_de_Abecedario_no_presentes:
            lista_de_Abecedario_no_presentes.remove(letra)

print(lista_de_Abecedario_no_presentes)















