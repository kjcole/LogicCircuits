# or1.py
#
#  Build an OR gate from simpler components

import pygame as pg
from   gates     import Nand2, Inv, Swt
from   circuit   import Circuit

class TestOr (Circuit) :
    def setupGraphics(s) :
        s.banner = "Building an OR gate from basic components"
        n1 = Nand2(s,"N1", s.scale1((150, 30))) # Nand Gate
        i1 = Inv  (s,"I1") # Inverter for n1.A
        i2 = Inv  (s,"I2") # Inverter for n1.B
        s1 = Swt  (s,"S1") # Switch feeding input A
        s2 = Swt  (s,"S2") # Switch feeding input B

        s2.align(s2.B, n1.B, -30,  0)
        i1.align(i1.B, n1.A, -40,-20)  # inverter precedes Nand
        s1.align(s1.B, i1.A, -50,  0)  # line up the gates
        i2.align(i2.B, n1.B, -40, 20)  # inverter precedes Nand
        s2.align(s2.B, i2.A, -50,  0)  # line up the gates

        n1.A.labelQuad = 3            # Label all the connectors
        n1.B.labelQuad = 2
        n1.C.labelQuad = 1
        i1.A.labelQuad = 2            # Inverter
        i1.B.labelQuad = 1
        i2.A.labelQuad = 3            # Inverter
        i2.B.labelQuad = 4
        s1.B.labelQuad = 1            # Switches
        s2.B.labelQuad = 1

        s.gates = (s1,s2,i1,i2,n1)
        s1.B.addWire(i1.A)
        s2.B.addWire(i2.A)
        i1.B.addWire(n1.A)
        i2.B.addWire(n1.B)
        n1.C.addWire( (n1.C.x(30), n1.C.y()))  # tail to see

if __name__ == "__main__" : 
    import gameloop
    from   settings import CmdScale
    circuit = TestOr (None, "TestOr",(100,100),scale=CmdScale)
    gameloop.gameloop(circuit)
