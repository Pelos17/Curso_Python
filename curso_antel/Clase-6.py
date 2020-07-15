'''
Ejercicio 1.
Escribir una función que reciba una tupla de elementos e indique si se encuentran ordenados de
menor a mayor o no  (pueden usar las funciones max y min, pero cuidado,
no se pueden comparar tipos diferentes).
--------------------------------------------------
'''
# def ordenados(tupla):
#     ordenado = False
#     comparador = 0
#     for x in tupla:
#         if x > comparador:
#             ordenado = True
#             comparador = x
#         elif x < comparador:
#             ordenado = False
#             break
#     if ordenado == True:
#         print("Tupla Ordenada")
#     elif ordenado == False:
#         print ("Tupla Desordenada")

# tupla1 = (10,23,45,60)
# tupla2 = (23,24,21,56)
# ordenados (tupla1)

'''
Ejercicio 2. Dominó.
a) Escribir una función que indique si dos fichas de dominó encajan o no.
Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4).

b) Escribir una función que indique si dos fichas de dominó encajan o no.
Las fichas son recibidas en una cadena, por ejemplo: 3-4 2-5.
Nota: utilizar la función split de las cadenas.
-------------------------------------------------
'''
#a
# def domino(ficha1,ficha2):
#     encajan = False
#     for x in ficha1:
#         for y in ficha2:
#             if x == y:
#                 encajan = True
#     if encajan == True:
#         print("Encajan")
#     elif encajan == False:
#         print("No encajan")

# ficha1 = (1,3)
# ficha2 = (3,3)

# domino(ficha1,ficha2)

#b
# def domino(ficha1,ficha2):
#     encajan = False
#     ficha1 = ficha1.split("-")
#     ficha2 = ficha2.split("-")
#     for x in ficha1:
#         for y in ficha2:
#             if x == y:
#                 encajan = True
#     if encajan == True:
#         print("Encajan")
#     elif encajan == False:
#         print("No encajan")

# ficha1 = "4-5"
# ficha2 = "1-1"

# domino(ficha1,ficha2)

'''
Ejercicio 3
Escribir una función que reciba una lista de tuplas (apellido, nombre, inicial del segundo_nombre)
y devuelva una lista de strings donde cada uno contenga, primero el nombre,
luego la inicial con un punto, y luego el apellido.
-------------------------------------------------
'''
def nombres(lista):
    nueva_lista = []
    for persona in lista:
        datos = str(persona[1] + " " + persona[2] + "." + " " + persona[0])
        nueva_lista.append(datos)
    print(nueva_lista)
    return(nueva_lista)
    

lista = [("Vignolo","Juan","M"),("Pedroncino","Gloria","S"),("Vignolo","Mario","G")]

nombres(lista)