from jugador import *
import os

class JugadorHumano(Jugador):

    def __init__(self):
        Jugador.__init__(self,"JugadorHumano")

    def imprimirActuaciones(self,lista):
        i=0
        for actuacion in lista:
            actuacion.displayCompacto(i)
            i+=1

    def jugar(self,marcadores,actuacionesPosibles,dados,resultadoPrevio):
        valorMayor=0
        indiceValorMayor=-1

        if(self.intento==1):
            os.system("clear")
        opcion = -1
        while(opcion<0 or opcion>len(actuacionesPosibles)):
              print "\n Tiene estos dados:"+str(dados)
              print "Seleccione una de las siguientes opciones:"
              self.imprimirActuaciones(actuacionesPosibles)
              print "Opcion: "
              opcion = int(raw_input())

        return(opcion)
