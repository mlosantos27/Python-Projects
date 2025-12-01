try:
    numero=int(input("Introduce un numero entero: "))
    if numero<0:
        raise ValueError
except ValueError:
    print("Los datos introducidos no son correctos")
    numero=int(input("Introduce un numero entero: "))
num=numero
binario=[]
while num>0:
    resto=num%2
    binario.append(resto)
    num=num//2
else:
    binario.reverse()
    print(f"El número {numero} en forma binaria es: {binario}")
