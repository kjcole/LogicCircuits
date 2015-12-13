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

# circuit.py

import pygame as pg
from   component import Component
from   text      import textDraw, textFont
from   settings  import GREEN, BLUE

class Circuit(Component) :
    def computeOutput(self) :
        for gate in self.gates :
            gate.computeOutput()
            gate.sendOutput()

    def checkClicked(self, pos) :
        for gate in self.gates :
            gate.checkClicked(pos)
        
    def draw(self, screen) :
        if self.hidden() : return
        font = pg.font.Font(None,12)

        if self.encapsulated() :
            bx1,bx2,bx3,bx4 = self.scaleM((0,0),(20,0),(20,40),(0,40))
            pg.draw.polygon(screen,BLUE,(bx1,bx2,bx3,bx4),1)
            textDraw(screen, self.scale1((3,3)), BLUE, self.name, quad=4)
        elif not self.hidden() :
            if self.banner :
                textDraw(screen, self.scale1((0,0)), GREEN, self.banner,
                          quad=1, font=textFont(24))
            gates = self.gates
            for g in gates :
                g.output.drawWires(screen)
                g.draw(screen)
