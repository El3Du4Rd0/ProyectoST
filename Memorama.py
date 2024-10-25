"""Memory, juego de pares numéricos con 10 pares.

Este es un juego de memoria donde se deben hacer coincidir

10 pares de números. El juego utiliza un tablero con cuadrados

ocultos que se revelan al hacer clic en ellos.

Ejercicios:

1. Contar e imprimir cuántos clics se realizan.

2. Reducir el número de fichas a una cuadrícula de 4x4.

3. Detectar cuando todas las fichas están reveladas.

4. Centrar la ficha de un solo dígito.

5. Usar letras en lugar de números.
"""

# Librerías
from random import shuffle
from freegames import path
from turtle import (
    up, goto, down, color, begin_fill, forward, left,
    end_fill, clear, shape, stamp, write, update, ontimer,
    setup, addshape, hideturtle, tracer, onscreenclick, done
)

# Configuración inicial del juego
car = path('car.gif')
tiles = list(range(10)) * 2  # Lista de pares de números (10 pares)
state = {'mark': None, 'taps': 0}  # Estado del juego
hide = [True] * 20  # Lista que indica si las fichas están ocultas


def square(x, y):
    """Dibuja un cuadrado blanco con borde negro en la posición (x, y)."""
    up()  # Levanta el lápiz para moverlo sin dibujar
    goto(x, y)  # Mueve el lápiz a la posición (x, y)
    down()  # Baja el lápiz para empezar a dibujar
    color('black', 'white')  # Define el color del borde y del relleno
    begin_fill()  # Inicia el relleno del cuadrado
    for count in range(4):  # Dibuja un cuadrado de 4 lados
        forward(50)  # Avanza 50 píxeles
        left(90)  # Gira 90 grados a la izquierda
    end_fill()  # Termina el relleno del cuadrado


def index(x, y):
    """Convierte las coordenadas (x, y) al índice de una ficha."""
    return int((x + 100) // 50 + ((y + 100) // 50) * 4)


def xy(count):
    """Convierte el índice de una ficha a coordenadas (x, y)."""
    return (count % 4) * 50 - 100, (count // 4) * 50 - 100


def tap(x, y):
    """Actualiza la marca y las fichas ocultas basadas en un clic."""
    state['taps'] += 1  # Incrementa el contador de clics
    spot = index(x, y)  # Determina qué ficha se ha clicado
    mark = state['mark']  # Obtiene la marca actual

    # Actualiza la marca
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        # Si se hace clic en un par correcto, revela ambas fichas
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None  # Resetea la marca


def all_revealed():
    """Verifica si todas las fichas han sido reveladas."""
    return all(not h for h in hide)


def draw():
    """Dibuja la imagen de fondo y las fichas del juego."""
    clear()  # Limpia la pantalla
    goto(0, 0)  # Coloca el lápiz en el centro
    shape(car)  # Cambia la forma del cursor a la imagen del coche
    stamp()  # Imprime la imagen en la pantalla

    # Dibuja las fichas en el tablero
    for count in range(20):
        if hide[count]:  # Dibuja solo las fichas que están ocultas
            x, y = xy(count)  # Calcula las coordenadas de la ficha
            square(x, y)  # Dibuja la ficha

    mark = state['mark']  # Obtiene la marca actual

    # Si hay una marca seleccionada, muestra su número
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)  # Centra el número en la ficha
        color('black')  # Establece el color del texto
        write(tiles[mark], font=('Arial', 30, 'normal'))  # Escribe el número

    # Muestra el número de clics realizados
    up()
    goto(-200, 200)
    color('black')
    write(f'Taps: {state["taps"]}', font=('Arial', 16, 'normal'))

    # Verifica si todas las fichas han sido reveladas
    if all_revealed():
        up()
        goto(0, -250)
        color('green')
        write('¡Ganaste!', font=('Arial', 30, 'normal'))  # Mensaje de victoria

    update()  # Actualiza la pantalla
    ontimer(draw, 100)  # Llama a la función `draw` cada 100 ms


shuffle(tiles)  # Mezcla las fichas aleatoriamente
setup(500, 500, 370, 0)  # Configura el tamaño y la posición de la ventana
addshape(car)  # Añade la imagen del coche al juego
hideturtle()  # Oculta el cursor
tracer(False)  # Desactiva la animación para mejorar el rendimiento
onscreenclick(tap)  # Llama a la función `tap` al hacer clic en la pantalla
draw()  # Inicia el bucle de dibujo del juego
done()  # Termina el programa cuando se cierra la ventana
