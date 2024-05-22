#función para reemplazar palabras

def cambiar(texto,antiguo,nuevo):
    i=0
    while i<len(texto):
        if antiguo==texto[i:i+len(antiguo)]:
            r_1=texto[0:i]
            r_2=texto[i+len(antiguo)+1:]
        i=i+1
    final=r_1+nuevo+' '+r_2
    return final
    
texto1=input('Ingrese texto: ')
texto2=input('Ingrese definición: ')

#Contador de Emotes a remplazar
n_emotes=0
for a in texto2:
    if a=='$':
        n_emotes+=1

i=0
final_texto=texto1

while i<n_emotes:
    emoji=''
    significado=''
    r_1=''
    r_2=''
    a=0
#Buscador y remplazo significados
    while a<len(texto2) and texto2[a]!='$':
        r_1=r_1+texto2[a]
        a=a+1

    a=0
    while a<len(r_1) and r_1[a]!='*':
        emoji=emoji+r_1[a]
        a=a+1
    significado=r_1[a+1:]
    significado=significado.upper()

    texto2=cambiar(texto2,r_1,'')

    if i==0:
        final_texto=cambiar(final_texto,emoji,significado)
    else:
        final_texto=cambiar(final_texto,emoji,' '+significado)

    i+=1

print(final_texto)
