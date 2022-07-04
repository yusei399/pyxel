import pyxel
import random
import math

pyxel.init(200,200)

class Ball:
    def __init__(self):
        self.x = random.randint(0,200)
        self.y = 0
        self.vx = 0.866
        self.vy = 0.5
    def move (self, callbackHit):
        if self.x >= 200:
            self.vx *= -1
        if self.x <= 0:
            self.vx *= -1
        if self.y >= 200:
            callbackHit()
            self.y = 0
            self.x = random.randint(0, 200)
            radian = random.uniform(math.radians(20), math.pi - math.radians(20))
            self.vx = math.cos(radian)
            self.vy = math.sin(radian)

class Pad :
    x = 100
    def __init__(self, balls):
        self.balls = balls

    def hit(self, i):
        if abs(self.balls[i].y - 195) <= 10:
            if self.balls[i].x <= self.x + 20 and self.balls[i].x >= self.x - 20:
                return 1
        else:
            return 0


class App:
    def __init__(self):
        self.balls = [Ball()]
        self.speed = 10
        self.point = 0
        self.life = 10
        self.pad = Pad(self.balls)
        pyxel.run(self.update, self.draw)
    def update(self):
        self.pad.x = pyxel.mouse_x

        for i in range(len(self.balls)):
            self.balls[i].x += self.balls[i].vx * self.speed
            self.balls[i].y += self.balls[i].vy * self.speed


        #for i in range(len(balls)):
            self.balls[i].move(self.hit)
                #pyxel.play(0, 0)

            if self.pad.hit(i):
                self.point += 1
                if self.point % 10 == 0:
                    self.speed = 5
                    self.balls.append(Ball())
                self.balls[i].y = 0
                self.balls[i].x = random.randint(0, 200)
                radian = random.uniform(math.radians(20), math.pi - math.radians(20))
                self.balls[i].vx = math.cos(radian)
                self.balls[i].vy = math.sin(radian)
            # vx = math.cos(math.radians(90))
            # vy = math.sin(math.radians(90)
                #pyxel.play(0, 1)
    def hit(self):
        if self.life > 0:
            self.life -= 1
    def draw(self):
        pyxel.cls(7)
        pyxel.rect(self.pad.x - 20, 195, 40, 5, 14)
        if self.life > 0:
            for  i in range(len(self.balls)):
                pyxel.circ(self.balls[i].x, self.balls[i].y, 10, 6)
        pyxel.text(5, 5, f'points: {self.point}', 1)
        pyxel.text(5, 15, f'life: {self.life}', 1)
        if self.life<=0:
            pyxel.text(80,100,'gameover',1)

App()
