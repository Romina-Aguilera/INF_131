#Función para reemplazar palabras.

#Hola a todos como estan

def change(text,old,new):
    i=0

    while i<len(text):

        if old==text[i:i+len(old)]:

            recicle_1=text[0:i]
            recicle_2=text[i+len(old)+1:]
        i=i+1

    final=recicle_1+new+' '+recicle_2
    
    return final
    

text1=input('Ingrese texto: ')
text2=input('Ingrese definición: ')

#Contador de Emotes a remplazar

n_emotes=0

for a in text2:

    if a=='$':
        n_emotes+=1

i=0

final_text=text1

while i<n_emotes:

    emoji=''
    meaning=''
    recicle_1=''
    recicle_2=''
    a=0

    while a<len(text2) and text2[a]!='$':

        recicle_1=recicle_1+text2[a]
        a=a+1

    a=0

    while a<len(recicle_1) and recicle_1[a]!='*':

        emoji=emoji+recicle_1[a]
        a=a+1

    meaning=recicle_1[a+1:]
    meaning=meaning.upper()

    text2=change(text2,recicle_1,'')

    if i==0:

        final_text=change(final_text,emoji,meaning)

    else:

        final_text=change(final_text,emoji,' '+meaning)

    i+=1

print(final_text)
