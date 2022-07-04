import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0, 200, 10):
    pyxel.line(0,a,200,0,0)
    pyxel.line(a,0,0,200,0)
    pyxel.circ(200, 200, 200, 7)
    pyxel.circb(200, 200, 200, 0)
pyxel.show()
