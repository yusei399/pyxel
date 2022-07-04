import pyxel
import random
import math

pyxel.init(200,200)

ballx = [100,50, 30]
bally = [0,30,50]

vx = [0.866,0.866,0,866]   # cos 60 degree
vy = [0.5 ,0.5,0.5]# sin 60 degree
padx = 100
speed = 10
point = 0



def pad(i):
    global ballx, bally, padx
    if abs(bally[i] - 195) <= 10:
        if ballx[i] <= padx + 20 and ballx[i] >= padx - 20:
            return 1
    return 0

def update():
    global ballx, bally, vx, vy, padx, speed, point
    for i in range(3):
        ballx[i] += vx[i] * speed
        bally[i] += vy[i] * speed

    padx = pyxel.mouse_x
    for i in range(3):
        if ballx[i] >= 200:
            vx[i] *= -1
        if ballx[i] <= 0:
            vx[i]*= -1
        if bally[i] >= 200:
            bally[i] = 0
            ballx[i] = random.randint(0, 200)
            radian = random.uniform(math.radians(20), math.pi - math.radians(20))
            vx[i] = math.cos(radian)
            vy[i] = math.sin(radian)

        if pad(i):
            point += 1
            bally[i] =0
            ballx[i] = random.randint(0, 200)
            radian = random.uniform(math.radians(20), math.pi - math.radians(20))
            vx[i] = math.cos(radian)
            vy[i] = math.sin(radian)
        # vx = math.cos(math.radians(90))
        # vy = math.sin(math.radians(90))

def draw():
    global ballx, bally, padx, point
    pyxel.cls(7)
    for  i in range(3):
        pyxel.circ(ballx[i],bally[i],10,6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(5, 5, f'points: {point}', 1)

pyxel.run(update, draw)
