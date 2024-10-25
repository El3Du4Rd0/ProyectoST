from turtle import (
    pencolor, width, up, goto, down, circle, update, setup,
    hideturtle, tracer, onscreenclick, done
)
from freegames import line


def grid():
    """Coloca el grid o rejillas de juego."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Coloca X y con sus parámetros."""
    pencolor("blue")  # Cambia el color de la X
    width(4)  # Cambia el grosor de la X
    up()
    goto(x + 15, y + 15)
    down()
    line(x + 15, y + 15, x + 118, y + 118)
    up()
    goto(x + 118, y + 15)
    down()
    line(x + 118, y + 15, x + 15, y + 118)


def drawo(x, y):
    """Coloca O y con sus parámetros."""
    pencolor("red")  # Cambia el color de la O
    width(4)  # Cambia el grosor de la O
    up()
    goto(x + 67, y + 15)
    down()
    circle(52)  # Ajusta el radio del círculo para que se centre mejor


def floor(value):
    return ((value + 200) // 133) * 133 - 200


# Lista para llevar el registro de posiciones ocupadas
occupied = []

state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Coloca X o O en la casilla seleccionada."""
    x = floor(x)
    y = floor(y)

    # Verifica si la posición ya está ocupada
    if (x, y) in occupied:  # Verificación que impide volver a colocar un símbolo
        print("Casilla ocupada, elige otra.")  # Mensaje de aviso
        return  # Evita cualquier acción adicional

    occupied.append((x, y))  # Añadir la posición a la lista de ocupados
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
