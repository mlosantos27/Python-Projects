import os
import time
class Fibonacci():
    def __init__(self,longitud_sucesion):
        self.longitud=longitud_sucesion
        self.fibo=[0,1]
    def calcular(self):
        for i in range (self.longitud):
            nuevo=self.fibo[i]+self.fibo[i+1]
            self.fibo.append(nuevo)
    def mostrar(self):
        self.calcular()
        ancho=20
        for i in range(ancho+1): #creamos una barra de carga con un bucle en base a un ancho de caracteres que seleccionemos
            porcentaje=int((i/ancho)*100)
            os.system("cls") #importamos de la biblioteca os del modulo system que nos permite ejecutar comandos en la terminal (cls borra terminal en cada iteración)
            print ("Cargando resultado...")
            barra="#"*i + "-"*(ancho-i)
            print(f"{barra} {porcentaje}%")
            time.sleep(0.2)
        print(self.fibo)

print("SUCESIÓN DE FIBONACCI")
try:
    longitud_sucesion=int(input("Dime cuántos números quieres calcular: "))
    if longitud_sucesion<0:
        raise ValueError
    else:
        sucesion1=Fibonacci(longitud_sucesion)
        sucesion1.mostrar()
except ValueError:
    print("Valor introducido erróneo")