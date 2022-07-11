#!/usr/bin/python3

'''
    -------BATTLESHIPS-------

    Este programa muestra el juego Battleship en una interfaz grafica hecha en
    Gtk glade

    ¿Cómo funciona?
   1. Se crea un tablero de 10x10 donde se van a posicionar las naves.
   2. Dispone de 50 balas para hundir dichas naves.
   3. Puede escoger con el mouse una fila y una columna para disparar. (Ej. B5)
   4. Se indicará cada disparo errado.
   5. Una nave no puede ser posicionada diagonalmente,si un disparo golpea
   el resto de la nave está en alguno de los cuatro puntos cardinales.
   6. Si las naves se hunden antes de usar todas las balas, usted gana.
   De otra manera, usted pierde.

   Legend:
   1. 'O' = Parte de la nave golpeada con un disparo
   2. '#' = Disparo errado

   Integrantes del Grupo:
   Ariel Mora Murcia - B24454
   Isabel Sabater Aguilar -  B97037
   Jose Carlos Acevedo Fontalvo - B90034
'''


# Se importan las librerias
import gi
from battleship_V2 import shoot_bullet
from battleship_V2 import create_grid

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk # noqa


# Definicion de funcion que coloca label # o O
def btlshipmain(widget, *data):

    result = shoot_bullet(data[0], data[1])
    if result == 0:
        widget.set_label('#')
    else:
        widget.set_label('O')


# Creacion del tablero
create_grid()

# Definicion del constructor para los elementos gtk glade
builder = Gtk.Builder()
builder.add_from_file('Interfaz_Battleships_Buttons.glade')

# Definicion de los handlers y su conexion
handlers = {'press': Gtk.main_quit}
builder.connect_signals(handlers)

# Obtenemos widgets por ID
win = builder.get_object('main_window')
btnA0 = builder.get_object('A0')
btnA0.connect('clicked', btlshipmain, 'A', '0')
btnA1 = builder.get_object('A1')
btnA1.connect('clicked', btlshipmain, 'A', '1')
btnA2 = builder.get_object('A2')
btnA2.connect('clicked', btlshipmain, 'A', '2')
btnA3 = builder.get_object('A3')
btnA3.connect('clicked', btlshipmain, 'A', '3')
btnA4 = builder.get_object('A4')
btnA4.connect('clicked', btlshipmain, 'A', '4')
btnA5 = builder.get_object('A5')
btnA5.connect('clicked', btlshipmain, 'A', '5')
btnA6 = builder.get_object('A6')
btnA6.connect('clicked', btlshipmain, 'A', '6')
btnA7 = builder.get_object('A7')
btnA7.connect('clicked', btlshipmain, 'A', '7')
btnA8 = builder.get_object('A8')
btnA8.connect('clicked', btlshipmain, 'A', '8')
btnA9 = builder.get_object('A9')
btnA9.connect('clicked', btlshipmain, 'A', '9')
btnB0 = builder.get_object('B0')
btnB0.connect('clicked', btlshipmain, 'B', '0')
btnB1 = builder.get_object('B1')
btnB1.connect('clicked', btlshipmain, 'B', '1')
btnB2 = builder.get_object('B2')
btnB2.connect('clicked', btlshipmain, 'B', '2')
btnB3 = builder.get_object('B3')
btnB3.connect('clicked', btlshipmain, 'B', '3')
btnB4 = builder.get_object('B4')
btnB4.connect('clicked', btlshipmain, 'B', '4')
btnB5 = builder.get_object('B5')
btnB5.connect('clicked', btlshipmain, 'B', '5')
btnB6 = builder.get_object('B6')
btnB6.connect('clicked', btlshipmain, 'B', '6')
btnB7 = builder.get_object('B7')
btnB7.connect('clicked', btlshipmain, 'B', '7')
btnB8 = builder.get_object('B8')
btnB8.connect('clicked', btlshipmain, 'B', '8')
btnB9 = builder.get_object('B9')
btnB9.connect('clicked', btlshipmain, 'B', '9')
btnC0 = builder.get_object('C0')
btnC0.connect('clicked', btlshipmain, 'C', '0')
btnC1 = builder.get_object('C1')
btnC1.connect('clicked', btlshipmain, 'C', '1')
btnC2 = builder.get_object('C2')
btnC2.connect('clicked', btlshipmain, 'C', '2')
btnC3 = builder.get_object('C3')
btnC3.connect('clicked', btlshipmain, 'C', '3')
btnC4 = builder.get_object('C4')
btnC4.connect('clicked', btlshipmain, 'C', '4')
btnC5 = builder.get_object('C5')
btnC5.connect('clicked', btlshipmain, 'C', '5')
btnC6 = builder.get_object('C6')
btnC6.connect('clicked', btlshipmain, 'C', '6')
btnC7 = builder.get_object('C7')
btnC7.connect('clicked', btlshipmain, 'C', '7')
btnC8 = builder.get_object('C8')
btnC8.connect('clicked', btlshipmain, 'C', '8')
btnC9 = builder.get_object('C9')
btnC9.connect('clicked', btlshipmain, 'C', '9')
btnD0 = builder.get_object('D0')
btnD0.connect('clicked', btlshipmain, 'D', '0')
btnD1 = builder.get_object('D1')
btnD1.connect('clicked', btlshipmain, 'D', '1')
btnD2 = builder.get_object('D2')
btnD2.connect('clicked', btlshipmain, 'D', '2')
btnD3 = builder.get_object('D3')
btnD3.connect('clicked', btlshipmain, 'D', '3')
btnD4 = builder.get_object('D4')
btnD4.connect('clicked', btlshipmain, 'D', '4')
btnD5 = builder.get_object('D5')
btnD5.connect('clicked', btlshipmain, 'D', '5')
btnD6 = builder.get_object('D6')
btnD6.connect('clicked', btlshipmain, 'D', '6')
btnD7 = builder.get_object('D7')
btnD7.connect('clicked', btlshipmain, 'D', '7')
btnD8 = builder.get_object('D8')
btnD8.connect('clicked', btlshipmain, 'D', '8')
btnD9 = builder.get_object('D9')
btnD9.connect('clicked', btlshipmain, 'D', '9')
btnE0 = builder.get_object('E0')
btnE0.connect('clicked', btlshipmain, 'E', '0')
btnE1 = builder.get_object('E1')
btnE1.connect('clicked', btlshipmain, 'E', '1')
btnE2 = builder.get_object('E2')
btnE2.connect('clicked', btlshipmain, 'E', '2')
btnE3 = builder.get_object('E3')
btnE3.connect('clicked', btlshipmain, 'E', '3')
btnE4 = builder.get_object('E4')
btnE4.connect('clicked', btlshipmain, 'E', '4')
btnE5 = builder.get_object('E5')
btnE5.connect('clicked', btlshipmain, 'E', '5')
btnE6 = builder.get_object('E6')
btnE6.connect('clicked', btlshipmain, 'E', '6')
btnE7 = builder.get_object('E7')
btnE7.connect('clicked', btlshipmain, 'E', '7')
btnE8 = builder.get_object('E8')
btnE8.connect('clicked', btlshipmain, 'E', '8')
btnE9 = builder.get_object('E9')
btnE9.connect('clicked', btlshipmain, 'E', '9')
btnF0 = builder.get_object('F0')
btnF0.connect('clicked', btlshipmain, 'F', '0')
btnF1 = builder.get_object('F1')
btnF1.connect('clicked', btlshipmain, 'F', '1')
btnF2 = builder.get_object('F2')
btnF2.connect('clicked', btlshipmain, 'F', '2')
btnF3 = builder.get_object('F3')
btnF3.connect('clicked', btlshipmain, 'F', '3')
btnF4 = builder.get_object('F4')
btnF4.connect('clicked', btlshipmain, 'F', '4')
btnF5 = builder.get_object('F5')
btnF5.connect('clicked', btlshipmain, 'F', '5')
btnF6 = builder.get_object('F6')
btnF6.connect('clicked', btlshipmain, 'F', '6')
btnF7 = builder.get_object('F7')
btnF7.connect('clicked', btlshipmain, 'F', '7')
btnF8 = builder.get_object('F8')
btnF8.connect('clicked', btlshipmain, 'F', '8')
btnF9 = builder.get_object('F9')
btnF9.connect('clicked', btlshipmain, 'F', '9')
btnG0 = builder.get_object('G0')
btnG0.connect('clicked', btlshipmain, 'G', '0')
btnG1 = builder.get_object('G1')
btnG1.connect('clicked', btlshipmain, 'G', '1')
btnG2 = builder.get_object('G2')
btnG2.connect('clicked', btlshipmain, 'G', '2')
btnG3 = builder.get_object('G3')
btnG3.connect('clicked', btlshipmain, 'G', '3')
btnG4 = builder.get_object('G4')
btnG4.connect('clicked', btlshipmain, 'G', '4')
btnG5 = builder.get_object('G5')
btnG5.connect('clicked', btlshipmain, 'G', '5')
btnG6 = builder.get_object('G6')
btnG6.connect('clicked', btlshipmain, 'G', '6')
btnG7 = builder.get_object('G7')
btnG7.connect('clicked', btlshipmain, 'G', '7')
btnG8 = builder.get_object('G8')
btnG8.connect('clicked', btlshipmain, 'G', '8')
btnG9 = builder.get_object('G9')
btnG9.connect('clicked', btlshipmain, 'G', '9')
btnH0 = builder.get_object('H0')
btnH0.connect('clicked', btlshipmain, 'H', '0')
btnH1 = builder.get_object('H1')
btnH1.connect('clicked', btlshipmain, 'H', '1')
btnH2 = builder.get_object('H2')
btnH2.connect('clicked', btlshipmain, 'H', '2')
btnH3 = builder.get_object('H3')
btnH3.connect('clicked', btlshipmain, 'H', '3')
btnH4 = builder.get_object('H4')
btnH4.connect('clicked', btlshipmain, 'H', '4')
btnH5 = builder.get_object('H5')
btnH5.connect('clicked', btlshipmain, 'H', '5')
btnH6 = builder.get_object('H6')
btnH6.connect('clicked', btlshipmain, 'H', '6')
btnH7 = builder.get_object('H7')
btnH7.connect('clicked', btlshipmain, 'H', '7')
btnH8 = builder.get_object('H8')
btnH8.connect('clicked', btlshipmain, 'H', '8')
btnH9 = builder.get_object('H9')
btnH9.connect('clicked', btlshipmain, 'H', '9')
btnI0 = builder.get_object('I0')
btnI0.connect('clicked', btlshipmain, 'I', '0')
btnI1 = builder.get_object('I1')
btnI1.connect('clicked', btlshipmain, 'I', '1')
btnI2 = builder.get_object('I2')
btnI2.connect('clicked', btlshipmain, 'I', '2')
btnI3 = builder.get_object('I3')
btnI3.connect('clicked', btlshipmain, 'I', '3')
btnI4 = builder.get_object('I4')
btnI4.connect('clicked', btlshipmain, 'I', '4')
btnI5 = builder.get_object('I5')
btnI5.connect('clicked', btlshipmain, 'I', '5')
btnI6 = builder.get_object('I6')
btnI6.connect('clicked', btlshipmain, 'I', '6')
btnI7 = builder.get_object('I7')
btnI7.connect('clicked', btlshipmain, 'I', '7')
btnI8 = builder.get_object('I8')
btnI8.connect('clicked', btlshipmain, 'I', '8')
btnI9 = builder.get_object('I9')
btnI9.connect('clicked', btlshipmain, 'I', '9')
btnJ0 = builder.get_object('J0')
btnJ0.connect('clicked', btlshipmain, 'J', '0')
btnJ1 = builder.get_object('J1')
btnJ1.connect('clicked', btlshipmain, 'J', '1')
btnJ2 = builder.get_object('J2')
btnJ2.connect('clicked', btlshipmain, 'J', '2')
btnJ3 = builder.get_object('J3')
btnJ3.connect('clicked', btlshipmain, 'J', '3')
btnJ4 = builder.get_object('J4')
btnJ4.connect('clicked', btlshipmain, 'J', '4')
btnJ5 = builder.get_object('J5')
btnJ5.connect('clicked', btlshipmain, 'J', '5')
btnJ6 = builder.get_object('J6')
btnJ6.connect('clicked', btlshipmain, 'J', '6')
btnJ7 = builder.get_object('J7')
btnJ7.connect('clicked', btlshipmain, 'J', '7')
btnJ8 = builder.get_object('J8')
btnJ8.connect('clicked', btlshipmain, 'J', '8')
btnJ9 = builder.get_object('J9')
btnJ9.connect('clicked', btlshipmain, 'J', '9')


# Funcionalidad del boton exit
def closegame(widget, *data):
    btnquit = builder.get_object('quit')
    if btnquit.connect('press'):
        Gtk.main_quit


# Se crea una asociacion entre la senal 'destroy' y la funcion Gtk.main_quit
win.connect('destroy', Gtk.main_quit)

# Se muestran los widgets contenidos en una ventana (objeto win)
win.show_all()

# Se ejecuta el ciclo principal del GTK
# Llamada bloqueante
Gtk.main()
