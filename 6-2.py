import pyxel

pyxel.init(200,200)

a = 0

while True:
    pyxel.cls(7)
    pyxel.circ(100+a, a, 10, 0)
    pyxel.circ(a,100-a,10,0)
    pyxel.circ(200-a,100+a,10,0)
    pyxel.circ(100-a,200-a,10,0)
    pyxel.flip()
    a += 1
    if 100 < a:
        a = 0


