class Perro():
    tipo = "Mamifero"
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return "El perro {} tiene {} años.".format(self.nombre,self.edad)
    def ladrido(self,ladrido):
        return ('El perro {} ladra {}'.format(self.nombre,ladrido))
    def __gt__(self,otro_perro):
        return self.edad > otro_perro.edad
    def __ge__(self,otro_perro):
        return self.edad >= otro_perro.edad
    def __len__(self):
        return self.edad


perro1 = Perro ("Tobi",20)
perro2 = Perro ("Puchi",11)
perro3 = Perro ("Lalo",3)

lista_perros = sorted([perro1,perro2,perro3])
#Para sacar el mas viejo 
print("El perro mas viejo es: {}".format(lista_perros[-1].nombre))
#Ladrido
print(perro1.ladrido("Bark, bark"))
#Len
print(len(perro1))


'''Crear una clase que ereda de perro, se llama salchica y tiene el atrivuto altura'''

class Salchicha(Perro):
    def __init__(self,altura):
        self.altura = altura
    def __str__(self):
        return "El salchica {} tiene {} años y mide {} cm.".format(self.nombre,self.edad,self.altura)

salchicha1 = Salchicha("Pepe",20,30)

print(str(salchicha1))