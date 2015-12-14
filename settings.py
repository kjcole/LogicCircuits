#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Logic Circuits - settings.py
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

from sys import argv, version

CmdScale          = 2   # generally just right
CmdEncapsuleLayer = 2   # shows detail on of outermost circuit
Debug   = 0             # Debug level

if len(argv)  >  1:
    CmdEncapsuleLayer = int(argv[1])
if len(argv)  >  2:
    CmdScale          = int(argv[2])

BGCOLOR = ( 75,  75,  75)
RED     = (255,   0,   0)
GREEN   = (  0, 255,   0)
BLUE    = (  0,   0, 255)
YELLOW  = (255, 255,   0)

COLD = BLUE    # wire colors
HOT  = RED

TICKS_PER_SECOND = 200

SCREEN_WIDTH  = 1200
SCREEN_HEIGHT =  600

PULS_INTERVAL       = 50   # ticks
MULT_PULS_HALFCYCLE = 50   # ticks each half
