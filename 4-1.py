import pyxel

r =10
num=10
pyxel.init(2*r*num,2*r*num);
pyxel.cls(7)

for a in range(num):
    for b in range(num):
        color=6 if (a+b) %2==1 else 14
        pyxel .circ(a*2*r+r,b*2*r+r,r,color)

pyxel.show()


