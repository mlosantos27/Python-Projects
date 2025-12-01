def añadir_cliente(diccionario):
    NIF=(input("Dime tu NIF: "))
    nombre=input("Dime tu nombre: ")
    direccion=input("Dime tu dirección: ")
    telefono=(input("Dime tu teléfono: "))
    correo=input("Dime tu correo: ")
    preferente=input("Dime si eres preferente (s/n): ")
    if preferente=="s":
        preferente=True
    else:
        preferente=None
    diccionario[NIF]={"Nombre":nombre,"Dirección":direccion,"Teléfono":telefono,"Correo":correo,"Preferente":preferente}
    
def eliminar_cliente(diccionario):
    NIF=(input("Dime el NIF del cliente a eliminar: "))
    del diccionario[NIF]
    print("El cliente se eliminó correctamente")

def mostrar_datos(diccionario):
    NIF=(input("Dime el NIF del cliente a mostrar: "))
    print(f"{NIF}: {diccionario[NIF]}")
    
def nombre(diccionario):
    for clave,valor in diccionario.items():
        print(f"{clave}---{valor["Nombre"]}")

def preferentes(diccionario):
    for clave,valor in diccionario.items():
        if valor["Preferente"]==True:
            print(f"{clave}---{valor["Nombre"]}")
            
def menu():
    seguir=True
    while seguir==True:
        seleccion=int(input("1.Añadir cliente 2.Elminar cliente 3.Mostrar datos cliente 4.Mostrar todos los clientes 5.Mostrar preferentes 6.Salir: "))
        match seleccion:
            case 1:
                añadir_cliente(base_datos)
            case 2:
                eliminar_cliente(base_datos)
            case 3:
                mostrar_datos(base_datos)
            case 4:
                nombre(base_datos)
            case 5:
                preferentes(base_datos)
            case 6:
                seguir=False
                print("Hasta Luego")


base_datos={}
menu()