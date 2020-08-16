"""a) Escribir una clase Personaje que contenga los atributos vida, posición (es un número, representa la posición sobre un eje) y 
velocidad, y los métodos recibir_ataque, que reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser 
menor o igual que cero, y mover que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.

b) Escribir una clase Enemigo que herede de Personaje, y agregue el atributo ataque y el método atacar. 
Este método recibe otro personaje y lo daña según la cantidad indicada por el atributo ataque (le resta vidas).
Las clases Enemigo y Personaje deben estar en diferentes módulos y las instanciaciones y pruebas, en un tercer módulo."""

class personaje():
    def __init__(self,vida,velocidad,posicion):
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad
    
    def recibir_ataque (self,daño):
        self.daño = daño
        self.vida = self.vida - daño
        print("La vida restante es:",self.vida)
        if self.vida <= 0:
            print("Lo mataste")

    def mover(self,movimiento):
        self.movimiento = movimiento
        self.posicion = [movimiento[0] + self.velocidad, movimiento[1] + self.velocidad,]
        print("Posicion Actual",self.posicion)




roge = personaje(10,6,[0,0])

roge.recibir_ataque(11)
roge.mover([10,15])