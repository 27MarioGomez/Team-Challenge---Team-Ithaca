import random

# Función para pintar los barcos
def posicionar_barco(tablero, posiciones):
    for posicion in posiciones:
        tablero[posicion] = "O"

# Funcion para posicionar los barcos aleatoriamente desde el inicio
def posicionar_barco_aleatorio (tablero, tamanio, barcos):
    for barco, longitud in barcos.items():
        colocado = False
        while not colocado:
            orientaciones = ["N", "S", "E", "O"]
            orientacion = random.choice(orientaciones)
            # Definimos las variables para la fila inicial y para la columna inicial
            fila_inicial = random.randint(0, tablero.shape[0] - 1)
            columna_inicial = random.randint(0, tablero.shape[1] - 1)
            posiciones = []
            for i in range(longitud):
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
                if 0 <= fila < tablero.shape[0] and 0 <= columna < tablero.shape[1]:
                    posiciones.append((fila, columna))
                else:
                    break