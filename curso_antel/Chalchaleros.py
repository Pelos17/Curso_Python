import random

def baldeacorazones(numero):
    #numero = int(input("Ingrese la gente a chequear:"))
    artista = ["Chalchalero", "Rolling Stone"]
    integrantes = [random.choice(artista) for n in range(0, numero)]
    contador_de_rollingas = 0
    contador_de_chalchaleros = 0
    for persona in integrantes:
        if persona == "Rolling Stone":
            contador_de_rollingas = contador_de_rollingas + 1
        if persona == "Chalchalero":
            contador_de_chalchaleros = contador_de_chalchaleros + 1
    print("En una lista de {} personas, hay {} Rolling Stone y {} Chalchaleros.".format(len(integrantes),contador_de_rollingas,contador_de_chalchaleros))

baldeacorazones(int(input("Ingresee la cantidad de gente a chequear:")))