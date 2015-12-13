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

# connector.py

import pygame as pg
from   component import posAdd
from   settings  import HOT, COLD, CmdEncapsuleLayer
from   text      import textDraw

class Connector :
    def __init__ (s, parent, name, pos, value=0, feeds=()) :
        s.name, s.pos, s.value, s.feeds = name,pos,value,feeds
        s.parent = parent
        s.layer  = parent.layer
        s.prevValue = None
        s.labelQuad = 0
        parent.kids += (s,)

    def x(s, val=0) : return s.pos[0]+val*s.parent.scale

    def y(s, val=0) : return s.pos[1]+val*s.parent.scale

    def scootOver (self, xmov, ymov, nest=0) :
        self.pos = posAdd(self.pos, (xmov,ymov))

    def addWire(s, *others) :  # to a series of connectors
        this = s
        anons = []
        maxLayer = 0
        for other in others :
            if type(other) == type(()) : # only pos? make new one
                other = Connector(s.parent,"Anon",other,s.value)
                anons.append(other)  # save to assign layer later
                other.layer = None   # hold for now
            else :
                maxLayer = max(maxLayer,other.layer)

            this.feeds += (other,)
            this = other            # chain 'em
        for anon in anons : anon.layer = maxLayer
        return this   # lets us chain calls left to right

    def drawWires(s, screen, color=None) :
        if not color : color = [COLD,HOT][s.value]
        slq = s.labelQuad
        for d in s.feeds :
            dlq = d.labelQuad
            txt = "Draw wire %s.%s=%s @ %s - %s.%s=%s @ %s"  \
               % (s.parent.name, s.name, s.layer, s.pos,
                  d.parent.name, d.name, d.layer, d.pos)
            if max(s.layer,d.layer) <= CmdEncapsuleLayer :
                pg.draw.lines(screen, color, False, (s.pos,d.pos))
                if slq :
                    textDraw(screen, s.pos, color, s.name, quad=slq)
                if dlq :
                    textDraw(screen, d.pos, color, d.name, quad=dlq)
            d.drawWires(screen, color)  # fan out
            
    def sendOutput(self) :       # from connector to all targets
        if self.prevValue == self.value : return # short cut
        self.prevValue = self.value
        for dest in self.feeds :
            dest.value = self.value
            dest.sendOutput()
            
    def __repr__ (s) :
        par = s.parent.name
        return "<Conn: %s.%s %s %d>" % (par,s.name,s.pos,s.layer)
