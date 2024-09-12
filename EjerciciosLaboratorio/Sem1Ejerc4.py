import math    #MODULO DE MATEMATICAS, SIN ESTO NO RECONOCE NADA DE PI

radio_circulo=int(input("inserte radio del circulo: "))
area_circulo= (radio_circulo**2)* math.pi
circunferencia_circulo = 2*radio_circulo*math.pi

print(f"el area del circulo es {area_circulo}", f"y su circunferencia es {circunferencia_circulo}")


