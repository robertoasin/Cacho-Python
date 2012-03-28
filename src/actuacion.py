class Actuacion:
    """ Abstraccion de una posible actuacion """
    def __init__(self, accion, anotacion, indiceDados, seRespeta):
        self.accion = accion
        self.anotacion = anotacion
        self.indiceDados = indiceDados
        self.seRespeta = seRespeta

    def display(self):
        print "accion: "+self.accion
        print "anotacion: "+str(self.anotacion)
        print "indiceDados: "+str(self.indiceDados)
        print "seRespeta: "+str(self.seRespeta)

#    def displayCompacto(self):
#        print "("+self.accion+","+str(self.anotacion)+","+str(self.indiceDados)+","+str(self.seRespeta)+")"

    def displayCompacto(self,indice=-1):
        if(indice > -1):
            print "["+str(indice)+"]"+"("+self.accion+","+str(self.anotacion)+","+str(self.indiceDados)+","+str(self.seRespeta)+")"
        else:
            print "("+self.accion+","+str(self.anotacion)+","+str(self.indiceDados)+","+str(self.seRespeta)+")"

    def imprimirEnArchivo(self,archivo):
        archivo.write("("+self.accion+","+str(self.anotacion)+","+str(self.indiceDados)+","+str(self.seRespeta)+")\n")
