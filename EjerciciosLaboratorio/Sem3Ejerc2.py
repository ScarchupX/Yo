prim_medida=int(input("inserte 1° medida del triangulo: "))
seg_medida=int(input("inserte 2° medida del triangulo: "))
terc_medida=int(input("inserte 3° medida del triangulo: "))

if prim_medida==seg_medida==terc_medida:
    print("el triangulo es equilatero")
elif prim_medida==seg_medida!=terc_medida:
    print("el triangulo es isoceles")
elif prim_medida==terc_medida!=seg_medida:
    print("el triangulo es isoceles")
elif seg_medida==terc_medida!=prim_medida:
    print("el triangulo es isoceles")
else:
    print(" el triangulo es escaleno")
    
    