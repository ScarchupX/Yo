texto_num=str(input("inserte texto: "))
prefijo_verificar = str(input("inserte prefijo a verificar: "))
sufijo_verificar = str(input("inserte sufijo a verificar: "))

prefijo_inicio=texto_num.startswith(prefijo_verificar)
sujifo_final=texto_num.endswith(sufijo_verificar)

if prefijo_inicio and sujifo_final :
    print(f"si, inicia con el prefijo {prefijo_verificar} y termina con el sujifo {sufijo_verificar}")
elif prefijo_inicio and not sujifo_final:
    print(f"si inicia con el prefijo {prefijo_verificar}, pero no termina con el sujifo {sufijo_verificar}")
elif sujifo_final and not prefijo_inicio:
    print(f"no inicia con el prefijo {prefijo_verificar}, pero si termina con el sufijo {sufijo_verificar}")
else:
    print(f"no inicia ni con el prefijo {prefijo_verificar}, ni termina con el sufijo {sufijo_verificar}")



