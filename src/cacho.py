#!/usr/bin/python
from anotador import *

juego = Anotador(["JugadorAleatorio","JugadorBase","JugadorHumano"],True)
ganadores = juego.hacerJugar()
juego.imprimirResultado()
print "Ganadores: "+str(ganadores)
