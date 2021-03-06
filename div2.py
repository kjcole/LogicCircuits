#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Logic Circuits - div2.py
#  Divide by 2 circuit. run with 2-6 layers
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
__appname__    = "Logic Circuits"

import pygame as pg
from   gates     import Swt, Puls, Nand2, Inv
from   circuit   import Circuit
from   connector import Connector
from   elatch    import ELatch


class DivBy2 (Circuit):
    def setupGraphics(s):
        el  = ELatch(s, "EL", s.scale1((50, 20)))
        inv = Inv(s, "Inv", (el.D.x(-40), el.D.y(-12)))
        # wire up the feedback loop
        cn1 = (el.Q.x(5),    el.Q.y())
        cn2 = (el.Q.x(5),    inv.y(-20))
        cn3 = (inv.A.x(-15), inv.y(-20))
        cn4 = (inv.A.x(-15), inv.A.y())
        el.Q.addWire(cn1, cn2, cn3, cn4, inv.A)
        inv.B.addWire(el.D)

        tc = (el.C.x(-60), el.C.y())  # terminal C
        tq = (el.Q.x( 60), el.Q.y())  # terminal Q
        s.C = Connector(s, "C", tc)
        s.Q = Connector(s, "Q", tq)
        el.output.addWire(s.Q)
        s.output = s.Q
        s.C.addWire(el.C)
        s.gates = (el, inv)
        if s.encapsulated():
            s.C.pos, s.Q.pos = s.scaleM((0, 32), (20, 20))


class TestDivBy2(Circuit):
    def setupGraphics(s):
        s.banner = "Divide by 2. Click C1 repeatably"
        div2 = DivBy2(s, "Dv2", s.scale1((20, 20)))
        c1 = Puls(s, "C1", (div2.C.x(-50), div2.C.y()))
        c1.align(c1.B, div2.C, -30, 0)
        c1.B.addWire(div2.C)
        div2.output.addWire((div2.output.x(20), div2.output.y()))

        s.gates = (c1, div2)

if __name__ == "__main__":
    import gameloop
    from   settings import CmdScale
    circuit = TestDivBy2(None, "TestDivBy2", (100, 100), scale=CmdScale)
    gameloop.gameloop(circuit)
