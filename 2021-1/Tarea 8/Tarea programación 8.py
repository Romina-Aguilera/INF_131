def obtener_valor_caracteristica (caracteristicas,buscada):
    for carac in caracteristicas:
        caracter,puntaje=carac
        if caracter==buscada:
            return (puntaje)
    if caracter!=buscada:
        return (0)



def puntaje_amigo (amigo, caracteristicas):
    count=0
    puntos=0
    while count < len(amigo[1]):
        for cualidad in amigo [1]:
            punto=obtener_valor_caracteristica(caracteristicas,cualidad)
            puntos=puntos+punto
            count=count+1
    return (puntos)



características = [
('kawaii',10), ('leal',20), ('acusete',-10), ('avaro',-15), ('respetuoso',20),
('otaku',25),('lolero',25),('furro',-50),('vtuver',25),('mechero',-30)
]



amigos = [('Sneki',('leal','kawaii','vtuver')),
          ('Otaku-taku',('otaku','avaro','lolero','leal')),
          ('Maiga',('paciente','otaku','leal')),
          ('Mojojojo',('mechero','kawaii','Furro','lolero')),
          ('Seiya',('leal','acusete')),
          ('Vegeta',('otaku','avaro')),
          ('Kalila',('lolero','kawaii')),
          ('Grogu',('avaro','kawaii','lolero','otaku')),
          ('Freezer',('acusete','furro','otaku','lolero'))]

#Programa principal
i=0
puntaje=[]
nombres=[]
while i<len(amigos):
    amigo=amigos[i]
    nombre,caracter=amigo
    if "lolero" in caracter:
        cali=puntaje_amigo(amigo,características)
        nombres.append(nombre)
        puntaje.append(cali)
    i=i+1
#Busqueda participante1:
a=0
mayor1=0
while a < len(puntaje):
    if puntaje[a]>mayor1:
        mayor1=puntaje[a]
        part1=nombres [a]
    a=a+1
    
#Eliminar los datos ya encontrados de la lista
nombres.remove(part1)
puntaje.remove(mayor1)

#Busqueda participante2:
b=0
mayor2=0
while b<len(puntaje):
    if puntaje[b]>mayor2:
        mayor2=puntaje[b]
        part2=nombres[b]
    b=b+1

print ("Equipo seleccionado:")
print(part1,",",mayor1,"puntos")
print(part2,",",mayor2,"puntos")
