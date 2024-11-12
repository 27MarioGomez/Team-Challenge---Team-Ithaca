import numpy as np
import variables as var
from variables import tamanio

var.tamanio
var.barcos


class Tablero:

    def __init__(self, id_jugador, tablero_vacio, tablero_maquina, tamanio = var.tamanio, barcos= var.barcos):
        self.id_jugador = id_jugador
        self.tamanio = tamanio
        self.barcos = barcos
        self.tablero_vacio = tablero_vacio
        self.tablero_maquina = tablero_maquina

    def posicionar_barco (self, tablero_vacio, posiciones): #revisar si hay que meter el primer self o no
        for posicion in posiciones:
            self.tablero_vacio[posicion] = "O"
#Hemos definido tamaño y barcos como variables fijas y tablero vacio seria un array a rellenar más adelante
