texto_contar=str(input(" inserte su texto: "))
print(texto_contar.count(" ") + 1)

#aqui no hacemos que cuente las palabras, sino los espacios que hay entre ellos, que es 1 menos, por ende tenemos que sumar 1 para igualar, pero si el usuario escribe doble esacio, nos jodimos