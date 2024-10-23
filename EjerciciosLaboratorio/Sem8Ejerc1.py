#CONVERSOR DE TEMPERATURA   Celsius y Fahrenheit
while True:
    try:
        temperatura_C_F=float(input("inserte la temperatura que quiera convertir: "))
        unidad_temp=str(input("cual es la unidad en la que esta dicha temperatura, Fahrenheit (F) o Celsius(C): ")).upper()
        if unidad_temp not in ["C", "F"]:
            raise ValueError
        break
    except ValueError:
        print("ocurrio un poblema de valor")
    except TypeError:
        print("ocurrio un probema de tipo")

def funcion_convertidor():
    if unidad_temp=="C":
        convertido_fahrenheit=temperatura_C_F*9/5 +32
        return convertido_fahrenheit
    elif unidad_temp=="F":
        convertido_celsius=(temperatura_C_F-32)*5/9
        return convertido_celsius
    

if unidad_temp=="C":
    print(f"{temperatura_C_F} c° en Fahrenheit es {funcion_convertidor():.2f}")
elif unidad_temp=="F":
    print(f"{temperatura_C_F}F° en grados Celsius es {funcion_convertidor():.2f}")
    
    


    
    
































