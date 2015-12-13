#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Animated Circuits
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
__appname__    = "Animated Circuits"

# gates.py

import pygame as pg
from   component import Component
from   connector import Connector
from   text      import textDraw
from   settings  import PULS_INTERVAL, MULT_PULS_HALFCYCLE, BGCOLOR, BLUE
    
class Nand2(Component) :
    def setupGraphics(s) :
        s.A = Connector(s,"A",s.scale1((0, 6)),1)
        s.B = Connector(s,"B",s.scale1((0,24)),1)
        s.output = s.C = Connector(s,"C",s.scale1((30,15)),0)

    def draw(self, screen, color=BLUE) :
        args = self.scaleM((15,15),15,   # big circle
           (0,0),(15,0),(15,30),(0,30),  # erase this rect
           ( 15,0),(0,0),(0,30),(15,30), # draw box behind
           (30,  15), 2)                 # and little NOT circle
        c1p, c1r, e1, e2, e3, e4, l1, l2, l3, l4, c2p, c2r = args
        pg.draw.circle(screen,color,c1p,c1r,1)
        pg.draw.polygon(screen,BGCOLOR,(e1,e2,e3,e4),0)
        pg.draw.lines(screen,color,False,(l1,l2,l3,l4),1)
        pg.draw.circle(screen,color,c2p,c2r,1)
        for con in (self.A, self.B, self.C) :
            pg.draw.circle(screen,color,con.pos,2,1)
        textDraw(screen, self.scale1((5,5)), color, self.name, quad=4)

    def computeOutput(s) :
        if s.A.value and s.B.value : newValue = 0  # note inverted
        else                       : newValue = 1
        s.C.value = newValue

#-----------------------------------------------------------

class Inv(Component) :
    def setupGraphics(s) :
        s.input  = s.A = Connector(s,"A",s.scale1((  0,12)),1)
        s.output = s.B = Connector(s,"B",s.scale1(( 26,12)),0)

    def draw(self, screen, color=BLUE) :
        args   = self.scaleM((  0,  0),(24,12),(  0,24), # triangle
                         ( 26, 12), 2)                   # NOT circle
        tp1,tp2,tp3, cp1,cr1 = args
        pg.draw.polygon(screen,color,(tp1,tp2,tp3),1)
        pg.draw.circle (screen,color,cp1,cr1,1)
        pg.draw.circle(screen,color,self.A.pos,2,1)
        pg.draw.circle(screen,color,self.B.pos,2,1)
        textDraw(screen, self.scale1((5,5)), color, self.name, quad=4)

    def computeOutput(self) :
        newValue = 1 - self.A.value   # swap 0 and 1
        self.B.value = newValue       # probably more to come

#-----------------------------------------------------------
    
class Swt(Component) :          # toggle switch w click
    def setupGraphics(s) :
        s.output = s.B = Connector(s,"B",s.scale1(( 6, 3)),0)
        s.B.value = 1

    def draw(self, screen, color=BLUE) :
        bp1, br1 = self.scaleM( (3,3), 3) # Body to click
        pg.draw.circle(screen,color,bp1,br1,1)
        textDraw(screen, self.pos, color, self.name, quad=2)
    
    def computeOutput(self) :
        pass                          # computed when clicked

    def takeClick(self) :
        newValue = 1 - self.B.value   # swap 0 and 1
        self.B.value = newValue       # probably more to come
        #print "%s was clicked - now %s" % (self.name,self.B.value)

class Puls(Swt) :
    def setupGraphics(s) :
        Swt.setupGraphics(s)
        s.timer  = 0

    def takeClick(self) :
        self.timer = PULS_INTERVAL
        #print "Puls %s clicked - now %s" % (self.name,self.B.value)

    def computeOutput(self) :
        if self.timer :
            self.B.value = 0       # keep down til time done
            self.timer  -= 1
        else : self.B.value = 1

class MultPuls(Swt) :
    def setupGraphics(self) :
        Swt.setupGraphics(self)
        self.halfcyc = MULT_PULS_HALFCYCLE
        self.on      = False

    def takeClick(self) :
        self.on = not self.on        # turn on or off
        self.timer = 0

    def computeOutput(self) :
        if self.on : 
            self.timer -= 1
            if self.timer <= 0 :
                self.B.value = 1 - self.B.value  # flip value 0/1
                self.timer = self.halfcyc
        else : self.B.value = 1

