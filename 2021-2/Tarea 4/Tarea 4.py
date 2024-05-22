from random import randint

cant_int=int(input("Ingrese cantidad de intentos: "))
i=1
gana=0
pierde=0

while i<=cant_int:
    inten=int(input("Ingrese intento "+str(i)+":"))
    if inten<=999:
        print("El numero ingresado debe ser mayor a 999")
    else:
        ciclo=True
        copy=inten
        res=0
        suma=0
        while ciclo:
            res=inten%10
            inten=inten-res
            inten=inten//10
            suma=suma+res
            if inten==0:
                ciclo=False
            else:
                ciclo=True
        n=randint(1,100)
        if n%2==0:
            if suma>n:
                print("Intento ganado!! suma:",suma," umbral:", n)
                gana=gana+1
            else:
                print("Intento perdido!! suma:",suma," umbral:", n)
                pierde=pierde+1
        else:
            if suma<n:
                print("Intento ganado!! suma:",suma," umbral:", n)
                gana=gana+1
            else:
                print("Intento perdido!! suma:",suma," umbral:", n)
                pierde=pierde+1
        i=i+1

if gana>pierde:
    print("Felicidades, ganaste la partida")
elif gana==pierde:
    print("Has Empatado!")
else:
    print("Lo siento!!, perdiste la partida")
