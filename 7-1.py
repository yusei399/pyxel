import pyxel

pyxel.init(200,200)

a = 0
speed = 1
def update():
    global a
    global speed
    if pyxel.btnp(pyxel.KEY_SPACE):
        speed *= -1
    a += speed

def draw():
    global a
    pyxel.cls(7)
    pyxel.circ(a, a, 10, 0)

pyxel.run(update, draw)
