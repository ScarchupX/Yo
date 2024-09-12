texto_usuario=str(input("inserte su texto a desglozar: "))
inicio_subcadena= str(input("de que palabra quiere que inicie la nuevo texto: "))
final_subcadena= str(input("de que palabra quiere que termine la nuevo texto: "))

palabra_1=texto_usuario.find(inicio_subcadena)
palabra_2=texto_usuario.find(final_subcadena)
print(texto_usuario[palabra_1:palabra_2])

# si el usuario ingresa un incio y un final que no existe, no dara nada → tenemos que validad con for e if, pero ya despues 