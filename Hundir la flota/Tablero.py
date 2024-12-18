import numpy as np
import variables as var
from variables import tamanio
import random

class Tablero:
# Definimos tamaño y barcos como variables fijas y tablero vacio seria un array a rellenar más adelante
    def __init__(self, id_jugador, tablero_vacio, tablero_disparos, tamanio = var.tamanio, barcos= var.barcos,):
        self.id_jugador = id_jugador
        self.tamanio = tamanio
        self.barcos = barcos
        self.tablero_vacio = tablero_vacio
        self.tablero_disparos = tablero_disparos


# Definimos tamaño y barcos como variables fijas y tablero vacio seria un array a rellenar más adelante
    def posicionar_barco (self, posiciones): #No hace falta meter el argumento tablero_disparos porque ya está declarado arriba
        for posicion in posiciones:
            self.tablero_disparos[posicion] = "O"
        return self.tablero_disparos


# Creamos la función de disparos tal y como vimos en clase
    def disparo_coordenada (self, coordenada):
        tocado = False
        if self.tablero_disparos[coordenada] == "O":
            self.tablero_disparos[coordenada] = "X"
            self.tablero_vacio[coordenada] = "X"
            tocado = True
            print ("\n¡Tocado! Sigue así, vuelves a disparar.\n")
        elif self.tablero_disparos[coordenada] == "-":
            print ("\nEstate atento. Ya habías disparado aqui :(\n)")
        elif self.tablero_disparos[coordenada] == "X":
            print ("\nEstate atento. Ya me habías dado\n")
        else:
            self.tablero_disparos[coordenada] = "-"
            self.tablero_vacio[coordenada] = "-"
            print ("\n¡Agua! Aquí no hay barco.\n")
        return [self.tablero_disparos , self.tablero_vacio, tocado]

# Funcion para posicionar los barcos aleatoriamente desde el inicio
    def posicionar_barco_aleatorio (self, barcos): # Algo va mal de esta funcion
        for barco, longitud in barcos.items():
            # colocado = False
            # while not colocado:
            while True:
                orientaciones = ["N", "S", "E", "O"]
                orientacion = random.choice(orientaciones)

                # Definimos las variables para la fila inicial y para la columna inicial
                fila_inicial = random.randint(0, self.tablero_disparos.shape[0] - 1)
                columna_inicial = random.randint(0, self.tablero_disparos.shape[1] - 1)
                posiciones = []
                for i in range(longitud): # no se si son unos o is
                    if orientacion == "N":
                        fila = fila_inicial - i # Lo restamos para movernos al norte
                        columna = columna_inicial
                    elif orientacion == "S":
                        fila = fila_inicial + i
                        columna = columna_inicial
                    elif orientacion == "E":
                        fila = fila_inicial
                        columna = columna_inicial + i
                    elif orientacion == "O":
                        fila = fila_inicial
                        columna = columna_inicial - i
                    
                    # Comprobamos si la nueva posición está dentro del tablero
                    if (0 <= fila < self.tablero_disparos.shape[0]) and (0 <= columna < self.tablero_disparos.shape[1]):
                        posiciones.append((fila, columna))
                    else:
                        break

                # Comprobamos si cuando generamos un barco aleatoriamente, no pisemos a otro
                # Verifica si el barco tiene la longitud correcta
                if len(posiciones) == longitud:
                    # Comprueba si todas las posiciones están vacías
                    posiciones_vacias = True
                    for pos in posiciones:
                        if self.tablero_disparos[pos] != " ":
                            posiciones_vacias = False
                            break
                            
                    # Si todas las posiciones están vacías, posiciona el barco y termina el bucle
                    if posiciones_vacias:
                        self.posicionar_barco(posiciones) #self.tablero_disparos,
                        break
        return self.tablero_disparos
    
    
