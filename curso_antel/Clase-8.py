#Ejercicio 1
'''
import functools

#a
def palabraslarga(p1,p2):
    if len(p1) > len (p2):
        return p1
    elif len(p1) < len (p2):
        return p2

#b
def palabrascorta(p1,p2):
    if p1 < p2:
        return p1
    elif p1 > p2:
        return p2


lista = ["Hola","Caballo","Cacerola","Azucar"]
nueva_lista = functools.reduce(palabrascorta,lista)
print(nueva_lista)
'''
#Ejercicio 2
'''
def largo(p):
    largop = len(p)
    return (p,largop)

lista = ["Hola","Perro","Pajaro","Cucaracha"]
lista_final = list(map(largo,lista))
print(lista_final)
'''

# Ejericio 3
'''
def esMenor2(lista, n):
    def es_menor(txt):
        return len(txt)>n

    return filter(es_menor,lista)

lista = ["Hola","Perro","Pajaro","Cucaracha"]
print(list(esMenor2(lista,4)))

#profesor
lista_palabra = ['hola','como','andannnnn','todos','a']

def es_mayor_3_aux(palabra):
    return len(palabra) > 3

def ejercicio3(max,lista_palabra):

    print(list(filter(es_mayor_3_aux,lista_palabra)))
'''