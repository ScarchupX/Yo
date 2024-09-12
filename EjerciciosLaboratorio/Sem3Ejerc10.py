long_metr=float(input("inserte la longitud en metros: "))
conv_uni=str(input("""a que unidad quiere transformar:
                      -Pies
                      -Pulgadas
                      -Yardas
                      escoge: """))

uni_pies=long_metr*3.281
uni_pulgadas=long_metr*39.37
uni_yardas=long_metr*1.094

if conv_uni=="pies":
    print(uni_pies)
elif conv_uni=="pulgadas":
    print(uni_pulgadas)
elif conv_uni=="yardas":
    print(uni_yardas)
    