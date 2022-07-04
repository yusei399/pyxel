import pyxel
from math import sin, sqrt



pyxel.init(200,200)
a=0
while 1:
 pyxel.cls(1)
 for x in range(0,200,4):
  for y in range(0,200,4):
   d=sqrt((x-64)**2+(y-64)**2)
   b=sin(d*0.2+a)*4
   c=(15-d*0.2)%16
   pyxel.circ(x+b,y+sin(b/4)*4,1,c)
 a+=0.2
 pyxel.flip()
