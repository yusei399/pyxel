import pyxel
import random
import math
pyxel.init(200,200)


class Ball:
    speed = 10
    def __init__(self):
        self.x = random.randint(0, 199)
        self.y = 0
        angle = math.radians(random.randint(30, 150))
        self.vx = math.cos(angle)
        self.vy = math.sin(angle)
        pyxel.run(self.update,self.draw)

    def update(self):
        self.x += self.vx * Ball.speed
        self.y += self.vy* Ball.speed

        padx = pyxel.mouse_x
        #for i in range(2):
        if self.x >= 200:
            self.vx *= -1
        if self.x <= 0:
            self.vx *= -1
        if self.y>= 200:
            self.y = 0
            self.x = random.randint(0, 200)
            radian = random.uniform(math.radians(20), math.pi - math.radians(20))
            self.vx = math.cos(radian)
            self.vy = math.sin(radian)



    def draw(self):
        pyxel.cls(7)
        pyxel.circ(self.x,self.y,10,6)
        pyxel.rect(self.x-20, 195, 40, 5, 14)

class Pad :

    def __init__(self):

        self.x = 100
    def update(self):
        self.x = pyxel.mouse_x
    def draw (self):
        pyxel.rect(self.x-20, 195, 40, 5, 14)


Ball(),Pad()
