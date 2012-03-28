#!/usr/bin/python
from anotador import *

juego = Anotador(["JugadorAleatorio","JugadorBase","JugadorAleatorio2"],True)
ganadores = juego.hacerJugar()
print "Ganadores: "+str(ganadores)
