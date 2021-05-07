#Rectangulo
'''
def rectangulo(ancho=0,alto=0,caracter=0):
    alto = int(input("Ingrese el alto:"))
    ancho = int(input("Ingrese el ancho:"))
    caracter = input("Ingrese el caracter a dibujar:")
    for x in range(alto):
        for y in range(ancho):
            print("{} ".format(caracter), end="")
        print()

rectangulo()
'''
#Triangulo
'''
Ejercicio 5
Escribir una función que reciba un entero n y represente un triángulo isósceles con sus dos lados 
iguales de largo n,
'''
def isoceles(largo):
    for x in range(largo+1):
        print("*"*x)
    for y in range(largo-1,0,-1):
        print("*"*y)

isoceles(10)
