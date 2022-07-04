import pyxel

pyxel.init(200,200)

a = 0
b = 1
def update():
    global a,b
    a += b
    if a == 200:
        b += -1
    elif a == 0:
        b += 1


def draw():
    global a,b
    pyxel.cls(7)
    pyxel.circ(a, a, 10, 0)

pyxel.run(update, draw)
