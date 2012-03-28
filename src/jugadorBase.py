from jugador import *
import os

class JugadorBase(Jugador):

    def __init__(self):
        Jugador.__init__(self,"JugadorBase")

    def imprimirActuaciones(self,lista):
        i=0
        for actuacion in lista:
            actuacion.displayCompacto(i)
            i+=1


    def determinarPerdida(self,anotacionPosible):
        return {
            'balas': 10 - anotacionPosible[1],
            'tontos': 12 - anotacionPosible[1],
            'trenes': 15 - anotacionPosible[1],
            'cuadras': 18 - anotacionPosible[1],
            'quinas': 21 - anotacionPosible[1],
            'senas': 24 - anotacionPosible[1],
            'escalera': 25 - anotacionPosible[1],
            'full': 35 - anotacionPosible[1],
            'poker': 45 - anotacionPosible[1],
            'grande': 50 - anotacionPosible[1]
        }.get(anotacionPosible[0], 50)

    def jugar(self,marcadores,actuacionesPosibles,dados,resultadoPrevio):
        valorMenorPerdida  = 50
        indiceMenorPerdida = -1

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
                    puntosPerdidos = self.determinarPerdida(actuacionesPosibles[i].anotacion)
                    if (puntosPerdidos <= valorMenorPerdida):
                        valorMenorPerdida = puntosPerdidos
                        indiceMenorPerdida = i

        return indiceMenorPerdida
