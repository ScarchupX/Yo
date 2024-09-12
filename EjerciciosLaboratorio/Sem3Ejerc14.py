eleg_usuar=str(input("""jugara contra la maquina: 
                                                -piedra
                                                -papel
                                                -tijera
                                                escoja: """))

lista_cart=["piedra", "papel", "tijera"]
import random

maq_bot=random.choice(lista_cart)

if eleg_usuar=="piedra" and maq_bot=="piedra":
    print(f"empataron por escoger ambos {eleg_usuar}")
elif eleg_usuar=="piedra" and maq_bot=="papel":
    print("la maquina gana por eleccion de papel")
elif eleg_usuar=="piedra" and maq_bot=="tijera":
    print("usted gana por elegir piedra, maquina eligio tijera")
elif eleg_usuar=="papel" and maq_bot=="papel":
    print("empatan por eleccion de papel")
elif eleg_usuar=="papel" and maq_bot=="piedra":
    print("usted gana por eleccion de papel, maquina eligio piedra")
elif eleg_usuar=="papel" and maq_bot=="tijera":
    print("la maquina gana por eleccion de tijera")
elif eleg_usuar=="tijera" and maq_bot=="tijera":
    print("empatan, por elegir tijera")
elif eleg_usuar=="tijera" and maq_bot=="piedra":
    print("la maquina gana por elegir piedra")
elif eleg_usuar=="tijera" and maq_bot=="papel":
    print("usted gana por elegir tijera, maquina eligio papel")
    
    