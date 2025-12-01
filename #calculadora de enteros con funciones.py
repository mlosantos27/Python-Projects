def suma(x,y):
    suma=x+y
    print(f"La suma de los números {x} + {y} es: {suma :.2f}")

def resta(x,y):
    resta=x-y
    print(f"La resta de los números {x} + {y} es: {resta :.2f}")

def multiplicación(x,y):
    multiplicación=x*y
    print(f"La multiplicación de los números {x} + {y} es: {multiplicación :.2f}")

def división(x,y):
    división=x/y
    print(f"La división de los números {x} + {y} es: {división :.2f}")
    
def menu(x,y):
    seguir=True
    while seguir==True:
        selección=int(input("Elige una opción: 1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir: "))
        match selección:
            case 1:
                suma(x,y)
            case 2:
                resta(x,y)
            case 3:
                multiplicación(x,y)
            case 4:
                división(x,y)
            case 5:
                seguir=False
                print("Hasta Pronto")
                
num1=float(input("Dime un número: "))
num2=float(input("Dime un número: "))
menu(num1,num2)