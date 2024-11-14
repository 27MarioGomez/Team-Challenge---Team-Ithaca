import numpy as np
import variables as var
from variables import tamanio

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
            print ("Tocado")
        elif self.tablero_disparos[coordenada] == "-":
            print ("Ya habías disparado aqui")
        elif self.tablero_disparos[coordenada] == "X":
            print ("Ya me habías dado")
        else:
            self.tablero_disparos[coordenada] = "-"
            self.tablero_vacio[coordenada] = "-"
            print ("Agua")
        return [self.tablero_disparos , self.tablero_vacio, tocado]

# Creamos la función de posicionar el barco aleatoriamente
