'''
Ejercicio 1
Escribir una función que reciba una lista de tuplas, 
y que devuelva un diccionario en donde las claves sean los primeros elementos de las tuplas, 
y los valores una lista con los segundos.

Por ejemplo:
lista = [ (’Hola’, ’don Pepito’), (’Hola’, ’don Jose’), (’Buenos’, ’días’) ]
print (tuplas_a_diccionario(lista))
Deberá mostrar: { ’Hola’: [’don Pepito’, ’don Jose’], ’Buenos’: [’días’] }

-----------------------------------------
'''
# def diccionario(lista):
#     diccionario = {}
#     for dato in lista:
#         if dato[0] not in diccionario:
#             diccionario.update({dato[0]:[dato[1]]})
#         elif dato[0] in diccionario:
#             diccionario[dato[0]].append(dato[1])

#     print(diccionario)

# lista = [("Hola","Don Pepito"),("Hola","Don José"),("Buenos", "Días")]
# diccionario(lista)

'''
Ejercicio 2
Escribir una función para imprimir un diccionario donde las claves sean los números 
entre 1 y n, n es un número natural recibido como parámetro (ambos incluidos) y los valores son 
los cuadrados de la clave

Ejemplo:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 
13: 169, 14: 196, 15: 225}
'''
# def diccionario(numero):
#     diccionario = {}
#     lista = range(1,numero+1)
#     for n in lista:
#         diccionario.update({n:n*n})
#     print(diccionario)

# diccionario(10)

'''
Ejercicio 3

a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones 
de cada palabra en la cadena.
Por ejemplo, si recibe "Qué lindo día que hace hoy"debe devolver: ’que’: 2, ’lindo’: 1, ’día’: 1, 
’hace’: 1, ’hoy’: 1

b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena de texto, 
y los devuelva en un diccionario.

'''
#a
# def contador(cadena):
#     diccionario = {}
#     cadena = cadena.lower()
#     lista = cadena.split()
#     for x in lista:
#         contador = 0
#         for y in lista:
#             if x == y:
#                 contador = contador + 1
#         diccionario.update({x:contador})
#     print (diccionario)

# cadena = "Que lindo dia que hace hoy"
# contador(cadena)

#b
# def contador(cadena):
#     diccionario = {}
#     cadena = cadena.lower()
#     lista = list(cadena)
#     for x in lista:
#         contador = 0
#         for y in lista:
#             if x == y:
#                 contador = contador + 1
#         diccionario.update({x:contador})
#     print (diccionario)

# cadena = "Que lindo dia que hace hoy"
# contador(cadena)