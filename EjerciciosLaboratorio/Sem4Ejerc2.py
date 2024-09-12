num_usu=int(input("Inserte un numero cualquiera: "))

# par_num=num_usu%2 → si usaramos esta variable dentro del bucle no se actualizaria, por eso prohibido usar esta varibale

while num_usu!=1 :
    if num_usu%2==0:
        num_usu//=2
    else:
        num_usu=num_usu*3 + 1 
    print(num_usu)
    
        
    

        
