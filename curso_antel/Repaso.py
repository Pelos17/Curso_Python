#Ejercicio 1
"""
def busca_pares(cadena):
    lista_pares = []
    lista_inpares = []
    par = ""
    contador = 0
    if len(cadena)%2 == 0:
        for x in cadena:
            par = par+x
            contador = contador + 1
            if contador == 2:
                lista_pares.append(par)
                contador = 0
                par = ""
        print(lista_pares)
    else:
        cadena = cadena+"_"
        for x in cadena:
            par = par+x
            contador = contador + 1
            if contador == 2:
                lista_inpares.append(par)
                contador = 0
                par = ""
        print(lista_inpares)

cadena_par = "abcdef"
cadena_inpar = "abcde"
busca_pares(cadena_inpar)
"""

#Ejercicio 2
"""
def is_uppercase(cadena):
    if cadena == cadena.upper():
        print("Esta todo en mayuscula")
        return True
    else:
        print("Hay letras minusculas")
        return False

is_uppercase("A")
is_uppercase("a")
is_uppercase("ASD")
is_uppercase("Asd")
"""

#Ejercicio 3
'''
def tribonacci(lista,largo):
    indice = 0
    if len(lista) < 3:
        print("Se ingresaron numeros insuficientes")
    else:
        while len(lista) < largo:
            suma = sum(lista[indice:indice+3])
            lista.append(suma)
            indice = indice + 1
    print(lista)


tribonacci([1,1,1],10)
'''

#Ejercicio 4

# with open("clave.txt",'r') as clave:
#     clave = clave.read()
#     clave = list(clave)
# def cifrar(cadena):
#     cadena = list(cadena)
    

# def decifrar(cadena):
#     pass


# cadena = "Hola Mundo"

# cifrar(cadena)
