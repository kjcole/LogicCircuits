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
