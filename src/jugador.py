from marcador import *
import random

class Jugador:
    def __init__(self,nom = "generico"):
        self.nombre   = nom
        self.intento  = 0
        self.turno    = 0
        print "Jugador "+self.nombre+" se ha creado"

    def setNuevoTurno(self):
        #print "nuevo turno para jugador "+self.nombre
        self.turno+=1
        self.intento=0

    def setNuevoIntento(self):
        #print "nuevo intento para jugador "+self.nombre
        self.intento+=1

    def jugar(self,marcadores,actuacionesPosibles,dados,resultadoPrevio):
        #print "turno = "+str(self.turno)
        #print "intento = "+str(self.intento)
        assert(len(actuacionesPosibles)>0)
        return(random.randrange(len(actuacionesPosibles)))
