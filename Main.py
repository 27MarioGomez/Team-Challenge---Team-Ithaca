# Imports
import numpy as np
import variables as var
from Tablero import Tablero
import random

# Inicio del juego
print ("\nBienvenido al juego Hundir la flota\n")

print ("Instrucciones:\n- Objetivo: Hunde todos los barcos del oponente antes de que hunda los tuyos.\n"
       "- Preparación: Se colocan aleatoriamente 10 barcos de tamaños variados en un tablero de 10x10.\n"
        "- Juego por turnos: En tu turno, elige una coordenada para disparar; tu oponente dirá si acertaste"
         "o fallaste. Si aciertas, sigues disparando.\n- Victoria: Gana el primer jugador que logre hundir "
         "todos los barcos del oponente.\n")

nombre_jugador = input ("\nPor favor, introduce tu nombre: ")

# Condición inicial para jugar o no (se podría mirar añadir condición de salida)
condicion = input(f"\nHola {nombre_jugador}, ¿te apetece comenzar una partida contra mi? ¿Sí o no? ") 
if (condicion.lower() == "si") or (condicion.lower() == "sí"):
    
    # Creamos los tableros del pc y del jugador
    tablero_pc = Tablero("PC", np.full((var.tamanio,var.tamanio), " "), np.full((var.tamanio,var.tamanio), " "))
    tablero_jugador = Tablero(nombre_jugador, np.full((var.tamanio,var.tamanio), " "), np.full((var.tamanio,var.tamanio), " "))

    # Colocamos los barcos del pc y jugador
    posiciones_pc = tablero_pc.posicionar_barco_aleatorio(var.barcos)
    posiciones_jugador = tablero_jugador.posicionar_barco_aleatorio(var.barcos)

    print("\nTu tablero es:\n", posiciones_jugador)

    # Definimos el juego hasta que no haya barcos restantes
    juego_terminado = False

    # Bucle principal que controla el juego hasta que termine
    while not juego_terminado:

        # ---- Turno del Jugador ----
        tocado = True  # El jugador sigue disparando si acierta
        while tocado:
            print(f"\n-------------------------Es tu turno {nombre_jugador}:-------------------------\n")
            # Añadir que no pueda introducirse una letra o numero >10 y <0, control errores.
            disparo1 = int(input("\nPor favor, introduce tu disparo X ")) 
            disparo2 = int(input("\nPor favor, introduce tu disparo Y "))
            coordenadas = (disparo1, disparo2)
            print(f"\nHas disparado a las coordenadas: {coordenadas}")

            disparo_jugador = tablero_pc.disparo_coordenada(coordenadas)
            print(f"\nTablero de disparos de {nombre_jugador} después del disparo:\n", disparo_jugador[1])
            
            # Verificar si se ha hundido un barco
            tocado = disparo_jugador[2]

            # Verificar si todos los barcos del PC han sido hundidos
            barcos_pc_restantes = np.sum(tablero_pc.tablero_disparos == "O")
            if barcos_pc_restantes == 0:
                print(f"\n¡Felicidades {nombre_jugador}! Has hundido todos los barcos del oponente. ¡Ganaste!\n")
                juego_terminado = True
                break
        # Si el juego ha terminado, rompemos el bucle principal antes de continuar
        if juego_terminado is True:
            break


        # ---- Turno del PC ----
        if not juego_terminado:
            print("\n-------------------------Turno del PC:-------------------------\n")
            tocado_pc = True  # El PC sigue disparando si acierta
            while tocado_pc:
                disparo1_pc = random.randint(0, var.tamanio - 1)
                disparo2_pc = random.randint(0, var.tamanio - 1)
                coordenadas_pc = (disparo1_pc, disparo2_pc)
                print(f"\nEl PC ha disparado a las coordenadas: {coordenadas_pc}\n")

                disparo_pc = tablero_jugador.disparo_coordenada(coordenadas_pc)
                print(f"\nTablero de {nombre_jugador} después del disparo del PC:\n",disparo_pc[0])
            
                # Verificar si se ha hundido un barco
                tocado_pc = disparo_pc[2]

                # Verificar si todos los barcos del jugador han sido hundidos
                barcos_jugador_restantes = np.sum(tablero_jugador.tablero_disparos == "O")
                if barcos_jugador_restantes == 0:
                    print(f"\n¡El PC ha hundido todos tus barcos! ¡Perdiste {nombre_jugador}!\n")
                    juego_terminado = True
                    break

        # Si el juego ha terminado, rompemos el bucle principal antes de continuar
        if juego_terminado is True:
            break

else:
    print(f"\nPues nada {nombre_jugador}, has decidido salir del juego.\n")


