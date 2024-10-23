editor_usu=input("Que desea agregar al archivo archivo_de_pruedddddba.txt: ")

with open("archivo_de_pruedddddba.txt", "a+") as archivo_escritura_lectura:
    archivo_escritura_lectura.write(f"\nel contenido nuevo agregado por el usuario es: {editor_usu}")
    archivo_escritura_lectura.seek(0)
    lineas=archivo_escritura_lectura.read()   #EL READ PARA QUE SALGA TAL CUAL, EL READLINES PARA TDOEN UNA LISTA
print(lineas) 
