l1=[("one",1), ("two",2), ("three",3), ("four", 4), ("five",5)]
l2=[("one", 1), ("two",2), ("six",6)]

#parte a)crear una lista apartir de las 2
lista_total=l1+l2
#parte b)encontarr los elmetnos que son comunes en ambas listas y almacenarlas en un conjunto
l1=set(l1)
l2=set(l2)
conjunto_interseccion=l1.intersection(l2)
print(conjunto_interseccion)
print()
#parte c)encontrar los elementos que son unicos de las dos listas y almacenarlas en un conjunto
l1.update(l2) # o puedes usar "union"
print(l1)
print()
#parte d) crea una nueva lista y ordena 
l1=list(l1)
l1.sort(key=lambda x: x[1])
print(l1)




