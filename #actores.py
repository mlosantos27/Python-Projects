def lista_nombres(lista):
    nombres_sin_duplicados=[]
    for elemento in lista:
        elemento=elemento.title()
        if elemento not in nombres_sin_duplicados:
            nombres_sin_duplicados.append(elemento)
    print(f"La lista de nombres sin duplicados es {nombres_sin_duplicados}")
    
def apellidos_orden_des(lista):
    nombres_sin_duplicados=[]
    for elemento in lista:
        elemento=elemento.title()
        if elemento not in nombres_sin_duplicados:
            nombres_sin_duplicados.append(elemento)
    nombres_ordenados=sorted(nombres_sin_duplicados, key=lambda x: x.split()[1], reverse=True)
    print(f"La lista de actores ordenada por apellidos es {nombres_ordenados}")
    
def nombre_corto(lista):
    nombres_sin_duplicados=[]
    for elemento in lista:
        elemento=elemento.title()
        if elemento not in nombres_sin_duplicados:
            nombres_sin_duplicados.append(elemento)
    nombre_apellido_corto=min(nombres_sin_duplicados, key=lambda x: len(x.split()[0]))
    nombre_corto=nombre_apellido_corto.split()[0]
    print(f"El nombre más corto de la lista es: {nombre_corto}")
    
def nombre_largo(lista):
    nombres_sin_duplicados=[]
    for elemento in lista:
        elemento=elemento.title()
        if elemento not in nombres_sin_duplicados:
            nombres_sin_duplicados.append(elemento)
    nombre_apellido_largo=max(nombres_sin_duplicados, key=lambda x: len(x.split()[0]))
    nombre_largo=nombre_apellido_largo.split()[0]
    print(f"El nombre más largo de la lista es: {nombre_largo}")



names=['arnold schwarzenegger', 'alec baldwin', 'antonio banderas',
'julian sequeira', 'sandra bullock', 'keanu reeves',
'julbob pybites', 'antonio banderas', 'julian sequeira',
'al pacino', 'brad pitt', 'matt damon', 'brad pitt',
'charlie chaplin', 'sandra bullock']

lista_nombres(names)
apellidos_orden_des(names)
nombre_corto(names)
nombre_largo(names)