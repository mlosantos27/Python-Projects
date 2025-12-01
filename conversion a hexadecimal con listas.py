numero=int(input("Introduce un numero decimal: "))
num=numero
hexadecimal=[]
while num>0:
    resto=str(num%16)
    hexadecimal.append(resto)
    num=num//16
else:
    hexadecimal.reverse()
    for i in range (len(hexadecimal)):
        if hexadecimal[i]=="10":
            hexadecimal[i]="A"
        elif hexadecimal[i]=="11":
            hexadecimal[i]="B"
        elif hexadecimal[i]=="12":
            hexadecimal[i]="C"
        elif hexadecimal[i]=="13":
            hexadecimal[i]="D"
        elif hexadecimal[i]=="14":
            hexadecimal[i]="E"
        elif hexadecimal[i]=="15":
            hexadecimal[i]="F"
    hexa="".join(hexadecimal)
    print (f"El numero {numero} en forma hexadecimal es: {hexa}")