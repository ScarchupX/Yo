peso_usu=float(input("inserte su peso en Kg: "))
talla_usu=float(input("inserte su talla en M: "))

imc_usu=peso_usu/talla_usu**2

if imc_usu < 18.5:
    print(f"usted tiene un bajo peso con un IMC de {imc_usu: .2f}")
elif imc_usu>18.5 and imc_usu<24.9:
    print(f"usted tiene un peso normal con un IMC de {imc_usu: .2f}")
elif imc_usu>25 and imc_usu<29.9:
    print(f"usted tiene sobrepeso con un IMC de {imc_usu: .2f}")
elif imc_usu>30:
    print(f"usted tiene obsidad con un IMC de {imc_usu: .2f}")
    
# ese .2f significa, 2 puntos decimales, o como se duga, la cantidad de digitos hacia la derecha despues del entero
     