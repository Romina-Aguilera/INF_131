#función para calcular nota final según media aritmetica
def nota_final_MA (n1,n2,n3):
    nota_MA= ((n1+n2+n3)/3)
    return round(nota_MA)

#Función para calcular nota final según media geometrica
def nota_final_MG (n1,n2,n3):
    nota_MG= (n1*n2*n3)**(1/3)
    return round (nota_MG)

#Función para calcular nota final según media vuelta
def nota_final_MV (n1,n2,n3):
    nota_MV=(n3*nota_final_MA(n1,n2,n3)**2)**(1/3)
    return round (nota_MV)

#Función para saber si aprueba o reprueba la asignatura
def aprobar (nota_MA, nota_MG, nota_MV):
    if nota_MA >= 55:
        num=1
        return num
    elif nota_MG >= 55:
        num=2
        return num
    elif nota_MV >=55:
        num= 3
        return num
    else:
        num=0
        return num

pedir_notas = True
while pedir_notas:
    ramo = input("Ingrese el nombre del ramo: ")

    if ramo == "salir":
        pedir_notas = False
        print("Fin del programa - Desarrollado por Kiwi :D!")
    else:
        n1 = int(input("Ingrese la 1era nota: "))
        n2 = int(input("Ingrese la 2era nota: "))
        n3 = int(input("Ingrese la 3era nota: "))

        #llamado a las funciones para calcular nota final
        nf_aritmetica = nota_final_MA (n1,n2,n3)
        nf_geometrica = nota_final_MG (n1,n2,n3)
        nf_vuelta = nota_final_MV (n1,n2,n3)

        print("Su nota final según la Media Aritmética es:", nf_aritmetica)
        print("Su nota final según la Media Geométrica es:", nf_geometrica)
        print("Su nota final según la Media Vuelta es:", nf_vuelta)
        
        #Llamado a la función para saber si se aprueba o se reprueba
        nf_aprobacion = aprobar (nf_aritmetica, nf_geometrica, nf_vuelta)

        if nf_aprobacion == 0:
            print("Lamentablemente no puedes aprobar con ninguna de las fórmulas :'c")
        elif nf_aprobacion == 1:
            print("Si la NF del ramo se calcula usando la Media Aritmética, entonces apruebas", ramo, ":D")
        elif nf_aprobacion == 2:
            print("Si la NF del ramo se calcula usando la Media Geométrica, entonces apruebas", ramo, ":D")
        elif nf_aprobacion == 3:
            print("Si la NF del ramo se calcula usando la Media Vuelta, entonces apruebas", ramo, ":D")


