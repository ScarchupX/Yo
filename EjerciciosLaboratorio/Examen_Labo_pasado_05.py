cadenas={'apple', 'banana', 'cherry', 'gran puta'}

cadenas_contando=set()

for i in cadenas:
    if i not in cadenas_contando:
        cadenas_contando.add((i,len(i)))
        
 
print(cadenas_contando)
    