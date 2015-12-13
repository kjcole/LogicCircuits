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
