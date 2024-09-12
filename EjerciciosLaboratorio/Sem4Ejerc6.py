num_contar=int(input("inserte numero a contar: "))
suma_contador=0

while num_contar >0:
    ultimo_digito=num_contar%10
    suma_contador+=ultimo_digito                #lo que estamos haciendo es que al contador estamos sumando unicamente el ultimo digito, asi sucesivamente hasta que el # ingresado sea 0
    num_contar=num_contar//10
    
print(f"la suma de digitos es: {suma_contador}")