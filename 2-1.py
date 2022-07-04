import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0, 100, 10):
    pyxel.line(a,0, 100+a, 200, 0)
    pyxel.flip()
pyxel.show()
