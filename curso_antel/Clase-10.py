#Ejercicio 3
# def palabras(p):
#     if len(p) > 5:
#         return p
#
#
# lista = ['Hola','Cacerola','Pomarola','Escritorio','Perro','Gato']
#
# def filtro(palabras,lista):
#     print(list(filter(palabras,lista)))
#
# filtro(palabras,lista)

'''Ejercicio 4 Prog Funcional. Dado un string usar Reduce para obtener una lista de las vocales que contenga'''
#
# def vocales(cadena):
#     if cadena in ['a','e','i','o','u']:
#         return True
#     else:
#         return False
#
#
# cadena = 'La cadena solicitada'
#
# def filtro(vocales,cadena):
#     print(list(filter(vocales,cadena)))
#
# filtro(vocales,cadena)

#Ejercicio 5
# def programa(lista):
#     if lista[2]*lista[3] > 100:
#         calculo = lista[2]*lista[3]*0.9
#     else:
#         calculo = lista[2]*lista[3]
#     return (lista[0],calculo)
#
# orders = [['34857','Learning Python, Mark Lutz',4,40.95],['98762','Programming Python, Mark Lutz',5,56.8],['77226','Head First Python, Paul Barry',3,32.95]]
#
# def filtro(programa,lista):
#     print(list(map(programa,lista)))
#
# filtro(programa,orders)

#Profe


# def f1(l):
#     return (l[0], l[2]*l[3])
#
# def f2(x):
#     if x[1] >= 100:
#         return (x[0], round(x[1]*0.9,2))
#     else:
#         return (x[0], round(x[1],2))
#
# invoice_totals_2 = list(map(f2, map(f1, orders)))
#
# print(invoice_totals_2)

'''Segunda parte de la clase'''

'''Ejercicio 1: Utilizando listas por comprensión, generar una lista de los primeros 10 números naturales elevados al cuadrado'''
# lista = [x**2 for x in range(1,11)]
# print(lista)

'''Ejercicio 2: Utilizando una función lambda, escribir una función que tome como parámetro una oración y retorne una lista con el largo de cada palabra.'''

# oracion = "La famosa oracion"
# print(list(map(lambda p:len(p),list(oracion.split()))))

'''Ejercicio 3: Dar el resultado de sumar todos los números primos del 1 al 1000'''
# import functools
#
# def primos():
#     listaprimos = []
#     for i in range(2,1000):
#         creciente = 2
#         esPrimo = True
#         while esPrimo and creciente < i:
#             if i%creciente == 0:
#                 esPrimo = False
#             else:
#                 creciente += 1
#         if esPrimo:
#                 listaprimos.append(i)
#     return listaprimos
#
#
# print(functools.reduce(lambda x,y:y+x,primos()))

#Profe con lista por comprension
# tope=1001
# primes = [num for num in range(tope) if 0 not in [num%i for i in range(2,num)]]  
# print(functools.reduce(lambda x, y: x+y, primes))

'''
Ejercicio 4 

Escribir una función (clásica) que reciba cuatro parámetros: lista, n, inc_1, inc_2 y devuela otra lista
- lista es una lista (de largo 10) compuesta por valores numéricos aleatorios entre 1 y 50
- n es un entero, todos los números del parámetro lista mayores o iguales a n deben incrementarse en inc_2, los restantes se incrementarán en inc_1
La lista a devolver se debe resolver usando comprensión, la lista pasada como parámetro también.
'''

# import random
# def funcionClasica(lista,n,inc_1,inc_2):
#     nueva_lista = [i*inc_2 if i>=n else i*inc_1 for i in lista]
#     return print("Lista original:{}, lista procesada:{}".format(lista,nueva_lista))
#
# lista = [random.randrange(1,50) for n in range(0,10)]
# funcionClasica(lista,25,2,4)

'''
Ejercicio 5 

Obtener una matriz de dos dimensiones a partir de un string del siguiente modo
String: “Hola esto es Python en Antel”
Matriz resultado:
[[“HOLA”, “Hola”, 4] , ]
[“ESTO”, “esto”, 4],
[“ES”, “es”, 2], ….
'''
# cadena = 'Hola esto es Python en Antel'
# def listas(palabra):
#     lista = []
#     lista.append(palabra.upper())
#     lista.append(palabra.lower())
#     lista.append(len(palabra))
#     return lista
#
# print(list(map(listas,cadena.split())))

#Profesor
# words = 'The quick brown fox jumps over the lazy dog'.split()
 
# stuff = [[w.upper(), w.lower(), len(w)] for w in words]

'''
Ejercicio 6:
Utilizando una función lambda y la función reduce, escribir una función que tome una lista y devuelva la lista sin repetidos
'''
# import functools
#
# lista = ['Hola','Mundo','Pedro','Mundo','Caja','Pedro']
#
# print(functools.reduce(lambda a,b: a if b[0] in a else a+b, list(map(lambda x: [x] ,lista))))

#Profesor
# lista = [1, 2, 2, 3, 3, 3, 4, 3]
# print(functools.reduce(lambda x, y: x + [y] if not y in x else x, lista, []))