import pyxel
import random
import math

pyxel.init(200,200)
class Ball:
    x = 100
    y = 0
    vx = 0.866
    vy = 0.5

balls = [Ball()]

class Pad :
    x = 100
    def hit(self,i):
        if abs(balls[i].y - 195) <= 10:
            if balls[i].x <= pad.x + 20 and balls[i].x >= pad.x - 20:
                return 1
        else:
            return 0

pad=Pad()




speed = 10
point = 0
life = 10

for ball in balls:
    ball.x =random.randint(0,200)


def update():
    global  speed, point, life

    pad.x = pyxel.mouse_x

    for i in range(len(balls)):
        balls[i].x += balls[i].vx * speed
        balls[i].y += balls[i].vy * speed


    for i in range(len(balls)):
        if balls[i].x >= 200:
            balls[i].vx *= -1
        if balls[i].x <= 0:
            balls[i].vx *= -1
        if balls[i].y >= 200:
            life -= 1
            balls[i].y = 0
            balls[i].x = random.randint(0, 200)
            radian = random.uniform(math.radians(20), math.pi - math.radians(20))
            balls[i].vx = math.cos(radian)
            balls[i].vy = math.sin(radian)
            #pyxel.play(0, 0)

        if pad.hit(i):
            point += 1
            if point%10 == 0:
                speed = 5
                balls.append(Ball())
            balls[i].y = 0
            balls[i].x = random.randint(0, 200)
            radian = random.uniform(math.radians(20), math.pi - math.radians(20))
            balls[i].vx = math.cos(radian)
            balls[i].vy = math.sin(radian)
        # vx = math.cos(math.radians(90))
        # vy = math.sin(math.radians(90)
            #pyxel.play(0, 1)


def draw():
    global point,life,gameover
    pyxel.cls(7)
    pyxel.rect(pad.x-20, 195, 40, 5, 14)
    if life > 0:
        for  i in range(len(balls)):
            pyxel.circ(balls[i].x,balls[i].y,10,6)
    pyxel.text(5, 5, f'points: {point}', 1)
    pyxel.text(5, 15, f'life: {life}', 1)
    if life<=0:
        pyxel.text(80,100,'gameover',1)
pyxel.run(update, draw)
