año_usu=int(input("inserta un año: "))

plam_t=año_usu%4
plam_z=año_usu%100
plam_w=año_usu%400
if plam_t==0 and plam_z!=0 :
    print("si, es año bisiestro")
elif plam_t==0 and plam_z==0 and plam_w==0:
    print("si, es año bisiestro")
else:
    print("no, no es año bisiestro")
    
    
    