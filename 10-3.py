import pyxel
import random
import math

pyxel.init(200,200)

ballx = [100]
bally = [0]

vx = [0.866]   # cos 60 degree
vy = [0.5 ]# sin 60 degree
color = 6
padx = 100
speed = 10
point = 0
life = 10


pyxel.sound(0).set(note='C3', tone='P', volume='3', effect='S', speed=30)
pyxel.sound(1).set(note='C3', tone='T', volume='3', effect='N', speed=30)
def pad(i):
    global ballx, bally, padx
    if abs(bally[i] - 195) <= 10:
        if ballx[i] <= padx + 20 and ballx[i] >= padx - 20:
            return 1
    return 0

def update():
    global ballx, bally, vx, vy, padx, speed, point, life, point,color



    for i in range(len(ballx)):
        ballx[i] += vx[i] * speed
        bally[i] += vy[i] * speed

    padx = pyxel.mouse_x
    for i in range(len(ballx)):
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
            if life > 0:
                life -= 1
        if point % 5 == 0:
            color = 14
        else:
            color = 6







        if pad(i):
            if color == 6:
                point += 1
            else:
                point += 2
            if point%10 == 0:
                speed = 5
                ballx.append(100)
                bally.append(0)
                vx.append(0.866)
                vy.append(0.5)
            bally[i] = 0
            ballx[i] = random.randint(0, 200)
            radian = random.uniform(math.radians(20), math.pi - math.radians(20))
            vx[i] = math.cos(radian)
            vy[i] = math.sin(radian)
        # vx = math.cos(math.radians(90))
        # vy = math.sin(math.radians(90)
            pyxel.play(0, 1)


def draw():
    global ballx, bally, padx, point,life,gameover,color
    pyxel.cls(7)

    if life > 0:
        for  i in range(len(ballx)):
            pyxel.circ(ballx[i],bally[i],10,color)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(5, 5, f'points: {point}', 1)
    pyxel.text(5, 15, f'life: {life}', 1)
    if life<=0:
        pyxel.text(80,100,'gameover',1)
pyxel.run(update, draw)
