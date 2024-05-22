def guardar_fecha (ai,mi,di,af,mf,df):
    lista_inicio=[ai,mi,di]
    lista_final=[af,mf,df]
    lista=[]
    lista.append(lista_inicio)
    lista.append(lista_final)
    return lista

def formar_tarea(i,nombre,estado,fecha):
    lista=[i,nombre,estado]
    for x in fecha:
        lista.append(x)
    return lista

def modificar_estado(lista,cambio):
    i=0
    while i <len(lista):
        if lista[i]!=lista[2]:
            lista.insert(2,cambio)
            lista.remove(lista[3])
            i=999999
        else:
            i+=1
    return lista

cont=0
Tareas=[]
flag=True
while flag:
    print("1.- Crear Tarea")
    print("2.- Modificar Tarea")
    print("3.- Consultar Tarea")
    print("4.- Salir")
    opcion=int(input("Ingrese opcion: "))
    print()

    if opcion==1:
        print("Selecciono la opción crear")
        nombre=input("Nombre: ")
        año_i=int(input("Año de Inicio: "))
        mes_i=int(input("Mes de Inicio: "))
        dia_i=int(input("Día de Inicio: "))
        año_f=int(input("Año de Finalización: "))
        mes_f=int(input("Mes de Finalización: "))
        dia_f=int(input("Día de Finalización: "))
        cont+=1
        estado="Pendiente"
        fecha=guardar_fecha(año_i,mes_i,dia_i,año_f,mes_f,dia_f)
        lista=formar_tarea(cont,nombre,estado,fecha)
        Tareas.append(lista)
        print("El id de la tarea será: ",cont)
        print("Tarea ingresada correctamente!!")
        print()

    elif opcion==2:
        print("Seleccionó la opción modificar")
        numero=int(input("¿Id de la tarea?: "))
        i=0
        while i<len(Tareas):
            if numero == Tareas[i][0]:
                print("Nombre: ",Tareas[i][1])
                print("Estado: ",Tareas[i][2])
                print("Fecha Inicio: ",Tareas[i][3])
                print("Fecha término: ",Tareas[i][4])
                nuevo_est=input("Indique el nuevo estado ")
                fin=modificar_estado(Tareas[i],nuevo_est)
                i=len(Tareas)+1
                print("Estado de la tarea, actualizado!!")
            else:
                if i==len(Tareas)-1:
                    print("Tarea no encontrada, ingrese un id válido")
                    i=len(Tareas)+1
                else:
                    i=i+1

    elif opcion==3:
        print("Selecciono la opcion consultar")
        categoria=input("Indique el nombre de la categoria que desea listar: ")
        vacia=[]
        vacia2=[]
        final=[]
        y=0
        tipo=0
        for x in Tareas:
            while y<len(x):
                if x[y]==categoria:
                    vacia.append(x)
                    vacia2.append(x[y+1])
                    y=y+1
                y=y+1
            y=0
        vacia2.sort()
        for a in vacia2:
            for b in vacia:
                for c in b:
                    if c==a:
                        final.append(b)
        print("Tareas que se encuentran en el estado",categoria)
        print("-----------------------------------------------")
        while tipo<len(final):
            tarea=final[tipo][0]
            name=final[tipo][1]
            fecha_i=final[tipo][3]
            fecha_t=final[tipo][4]
            tipo+=1
            print("Tarea: ",tarea," - ",name,"Inicio: ",fecha_i,"Fin: ",fecha_t)
        print("-----------------------------------------------")
        print()

    elif opcion==4:
        print("Selecciono la opcion Salir")
        print("Hasta pronto!!")
        flag=False
    else:
        print("Opcion no valida")

