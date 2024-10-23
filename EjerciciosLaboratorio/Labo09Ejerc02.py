"--------------TEMPERATURAS------------------------"
with open("datosTemp.csv", "r") as other_archive:
    other_archive.seek(15)
    posicion=other_archive.tell()
    lineas=other_archive.read()
    ordenado=lineas.split("\n")
lista_temperatura=[]
for i in ordenado:
    lista_temperatura.append(int(i))
num_datos_temp=len(lista_temperatura)
media_temperaturas=sum(lista_temperatura)/num_datos_temp
valor_min=min(lista_temperatura)
valor_max=max(lista_temperatura)
print(f"La media de la siguiente lista de temperaturas {lista_temperatura} es {media_temperaturas:.2f}",f"y el valor min y max respectivamente son {valor_min}│{valor_max}")
"---------------NOTASSSSSS--------------------------"
with open("datosCalificaciones.csv", "r") as other_archive2:
    other_archive2.seek(8)
    posicion2=other_archive2.tell()
    lineas2=other_archive2.read()
    ordenado2=lineas2.split("\n")
lista_notas=[]
for i in ordenado2:
    lista_notas.append(float(i))
num_datos_notas=len(lista_notas)
media_notas=sum(lista_notas)/num_datos_notas
valor_min2=min(lista_notas)
valor_max2=max(lista_notas)
print(f"La media de la siguiente lista de Notas {lista_notas} es {media_notas:.2f}",f"y el valor min y max respectivamente son {valor_min2}│{valor_max2}")
"---------------VENTAS--------------------------"
with open("datosVentas.csv", "r") as other_archive3:
    other_archive3.seek(9)
    posicion3=other_archive3.tell()
    lineas3=other_archive3.read()
    ordenado3=lineas3.split("\n")
lista_v=[]
for i in ordenado3:
    lista_v.append(int(i))
num_datos_notas=len(lista_v)
media_notas=sum(lista_v)/num_datos_notas
valor_min3=min(lista_v)
valor_max3=max(lista_v)
print(f"La media de la siguiente lista de Ventas {lista_v} es {media_notas:.2f}",f"y el valor min y max respectivamente son {valor_min3}│{valor_max3}")
"-------------------CALORIAS---------------------"
with open("datosCalorias.csv", "r") as other_archive4:
    other_archive4.seek(20)
    posicion4=other_archive4.tell()
    lineas4=other_archive4.read()
    ordenado3=lineas4.split("\n")
lista_c=[]
for i in ordenado3:
    lista_c.append(int(i))
num_datos_C=len(lista_c)
media_notas=sum(lista_c)/num_datos_C
valor_min4=min(lista_c)
valor_max4=max(lista_c)
print(f"La media de la siguiente lista de Calorias {lista_c} es {media_notas:.2f}",f"y el valor min y max respectivamente son {valor_min4}│{valor_max4}")