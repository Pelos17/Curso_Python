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
# Profe
# def lectura_primeros_n(archivo,n):
#     with open(archivo,"r") as archivo:
#         for x in range(n):
#             print(archivo.readline())
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

#Ejercicio 3

# import datetime
#
# def ejercicio3(archivo,texto):
#     with open(archivo,"a") as archivo:
#         archivo.write("\n")
#         archivo.write(texto)
#         archivo.write(" ")
#         archivo.write(str(datetime.datetime.now()))
#
#Profe

# def guarda_en_log(archivo,texto):
#     with open(archivo,"a") as log:
#         #log.writelines([texto,' ',str(datetime.datetime.now()),"\n"])
#         log.write(f'{texto} {datetime.datetime.now()} \n')

# ejercicio3("archivo","Prueba 3")

#Ejercicio 4

'''Usando la biblioteca glob, leer de un directorio todos los archivos llamados notas_dddd.txt, donde dddd son 4 dígitos que representan un año.
El formato de estos archivos es:
nombre_alumno; nota
nombre_alumno; nota

....

nombre_alumno; nota
Se deben imprimir los promedios por año,  y el promedio general de notas.
'''

# import glob
#
# archivos = glob.glob('./notas/notas_[0-9][0-9][0-9][0-9]')
# total = []
# for x in archivos:
#     año = str(x)
#     with open(x,"r") as x:
#         alumnos = x.readlines()
#         suma = 0
#         for y in alumnos:
#             y = int(y[-2:])
#             suma = suma+y
#             total.append(y)
#         print('Promedio año {}:{}'.format(año[-4:],suma/len(alumnos)))
# suma_total = 0
# for n in total:
#     suma_total = suma_total + n
# print("El promedio total es:",suma_total/len(total))


