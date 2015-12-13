#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Logic Circuits - text.py
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

import pygame as pg


def textFont(pointSize):
    return pg.font.Font(None, pointSize)


def textDraw(screen, pos, color, text, quad=0, font=None):
    if not quad:
        return
    if not font:
        font = textFont(14)
    rend = font.render(text, 1, color)
    tw, th = font.size(text)
    tw += 3                # room to breath
    w, h = (None, (0, -1), (-1, -1), (-1, 0), (0, 0))[quad]
    org = (tw * w + pos[0],
           th * h + pos[1])
    screen.blit(rend, org)

# ----------------------------------------------------------
from settings import BGCOLOR, RED


def testTextDraw():
    pg.init()
    width = height = 300
    screen  = pg.display.set_mode((width, height))

    screen.fill(BGCOLOR)
    pg.draw.line(screen, RED, (  0, 150), (300, 150), 1)
    pg.draw.line(screen, RED, (150,   0), (150, 300), 1)

    for quad in range(0, 5):
        which = (None, "first", "second", "third", "fourth")[quad]
        text = "This is in the {0} quadrant".format(which)
        textDraw(screen, (150, 150), RED, text, quad)
    pg.display.flip()
    input("Hit return to exit:")

if __name__ == "__main__":
    testTextDraw()
