"""a) Escribir una clase Personaje que contenga los atributos vida, posición (es un número, representa la posición sobre un eje) y 
velocidad, y los métodos recibir_ataque, que reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser 
menor o igual que cero, y mover que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
"""


class Personaje():
    def __init__(self,vida,velocidad,posicion):
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad
    
    def recibir_ataque (self,ataque):
        self.ataque = ataque
        self.vida = self.vida - ataque
        print("La vida restante es:",self.vida)
        if self.vida <= 0:
            print("Lo mataste")

    def mover(self,movimiento):
        self.movimiento = movimiento
        self.posicion = [movimiento[0] + self.velocidad, movimiento[1] + self.velocidad,]
        print("Posicion Actual",self.posicion)