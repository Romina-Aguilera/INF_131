print("Bienvenidos a Kiwi-Factory")
tipo=str(input("¿Cuales productos comprará? (A) Ram 8GB, (B) SSD 256 GB, (C) RAM 8GB Y SSD 256GB: "))
if tipo == "A":
    cantidad= int(input("Cuantas unidades de RAM 8GB?: "))
    if cantidad==1:
        total_p=cantidad*18500
    elif cantidad==2 or cantidad==3:
        total_p=cantidad*18000
    else:
        total_p=cantidad*15500


elif tipo== "B":
    cantidad= int(input("Cuantas unidades de SSD 256GB?: "))
    if cantidad==1:
        total_p=cantidad*42200
    elif cantidad==2 or cantidad==3:
        total_p=cantidad*40000
    else:
        total_p=cantidad*35000


else:
    cantidad1=int(input("Cuantas unidades de RAM 8GB?: "))
    cantidad2=int(input("Cuantas unidades de SSD 256GB?: "))
    if cantidad1==1:
        total_p1=cantidad1*18500
    elif cantidad1==2 or cantidad1==3:
        total_p1=cantidad1*18000
    else:
        total_p1=cantidad1*15500

    if cantidad2==1:
        total_p2=cantidad2*42200
    elif cantidad2==2 or cantidad2==3:
        total_p2=cantidad2*40000
    else:
        total_p2=cantidad2*35000
    total_p=total_p1+total_p2

print ("Subtotal productos: $",total_p)


cod=str(input("Ingrese código de descuento: "))
if cod=="uwu-131":
    desc=round(total_p*0.1)
    if desc>100000:
        desc=100000
        print("Descuento: $",desc)
    else:
        print("Descuento: $",desc)
else:
    print("Codigo inválido")

if cod!="uwu-131":
    cod=str(input("Ingrese código de descuento: "))
    if cod=="uwu-131":
        desc=round(total_p*0.1)
        if desc>100000:
            desc=100000
            print("Descuento: $",desc)
        else:
            print("Descuento: $",desc)
    else:
        print("Codigo inválido")

if cod!="uwu-131":
    cod=str(input("Ingrese código de descuento: "))
    if cod=="uwu-131":
        desc=round(total_p*0.1)
        if desc>100000:
            desc=100000
            print("Descuento: $",desc)
        else:
            print("Descuento: $",desc)
    else:
        desc=0
        print("Descuento: $",desc)


subtotal=total_p-desc
print("Subtotal: $",subtotal)

envio=int(input("Envio a domicilio (1) / Retiro en tienda (2): "))
if envio==1:
    if subtotal>75000:
        env=0
        print("Costo envio: $",env)
    else:
        env=4990
        print("Costo envio: $",env)
else:
    env=0
    print("Costo envio: $",env)

Total= subtotal+env
print("Total: $",Total)

