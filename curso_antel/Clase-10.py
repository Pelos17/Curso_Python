# def square(x):
#     print("Cuadrado de ",format(x))
#     return x*x

# def digit_sum(x):
#     print("Suma de digitos de ",format(x))
#     return sum(map(int, str(x)))

# numbers = range(1,6)
# squares = (square(n) for n in numbers)
# print(squares)

# dsums = (digit_sum(n) for n in squares)

# for n in dsums:
#     print(n)

#Ejercicio Generadores
#Solucion con funcion traducional

# def ejercicio(lista):
#     nueva_lista = []
#     for x in lista:
#         if type(x) == int and x%2 == 0:
#             nueva_lista.append(x)
#     for y in nueva_lista:
#         if str(y)[0] == "1":
#             print(y)

#ejercicio(entrada)

#Dos funciones
# def pares(lista):
#     nueva_lista = []
#     for x in lista:
#         if type(x) == int and x%2 == 0:
#             nueva_lista.append(x)
#     return nueva_lista
            

# def filtro(lista):
#     for y in lista:
#         if str(y)[0] == "1":
#             print(y)

# filtro(pares(entrada))

#Generadores

entrada = [1,12,22,124,"1Hola",[1,2,3],True,33]
 
filtro_enteros = (x for x in entrada if isinstance(x,int))
filtro_pares = (x for x in filtro_enteros if x%2==0)
final = (x for x in filtro_pares if str(x)[0] =="1")
#cadena = (str(x) for x in filtro_pares)
#comenienza_en_1: (x for x in cadena if x[0]=="1")

for x in final:
    print(x)

entrada = [1,12,124,22,"1Hola",[1,2,3],True,33]






