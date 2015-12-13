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
