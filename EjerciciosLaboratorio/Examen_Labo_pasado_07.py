numbers_list=[1,2,3,4,5,6,7,8,9,16,25,36,49,64,81]
numeros_potencia=list()

for numero in numbers_list:
    if numero**0.5 in numbers_list:
        numeros_potencia.append(numero)
        
print(numeros_potencia)