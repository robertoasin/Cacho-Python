import random
from actuacion import *
from jugadorHumano import *
from jugadorHumano2 import *
from jugadorBase import *
from jugadorBase2 import *
from jugadorBase3 import *
from jugadorBase4 import *
from jugadorAleatorio import *
from moebious import *
class Anotador:
    """ Abstraccion del anotador del juego """
    def __init__(self, listaJugadores, modoCompeticion = False):
        self.modoCompeticion = modoCompeticion
        self.listaJugadores = listaJugadores
        self.juegosPosibles = ["balas","tontos","trenes","cuadras","quinas","senas","escalera","full","poker","grande", "grande2"]
        self.jugadores      = {} #hash de jugadores
        self.marcadores     = {} #hash de marcadores
        filename = "log"
        for jugador in listaJugadores:
            filename=filename+"-"+jugador
            self.jugadores.update({jugador : eval(jugador+"()")})
            self.marcadores.update({jugador : Marcador()})
        self.log = open(filename,"at")

        if not modoCompeticion:
            print "nuevo juego entre jugadores: "+str(listaJugadores)
        else:
            self.log.write("\n\nnuevo juego entre jugadores: "+str(listaJugadores)+"\n\n")

        random.seed()
            
    def generarTodoLanzamientoPosible(self):
        lista=[]
        lista.append(Actuacion("lanzar",(-1,-1),[0],False))
        lista.append(Actuacion("lanzar",(-1,-1),[1],False))
        lista.append(Actuacion("lanzar",(-1,-1),[2],False))
        lista.append(Actuacion("lanzar",(-1,-1),[3],False))
        lista.append(Actuacion("lanzar",(-1,-1),[4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,1],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,2],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,3],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[1,2],False))
        lista.append(Actuacion("lanzar",(-1,-1),[1,3],False))
        lista.append(Actuacion("lanzar",(-1,-1),[1,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[2,3],False))
        lista.append(Actuacion("lanzar",(-1,-1),[2,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[3,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,1,2],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,1,3],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,1,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,2,3],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,2,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,3,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[1,2,3],False))
        lista.append(Actuacion("lanzar",(-1,-1),[1,2,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[1,3,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[2,3,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,1,2,3],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,1,2,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,1,3,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,2,3,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[1,2,3,4],False))
        lista.append(Actuacion("lanzar",(-1,-1),[0,1,2,3,4],False))
        return lista

    def verificarSiYaAnotado(self, juego, jugador):
        if(juego == "grande"):
            return ( self.marcadores[jugador].yaAnotado("grande") and self.marcadores[jugador].yaAnotado("grande2"))
        else:
            return self.marcadores[jugador].yaAnotado(juego)

    def anotar(self, jugador, actuacion):
        if actuacion.accion == "anotar":
            if(actuacion.anotacion[0]=="grande"):
                if(self.marcadores[jugador].yaAnotado("grande")):
                    actuacion.anotacion=('grande2',actuacion.anotacion[1])
            #print "por anotar: "
            #print actuacion.anotacion
            self.marcadores[jugador].anotar(actuacion.anotacion)
        else:
            assert actuacion.accion == "dormida"
            self.marcadores[jugador].anotarDormida()

    def lanzarDados(self,indiceDados,dados):
        for i in indiceDados:
            dados[i] = random.randrange(6)+1
        #print "Dados: "+str(dados)
        return dados


    def verificarEscaleraDeMano(self, dados):
        dadosOrdenados = sorted(dados)
        if dadosOrdenados[0] == 1 and dadosOrdenados[1] == 3:
            i=1
        else:
            i=0

        ordenados = True
        while ordenados and i<4:
            if dadosOrdenados[i+1]!=dadosOrdenados[i]+1:
                ordenados = False
            i = i + 1
            
        return ordenados
    
    def verificarFullDeMano(self,dados):
        dadosOrdenados = sorted(dados)
        return (dadosOrdenados[0] == dadosOrdenados[1] and dadosOrdenados[3] == dadosOrdenados[4] and dadosOrdenados[0] != dadosOrdenados[4]) and ( dadosOrdenados[2] == dadosOrdenados[3] or dadosOrdenados[2]==dadosOrdenados[1])
    
    def verificarPokerDeMano(self,dados):
        dadosOrdenados = sorted(dados)
        return ( (dadosOrdenados[0] == dadosOrdenados[3]) and (dadosOrdenados[3] != dadosOrdenados[4]) ) or ( (dadosOrdenados[1] == dadosOrdenados[4]) and (dadosOrdenados[0]!=dadosOrdenados[1]))

    def verificarDormida(self,dados):
        dadosOrdenados = sorted(dados)
        return dadosOrdenados[0] == dadosOrdenados[4]

    def verificarJugadasDeMano(self, jugador, dados, puedeSerSobre, esPrimerTiro):        
        lista = []
        esDeMano = self.verificarEscaleraDeMano(dados)
        if esDeMano:
            yaAnotado = self.verificarSiYaAnotado("escalera",jugador)

            if not yaAnotado:
                lista.append(Actuacion("anotar",("escalera",25),[],False))
                if puedeSerSobre: 
                    lista.append(Actuacion("sobre",("escalera",25),[],False))
            elif self.marcadores[jugador].escalera==25 and self.marcadores[jugador].escaleraRespetada == False and esPrimerTiro:
                self.marcadores[jugador].escaleraRespetada = True
                lista.append(Actuacion("lanzar",(-1,-1),[0,1,2,3,4],True))

        esDeMano = self.verificarFullDeMano(dados)
        if esDeMano:
            yaAnotado = self.verificarSiYaAnotado("full",jugador)
            if not yaAnotado:
                lista.append(Actuacion("anotar",("full",35),[],False))
                if puedeSerSobre: 
                    lista.append(Actuacion("sobre",("full",35),[],False))
            elif self.marcadores[jugador].full==35 and self.marcadores[jugador].fullRespetado == False and esPrimerTiro:
                self.marcadores[jugador].fullRespetado = True
                lista.append(Actuacion("lanzar",(-1,-1),[0,1,2,3,4],True))

        esDeMano = self.verificarPokerDeMano(dados)
        if esDeMano:
            yaAnotado = self.verificarSiYaAnotado("poker",jugador)
            if not yaAnotado:
                lista.append(Actuacion("anotar",("poker",45),[],False))
                if puedeSerSobre: 
                    lista.append(Actuacion("sobre",("poker",45),[],False))
            elif self.marcadores[jugador].poker==45 and self.marcadores[jugador].pokerRespetado == False and esPrimerTiro:
                self.marcadores[jugador].pokerRespetado = True
                lista.append(Actuacion("lanzar",(-1,-1),[0,1,2,3,4],True))

        esDeMano = self.verificarDormida(dados)
        if esDeMano:
            lista.append(Actuacion("dormida",(-1,-1),[],False))
        return lista

    def verificarSuma(self,valor,dados):
        dadosOrdenados = sorted(dados)
        if (dadosOrdenados[0] == dadosOrdenados[4] == valor ):
            return 4*valor

        suma = 0
        volcados = 0
        for i in range(5):
            if(dadosOrdenados[i] == valor): suma+=valor
            elif(dadosOrdenados[i] == 7-valor and volcados<2): 
                suma+= valor
                volcados+= 1            
        return suma

    def verificarSumaSinVuelque(self,valor,dados):
        suma = 0
        for i in range(5):
            if(dados[i] == valor): suma+=valor

        return suma

    def verificarSiBorres(self,dados, jugador):
        borres = False;
        dadosCambiados = dados[:] #copiamos los dados para hacer pruebas

        for i in range(5):
            dadosCambiados[i] = 7 - dadosCambiados[i] #Probamos volcando un dado
            todosCeros=0
            faltanPorAnotar=0
            for j in range(1,7):
                yaAnotado = self.verificarSiYaAnotado(self.juegosPosibles[j-1],jugador)
                if(not yaAnotado):
                    faltanPorAnotar+=1
                    suma = self.verificarSumaSinVuelque(j,dadosCambiados)
                    if (suma > 0): break
                    else: todosCeros+=1

            yaAnotado = self.verificarSiYaAnotado("escalera",jugador)
            if(not yaAnotado):
                faltanPorAnotar+=1
                esJugada = self.verificarEscaleraDeMano(dadosCambiados)
                if(not esJugada): todosCeros+=1

            yaAnotado = self.verificarSiYaAnotado("full",jugador)
            if(not yaAnotado):
                faltanPorAnotar+=1
                esJugada = self.verificarFullDeMano(dadosCambiados)
                if(not esJugada): todosCeros+=1

            yaAnotado = self.verificarSiYaAnotado("poker",jugador)
            if(not yaAnotado):
                faltanPorAnotar+=1
                esJugada = self.verificarPokerDeMano(dadosCambiados)
                if(not esJugada): todosCeros+=1

            yaAnotado = self.verificarSiYaAnotado("grande",jugador)
            if(not yaAnotado):
                faltanPorAnotar+=1
                esJugada = self.verificarDormida(dadosCambiados)
                if(not esJugada): todosCeros+=1

            if(todosCeros == faltanPorAnotar):
                borres = True
                break

            for j in range(i+1,5):
                dadosCambiados[j] = 7 - dadosCambiados[j]#volcamos otro dado

                todosCeros=0
                faltanPorAnotar=0
                for k in range(1,7):
                    yaAnotado = self.verificarSiYaAnotado(self.juegosPosibles[k-1],jugador)
                    if(not yaAnotado):
                        faltanPorAnotar+=1
                        suma = self.verificarSumaSinVuelque(k,dadosCambiados)
                        if (suma > 0): break
                        else: todosCeros+=1

                yaAnotado = self.verificarSiYaAnotado("escalera",jugador)
                if(not yaAnotado):
                    faltanPorAnotar+=1
                    esJugada = self.verificarEscaleraDeMano(dadosCambiados)
                    if(not esJugada): todosCeros+=1

                yaAnotado = self.verificarSiYaAnotado("full",jugador)
                if(not yaAnotado):
                    faltanPorAnotar+=1
                    esJugada = self.verificarFullDeMano(dadosCambiados)
                    if(not esJugada): todosCeros+=1

                yaAnotado = self.verificarSiYaAnotado("poker",jugador)
                if(not yaAnotado):
                    faltanPorAnotar+=1
                    esJugada = self.verificarPokerDeMano(dadosCambiados)
                    if(not esJugada): todosCeros+=1

                yaAnotado = self.verificarSiYaAnotado("grande",jugador)
                if(not yaAnotado):
                    faltanPorAnotar+=1
                    esJugada = self.verificarDormida(dadosCambiados)
                    if(not esJugada): todosCeros+=1

                if(todosCeros == faltanPorAnotar):
                    borres = True
                    break

                dadosCambiados[j] = 7 - dadosCambiados[j]#restituimos vuelque 2

            if (borres): break

            dadosCambiados[i] = 7 - dadosCambiados[i]#restituimos vuelque 1
        #For principal termina aqui
        return borres

    def verificarEscaleraDeHuevo(self,dados):
        vecesTres = dados.count(3)
        vecesCuatro = dados.count(4)
        if vecesTres+vecesCuatro != 2:
            return False
        else:
            vecesUno = dados.count(1)
            vecesSeis = dados.count(6)
            suma = vecesUno+vecesSeis
            if suma == 0 or suma == 3:
                return False
            else: #suma solo puede ser 1 o 2
                if(vecesTres==0 or vecesCuatro==0):
                    vecesDos = dados.count(2)
                    if ( vecesUno == 2 or vecesSeis == 2 ) and vecesDos==1:
                        return False
                    else:
                        return True
                else:
                    return True
        assert(False)

    def verificarFullDeHuevo(self,dados): #revisar
        for i in range(1,3):
            vecesValor = dados.count(i)
            vecesComplemento = dados.count(7-i)
            suma = vecesValor + vecesComplemento
            if suma==0:
                continue
            elif suma==5:
                return True
            elif suma==1 or suma==4:
                return False
            else:
                vecesValor = dados.count(i+1)
                vecesComplemento = dados.count(7-i-1)
                suma2 = vecesValor + vecesComplemento
                if suma2 == 1 or suma+suma2 == 4:
                    return False
                else:
                    assert(suma+suma2==2 or suma+suma2==3 or suma+suma2==5)
                    return True

        vecesValor = dados.count(3)
        vecesComplemento = dados.count(4)
        assert(vecesValor+vecesComplemento==5)
        return True

    def verificarPokerDeHuevo(self,dados):
        for i in range(1,4):
            vecesValor = dados.count(i)
            vecesComplemento = dados.count(7-i)
            if vecesValor+vecesComplemento>=4:
                return True
        return False

    def verificarGrande(self,dados):
        dadosOrdenados = sorted(dados)
        
        if (dadosOrdenados[0] == 7-dadosOrdenados[4]):
            if (dadosOrdenados[0] == dadosOrdenados[3]) or (dadosOrdenados[1] == dadosOrdenados[4]):
                return True
            elif ((dadosOrdenados[0] == dadosOrdenados[2]) and (dadosOrdenados[3] == dadosOrdenados[4])) or ((dadosOrdenados[2] == dadosOrdenados[4]) and (dadosOrdenados[0] == dadosOrdenados[1])):
                return True
         
        return False

    def verificarJugadasConVuelque(self,jugador,dados,puedeSerSobre):
        lista = []
        incluirBorres = self.verificarSiBorres(dados, jugador)
        for i in range(1,7):
            yaAnotado = self.verificarSiYaAnotado(self.juegosPosibles[i-1],jugador)
            if not yaAnotado:
                resultado = self.verificarSuma(i,dados)
                if resultado >0 or incluirBorres: 
                    lista.append(Actuacion("anotar",(self.juegosPosibles[i-1],resultado),[],False))
                if puedeSerSobre and (resultado > 0 or incluirBorres):
                    lista.append(Actuacion("sobre",(self.juegosPosibles[i-1],resultado),[],False))

        yaAnotado = self.verificarSiYaAnotado("escalera",jugador)
        if not yaAnotado:
            resultado = self.verificarEscaleraDeHuevo(dados)
            if resultado:
                lista.append(Actuacion("anotar",("escalera",20),[],False))
                if puedeSerSobre:
                    lista.append(Actuacion("sobre",("escalera",20),[],False))
            elif incluirBorres:
                lista.append(Actuacion("anotar",("escalera",0),[],False))
                if puedeSerSobre:
                    lista.append(Actuacion("sobre",("escalera",0),[],False))

        yaAnotado = self.verificarSiYaAnotado("full",jugador)
        if not yaAnotado:
            resultado = self.verificarFullDeHuevo(dados)
            if resultado:
                lista.append(Actuacion("anotar",("full",30),[],False))
                if puedeSerSobre:
                    lista.append(Actuacion("sobre",("full",30),[],False))
            elif incluirBorres:
                lista.append(Actuacion("anotar",("full",0),[],False))
                if puedeSerSobre:
                    lista.append(Actuacion("sobre",("full",0),[],False))

        yaAnotado = self.verificarSiYaAnotado("poker",jugador)
        if not yaAnotado:
            resultado = self.verificarPokerDeHuevo(dados)
            if resultado:
                lista.append(Actuacion("anotar",("poker",40),[],False))
                if puedeSerSobre:
                    lista.append(Actuacion("sobre",("poker",40),[],False))
            elif incluirBorres:
                lista.append(Actuacion("anotar",("poker",0),[],False))
                if puedeSerSobre:
                    lista.append(Actuacion("sobre",("poker",0),[],False))

        yaAnotado = self.verificarSiYaAnotado("grande",jugador)
        if not yaAnotado:
            resultado = self.verificarGrande(dados)
            if resultado:
                lista.append(Actuacion("anotar",("grande",50),[],False))
                if puedeSerSobre:
                    lista.append(Actuacion("sobre",("grande",50),[],False))
            elif incluirBorres:
                lista.append(Actuacion("anotar",("grande",0),[],False))
                if puedeSerSobre:
                    lista.append(Actuacion("sobre",("grande",0),[],False))

        return lista

    def agregarBorres(self):
        lista=[]
        for jugada in self.juegosPosibles:
            lista.append(Actuacion("anotar",(jugada,0),[],False))

        return lista


    def imprimirActuaciones(self,lista):
        for actuacion in lista:
            actuacion.displayCompacto()


    def imprimirResultado(self):
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

        for nombreJugador in self.listaJugadores:
            nombres+=nombreJugador.center(30)
            balas+=repr(self.marcadores[nombreJugador].balas).rjust(30)
            tontos+=repr(self.marcadores[nombreJugador].tontos).rjust(30)
            trenes+=repr(self.marcadores[nombreJugador].trenes).rjust(30)
            cuadras+=repr(self.marcadores[nombreJugador].cuadras).rjust(30)
            quinas+=repr(self.marcadores[nombreJugador].quinas).rjust(30)
            senas+=repr(self.marcadores[nombreJugador].senas).rjust(30)
            escalera+=repr(self.marcadores[nombreJugador].escalera).rjust(30)
            full+=repr(self.marcadores[nombreJugador].full).rjust(30)
            poker+=repr(self.marcadores[nombreJugador].poker).rjust(30)
            grande+=repr(self.marcadores[nombreJugador].grande).rjust(30)
            grande2+=repr(self.marcadores[nombreJugador].grande2).rjust(30)
            suma+=repr(self.marcadores[nombreJugador].suma).rjust(30)
            dormida+=repr(self.marcadores[nombreJugador].dormida).rjust(30)
            #self.marcadores[nombreJugador].display()

        if not self.modoCompeticion:
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
        else:
            self.log.write(nombres+"\n")
            self.log.write(balas+"\n")
            self.log.write(tontos+"\n")
            self.log.write(trenes+"\n")
            self.log.write(cuadras+"\n")
            self.log.write(quinas+"\n")
            self.log.write(senas+"\n")
            self.log.write(escalera+"\n")
            self.log.write(full+"\n")
            self.log.write(poker+"\n")
            self.log.write(grande+"\n")
            self.log.write(grande2+"\n")
            self.log.write(suma+"\n")
            self.log.write(dormida+"\n")

    def calcularActuaciones(self,jugador,turno,lanzamiento,indiceDados,dados,resultadoPrevio,yaAnotado):
        actuacionesPosibles=[]

        if lanzamiento==1:
            assert(len(indiceDados)==5)
            actuacionesPosibles+=self.generarTodoLanzamientoPosible()
            actuacionesPosibles+=self.verificarJugadasDeMano(jugador,dados,turno==1, lanzamiento==1)  #aqui podria agregarse realizar lanzamientos de dados porque se respeta
        else:
            assert(lanzamiento==2)
            #actuacionesPosibles+=self.agregarBorres()
            if len(indiceDados)==5:
                actuacionesPosibles+=self.verificarJugadasDeMano(jugador,dados,turno==1, lanzamiento==1)
            actuacionesPosibles+=self.verificarJugadasConVuelque(jugador,dados,turno==1)
            if turno==2:
                if yaAnotado:
                    actuacionesPosibles.append(Actuacion("nada",(-1,-1),[],False))
                else:
                    actuacionesPosibles.append(Actuacion("anotar",resultadoPrevio,[],False))
        
        assert(len(actuacionesPosibles)>0)
        #self.imprimirActuaciones(actuacionesPosibles)
        return actuacionesPosibles

    def ejecutarTurno(self,nombreJugador,jugador):
        self.imprimirResultado()

        if self.modoCompeticion:
            self.log.write("nuevo turno para jugador: "+nombreJugador+"\n")
        else:
            print "nuevo turno para jugador: "+nombreJugador

        jugador.setNuevoTurno()
        dados=[0,0,0,0,0]
        indiceDados=[0,1,2,3,4]
        resultadoPrevio=[-1,-1]
        yaAnotado=False
        import copy

        jugador.setNuevoIntento()
        if self.modoCompeticion:
            self.log.write("Intento: 1\n")

        lanzar=True
        lanzamiento=0
        while lanzar:
            lanzamiento+=1
            jugador.setNuevoLanzamiento()
            assert(len(indiceDados)>0)
            dados  = self.lanzarDados(indiceDados,dados)
            if self.modoCompeticion:
                self.log.write("Lanzamiento: "+str(lanzamiento)+"\n")
                self.log.write("tiene dados: "+str(dados)+"\n")
            else:
                print "lanzamiento: "+str(lanzamiento)

            actuacionesPosibles = self.calcularActuaciones(nombreJugador,1,lanzamiento,indiceDados,dados,resultadoPrevio,yaAnotado)
            assert(len(actuacionesPosibles)>0)
            copiaDados = copy.deepcopy(dados)
            copiaActuaciones = copy.deepcopy(actuacionesPosibles)
            copiaMarcadores = copy.deepcopy(self.marcadores)
            copiaResultadoPrevio = copy.deepcopy(resultadoPrevio)
            indiceActuacion = jugador.jugar(copiaMarcadores,copiaActuaciones,copiaDados,copiaResultadoPrevio)
            assert(indiceActuacion<len(actuacionesPosibles))
            actuacion = actuacionesPosibles[indiceActuacion]
            if self.modoCompeticion:
                self.log.write("Escoge: ")
                actuacion.imprimirEnArchivo(self.log)
            #print "actuacion seleccionada: "
            #actuacion.display()

            lanzar = ( actuacion.accion == "lanzar" )
            if lanzar:
                indiceDados=actuacion.indiceDados
                if actuacion.seRespeta:
                    jugador.setSeRespeta()
                    lanzamiento-=1

        if actuacion.accion == "dormida":
            self.anotar(nombreJugador,actuacion)
            return True

        if actuacion.accion == "anotar":
            #intento+=1
            yaAnotado=True
            self.anotar(nombreJugador,actuacion)
        else:
            assert(actuacion.accion == "sobre")
            resultadoPrevio = actuacion.anotacion


        if  (not self.marcadores[nombreJugador].marcadorIncompleto()) or self.marcadores[nombreJugador].tieneAlalay():
            return self.marcadores[nombreJugador].tieneAlalay()

        jugador.setNuevoIntento()
        if self.modoCompeticion:
            self.log.write("Intento: 2\n")
        indiceDados=[0,1,2,3,4]
        lanzar=True
        lanzamiento=0
        while lanzar:
            lanzamiento+=1
            jugador.setNuevoLanzamiento()
            dados  = self.lanzarDados(indiceDados,dados)
            if self.modoCompeticion:
                self.log.write("Lanzamiento: "+str(lanzamiento)+"\n")
                self.log.write("tiene dados: "+str(dados)+"\n")
            actuacionesPosibles = self.calcularActuaciones(nombreJugador,2,lanzamiento,indiceDados,dados,resultadoPrevio,yaAnotado)
            assert(len(actuacionesPosibles)>0)
            copiaDados = copy.deepcopy(dados)
            copiaActuaciones = copy.deepcopy(actuacionesPosibles)
            copiaMarcadores = copy.deepcopy(self.marcadores)
            copiaResultadoPrevio = copy.deepcopy(resultadoPrevio)
#            self.imprimirResultado()
            indiceActuacion = jugador.jugar(copiaMarcadores,copiaActuaciones,copiaDados,copiaResultadoPrevio)
            assert(indiceActuacion<len(actuacionesPosibles))
            actuacion = actuacionesPosibles[indiceActuacion]
            if self.modoCompeticion:
                self.log.write("Escoge: ")
                actuacion.imprimirEnArchivo(self.log)
            #print "actuacion seleccionada: "
            #actuacion.display()

            lanzar = ( actuacion.accion == "lanzar" )
            if lanzar:
                indiceDados=actuacion.indiceDados
                if actuacion.seRespeta:
                    jugador.setSeRespeta()
                    lanzamiento-=1

        if actuacion.accion == "dormida":
            self.anotar(nombreJugador,actuacion)
            return True

        if actuacion.accion == "anotar":
            yaAnotado=True
            self.anotar(nombreJugador,actuacion)
        else:
            assert(actuacion.accion=="nada")

        assert(yaAnotado)
        return self.marcadores[nombreJugador].tieneAlalay()

    def hacerJugar(self):
        marcadoresIncompletos = len(self.listaJugadores)
        alalayODormida=False

        ganadores=[]

        while marcadoresIncompletos!=0 and not alalayODormida:
            marcadoresIncompletos=len(self.listaJugadores)
            for nombreJugador in self.listaJugadores:
                if self.marcadores[nombreJugador].marcadorIncompleto():
                    alalayODormida = self.ejecutarTurno(nombreJugador,self.jugadores[nombreJugador])
                    if(alalayODormida):
                        ganadores.append(nombreJugador)
                        break
                else:
                    marcadoresIncompletos-=1

        self.imprimirResultado()
        if not alalayODormida:
            puntajeMayor=0
            for nombreJugador in self.listaJugadores:
                if self.marcadores[nombreJugador].suma > puntajeMayor:
                    puntajeMayor = self.marcadores[nombreJugador].suma

            for nombreJugador in self.listaJugadores:
                if self.marcadores[nombreJugador].suma == puntajeMayor:
                    ganadores.append(nombreJugador)

        sumaGanador = self.marcadores[ganadores[0]].suma
        for i in range(len(ganadores)):
            if(len(ganadores)>1):
                assert(self.marcadores[ganadores[i]].dormida==False and self.marcadores[ganadores[i]].panzaDeOro==False)
                assert(self.marcadores[ganadores[i]].suma == sumaGanador)

        return ganadores



            
                    
            
    
    
