#  elatch.py
#
#  Edge triggered latch. Try this at drawing depth 2-3-4-5.

import pygame as pg
from   gates     import Swt, Puls, Nand2, Inv
from   circuit   import Circuit
from   connector import Connector
from   dlatch    import DLatch
from   text      import textDraw

class ELatch (Circuit) :
    def setupGraphics(s) :
        dl1 = DLatch(s,"DL1", s.scale1(( 50,0)))
        dl2 = DLatch(s,"DL2")
        dl2.align(dl2.D, dl1.Q, 20, 0)

        ei1 = Inv  (s,"I3")
        ei1.align (ei1.A, dl1.C, 0, 60)

        td = (dl1.D.x(-30), dl1.D.y()) # terminal D 
        tc = (dl1.C.x(-30), dl1.C.y()) # terminal C 
        tq = (dl2.Q.x( 30), dl2.Q.y()) # terminal Q 
        s.D = Connector(s,"D", td)
        s.C = Connector(s,"C", tc)
        s.Q = Connector(s,"Q", tq)
        s.D.addWire(dl1.D)
        s.C.addWire(dl1.C)
        s.C.addWire((s.C.x(),ei1.A.y()), ei1.A)
        ei1.B.addWire((dl2.C.x(-10),dl2.C.y()), dl2.C)
        dl1.Q.addWire(dl2.D)
        dl2.Q.addWire(s.Q)
        s.output = s.Q
        s.gates = (ei1,dl1,dl2)
        if s.encapsulated() :
            s.D.pos,s.C.pos,s.Q.pos = s.scaleM((0,8),(0,32),(20,20))

class TestELatch(Circuit) :
    def setupGraphics(s) :
        s.banner = "Edge Triggered Latch. Click S1 and P1"
        el1 = ELatch(s, "EL1", s.scale1((20,20)))
        p1 = Puls(s,"P1") ; p1.align(p1.B,el1.C,-20,0)
        s1 = Swt (s,"S1") ; s1.align(s1.B,el1.D,-20,0)
        p1.B.addWire(el1.C)
        s1.B.addWire(el1.D)
        el1.output.addWire((el1.output.x(20),el1.output.y())) 
        s.gates = (p1,s1,el1)

if __name__ == "__main__" : 
    import gameloop
    from   settings import CmdScale
    circuit = TestELatch (None, "TestLatch",(100,100),scale=CmdScale)
    gameloop.gameloop(circuit)
