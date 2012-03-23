import sys
class Marcador:
    """ Abstraccion de un marcador de jugador """

    def __init__(self):
        self.porAnotar         = 11
        self.balas             = -1
        self.tontos            = -1
        self.trenes            = -1
        self.cuadras           = -1
        self.quinas            = -1
        self.senas             = -1
        self.escalera          = -1
        self.full              = -1
        self.poker             = -1
        self.grande            = -1
        self.grande2           = -1
        self.dormida           = False
        self.panzaDeOro        = False
        self.escaleraRespetada = False
        self.fullRespetado     = False
        self.pokerRespetado    = False
        self.suma              = 0

    def yaAnotado(self, juego):
        comparacion = 'self.' + juego + "!= -1"
        return eval(comparacion)

    def anotar(self,anotacion):
        asignacion = 'self.'+str(anotacion[0]) + "=" + str(anotacion[1])
        exec(asignacion)
#        locals()[atributo]= anotacion[1]
#        print atributo
#        print locals()[atributo] 
        self.porAnotar-=1
        self.suma += anotacion[1]

    def anotarDormida(self):
        self.dormida = True

    def marcadorIncompleto(self):
        return ( self.porAnotar > 0 )

    def display(self):
        print "balas             = "+str(self.balas)
        print "tontos            = "+str(self.tontos)
        print "trenes            = "+str(self.trenes)
        print "cuadras           = "+str(self.cuadras)
        print "quinas            = "+str(self.quinas)
        print "senas             = "+str(self.senas)
        print "escalera          = "+str(self.escalera)
        print "full              = "+str(self.full)
        print "poker             = "+str(self.poker)
        print "grande            = "+str(self.grande)
        print "grande2           = "+str(self.grande2)
        print "dormida           = "+str(self.dormida)
        print "Panza de oro      = "+str(self.panzaDeOro)
        print "escaleraRespetada = "+str(self.escaleraRespetada)
        print "fullRespetado     = "+str(self.fullRespetado)
        print "pokerRespetado    = "+str(self.pokerRespetado)
        print "suma              = "+str(self.suma)

    def tieneAlalay(self):
        return (self.grande==50 and self.grande2==50) and ((self.escalera==25 and self.full==35 and self.poker==45) or (self.balas==4 and self.tontos==8 and self.trenes==12 and self.cuadras==16 and self.quinas==20 and self.senas==24))

