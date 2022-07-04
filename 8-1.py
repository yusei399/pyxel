import pyxel

pyxel.init(200,200)

ballx = 100
bally = 0
vx = 0.866    # cos 30 degree
vy = 0.5     # sin 30 degree
def update():
    global ballx, bally, vx, vy
    ballx += vx
    bally += vy


    if ballx >= 200:
        vx = -0.866
    if 0 >= ballx:
        vx = 0.866
    if bally >= 200:
        ballx = 100
        bally = 0



def draw():
    global ballx, bally, vx, vy
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)

pyxel.run(update, draw)
