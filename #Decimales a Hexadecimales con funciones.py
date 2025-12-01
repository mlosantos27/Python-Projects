#Decimales a Hexadecimales con funciones
def hexadecimal(num):
    hexa=""
    decimal=num
    while decimal>0:
       resto=int(decimal%16)
       match resto:
            case 10:
                hexa="A"+hexa
            case 11:
                hexa="B"+hexa
            case 12:
                hexa="C"+hexa
            case 13:
                hexa="D"+hexa
            case 14:
                hexa="E"+hexa
            case 15:
                hexa="F"+hexa        
            case _:
                hexa=str(resto)+hexa
       decimal=decimal//16
    print(f"El numero {num} en hexadecimal es: {hexa}")

num_decimal=int(input("Dime un número decimal: "))
hexadecimal(num_decimal)
