#!/usr/bin/python3
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk # noqa

builder = Gtk.Builder()
glade_file = (
              '/home/isabater/UCR/Programacion_Bajo_Plataformas_Abiertas/'
              'Proyecto_Python_Battleship/Interfaz_Battleships_Buttons.glade'
)
builder.add_from_file(glade_file)

handlers = {'terminar aplicacion': Gtk.main_quit}
builder.connect_signals(handlers)

# Obtenemos widgets por ID
win = builder.get_object('main_window')
posicion_A1 = builder.get_object('A1')

# Se crea una asociacion entre la senal 'destroy' y la funcion Gtk.main_quit
# win.connect('destroy', Gtk.main_quit)


# Se muestran los widgets contenidos en una ventana (objeto win)
win.show_all()

# Se ejecuta el ciclo principal del GTK
# Llamada bloqueante
Gtk.main()
