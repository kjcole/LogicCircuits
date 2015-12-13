#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Logic Circuits
#
#  Copyleft 2015 Chris Meyers <chris.meyers47@gmail.com> 2015.12.13
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of
#  the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with this program; if not, write to the Free
#  Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301, USA.
#
#

from __future__ import print_function
from six.moves  import input           # use raw_input when I say input

__author__     = "Chris Meyers, Jeff Elkner and Kevin Cole"
__copyright__  = "Copyleft 2015, Chris Meyers (2015.12.13)"
__credits__    = ["Chris Meyers", "Jeff Elkner",
                  "Kevin Cole"]  # Authors and bug reporters
__license__    = "GPL"
__version__    = "2.0"
__maintainer__ = "Chris Meyers, Jeff Elkner, Kevin Cole"
__email__      = "kevin.cole@novawebcoop.org"
__status__     = "Development"  # "Prototype", "Development" or "Production"
__appname__    = "Logic Circuits"

# or2.py
#
#  Generic Or class with test 
#
from   gates     import Nand2, Inv, Swt
from   circuit   import Circuit
from   connector import Connector

class Or (Circuit) :
    def setupGraphics(self) :
        n1 = Nand2(self,"N1", self.scale1((80, 30))) # Nand Gate
        i1 = Inv  (self,"I1") # Inverter for n1.A
        i2 = Inv  (self,"I2") # Inverter for n1.B
        # external connectorself. Same depth as xor circuit
        i1.align(i1.B, n1.A, -40, -20)  # inverter precedes Nand
        i2.align(i2.B, n1.B, -40,  20)  # inverter precedes Nand
        self.A = Connector(self,"A",((i1.A.x(-20),i1.A.y() )))
        self.B = Connector(self,"B",((i2.A.x(-20),i2.B.y() )))
        self.C = Connector(self,"C",((n1.C.x( 20),n1.C.y() )))
        self.output = self.C       # who is output

        self.gates = (i1,i2,n1)
        self.i1,self.i2,self.n1 = (i1,i2,n1)

        i1.B.addWire(n1.A)
        i2.B.addWire(n1.B)
        self.A.addWire(i1.A)
        self.B.addWire(i2.A)
        n1.C.addWire(self.C)

        if self.encapsulated() :  # if encapsulated re-work externals
            self.A.pos, self.B.pos, self.C.pos = self.scaleM((0,5),(0,35),(20,20))


class TestOr (Circuit) :
    def setupGraphics(self) :
        self.banner = "Encapsulated OR circuit"
        or2 = Or(self,"O2"  , self.scale1((50,30)))
        s1 = Swt  (self,"S1")   # Switch feeding input A
        s2 = Swt  (self,"S2")   # Switch feeding input B

        s1.align(s1.B, or2.A, -30, 0)  # line up the gates
        s2.align(s2.B, or2.B, -30, 0)
        s1.B.addWire(or2.A)
        s2.B.addWire(or2.B)
        s1.B.labelQuad = 1
        s2.B.labelQuad = 1
        self.gates = (s1,s2,or2)

        or2.n1.A.labelQuad = 3            # Label all the connectors
        or2.n1.B.labelQuad = 2
        or2.n1.C.labelQuad = 1
        or2.i1.A.labelQuad = 2            # Inverter
        or2.i1.B.labelQuad = 1
        or2.i2.A.labelQuad = 3            # Inverter
        or2.i2.B.labelQuad = 4
        or2.A.labelQuad = 1
        or2.B.labelQuad = 1
        or2.C.labelQuad = 1
        or2.C.addWire( (or2.C.x(30), or2.C.y()))  # tail to see

if __name__ == "__main__" : 
    import gameloop
    from   settings import CmdScale
    circuit = TestOr (None, "TestOr",(100,100),scale=CmdScale)
    gameloop.gameloop(circuit)
