# text.py

import pygame as pg

def textFont (pointSize) :
    return pg.font.Font(None,pointSize)

def textDraw(screen, pos, color, text, quad=0, font=None) :
    if not quad : return
    if not font : font = textFont(14)
    rend = font.render(text,1,color)
    tw,th = font.size(text)
    tw += 3                # room to breath
    w,h = (None,(0,-1),(-1,-1),(-1,0),(0,0))[quad]
    org = (tw*w + pos[0], th*h + pos[1])
    screen.blit(rend, org)

#-----------------------------------------------------------
from settings import BGCOLOR, RED, MyInput

def testTextDraw () :
    pg.init()
    width = height = 300
    screen  = pg.display.set_mode((width, height))
    
    screen.fill(BGCOLOR)
    pg.draw.line(screen, RED, (0,150), (300,150), 1)
    pg.draw.line(screen, RED, (150,0), (150,300), 1)

    for quad in range(0,5) :
        which = (None,"first","second","third","fourth")[quad]
        text = "This is in the %s quadrant" % which
        textDraw(screen, (150,150), RED, text, quad)
    pg.display.flip()
    MyInput ("Hit return to exit:")

if __name__ == "__main__" : testTextDraw()
