#  dlatch.py
#
#  Try this at drawing depth 2-3-4.

import pygame as pg
from   gates     import Swt, Puls, Nand2, Inv
from   circuit   import Circuit
from   connector import Connector
from   latch     import Latch

class DLatch (Circuit) :
    def setupGraphics(s) :
        n1 = Nand2(s,"N1",s.scale1((50, 0)))   # Upper Nand
        n2 = Nand2(s,"N2",s.scale1((50,40)))   # Lower Nand
        i1 = Inv  (s,"I1",(n2.B.x(-40),n2.B.y(0)))
        i2 = Inv  (s,"I2",(s.scale1((5,25))))
        i1.align(i1.B, n2.B, -10, 0)
        l1 = Latch(s,"L1",s.scale1((90,12)))

        td = (n1.A.x(-60), n1.A.y()) # terminal D 
        tc = (n1.A.x(-60), i2.A.y()) # terminal C
        s.D = Connector(s,"D",td)
        s.C = Connector(s,"C",tc)
        s.Q = Connector(s,"Q",l1.Q.pos)
        s.output = s.Q
        l1.Q.addWire(s.Q)
        s.gates = (i1,i2,n1,n2,l1)

        if s.encapsulated() :
            s.D.pos,s.C.pos,s.Q.pos = s.scaleM((0,8),(0,32),(20,20))

        n1.C.addWire (l1.A)    # Wire Nands to the latch
        n2.C.addWire (l1.B)
        s.C.addWire  (i2.A)
        i2.B.addWire (n1.B)
        i2.B.addWire (n2.A)
        s.D.addWire  (n1.A)
        s.D.addWire  ( (s.D.x(),i1.A.y()), i1.A) # down then take a right
        i1.B.addWire (n2.B)

class TestDLatch(Circuit) :
    def setupGraphics(s) :
        s.banner = "Testing the Data Latch"
        dl1 = DLatch(s, "DL1", s.scale1((50,30)))
        d1 = Swt (s,"D1")  # data switch
        c1 = Puls(s,"C1")  # pulse generator
        d1.align(d1.B, dl1.D, -30, 0) # align each with dlatch D & C
        c1.align(c1.B, dl1.C, -30, 0)
        c1.B.addWire(dl1.C)       # wire them to the dlatch
        d1.B.addWire(dl1.D)
        # add a piece of wire to monitor output
        dl1.output.addWire((dl1.output.x(20),dl1.output.y())) 
        s.gates = (c1,d1,dl1)

if __name__ == "__main__" : 
    import gameloop
    from   settings import CmdScale
    circuit = TestDLatch (None, "TestDLatch",(100,100),scale=CmdScale)
    gameloop.gameloop(circuit)
