def generar_palabra():
    # Retorna una palabra al azar desde una lista de palabras
    # No se preocupe por comprender cómo esta función hace su trabajo
    from random import choice
    lista = ["pandemia","programación","paralelepipedo","equilatero","panaderia","automatizacion"] # lista de palabras en minúsculas, sin tildes ni otros símbolos
    pala = choice(lista)
    return pala

def palabra_encriptada(palabra):
    encri = ""
    for x in palabra:
        encri+="_ "  # se cambia la letra de la palabra por un guión bajo y un espacio
    return encri

# Escriba aquí su implementación de la función verificar_letra
def verificar_letra(palabra,letra):
    if letra in palabra:
        return True
    else:
        return False

# Escriba aquí su implementación de la función mostrar_letra
def mostrar_letra(palabra,encriptada,letra):
    ver=verificar_letra(palabra,letra)
    if ver==True:
        i=0
        a=0
        encrip_final=""
        while a<len(encriptada)and i<len(palabra):
            if palabra[i]==letra:
                encrip_final=encrip_final+letra+" "
                i=i+1
                a=a+2
            else:
                encrip_final=encrip_final+encriptada[a]+" "
                i=i+1
                a=a+2
        return encrip_final
    else:
        return encriptada

# Programa principal:

print("Bienvenidos al juego del adivinador de palabras!!!")
print("dispones de 5 intentos máximos para adivinar la palabra")


palabra=generar_palabra()
msg_encrip=palabra_encriptada(palabra)
jugada=msg_encrip
print(msg_encrip)

i=0
while i<5:
    letra=str(input("Ingrese letra o palabra: "))
    if len(letra)>1:
        if letra==palabra:
            print("Felicitaciones, acertaste a la palabra")
            i=5
        else:
            print("Lo sentimos no es la palabra correcta")
            print(palabra)
            i=5

    else:
        if verificar_letra(palabra,letra)==True:
            print("acertaste!")
            i=i+1
            print("Intento",i)
            jugada=mostrar_letra(palabra,jugada,letra)
            print(jugada)

        else:
            print("La letra no es parte de la palabra!!")
            i=i+1
            print("Intento",i)
            jugada=mostrar_letra(palabra,jugada,letra)
            print(jugada)
print("Fin del juego")
