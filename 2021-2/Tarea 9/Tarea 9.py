def obtener_postulaciones (carreras,postulantes):
    d={}
    lista=[]
    for codigo,carrera in carreras:
        for nombre,cod,gen in postulantes:
            if cod==codigo:
                lista.append(nombre)
                d[carrera]=lista
        lista=[]
    return d

carreras = [
 ('INF','Ing. Civil en Informática'), ('ICO','Ing. Comercial'),
 ('IND','Ing. Civil Industrial'), ('QUI','Ing. Civil Química'),
 ('MAT','Ing. Civil Matemática'), ('IDP','Ing. en Diseño de Productos'),
 ('CON', 'Construcción Civil'), ('MEC','Ing. Civil Mecánica')
]


postulantes = [
 ("Ivonne Navia", 'ICO', 'F'), ("Gary Meza", 'IND', 'M'),
 ("Carlos Reyes", 'IND', 'M'), ("Cecilia Castro", 'INF', 'F'),
 ('Eduardo Villarroel', 'INF', 'M'), ("Ana Meza", 'ICO', 'F'),
 ('Claudia Sánchez', 'CON', 'F'), ("Sofía Arenas", 'INF', 'F'),
 ('Celso Vásquez', 'IND','M'), ("Natalia Ozerova", 'MAT', 'F'),
 ('Paula Soto', 'ICO','F'), ("Andrea Brereton",'MAT','F')
]

print("Postulación por carreras (sin ningún orden en particular):")
diccionario=obtener_postulaciones(carreras,postulantes)
for llave in diccionario:
    print("Carrera: ",llave)
    for x in diccionario[llave]:
        print(x)
    print()

#Extrae las carreras por gada vez que hay una mujer
lista=[]
for nombre,co,gen in postulantes:
    for x in diccionario:
        for y in diccionario[x]:
            if y==nombre:
                if gen=="F":
                    lista.append(x)

#Conteo de la cant de mujeres por carrera
dicc={}
for carrera in lista:
    if carrera not in dicc:
        dicc[carrera]=0
    dicc[carrera]+=1

print("Las 3 carreras con más postulantes mujeres (de mayor a menor):")
i=0
menor=float("inf")
while i<3:
    for llave in dicc:
        if dicc[llave] <= menor:
            print(llave)
            i=i+1
            menor=dicc[llave]

