def cambiar_taxis(vacia,taxi):
    p=0
    while p<len(vacia):
        if taxi in vacia[p]:
            if vacia[p][2]=="d":
                vacia[p].insert(2,"o")
                vacia[p].remove("d")

                p=p+1
        else:
            p=p+1

    return vacia


taxis = [ ('t01',(2.5,3),'d'), ('t02',(98,323),'o'),
('t03',(323,32),'d'), ('t04',(0.2,3434),'d'), ('t05',(2323,454),'o'),
('t06',(64,75),'d'), ('t07',(23,4),'d'), ('t08',(254,740),'o'),
('t09',(1,1),'d'), ('t10',(53,3),'d'), ('t11',(2354,40),'o'),
('t12',(231,10),'o') ]
pasajeros = [ ('p01', (23,43)), ('p02', (2,545)), ('p03',(2,5)),
('p04', (65,76)), ('p05', (75,5)), ('p06',(12,7)),
('p07', (11,66)), ('p08', (22,56)),('p09',(88,9))
 ]



menor=float("inf")

for pasajero,cord in pasajeros:
    x1,y1=cord
    for codigo,coordenada,estado in taxis:
        x2,y2=coordenada
        if estado=="d":
            dist=((x2-x1)**2+(y2-y1)**2)*0.5
            if dist<menor:
                menor=dist
                taxi=codigo
    print("Taxi",taxi," asignado a trasladar el pasajero",pasajero)

    i=0
    tup=pasajero,cord
    if tup==pasajeros[i]:
        del (pasajeros[i])
    else:
        i=i+1

    vacia=[]
    for x in taxis:
        a=list(x)
        vacia.append(a)

    taxis=cambiar_taxis(vacia,taxi)
