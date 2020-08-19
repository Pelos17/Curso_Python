#Ejercicio 1

#si no entendi mal el ejercicio, no querias que hicieramos n%3 == 0, primero querias que recorrieramos toda la secuencia, por eso lo hice asi.
'''
def divisible_3(n):
    sum = 0
    for x in str(n):
        sum = sum + int(x)
    if sum%3 == 0:
        print("Divisible")
        return True
    else:
        return False

divisible_3(8409)
'''

#Ejercicio 2
'''
def arbol(n):
    espacios = " "
    dibujo = "*"
    contador = n
    for i in range(1,n+1):
        print("{}{}".format(espacios * contador,dibujo))
        contador = contador - 1
        dibujo = dibujo + "*"+"*"

arbol(7)
'''

#Ejercicio 3
'''
class Oracion(str):
    def __init__(self, oracion):
        self.oracion = oracion
    def __add__(self,otro):
        return(self.oracion + " " + otro.oracion)

o1 = Oracion("Buenas tardes")
o2 = Oracion("que tal")

print(o1 + o2) # salida: Buenas tardes que tal        
'''

#Ejercicio 4
'''
class InmutableList(list):
'''


#Ejercicio 5
#solo compare si el archivo existe y sobvrescribo el mensaje de File not found. Adjunto mi archivo de ejemplo.
'''
def contar_caracteres(archivo):
    try:
        with open(archivo,"r") as archivo:
            archivo = archivo.read()
            archivo = list(archivo)
            diccionario = {}
            if archivo == []:
                print(diccionario)
            else:
                contador = 0
                for x in archivo:
                    if x==" " or x == "\n" or x == "\t":
                        continue
                    for y in archivo:
                        if x == y:
                            contador = contador + 1
                    diccionario.update({x: contador})
                    contador = 0
                print(diccionario)
    except FileNotFoundError as e:
        print("El archivo {} no existe".format(archivo))

contar_caracteres("archivo_prueba.txt")
'''