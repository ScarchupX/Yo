cadenas_palabras=['education', 'automobile', 'imagination', 'population', 'celebration', 'eucalipto']
vocales={"a","e","i","o","u"}

cadenas_con_5_vocales=list()
for palabra in cadenas_palabras:
    if vocales.issubset(palabra):
        cadenas_con_5_vocales.append(palabra)
        
print(cadenas_con_5_vocales)

        


