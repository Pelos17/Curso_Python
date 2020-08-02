#Ejercicio 1
# def ejercicio1():
#     archivo_usuario = input("Ingrese la ubicacion del archivo:")
#     numero = int(input("Ingrese el numero:"))
#     with open (archivo_usuario,"r") as archivo:
#         archivo = archivo.readlines()
#         if numero > len(archivo):
#             for x in archivo:
#                 print(x)
#         else:
#             for x in archivo[0:numero]:
#                 print(x)

# ejercicio1()

#Ejercicio 2

# def ejercicio2():
#     archivo_usuario = input("Ingrese la ubicacion del archivo:")
#     copia = archivo_usuario + "_copia"
#     with open (archivo_usuario,"r") as archivo:
#         archivo = archivo.read()
#         print("Archivo original")
#         print(archivo)
#         print("*"*40)
        
#     with open(copia,"w") as archivo2:
#         archivo2.write(archivo)
#     with open(copia,"r") as archivo3:
#         print("copia del archivo")
#         print(archivo3.read())


# ejercicio2()
