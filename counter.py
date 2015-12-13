
# Divide by 2 circuit. run with 2-6 layers

import pygame as pg
from   gates     import Swt, Puls, MultPuls, Nand2, Inv
from   circuit   import Circuit
from   connector import Connector
from   div2      import DivBy2

class Counter(Circuit) :
    def setupGraphics(s) :
        dv1 = DivBy2(s,"Dv1",s.scale1((50,30)))
        dv2 = DivBy2(s,"Dv2")
        dv4 = DivBy2(s,"Dv4")
        dv8 = DivBy2(s,"Dv8")

        dv2.align(dv2.C, dv1.Q, 20, 70)
        dv4.align(dv4.C, dv2.Q, 20, 70)
        dv8.align(dv8.C, dv4.Q, 20, 70)

        tc = (dv1.C.x(-60), dv1.C.y()) # counter input
        tq = (dv8.Q.x( 60), dv8.Q.y()) # counter output
        s.C = Connector(s,"C",tc)
        s.Q = Connector(s,"Q",tq)
        s.output = s.Q
        
        s.C.addWire(dv1.C)
        dv1.Q.addWire(dv2.C)
        dv2.Q.addWire(dv4.C)
        dv4.Q.addWire(dv8.C)
        ybottom = dv8.Q.y(50)
        xturn   = dv8.Q.x(30)
        for dv in (dv8,dv4,dv2,dv1) :
            dv.Q.addWire((xturn,dv.Q.y()),(xturn,ybottom))
            xturn += 10

#        dv1.Q.addWire((dv1.Q.x(170),dv1.Q.y()),
#                      (dv1.Q.x(170),dv8.Q.y(50))  )
#        dv2.Q.addWire((dv2.Q.x(120),dv2.Q.y()),
#                      (dv2.Q.x(120),dv8.Q.y(50))  )
#        dv4.Q.addWire((dv4.Q.x(70),dv4.Q.y()),
#                      (dv4.Q.x(70),dv8.Q.y(50))  )
#        dv8.Q.addWire((dv8.Q.x(20),dv8.Q.y()),
#                      (dv8.Q.x(20),dv8.Q.y(50))  )

        s.gates = (dv1,dv2,dv4,dv8)
        if s.encapsulated() :
            s.C.pos, s.Q.pos = s.scaleM((0,32),(20,20))

class TestCounter(Circuit) :
    def setupGraphics(s) :
        s.banner = "4 Bit Binary Counter. Click C1 to Start"
        cnt1 = Counter (s, "Cnt1", s.scale1((20,20)))
        c1 = MultPuls(s,"C1", (cnt1.C.x(-50),cnt1.C.y()))
        c1.align(c1.B, cnt1.C, -30,0)
        c1.B.addWire(cnt1.C)
        s.gates = (c1,cnt1)

if __name__ == "__main__" : 
    import gameloop
    from   settings import CmdScale
    circuit = TestCounter (None, "TestCounter",(100,100),scale=CmdScale)
    gameloop.gameloop(circuit)
