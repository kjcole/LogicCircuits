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
