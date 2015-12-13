# basics.py
#  Show off the basic gates in a simple circuit

from   gates     import MultPuls, Nand2, Inv, Swt
from   circuit   import Circuit

class TestBasic1 (Circuit) :
    def setupGraphics(self) :
        self.banner = "Basic components. Switch, Multipulsar, Nand, Inverter"

        n1 = Nand2(self,"N1", self.scale1((50, 30))) # Nand Gate
        i1 = Inv  (self,"I1")         # Inverter 
        s1 = Swt  (self,"S1")         # Switch feeding input A
        m1 = MultPuls (self,"MP1")    # Pulsar feeding input B

        s1.align(s1.B, n1.A, -50, 0)  # line up the gates
        m1.align(m1.B, n1.B, -30, 0)
        i1.align(i1.B, n1.C,  80, 0)  # inverter follows Nand

        n1.A.labelQuad = 2            # Label all connectors
        n1.B.labelQuad = 2
        n1.C.labelQuad = 1
        i1.A.labelQuad = 2
        i1.B.labelQuad = 1

        self.gates = (m1,s1,n1,i1)
        s1.B.addWire(n1.A)
        m1.B.addWire(n1.B)
        n1.C.addWire(i1.A)
        i1.B.addWire( (i1.B.x(30), i1.B.y()))  # tail to see

if __name__ == "__main__" :
    import gameloop
    from   settings import CmdScale
    circuit = TestBasic1 (None, "TestBasic1",(100,100),scale=CmdScale)
    gameloop.gameloop(circuit)
