from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player with specific color and width."""
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
    """Draw O player with specific color and width."""
    pencolor("red")  # Cambia el color de la O
    width(4)  # Cambia el grosor de la O
    up()
    goto(x + 67, y + 15)
    down()
    circle(52)  # Ajusta el radio del círculo para que se centre mejor


def floor(value):
    """Round the given value down to the nearest Tic-Tac-Toe grid square.

    Args:
        value (int): The coordinate value to be rounded.

    Returns:
        int: The coordinate aligned to the grid.
    """
    return ((value + 200) // 133) * 133 - 200


# Lista para llevar el registro de posiciones ocupadas
occupied = []

state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    # Verifica si la posición ya está ocupada
    if (x, y) in occupied:  # <- Verificación que impide volver a colocar un símbolo
        print("Casilla ocupada, elige otra.")  # <- Mensaje de aviso
        return  # <- Evita cualquier acción adicional

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
