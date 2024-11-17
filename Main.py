import numpy as np
import variables as var
from Tablero import Tablero
import random

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
posiciones_jugador = tablero_jugador.posicionar_barco_aleatorio(var.barcos)
#posiciones_pc = tablero_pc.posicionar_barco([(0,0)])
print(posiciones_pc)

#introducimos los disparos y si aciertas te sigue tocando
# Definimos el juego hasta que no haya barcos restantes
juego_terminado = False

# Bucle principal que controla el juego hasta que termine
while not juego_terminado:
    # ---- Turno del Jugador ----
    tocado = True  # El jugador sigue disparando si acierta
    while tocado:
        disparo1 = int(input("Por favor, introduce tu disparo X "))
        disparo2 = int(input("Por favor, introduce tu disparo Y "))
        coordenadas = (disparo1, disparo2)
        print(f"Coordenadas del disparo del jugador: {coordenadas}")

        disparo_jugador = tablero_pc.disparo_coordenada(coordenadas)
        print("Tablero de disparos del jugador después del disparo:")
        print(disparo_jugador[1])
        
        # Verificar si se ha hundido un barco
        tocado = disparo_jugador[2]

    # Verificar si todos los barcos del PC han sido hundidos
        barcos_pc_restantes = np.sum(tablero_pc.tablero_disparos == "O")
        if barcos_pc_restantes == 0:
            print("¡Felicidades! Has hundido todos los barcos del oponente. ¡Ganaste!")
            juego_terminado = True
            break
    # Si el juego ha terminado, rompemos el bucle principal antes de continuar
    if juego_terminado is True:
        break


    # ---- Turno del PC ----
    if not juego_terminado:
        print("\nTurno del PC:")
        tocado_pc = True  # El PC sigue disparando si acierta
        while tocado_pc:
            disparo1_pc = random.randint(0, var.tamanio - 1)
            disparo2_pc = random.randint(0, var.tamanio - 1)
            coordenadas_pc = (disparo1_pc, disparo2_pc)
            print(f"Coordenadas del disparo del PC: {coordenadas_pc}")

            disparo_pc = tablero_jugador.disparo_coordenada(coordenadas_pc)
            print("Tablero del jugador después del disparo del PC:")
            print(disparo_pc[1])
        
            # Verificar si se ha hundido un barco
            tocado_pc = disparo_pc[2]

            # Verificar si todos los barcos del jugador han sido hundidos
            barcos_jugador_restantes = np.sum(tablero_jugador.tablero_disparos == "O")
            if barcos_jugador_restantes == 0:
                print("¡El PC ha hundido todos tus barcos! ¡Perdiste!")
                juego_terminado = True
                break

    if juego_terminado is True:
        break




