import pyxel
import random

pyxel.init(200,200)


ballx = [100]
bally = [0]
vx = [0.866,0.866,0,866]
vy = [0.5 ,0.5,0.5]
point = 0
padx = 100
speed = 10


def pad(i):
    global ballx, bally, padx , speed
    if abs(bally[i] - 195) <= 10:
        if ballx[i] <= padx + 20 and ballx[i] >= padx - 20:
            return 1
    return 0



def update():
    global balx , bally , padx ,vx,vy
    for i in range(3):
        ballx[i] += vx[i] * speed
        bally[i] += vy[i] * speed

    for i in range(3):
        if ballx[i] >= 200:
            vx[i] *= -1
        if ballx[i] <= 0:
            vx[i] *= -1
        if bally[i] >= 200:
            bally[i] = 0
            ballx[i] = random.randint(0, 200)
            radian = random.uniform(math.radians(20), math.pi - math.radians(20))
            vx[i] = math.cos(radian)
            vy[i] = math.sin(radian)
            pyxel.play(0, 0)




    if pad(i):
        point += 1
        bally[i] =0
        ballx[i] = random.randint(0, 200)
        radian = random.uniform(math.radians(20), math.pi - math.radians(20))
        vx[i] = math.cos(radian)
        vy[i] = math.sin(radian)
# vx = math.cos(math.radians(90))
# vy = math.sin(math.radians(90)
        pyxel.play(0, 1)

def draw():
    global ballx,bally, vx, vy, padx
    pyxel.cls(7)
    for i in range(0, len(ballx)):
        pyxel.rect(padx-20, 195, 40, 5, 14)
        pyxel.circ(ballx[i], bally[i],10 , 6)
        pyxel.rect(padx-20, 195, 40, 5, 14)
        pyxel.text(5, 5, f'points: {point}', 1)


pyxel.run(update, draw)
