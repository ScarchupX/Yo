primer_numero=int(input("inserte el primer numero: "))
segundo_numero=int(input("inserte el segundo numero: "))

ope_num=str(input("""que operacion quieres que se realice:
                  -suma
                  -resta
                  -multiplicacion
                  -division
                  
                  escoja: """))

suma_num= primer_numero+segundo_numero
resta_num= primer_numero-segundo_numero
multipl_num=primer_numero*segundo_numero
division_num=primer_numero/segundo_numero

if ope_num=="suma":
    print(f" la suma es {suma_num}")
elif ope_num=="resta":
    print(f"la resta es {resta_num}")
elif ope_num=="multiplicacion":
    print(f"la multiplicacion es {multipl_num}")
else:
    print(f"la division es {division_num}")
    
