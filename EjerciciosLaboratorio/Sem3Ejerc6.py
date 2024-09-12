prim_num=int(input("inserte 1° numero: "))
segu_num=int(input("inserte 2° numero: "))
terc_num=int(input("inserte 3° numero: "))

if prim_num>segu_num:
    print(f"el numero {prim_num} es mayor que {segu_num} ")
    if prim_num>terc_num:
        print(f"tambien es mayor a {terc_num}")
    else:
        print(f"pero no es mayor a {terc_num}")

if segu_num>prim_num:
    print(f"el numero {segu_num} es mayor a {prim_num}")
    if segu_num>terc_num:
        print(f"tambien es mayor a {terc_num}")
    else:
        print(f"pero no es mayor a {terc_num}")
if terc_num>prim_num:
    print(f"el numero {terc_num} es mayor a {prim_num}")
    if terc_num>segu_num:
        print(f"tambien es mayor a {segu_num}")
    else:
        print(f"pero no es mayor a {segu_num}")
    
    