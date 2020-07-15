'''
Ejercicio 1. Dada una lista de números enteros, escribir una función que:
a) Devuelva la sumatoria y el promedio de los valores.
b) Devuelva una lista con el factorial de cada uno de esos números.

------------------------------------------

Ejercicio 2. Dada una lista de números enteros y un entero k, escribir una función que:
a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
b) Devuelva una lista con aquellos que son múltiplos de k.


------------------------------------------

Ejercicio 3: Escriba una función que reciba una lista de palabras y devuelva una segunda lista, igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino de crear una lista distinta)
Ejemplo:
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Alberto
Dígame la palabra 2: Carmen
Dígame la palabra 3: Benito
Dígame la palabra 4: Daniel
La lista creada es: ['Alberto', 'Carmen', 'Benito', 'Daniel']
La lista inversa es: ['Daniel', 'Benito', 'Carmen', 'Alberto']

------------------------------------------------------------

Ejercicio 4: Escriba una función que reciba dos listas de palabras y que imprima las siguientes listas: 
Lista de palabras que aparecen en las dos listas.
Lista de palabras que aparecen en la primera lista, pero no en la segunda.
Lista de palabras que aparecen en la segunda lista, pero no en la primera.
Lista de palabras que aparecen en ambas listas.
'''

#Ejercicio 1
# import math
# def sumatoria(lista):
#     contador = 0
#     factoriales=[]
#     for x in lista:
#         contador = contador + x
#         promedio = contador / len(lista)
#         factoriales.append(math.factorial(x))
#     print(contador)
#     print(promedio)
#     print(factoriales)

# sumatoria([1,2,3,4,5,6,7,8])

#Ejercicio 2
'''
Ejercicio 2. Dada una lista de números enteros y un entero k, escribir una función que:
a) Devuelva tres listas, una con los menores, otra con los mayores y otra con los iguales a k.
b) Devuelva una lista con aquellos que son múltiplos de k.
'''
# def listador(lista,entero):
#     mayores = []
#     menores = []
#     iguales = []
#     multiplos = []
#     for n in lista:
#         if n > entero:
#             mayores.append(n)
#         elif n < entero:
#             menores.append(n)
#         elif n == entero:
#             iguales.append(n)
#     for y in lista:
#         if y%entero == 0:
#             multiplos.append(y)
#     print("Lista de Mayores:",mayores)
#     print("Lista de Menores:",menores)
#     print("Lista de Iguales:",iguales)
#     print("Lista de Multiplos:",multiplos)

# lista = []
# for x in range(0,1000):
#     lista.append(x)

# listador(lista,12)

#Ejercicio 3
'''
Ejercicio 3: Escriba una función que reciba una lista de palabras y devuelva una segunda lista, 
igual a la primera, pero al revés (no se trata de escribir la lista al revés, 
sino de crear una lista distinta)
Ejemplo:
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Alberto
Dígame la palabra 2: Carmen
Dígame la palabra 3: Benito
Dígame la palabra 4: Daniel
La lista creada es: ['Alberto', 'Carmen', 'Benito', 'Daniel']
La lista inversa es: ['Daniel', 'Benito', 'Carmen', 'Alberto']
''' 

# def ordena_palabras(cantidad=0):
#     cantidad = (int(input("Dígame cuántas palabras tiene la lista:")))
#     lista_ordenada = []
#     lista_desordenada = []

#     for x in range(1,cantidad+1):
#         palabra=input("Dígame la palabra {}: ".format(x))
#         lista_ordenada.append(palabra)
#         lista_desordenada[0:0] = [palabra]
#     print("Palabras Ordenadas",lista_ordenada)
#     print("Palabras Desordenadas",lista_desordenada)

# ordena_palabras()

#Ejercicio 4
'''
Ejercicio 4: Escriba una función que reciba dos listas de palabras y que imprima las siguientes listas: 
Lista de palabras que aparecen en las dos listas.
Lista de palabras que aparecen en la primera lista, pero no en la segunda.
Lista de palabras que aparecen en la segunda lista, pero no en la primera.
Lista de palabras que aparecen en ambas listas.
'''
# def compara_listas(lista1,lista2):
#     repetidas = []
#     no_en_1 = []
#     no_en_2 = []
#     for x in lista1:
#         if x in lista2:
#             repetidas.append(x)
#         elif x not in lista2:
#             no_en_2.append(x)
#     for y in lista2:
#         if y not in lista1:
#             no_en_1.append(y)
#     print("Lista de palabras repetidas",repetidas)
#     print("Lista de palabras fuera de la lista 1",no_en_1)
#     print("Lista de palabras fuera de la lista 2",no_en_2)

# lista1 = ["Hola","Padre","Madre","Casa","Arbol"]
# lista2 = ["Panadero","Padre","Madre","Coca","Perro"]

# compara_listas(lista1,lista2)

#Ejercicio 5
'''
Ejercicio 5:
    
  A - Escribe una función llamada "duplicado" que tome una lista y devuelva True si tiene algún 
elemento duplicado.
La función no debe modificar la lista.

B - Crear una función que genere una lista de 23 números aleatorios del 1 al 100 y
comprobar con la función anterior si existen elementos duplicados.
'''
# import random

# def duplicado(lista):
#     duplicado = False
#     comparador = []
#     for x in lista:
#         if x in comparador:
#             duplicado = True
#         else:
#             comparador.append(x)
#             print(comparador)
#     if duplicado == True:
#         print ("Duplicado")
#         return True
#     elif duplicado == False:
#         print ("No hay duplicados")
#         return False

# lista=[]
# for n in range(0,23):
#     y = random.randrange(0,100)
#     lista.append(y)

# duplicado(lista)