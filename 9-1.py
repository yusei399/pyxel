import pyxel
import random
import math

pyxel.init(200,200)

ballx = 100
bally = 0
vx = 0.866    # cos 60 degree
vy = 0.5 # sin 60 degree
padx = 100
speed = 10
point = 0

def pad():
    global ballx, bally, padx
    if abs(bally - 195) <= 10:
        if ballx <= padx + 20 and ballx >= padx - 20:
            return 1
    return 0

def update():
    global ballx, bally, vx, vy, padx, speed, point,angle
    ballx += vx * speed
    bally += vy * speed

    padx = pyxel.mouse_x

    if ballx >= 200:
        vx *= -1
    if ballx <= 0:
        vx *= -1
    if bally >= 200:
        bally = 0
        ballx = random.randint(30, 150)
        radian = random.uniform(math.radians(20), math.pi - math.radians(20))
        vx = math.cos(radian)
        vy = math.sin(radian)

    if pad():
        point += 1
        bally = 0
        ballx = random.randint(30, 150)
        radian = random.uniform(math.radians(20), math.pi - math.radians(20))
        vx = math.cos(radian)
        vy = math.sin(radian)
        # vx = math.cos(math.radians(90))
        # vy = math.sin(math.radians(90))

def draw():
    global ballx, bally, padx, point
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(5, 5, f'points: {point}', 1)
    pyxel.sound(0).set(note='C3', tone='T', volume='1', effect='N', speed=30)

pyxel.run(update, draw)
