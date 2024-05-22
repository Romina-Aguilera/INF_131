#datos solicitados
S1=str(input("Nombre sucursal 1: "))
x_s1=int(input("Coordenada x: "))
y_s1=int(input("Coordenada y: "))
S2=str(input("Nombre sucursal 2: "))
x_s2=int(input("Coordenada x: "))
y_s2=int(input("Coordenada y: "))
S3= str(input("Nombre sucursal 3: "))
x_s3=int(input("Coordenada x: "))
y_s3=int(input("Coordenada y: " ))
print ("\n")

#contadores para cant. pedidos
cont=0
cont2=0
cont3=0
p="si"
ptotal=0


#inicio del ciclo

while p=="si":
    
    plato=0
    precio=0
    
    #cantidad de platos
    while plato!=-1:
        plato=int(input("Ingrese número del plato: "))
        if plato==1:
            precio=precio+4000
        elif plato==2:
            precio= precio+3000
        elif plato==3:
            precio=precio+3500
        
        
    #Precio del pedido y coordenadas del cliente solicitadas 
    print ("Total del pedido $ ",precio)
    x_cc= int(input("Ingrese coordenada x cliente: "))
    y_cc= int(input("ingrese coordenada y cliente: "))

    #Calculo y comparación de distancias
    dist1= ((x_s1-x_cc)**2+(y_s1-y_cc)**2)**0.5
    dist2= ((x_s2-x_cc)**2+(y_s2-y_cc)**2)**0.5
    dist3= ((x_s3-x_cc)**2+(y_s3-y_cc)**2)**0.5

    if dist1<=dist2 and dist1<=dist3:
        cont=cont+1
        print("Pedido será entregado por", S1)
    elif dist2<=dist1 and dist2<=dist3:
        cont2=cont2+1
        print("Pedido será entregado por", S2)
    elif dist3<=dist2 and dist3<=dist1:
        cont3=cont3+1
        print("Pedido será entregado por", S3)
    p=str(input("¿Desea registrar otro pedido?: "))
    print ("\n\n")

    ptotal=ptotal+precio

#Estadisticas finales
print("##### Estadísticas Finales #####")
print("Monto total recaudado", ptotal,"$")
print(S1,"entregó", cont, "pedidos")
print(S2, "entregó", cont2, "pedidos")
print(S3,"entregó",cont3, "pedidos")
