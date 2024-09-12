num_usu= int(input("inserte numero entero a comprobar si es par o no: "))
num_2=2
residuo=num_usu%num_2

if residuo==0:
    print(f"si, el numero {num_usu} es par")
else:
    print(f"no, el numero {num_usu} no es par")
    