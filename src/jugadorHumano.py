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

    def imprimirMarcadores(self, marcadores):
        nombres="Jugador:".rjust(20)
        balas="Balas:".rjust(20)
        tontos="Tontos".rjust(20)
        trenes="Trenes".rjust(20)
        cuadras="Cuadras".rjust(20)
        quinas="Quinas".rjust(20)
        senas="Senas".rjust(20)
        escalera="Escalera".rjust(20)
        full="Full".rjust(20)
        poker="Poker".rjust(20)
        grande="Grande".rjust(20)
        grande2="Grande1".rjust(20)
        suma="Suma".rjust(20)
        dormida="Dormida".rjust(20)

        for nombreJugador in marcadores.keys():
            nombres+=nombreJugador.center(30)
            balas+=repr(marcadores[nombreJugador].balas).rjust(30)
            tontos+=repr(marcadores[nombreJugador].tontos).rjust(30)
            trenes+=repr(marcadores[nombreJugador].trenes).rjust(30)
            cuadras+=repr(marcadores[nombreJugador].cuadras).rjust(30)
            quinas+=repr(marcadores[nombreJugador].quinas).rjust(30)
            senas+=repr(marcadores[nombreJugador].senas).rjust(30)
            escalera+=repr(marcadores[nombreJugador].escalera).rjust(30)
            full+=repr(marcadores[nombreJugador].full).rjust(30)
            poker+=repr(marcadores[nombreJugador].poker).rjust(30)
            grande+=repr(marcadores[nombreJugador].grande).rjust(30)
            grande2+=repr(marcadores[nombreJugador].grande2).rjust(30)
            suma+=repr(marcadores[nombreJugador].suma).rjust(30)
            dormida+=repr(marcadores[nombreJugador].dormida).rjust(30)
            #self.marcadores[nombreJugador].display()

        print nombres  
        print balas    
        print tontos   
        print trenes   
        print cuadras  
        print quinas   
        print senas    
        print escalera 
        print full     
        print poker    
        print grande   
        print grande2  
        print suma     
        print dormida      

    def jugar(self,marcadores,actuacionesPosibles,dados,resultadoPrevio):
        valorMayor=0
        indiceValorMayor=-1

        if(self.intento==1):
            os.system("clear")
            self.imprimirMarcadores(marcadores)

        opcion = -1
        while(opcion<0 or opcion>len(actuacionesPosibles)):
              print "\n Tiene estos dados:"+str(dados)
              print "Seleccione una de las siguientes opciones:"
              self.imprimirActuaciones(actuacionesPosibles)
              print "Opcion: "
              opcion = int(raw_input())

        return(opcion)
