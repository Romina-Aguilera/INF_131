
def obtener_calendario(nombre_archivo):
    lista_depa=[]
    lista_mes=[]
    meses = {"01":"Enero","02":"Febrero","03":"Marzo","04":"Abril","05":"Mayo",
         "06":"Junio", "07":"Julio", "08":"Agosto", "09":"Septiembre",
         "10":"Octubre", "11":"Noviembre", "12":"Diciembre"}
    dicc_nuevo ={}
    dicc_final={}
    archivo=open(nombre_archivo)
    for linea in archivo:
        x=linea.strip().split(";")
        nombre=x[0]
        depa=x[1]
        fecha=x[2]
        fecha_sepa=fecha.split("/")
        if depa not in dicc_nuevo:
            dicc_nuevo[depa]=[]
        dicc_nuevo[depa].append((nombre,fecha_sepa))

    for depa in dicc_nuevo:
        valor=dicc_nuevo[depa]
        for n in meses:
            mes=int(n)
            for nombre,fecha in valor:
                if mes==int(fecha[1]):
                    tupla=(meses[n],fecha[0],nombre)
                    if depa not in dicc_final:
                        dicc_final[depa]=[]
                    dicc_final[depa].append(tupla)


    for datos in dicc_final:
        documento=open(datos+".txt","a")
        mensaje1="CUMPLEAÑOS DEL DPTO DE {}\n".format(datos)
        documento.write(mensaje1)
        variable=dicc_final[datos]
        i=0
        resp=""
        while i<len(variable):
            mes=variable[i][0]
            dia=variable[i][1]
            persona=variable[i][2]
            if mes != resp:
                mensaje2="Funcionarios nacidos en el mes de {}\n".format(mes)
                documento.write("\n")
                documento.write(mensaje2)
                mensaje3="{} se celebra el cumpleaños de {}\n".format(dia,persona)
                documento.write(mensaje3)
                documento.write("###############################################")
                documento.write("\n")
                resp=mes
                i=i+1
            else:
                mensaje3="{} se celebra el cumpleaños de {} \n".format(dia,persona)
                documento.write(mensaje3)
                documento.write("###############################################")
                documento.write("\n")

                i=i+1

    archivo.close()


    return(dicc_final)

