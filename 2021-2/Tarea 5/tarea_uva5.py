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


# Escriba aquí su implementación de la función mostrar_letra



# Programa principal:

print("Bienvenidos al juego del adivinador de palabras!!!")

# Complete aquí el programa que implementa el juego

print("Fin del juego")
