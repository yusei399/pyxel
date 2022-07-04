import pyxel

pyxel.init(200,200)
pyxel.mouse(True)

state = 0

startX = 0
startY = 0
lastX = 0
lastY = 0

color = 0

def update():
    global startX , startY
    global lastX , lastY
    global state
    if state == 1:
        lastX = pyxel.mouse_x
        lastY = pyxel.mouse_y
    if pyxel.btnp(pyxel.KEY_SPACE):
        if state == 0:
            startX = pyxel.mouse_x
            startY = pyxel.mouse_y
            lastX = startX
            lastY = startY
            state = 1
        elif state == 1:
            lastX = pyxel.mouse_x
            lastY = pyxel.mouse_y
            state = 2
        elif state == 2:
            state = 0



def draw():
    global startX , startY
    global lastX , lastY
    global state
    pyxel.cls(7)
    if state != 0:
        pyxel.line(startX,startY,lastX,lastY,color)
    # pyxel.text(5, 5, f'state: {state}', 0)
pyxel.run(update,draw)
