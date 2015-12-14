#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Logic Circuits - basics.py
#  Show off the basic gates in a simple circuit
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

__author__     = "Chris Meyers, Jeff Elkner and Kevin Cole"
__copyright__  = "Copyleft 2015, Chris Meyers (2015.12.13)"
__credits__    = ["Chris Meyers", "Jeff Elkner",
                  "Kevin Cole"]  # Authors and bug reporters
__license__    = "GPL"
__version__    = "2.0"
__maintainer__ = "Chris Meyers, Jeff Elkner, Kevin Cole"
__email__      = "kevin.cole@novawebcoop.org"
__status__     = "Development"  # "Prototype", "Development" or "Production"
__appname__    = "Logic Circuits - Basic"

from gates   import MultPuls, Nand2, Inv, Swt
from circuit import Circuit


class TestBasic1(Circuit):
    def setupGraphics(self):
        self.banner = "Basic components. Switch, Multipulsar, Nand, Inverter"

        n1 = Nand2(self, "N1", self.scale1((50, 30))) # Nand Gate
        i1 = Inv(self, "I1")           # Inverter
        s1 = Swt(self, "S1")           # Switch feeding input A
        m1 = MultPuls(self, "MP1")     # Pulsar feeding input B

        s1.align(s1.B, n1.A, -50, 0)   # line up the gates
        m1.align(m1.B, n1.B, -30, 0)
        i1.align(i1.B, n1.C,  80, 0)   # inverter follows Nand

        n1.A.labelQuad = 2             # Label all connectors
        n1.B.labelQuad = 2
        n1.C.labelQuad = 1
        i1.A.labelQuad = 2
        i1.B.labelQuad = 1

        self.gates = (m1, s1, n1, i1)
        s1.B.addWire(n1.A)
        m1.B.addWire(n1.B)
        n1.C.addWire(i1.A)
        i1.B.addWire( (i1.B.x(30), i1.B.y()))  # tail to see

if __name__ == "__main__":
    import gameloop
    from   settings import CmdScale
    circuit = TestBasic1(None, "TestBasic1", (100, 100), scale=CmdScale)
    gameloop.gameloop(circuit)
