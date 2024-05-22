frase=str(input("Frase original:"))
if frase[-1]==".":
    frase1=frase[:len(frase)-1]+" "
else:
    frase1=frase+" "

final=""
i=0
palabra=""

while i<len (frase1):
    if frase1[i] !=" ":
        palabra+=frase1[i]
        i=i+1

    else:
        if len(palabra)>=6:
            final=final+" "
            for letra in palabra:
                a=""
                if letra not in "aeiou":
                    a=a+letra
                    final=final+a
        else:
            final=final+" "+palabra
        i=i+1
        palabra=""

if final[0]==" ":
    final=final[1:]
if final[-1]==" ":
    final=final[:-2]

if frase [-1]==".":
    final=final+"."

print("Frase resultante:",final)

