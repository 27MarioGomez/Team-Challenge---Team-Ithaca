import numpy as np
import variables as var
from Tablero import Tablero


print ("Bienvenido al juego Hundir la flota")
print ("Las instrucciones son:") #rellenar con las instrucciones
nombre_jugador = input ("Por favor, introduce tu nombre ")
print(f"Hola {nombre_jugador}, ¿te apetece comenzar una partida contra mí")

# Creamos los tableros del pc y del jugador
tablero_pc = Tablero("PC", np.full((var.tamanio,var.tamanio), " "), np.full((var.tamanio,var.tamanio), " "))
tablero_jugador = Tablero(nombre_jugador, np.full((var.tamanio,var.tamanio), " "), np.full((var.tamanio,var.tamanio), " "))

'''
barco1_pc = ([0,1])
barco2_pc = ([(2,2),(3,2)])
flota_pc = [barco1_pc, barco2_pc]

barco1_jugador = ([1,1])
barco2_jugador = ([(3,4),(3,5)])
flota_jugador = [barco1_jugador,barco2_jugador]
'''
# Creamos todas las posiciones de forma temporal como una lista de tuplas
flota_pc = [(0,1),(2,2),(3,2)]
# Colocmos los barcos del pc
#posiciones_pc = tablero_pc.posicionar_barco (flota_pc)
posiciones_pc = tablero_pc.posicionar_barco_aleatorio(var.barcos)
print(posiciones_pc)

#introducimos los disparos y si aciertas te sigue tocando
tocado = True
while tocado:
    disparo1 = int(input ("Por favor, introduce tu disparo X "))
    disparo2 = int(input ("Por favor, introduce tu disparo Y "))
    coordenadas = (disparo1,disparo2)
    print(coordenadas)
    disparo_jugador = tablero_pc.disparo_coordenada(coordenadas)
    print (disparo_jugador[1])
    tocado = disparo_jugador[2]
    

