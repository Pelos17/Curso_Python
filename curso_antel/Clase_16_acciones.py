from Clase_16_personaje import Personaje
from Clase_16_enemigo import Enemigo


roge = Personaje(10,6,[0,0])
archer = Enemigo(3,2,[0,0],11)

roge.recibir_ataque(11)
roge.mover([10,15])
archer.atacar(roge)