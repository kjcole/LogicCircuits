import pygame as pg
from   gates     import Puls, Inv, Nand2, Swt
from   circuit   import Circuit
from   connector import Connector

class Xor(Circuit) :
    def setupGraphics(s) :
        n1 = Nand2(s,"N1",s.scale1(( 20, 30)))   # West  Nand
        n2 = Nand2(s,"N2",s.scale1(( 70,  0)))   # North Nand
        n3 = Nand2(s,"N3",s.scale1(( 70, 60)))   # South Nand
        n4 = Nand2(s,"N4",s.scale1((120, 30)))   # East  Nand
        # external connectors. Same depth as xor circuit
        s.A = Connector(s,"A",((n1.A.x(-20),n2.A.y() )))
        s.B = Connector(s,"B",((n1.A.x(-20),n3.B.y() )))
        s.C = Connector(s,"C",((n4.C.x(   ),n4.C.y() )))
        s.output = s.C                        # who is output
        s.A.addWire(n2.A);  s.A.addWire(n1.A)  # internal wiring
        s.B.addWire(n1.B);  s.B.addWire(n3.B)
        n1.C.addWire(n2.B); n1.C.addWire(n3.A)
        n2.C.addWire(n4.A); n3.C.addWire(n4.B)
        n4.C.addWire(s.C)
        if s.encapsulated() :  # if encapsulated re-work externals
            s.A.pos, s.B.pos, s.C.pos = s.scaleM((0,5),(0,35),(20,20))
        s.n1=n1; s.n2=n2; s.n3=n3; s.n4=n4 # save gates w object
        s.gates = (n1,n2,n3,n4)

class TestXor(Circuit) :
    def setupGraphics(s) :
        i1 = Inv (s,"I1",s.scale1((200,50)))
        xor= Xor (s,"X1",(0,0))
        s1 = Swt (s,"S1",(0,0))
        s2 = Swt (s,"S2",(0,0))

        xor.align(xor.C, i1.A, -20, 0) # make xnor to test align
        s1.align (s1.B, xor.A, -30, 0)
        s2.align( s2.B, xor.B, -30, 0)

        s1.B.addWire(xor.A)
        s2.B.addWire(xor.B)
        xor.C.addWire(i1.A)
        s.gates = (s1,s2,xor,i1)
        s1.B.labelQuad = 1
        s2.B.labelQuad = 1
        s.banner = "XOR (4 Nands) plus Inverter for XNOR"
        xor.n2.A.labelQuad = 2
        xor.n2.B.labelQuad = 2
        xor.n2.C.labelQuad = 1
        xor.A.labelQuad = 2
        xor.B.labelQuad = 2
        xor.C.labelQuad = 1
        i1.A.labelQuad = 2
        i1.B.labelQuad = 1

        # wire works fine as LED
        s.led   = Connector(s,"LED",(i1.B.x(20),i1.B.y() ))
        i1.B.addWire(s.led)  # works as LED

if __name__ == "__main__" : 
    import gameloop
    from   settings import CmdScale
    circuit = TestXor (None, "TestXor",(100,100),scale=CmdScale)
    gameloop.gameloop(circuit)
