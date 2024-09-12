lista_notas=input("Inserte lista de notas usando comas: ")

notas=list(lista_notas.split(",")) 

new_lista=[float(x) for x in notas]

num_notas= len(new_lista)


print("tu promedio final es ", sum(new_lista)/num_notas)














