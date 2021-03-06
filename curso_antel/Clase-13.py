# class Test(Exception):
#     # constructor de la clase
#     def __init__(self, v, m):
#         self.valor = v
#         self.mensaje = m

#     # la clase Test tiene 2 atributos, valor y mensaje
#     # cada vez que creo un objeto de esta clase le
#     # debo pasar datos para esos 2 atributos, que se #almacenan gracias al constructor

#     def __str__(self):
#         return str(self.valor) + ", " + self.mensaje


# o1 = Test(56, "pepe")
# o2 = Test(9898, "Holaquetal")

# print(o1.valor)  # 56
# print(o2.mensaje)  # "Holaquetal"
# print(o1)

#Ejercicio
'''Escribir una función que reciba dos números (ingresados por el 
usuario) y a partir de las operaciones especificadas en un archivo 
(cuyo nombre deberá ser provisto como parámetro), realice los 
cálculos y devuelva el resultado final de cada línea (resultado que 
se obtiene operando los dos números recibidos). El archivo 
contendrá por línea una operación aritmética sencilla; por ej:
+
/
**
Nota: investigar la función de Python llamada eval.
En caso de producirse un error durante la lectura de una línea del 
archivo, se debe lanzar una excepción propia que informe número 
de línea, operación problemática y motivo del error. '''

'''
INTERPRETAR EL STRING COMO OPERADOR, USAR EVAL
TENERMOS QUE FORZAR ERRORES
'''
# class ErrorOperador(Exception):
#     def __init__ (self,valor,mensaje):
#         self.mensaje = mensaje
#         self.valor = valor
#     def __str__(self):
#         return str("Linea {}.Error:{}".format(self.valor,self.mensaje))

# Con este edito SyntaxError
# def operador(n1,n2):
#     with open('./curso_antel/operadores','r') as archivo:
#         archivo = archivo.read().splitlines()
#         contador = 0
#         print("Se ingresaron los numeros {} y {}.".format(n1,n2))
#         print("El resultado de las operacioens es:")
#         for x in archivo:
#             cadena = str(n1) + x + str(n2)
#             print("Operacion:",x)
#             contador = contador + 1
#             try:
#                 print(eval(cadena))
#             except SyntaxError as e:
#                 print('Se ingreso un operador incompatible y se genero un error {} debido a la operacion {} ingresada en la linea {} del archivo de operadores.'.format(type(e),x,contador))

#Uso mi error
# def operador(n1,n2):
#     with open('./curso_antel/operadores','r') as archivo:
#         archivo = archivo.read().splitlines()
#         contador = 0
#         print("Se ingresaron los numeros {} y {}.".format(n1,n2))
#         print("El resultado de las operacioens es:")
#         for x in archivo:
#             cadena = str(n1) + x + str(n2)
#             print("Operacion:",x)
#             contador = contador + 1
#             if x not in ["/","*","-","+"]:
#                 raise ErrorOperador(contador,"Operador incorrecto")
#             else:
#                 print(eval(cadena))


# operador(420,69)