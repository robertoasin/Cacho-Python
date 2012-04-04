#!/usr/bin/python
from anotador import *

juego = Anotador(["JugadorHumano2","JugadorHumano"],False)
ganadores = juego.hacerJugar()
juego.imprimirResultado()
print "Ganadores: "+str(ganadores)
