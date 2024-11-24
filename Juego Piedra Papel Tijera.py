# Importamos la libreria random para que la computadora pueda hacer su elección entre piedra, papel o tijera
import random

# Define una función que genera y devuelve una elección aleatoria para la computadora de la lista opciones
def obtener_eleccion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

# Define la función que determina el ganador según las reglas del juego
def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "Empate"
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdiste"
