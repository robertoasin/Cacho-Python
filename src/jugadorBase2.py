from jugador import *
import os

class JugadorBase2(Jugador):

    def __init__(self):
        Jugador.__init__(self,"JugadorBase2")

    def imprimirActuaciones(self,lista):
        i=0
        for actuacion in lista:
            actuacion.displayCompacto(i)
            i+=1


    def jugar(self,marcadores,actuacionesPosibles,dados,resultadoPrevio):
        valorMayorGanancia  = 0
        indiceMayorGanancia = -1

        #if(self.lanzamiento==1):
            #os.system("clear")
        #self.imprimirActuaciones(actuacionesPosibles)

        if(self.lanzamiento==1):
            if len(actuacionesPosibles)>=32:
                return 31
            else:
                prob = random.randrange(5)
                if(prob<4): 
                    return 30
                else:
                    return random.randrange(len(actuacionesPosibles))
        else:
            assert(self.lanzamiento==2)
            for i in range(len(actuacionesPosibles)):
                if(actuacionesPosibles[i].accion=="dormida" or actuacionesPosibles[i].accion=="nada"):
                    return i
                else:
                    assert(actuacionesPosibles[i].accion=="sobre" or actuacionesPosibles[i].accion=="anotar")
                    if (actuacionesPosibles[i].anotacion[1] >= valorMayorGanancia):
                        valorMayorGanancia = actuacionesPosibles[i].anotacion[1]
                        indiceMayorGanancia = i

        return indiceMayorGanancia
