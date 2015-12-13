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

import pygame as pg
from   settings import BGCOLOR, TICKS_PER_SECOND
from   settings import SCREEN_WIDTH, SCREEN_HEIGHT, MyInput, Debug

def gameloop(circuit) :
    pg.init()
    running = True
    screen  = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock  = pg.time.Clock()

    while running:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN :
            #if Debug : print "Mouse clicked at (%d, %d)" % event.pos
            circuit.checkClicked(event.pos)

        circuit.computeOutput()

        screen.fill(BGCOLOR)
        circuit.draw(screen)
        clock.tick(TICKS_PER_SECOND)   # times per second
        pg.display.flip()
        #if Debug : MyInput ("Hit return to continue:")
    pg.quit()
