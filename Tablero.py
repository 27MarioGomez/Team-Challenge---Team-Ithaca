import numpy as np
import variables as var
from variables import tamanio

class Tablero:

    def __init__(self, id_jugador, tablero_vacio, tamanio = var.tamanio, barcos= var.barcos):
        self.id_jugador = id_jugador
        self.tamanio = tamanio
        self.barcos = barcos
        self.tablero_vacio = tablero_vacio
#Hemos definido tamaño y barcos como variables fijas y tablero vacio seria un array a rellenar más adelante



    def posicionar_barco (self, posiciones): #No hace falta meter el argumento tablero_vacio porque ya está declarado arriba
        for posicion in posiciones:
            self.tablero_vacio[posicion] = "O"
        return self.tablero_vacio
#Hemos definido tamaño y barcos como variables fijas y tablero vacio seria un array a rellenar más adelante


#Comprobación del código: 

hundir_flota = Tablero(876, np.full((var.tamanio,var.tamanio), " "))
print(hundir_flota.tablero_vacio)
posicion = hundir_flota.posicionar_barco((0,1))
print(posicion)
