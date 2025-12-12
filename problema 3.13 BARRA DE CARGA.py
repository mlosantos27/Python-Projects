import time
import os
def analisis_color(color):
    if color=="Dorado":
        print("El color pinta bien.")
    else:
        print("El color debería ser dorado.")
def analisis_aroma(aroma):
    if aroma=="Suave":
        print("Esta piña huele perfecta.")
    else:
        print("El olor debería ser suave.")
def analisis_peso(peso):
    if peso=="Pesada":
        print("La piña tiene un buen peso.")
    else:
        print("La piña debe madurar.")
def resultado(color,aroma,peso):
    ancho=20
    for i in range(ancho+1): #creamos una barra de carga con un bucle en base a un ancho de caracteres que seleccionemos
        porcentaje=int((i/ancho)*100)
        os.system("cls") #importamos de la biblioteca os el modulo system que nos permite ejecutar comandos en la terminal (cls borra terminal en cada iteración)
        print ("Cargando resultado...")
        barra="#"*i + "-"*(ancho-i)
        print(f"{barra} {porcentaje}%")
        time.sleep(0.2)
    if color=="Dorado" and aroma=="Suave" and peso=="Pesada":
        print("La piña está lista para comer.")
    else:
        print("A esa piña le quedan aspectos que mejorar para poder comerse.")
        
        
p1_color=input("Dime el color de la piña: ").capitalize()
analisis_color(p1_color)
time.sleep(1)
p1_aroma=input("Dime el aroma de la piña: ").capitalize()
analisis_aroma(p1_aroma)
time.sleep(1)
p1_peso=input("Dime si es pesada o no pesada: ").capitalize()
analisis_peso(p1_peso)
time.sleep(1)
resultado(p1_color,p1_aroma,p1_peso)