'''Crear una clase que ereda de perro, se llama salchica y tiene el atrivuto altura'''

from perro import Perro

class Salchicha(Perro):
    # def __init__(self,altura):
    #     self.altura = altura
    # def __str__(self):
    #     return "El salchica {} tiene {} años y mide {} cm.".format(self.nombre,self.edad,self.altura)
    pass

salchicha1 = Salchicha("Pepe",20)

print(str(salchicha1))