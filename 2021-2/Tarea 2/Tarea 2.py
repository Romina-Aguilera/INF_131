#p=peso
#a=alto paquete
#an= ancho paquete
#l= largo paquete
#v= volumen paquete (a*an*l)
#va=valor almacenaje paquete

volumen_total=0
costo_almacenaje=0

p1=float(input("Ingrese peso del paquete 1 [grs]: "))
a1=float(input("alto paquete 1 en [cm]: "))
an1=float(input("ancho paquete 1 en [cm]: "))
l1=float(input("largo paquete 1 en [cm]: "))
v1=round(a1*an1*l1,1)
va1=round((v1*155.87+p1*1200.15)**(1/3))
volumen_total+=v1
costo_almacenaje+=va1
print("Volumen paquete 1: ",v1," [cm3]")
print("Valor almacenaje paquete 1: $ ",va1)

print()

p2=float(input("Ingrese peso del paquete 2 [grs]: "))
a2=float(input("alto paquete 2 en [cm]: "))
an2=float(input("ancho paquete 2 en [cm]: "))
l2=float(input("largo paquete 2 en [cm]: "))
v2=round(a2*an2*l2,1)
va2=round((v2*155.87+p2*1200.15)**(1/3))
volumen_total+=v2
costo_almacenaje+=va2
print("Volumen paquete 2: ",v2," [cm3]")
print("Valor almacenaje paquete 2: $ ",va2)

print()

p3=float(input("Ingrese peso del paquete 3 [grs]: "))
a3=float(input("alto paquete 3 en [cm]: "))
an3=float(input("ancho paquete 3 en [cm]: "))
l3=float(input("largo paquete 3 en [cm]: "))
v3=round(a3*an3*l3,1)
va3=round((v3*155.87+p3*1200.15)**(1/3))
volumen_total+=v3
costo_almacenaje+=va3
print("Volumen paquete 3: ",v3," [cm3]")
print("Valor almacenaje paquete 3: $ ",va3)

print()

print("Volumen ocupado por los 3 paquetes: ",volumen_total," [cm3]")

print()

coord_x=float(input("Ingrese coord x del punto de destino: "))
coord_y=float(input("Ingrese coord y del punto de destino: "))
dist=round(((coord_x**2)+(coord_y**2))**0.5,1)
print("Distancia del traslado ", dist, "[KM]")
print()
print()

print("____________________________________")
print("DETALLE DE COBRO POR SERVICIO")
print("Almacenaje: $ ",costo_almacenaje)
traslado=round(dist*1500)
print("Traslado: $ ",traslado)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
total_pagar=round(traslado+costo_almacenaje)
print("Total a pagar $ ",total_pagar)
print("____________________________________")
print("Hasta pronto!!")
