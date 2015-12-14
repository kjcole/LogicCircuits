#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Logic Circuits - component.py
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

import settings as set


class Component:
    def __init__(self, parent, name, pos=(0, 0), scale=1):
        self.parent = parent
        self.kids   = ()
        self.name   = name
        self.pos    = pos
        self.scale  = scale   # for magnification
        self.layer  = 1
        self.value  = 1
        self.banner = ""
        if parent:
            self.scale *= parent.scale
            self.layer  = parent.layer + 1
            parent.kids += (self,)
        self.setupGraphics()

    def x(s, val=0):
        return s.pos[0] + val * s.scale
    
    def y(s, val=0):
        return s.pos[1] + val * s.scale

    def align(s, myCon, pivotCon, xoff, yoff):
        # Align so that seperation of 2 connectors is (xoff,yoff)
        pivX, pivY = pivotCon.pos
        oldX, oldY = myCon.pos
        xoff *= s.scale
        yoff *= s.scale
        newX = pivX + xoff
        newY = pivY + yoff
        xmov = newX - oldX
        ymov = newY - oldY
        s.scootOver(xmov, ymov)

    def encapsulated(s):
        return s.layer == set.CmdEncapsuleLayer

    def hidden(s):
        return s.layer > set.CmdEncapsuleLayer

    def scaleM(self, *args):      # scale multiple args
        return map(self.scale1, args)

    def scale1(s, arg):       # transform single point or scalar
        if   type(arg) == type(5):
            return arg * s.scale
        elif type(arg) == type((4,)) or type(arg)==type([4]):
            return posAdd(s.pos, posMult(arg, s.scale))

    def sendOutput(self):
        self.output.sendOutput()   # between connectors

    def checkClicked(self, clicked):
        if abs(clicked[0] - self.pos[0]) <= 15:
            if abs(clicked[1] - self.pos[1]) <= 15:
                self.takeClick()

    def takeClick(self):          # default action
        if set.Debug:
            print("{0} was clicked".format(self.name))

    def scootOver(self, xmov, ymov, nest=""):
        # not only yourself but everything inside too
        self.pos = posAdd(self.pos, (xmov, ymov))
        for kid in self.kids:
            # kid is either an inner component or a connector
            kid.scootOver(xmov, ymov, nest + "  ")

    def __repr__(s):
        par = s.parent
        if par:
            par = par.name
        return "<Comp: {0}.{1} {2} {3}>".format(par, s.name, s.pos, s.layer)


def posMult(pos, factor):                # position math
    return (pos[0] * factor,
            pos[1] * factor)


def posAdd(pos1, pos2):
    return (pos1[0] + pos2[0],
            pos1[1] + pos2[1])
