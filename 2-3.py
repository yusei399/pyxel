import pyxel
import math


pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0,360, 2):
    b = math.radians(a)
    c = int(a*3/360)
    pyxel.line(100,100, 100+80*math.sin(b), 100+100*math.cos(b), c)
pyxel.show()
