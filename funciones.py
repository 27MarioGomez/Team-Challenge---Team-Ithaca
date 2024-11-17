import random

# Función para pintar los barcos
def posicionar_barco(tablero, posiciones):
    for posicion in posiciones:
        tablero[posicion] = "O"

# Funcion para posicionar los barcos aleatoriamente desde el inicio
def posicionar_barco_aleatorio (tablero, tamanio, barcos):
    for barco, longitud in barcos.items():
        colocado = False
        intentos = 0
        max_intentos = 100  # Limitar la cantidad de intentos para evitar bucles infinitos
        
        while not colocado and intentos < max_intentos:
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

                # Comprobamos si cuando generamos un barco aleatoriamente, no pisemos a otro
                # Verifica si el barco tiene la longitud correcta
                if len(posiciones) == longitud:
                    # Comprueba si todas las posiciones están vacías
                    posiciones_vacias = True
                    for pos in posiciones:
                        if tablero[pos] != " ":
                            posiciones_vacias = False
                            break
                            
                    # Si todas las posiciones están vacías, posiciona el barco y termina el bucle
                    if posiciones_vacias:
                        posicionar_barco(tablero, posiciones)
                        break


