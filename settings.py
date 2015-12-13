#  settings.py

CmdScale          = 2   # generally just right
CmdEncapsuleLayer = 2   # shows detail on of outermost circuit
Debug   = 0             # Debug level
MyInput = input         # assume Python 3

from sys import argv, version
if len(argv)  >  1 : CmdEncapsuleLayer = int(argv[1])
if len(argv)  >  2 : CmdScale          = int(argv[2])
if version[0] < '3': MyInput = raw_input # python 2

BGCOLOR = ( 75, 75, 75)
RED     = (255,  0,  0)
GREEN   = (  0,255,  0)
BLUE    = (  0,  0,255)
YELLOW  = (255,255,  0)

COLD = BLUE    # wire colors
HOT  = RED

TICKS_PER_SECOND = 200

SCREEN_WIDTH  = 1200
SCREEN_HEIGHT =  600

PULS_INTERVAL       = 50   # ticks
MULT_PULS_HALFCYCLE = 50   # ticks each half

