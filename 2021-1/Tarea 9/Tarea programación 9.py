vacunas = {"Sinovac":["11.111.111-1", "12.345.678-9"],"Pfizer": ["8.978.657-3"],"CanSino": ["13.789.456-k"]}

dosis = {"11.111.111-1":[55,(2021,4,11),(2021,5,10)],"12.345.678-9":[47,(2021,6,3)],"8.978.657-3":[79,(2021,3,23)],"13.789.456-k":[40,(2021,5,18),(2021,6,10)]}

#Solicitud de datos
dia= int(input("Día: "))
mes= int(input("Mes: "))
año= int(input("Año: "))

op="s"
while op=="s":

    rut= input("Rut: ")

    fecha=()
    info=[]
    #En caso que la persona ya esté vacunada
    if rut in dosis:
        for persona in dosis:
            if rut==persona:
                fecha=(año,mes,dia)
                dosis[persona].append(fecha)
        for vacuna in vacunas:
            if rut in vacunas[vacuna]:
                print ("Seguna dosis. Paciente debe ser inoculaco con: ",vacuna)

    #Si no tiene ninguna dosis            
    else:
        edad=int(input("Edad: "))
        tipo=input("Tipo Vacuna: ")
        #Actualizar dosis
        fecha=(año,mes,dia)
        info.append(edad)
        info.append (fecha)
        dosis[rut]=info

        #Actualizar vacunas
        if tipo not in vacunas:
            vacunas[tipo]=rut
        else:
            for vacuna in vacunas:
                if tipo==vacuna:
                    vacunas[vacuna].append(rut)
    op=input("¿Desea continuar? (s/n)")
print("\n","Edades con más personas con esquema de inoculación completo: ") 

# creacion de diccionario, llave=edad y valor=cantidad
d={}
for per in dosis:
    if len(dosis[per])==3:
        edad1,fecha1,fecha2=dosis[per]
        if edad1 not in d:
            d[edad1]=0
        d[edad1]+=1

#Convertir el diccionario a lista de tuplas para obtener los resultados
lista=[]
for eda in d:
    lista.append((d[eda],eda))
    lista.sort()
    lista.reverse()

final=lista[0:3]
for elemento in final:
    cantidad,edad2=elemento
    print (edad2,"años: ",cantidad,"personas")
    
        


