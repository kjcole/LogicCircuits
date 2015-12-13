# latch.py

import pygame as pg
from   gates     import Puls, Nand2 
from   circuit   import Circuit
from   connector import Connector

class Latch(Circuit) :
    def setupGraphics(s) :
        n1  = Nand2(s,"N1",s.scale1((10,  0)))        # Upper Nand
        n2  = Nand2(s,"N2",s.scale1((10, 50)))        # Lower Nand
        # external connectors. Same depth as latch circuit
        s.A = Connector(s,"A",((n1.A.x(-10),n1.A.y() )))
        s.B = Connector(s,"B",((n2.B.x(-10),n2.B.y() )))
        s.Q = Connector(s,"Q",((n1.C.x(  2),n1.C.y() )))
        s.output = s.Q

        if s.encapsulated() :
            s.A.pos,s.B.pos,s.Q.pos = s.scaleM((0,8),(0,32),(20,20))
        s.n1=n1; s.n2=n2
        s.gates = (n1,n2)

        s.A.addWire(n1.A); s.B.addWire(n2.B)
        c1 = (n1.C.x( 10), n1.C.y(   ) )   # zig-zag output to input 
        c2 = (n1.C.x( 10), n1.C.y( 10) ) 
        c3 = (n2.A.x(-10), n2.A.y(-10) )  
        c4 = (n2.A.x(-10), n2.A.y(   ) ) 
        n1.C.addWire(c1,c2,c3,c4,n2.A)
        n1.C.addWire(s.Q)
        
        c1 = (n2.C.x( 10), n2.C.y(   ) )    # zig-zag the other way
        c2 = (n2.C.x( 10), n2.C.y(-10) ) 
        c3 = (n1.B.x(-10), n1.B.y( 10) ) 
        c4 = (n1.B.x(-10), n1.B.y(   ) )  
        n2.C.addWire(c1,c2,c3,c4,n1.B)

class TestLatch(Circuit) :
    def setupGraphics(s) :
        s.banner = "Basic Latch Circuit"
        latch= Latch(s, "L1", s.scale1((50,30)))
        p1 = Puls (s,"P1")  # pulsars left and down
        p2 = Puls (s,"P2")
        p1.align(p1.B, latch.A, -25, 0)
        p2.align(p2.B, latch.B, -25, 0)
        s.gates = (p1,p2,latch)
        p1.B.addWire(latch.A)
        p2.B.addWire(latch.B)
        s.led1 = Connector(s,"LED1",(latch.Q.x(20),latch.Q.y() ))
        latch.Q.addWire(s.led1)

if __name__ == "__main__" : 
    import gameloop
    from   settings import CmdScale
    circuit = TestLatch (None, "TestLatch",(100,100),scale=CmdScale)
    gameloop.gameloop(circuit)
