import pyxel

pyxel.init(200,200)

ballx = 100
bally = 0
vx = 0.866    # cos 30 degree
vy = 0.5      # sin 30 degree
speed = 10

def update():
    global ballx, bally, vx, vy
    global speed
    ballx += vx * speed
    bally += vy * speed
    if ballx >= 200:
        vx *= -1
    if 0 >= ballx:
        vx = 0.866
    if bally >= 200:
        ballx = 100
        bally = 0
        speed += 1
def draw():
    global ballx, bally, vx, vy
    global speed
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)

pyxel.run(update, draw)
