precio_prod=int(input("inserte el precio del producto: "))
cat_des=str(input("""a que categoria pertenece para su descuento:             
                      -estudiante
                      -jubilado
                      -empleado
                      -otros
                            :   """))

desc_estudiante=precio_prod*0.1
desc_jubilado=precio_prod*0.15
desc_empleado=precio_prod*0.05
desc_otros=precio_prod*1

if cat_des=="estudiante":
    print(desc_estudiante)
elif cat_des=="jubilado":
    print(desc_jubilado)
elif cat_des=="empleado":
    print(desc_empleado)
elif cat_des=="otros":
    print(desc_otros)
    
    
    