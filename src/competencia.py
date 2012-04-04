#!/usr/bin/python
from anotador import *
import time


def imprimirHash(hashAImprimir):
    for key in hashAImprimir.keys():
        print "\t"+key+": "+str(hashAImprimir[key])


os.system("clear")
print "Iniciando competencia"
hashJugadores = {"JugadorAleatorio":0,
                 "JugadorBase":0,
                 "JugadorBase4":0,
                 "JugadorBase2":0}
numRepeticiones = 500

listaJugadores = hashJugadores.keys()
for i in range(0,len(listaJugadores)):
    for j in range(i+1,len(listaJugadores)):
        for k in range(j+1,len(listaJugadores)):
            for l in range(numRepeticiones):
                #time.sleep(1)
                juego = Anotador([listaJugadores[i],listaJugadores[j],listaJugadores[k]],True)
                ganadores = juego.hacerJugar()
                for ganador in ganadores:
                    hashJugadores[ganador]+=1
                    os.system("clear")
                    print "\nActualmente en Juego: "+"("+str(l+1)+"/"+str(numRepeticiones)+"): "+listaJugadores[i]+" "+listaJugadores[j]+" "+listaJugadores[k]+"\n"
                    print "PUNTAJES"
                    imprimirHash(hashJugadores)

resultado = open("resultadoCompetencia.txt","wt")
resultado.write(str(hashJugadores))

