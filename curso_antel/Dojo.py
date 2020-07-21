#Kata 1
# def suma_multiplos():
#     suma = 0
#     for i in range(1, 1000):
#         if i%3 == 0 or i%5 == 0:
#             suma += i

#     print(suma)

# suma_multiplos()

#Kata 2
# def rectangulo():
#     n = int(input("Ingrese valores:"))
#     print("0"*n*2)
#     for i in range(1,n-1):
#         espacios = " "*(n-1)*2
#         print("0{}0".format(espacios))
#     print("*"*n*2)

# rectangulo()

# def rectangulo():
#     n=int(input("introduzca un valor para n: "))
#     for i in range (0,n):
#         for j in range(0,2*n):
#             if j==0 or i==0 or i==n-1 or j==2*n-1:
#                 print("O",end="")
#             else:
#                 print(" ",end="")
#         print("")

# rectangulo()

#kata 3
# import random

# def kata3():
#     nros=list()
#     res={}
#     tot=0
#     #Carga lista de nros
#     for i in range(0,10000):
#         n=random.randrange(1,6+1)
#         nros.append(n)
#         tot+=n
#     for x in nros:
#         if x in res:
#             res[x] = res[x]+1
#         else:
#             res[x]=1
   
#     print("Repeticiones: ", res)     
#     print("Promedio: ", tot/len(nros))              
# kata3()

#Kata 4
# def kata4():
#     lista =[]
#     for x in range(100,1000):
#         for y in range(100,1000):
#             resultado = x*y
#             resultado = str(resultado)
#             if resultado == resultado[::-1]:
#                 lista.append(int(resultado))
#     print(max(lista))

# kata4()

#Kata 5