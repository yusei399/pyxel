import pyxel

pyxel.init(200,200)

a = 0
flip = True
while True:
        pyxel.cls(7)
        pyxel.circ(a, a, 10, 0)
        a += (1 if flip else -1);
        if a == 0 or a==200:
            flip = not flip
        pyxel.flip()
