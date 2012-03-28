from jugador import *
import os

class JugadorAleatorio(Jugador):

    def __init__(self):
        Jugador.__init__(self,"JugadorHumano")

    def imprimirActuaciones(self,lista):
        i=0
        for actuacion in lista:
            actuacion.displayCompacto(i)
            i+=1


    def jugar(self,marcadores,actuacionesPosibles,dados,resultadoPrevio):
        return random.randrange(len(actuacionesPosibles))
