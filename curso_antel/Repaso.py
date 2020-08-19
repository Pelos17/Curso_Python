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
'''
with open("clave.txt",'r') as clave:
    clave = clave.read()
    clave = list(clave)

def cifrar(cadena):
    cifrado = []
    cadena = list(cadena)
    for x in cadena:
        if x in clave:
            cifrado.append(clave.index(x))
        else:
            cifrado.append(x)
    print ("".join(str(e)for e in cifrado))
    return "".join(str(e)for e in cifrado)
    

def decifrar(cadena):
    decifrado = []
    for x in cadena:
        if x.isdigit() == True:
            decifrado.append(clave[int(x)])
        else:
            decifrado.append(x)
    print ("".join(str(e)for e in decifrado))
    return "".join(str(e)for e in decifrado)

cifrar("ABECEDARIO")
decifrar("7B535D7249")
'''
#Ejercicio 5
'''
#DefaultList
class DefaultList(list):
    def __init__(self,lst,default):
        super().__init__(lst)
        self.lst = lst
    self.default = default
 
def __getitem__(self,index):
    if index < len(self.lst) and index >= -len(self.lst):
        return self.lst[index]
    else:
        return self.default
 
 
l = ["hola", 3]
dl = DefaultList(l, -1)
 
print(dl[0]) # hola
print(dl[2]) #-1
'''

#Ejercicio 6
'''
import re
def bebidas(cadena):
    lista_bebidas = []
    patron = re.compile('[1-9]')
    for i in cadena:
        if patron.match(i):
            lista_bebidas.append(int(i))
    print("Deberia tomar {} basos de agua.".format(sum(lista_bebidas)))


cadena = "2 tragos, 1 ceveza, 4 copas de vino,9 botellas de vodka"
bebidas(cadena)
''' 