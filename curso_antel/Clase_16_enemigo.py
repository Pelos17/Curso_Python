
"""
b) Escribir una clase Enemigo que herede de Personaje, y agregue el atributo ataque y el método atacar. 
Este método recibe otro personaje y lo daña según la cantidad indicada por el atributo ataque (le resta vidas).
Las clases Enemigo y Personaje deben estar en diferentes módulos y las instanciaciones y pruebas, en un tercer módulo."""

from Clase_16_personaje import Personaje

class Enemigo(Personaje):
    def __init__(self,vida,velocidad,posicion,ataque):
        self.ataque = ataque
        Personaje.__init__(self,vida,velocidad,posicion)
    
    def atacar(self,personaje):
        personaje.recibir_ataque(self.ataque)