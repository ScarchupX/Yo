#CALCULADORA BASICA
while True:
    try:
        num1=float(input("inserte el primer numero: "))
        num2=float(input("inserte el segundo numero: "))
        operacion_elegir=input("""que operacion desea elegir:
                               -suma
                               -resta
                               -division
                               -multiplicacion
                               : """)
        if operacion_elegir not in ["suma", "resta", "division","multiplicacion"]:
            raise TypeError
        break
    except ValueError:
        print("error de valor")
    except TypeError:
        print("Error de tipo")
    
def funcion_sumar():
    sumar=num1+num2
    if operacion_elegir=="suma":
        return sumar
def funcion_resta():
    restar=num1-num2
    if operacion_elegir=="resta":
        return restar
def funcion_division():
    divisionn=num1/num2
    if operacion_elegir=="division":
        return divisionn
def funcion_multiplicar():
    multiplicacion=num1*num2
    if operacion_elegir=="multiplicacion":
        return multiplicacion
    
if operacion_elegir=="suma":
    print(f"la suma entre {num1} y {num2} es {funcion_sumar()}")
elif operacion_elegir=="resta":
    print(f"la resta entre {num1} y {num2} es {funcion_resta()}")
elif operacion_elegir=="division":
    print(f"la division entre {num1} y {num2} es {funcion_division}")
elif operacion_elegir=="multiplicacion":
    print(f"la multiplicacion entre {num1} y {num2} es {funcion_multiplicar()}")
    
    
    