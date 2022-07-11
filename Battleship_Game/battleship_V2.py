#!/usr/bin/python3

import random
import time

"""
    -------BATTLESHIPS-------
    ¿Cómo funciona?
   1. Se crea un tablero de 10x10 donde se van a posicionar las naves.
   2. Dispone de 50 balas para hundir dichas naves.
   3. Puede escoger una fila y una columna para disparar. (Ej. B5)
   4. Se indicará cada disparo errado.
   5. Una nave no puede ser posicionada diagonalmente,si un disparo golpea
   el resto de la nave está en alguno de los cuatro puntos cardinales.
   6. Si las naves se hunden antes de usar todas las balas, usted gana.
   De otra manera, usted pierde.
   Legend:
   1. '.' = Espacio vacío
   2. 'O' = Parte de la nave
   3. 'X' = Parte de la nave golpeada con un disparo
   4. '#' = Disparo errado
"""

# Variable global para la malla
grid = [[]]
# Variable global para el tamaño de la malla
grid_size = 10
# Variable global para el número de naves a colocar
num_of_ships = 2
# Variable global para munición restante
bullets_left = 50
# Variable global de juego terminado
game_over = False
# Variable global para número de naves hundidas
num_of_ships_sunk = 0
# Variable global para posición de las naves
ship_positions = [[]]
# Variable global para el alfabeto
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """
    Hace una revisión de la fila y columna para verificar que sea seguro
    posicionar una nave en ese espacio
    """
    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = 'O'
    return all_valid


def try_to_place_ship_on_grid(row, col, direction, length):
    """
    Basado en la dirección va a llamar a un método auxiliar para tratar
    de colocar una nave en el espacio de juego
    """
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == 'left':
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == 'right':
        if col + length >= grid_size:
            return False
        end_col = col + length

    elif direction == 'up':
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == 'down':
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)


def create_grid():
    """
    Se crea una malla de 10x10 y coloca de forma aleatoria naves de
    diferentes tamaños en diferentes direcciones
    """
    global grid
    global grid_size
    global num_of_ships
    global ship_positions

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append('.')
        grid.append(row)

    num_of_ships_placed = 0

    ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(['left', 'right', 'up', 'down'])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(
            random_row, random_col, direction, ship_size
        ):
            num_of_ships_placed += 1


def print_grid():
    """
    Ésta parte imprime la malla con indicadores de letras y números
    para facilitar la selección de la casilla donde se desea jugar
    """
    global grid
    global alphabet

    # debug_mode = True

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=') ')
        for col in range(len(grid[row])):
            if grid[row][col] == 'O':
                print(".", end=' ')
                # if debug_mode:
                #    print("O", end=" ")
                # else:
                #    print(".", end=" ")
            else:
                print(grid[row][col], end=' ')
        print('')

    print('  ', end=' ')
    for i in range(len(grid[0])):
        print(str(i), end=' ')
    print('')


def accept_valid_bullet_placement():
    """
    Obtiene una columna y una fila válidas para colocar el disparo
    """
    global alphabet
    global grid

    is_valid_placement = False
    row = -1
    col = -1
    while is_valid_placement is False:
        placement = input('Ingrese una fila (A-J) '
                          'y una columna (0-9) Ej. B5: ')
        placement = placement.upper()
        if len(placement) <= 0 or len(placement) > 2:
            print('Error: Por favor ingrese solo una fila y una columna')
            continue
        row = placement[0]
        col = placement[1]
        if not row.isalpha() or not col.isnumeric():
            print('Error: Por favor ingrese una letra (A-J) para fila '
                  'y un número (0-9) para la columna')
            continue
        row = alphabet.find(row)
        if not (-1 < row < grid_size):
            print('Error: Por favor ingrese una letra (A-J) para fila '
                  'y un número (0-9) para la columna')
            continue
        col = int(col)
        if not (-1 < col < grid_size):
            print('Error: Por favor ingrese una letra (A-J) para fila '
                  'y un número (0-9) para la columna')
            continue
        if grid[row][col] == '#' or grid[row][col] == 'X':
            print('Ya hizo un disparo en esta posición, '
                  'por favor elija otro lugar')
            continue
        if grid[row][col] == '.' or grid[row][col] == 'O':
            is_valid_placement = True

    return row, col


def check_for_ship_sunk(row, col):
    """
    Si todas las partes de la nave han sido golpeadas, la nave se hunde
    y se incrementa el contador de naves hundidas
    """
    global ship_positions
    global grid

    for position in ship_positions:
        start_row = position[0]
        end_row = position[1]
        start_col = position[2]
        end_col = position[3]
        if start_row <= row <= end_row and start_col <= col <= end_col:
            # Ship found, now check if its all sunk
            for r in range(start_row, end_row):
                for c in range(start_col, end_col):
                    if grid[r][c] != 'X':
                        return False
    return True


def shoot_bullet(row, col):
    # retorna 1 si una nave fue dañada, 0 en caso contrario
    """
    Actualiza la malla y las naves basadas en donde el disparo fue realizado
    """
    global grid
    global num_of_ships_sunk
    global bullets_left
    global alphabet
    row = alphabet.find(row)
    col = int(col)
    print('')
    print('----------------------------')
    bullets_left -= 1
    if grid[row][col] == '.':
        print('Falló, no hubieron naves dañadas')
        grid[row][col] = '#'
        return 0
    elif grid[row][col] == 'O':
        print('Acertó', end=' ')
        grid[row][col] = 'X'
        if check_for_ship_sunk(row, col):
            print('Una nave fue completamente hundida')
            num_of_ships_sunk += 1
        else:
            print('Una nave recibió un disparo')
        return 1
    else:
        return 0


def check_for_game_over():
    """
    Si todas las naves han sido hundidas o si se se queda sin balas se
    termina el juego
    """
    global num_of_ships_sunk
    global num_of_ships
    global bullets_left
    global game_over

    if num_of_ships == num_of_ships_sunk:
        print('Felicidades, ha ganado.')
        game_over = True
    elif bullets_left <= 0:
        print('Ha perdido. Se quedó sin municiones')
        game_over = True


def main():
    """
    Definición del main del programa
    """
    global game_over

    print('-----Bienvenido a Battleships-----')
    print('Dispone de 50 municiones para derribar 8 naves, '
          '¡que inicie la batalla!')

    create_grid()

    while game_over is False:
        print_grid()
        print('Número de naves restantes: ' +
              str(num_of_ships - num_of_ships_sunk))
        print('Número de municiones restantes: ' + str(bullets_left))
        shoot_bullet()
        print('----------------------------')
        print('')
        check_for_game_over()


if __name__ == '__main__':
    """
    Este método solo es llamado cuando el programa se corre desde la consola
    o un compilador
    """
    main()
