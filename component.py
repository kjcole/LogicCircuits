# component.py
#
import settings as set

class Component :
    def __init__(self, parent, name, pos=(0,0), scale=1) :
        self.parent = parent
        self.kids   = ()
        self.name   = name
        self.pos    = pos
        self.scale  = scale   # for magnification
        self.layer  = 1
        self.value  = 1
        self.banner = ""
        if parent :
            self.scale *= parent.scale
            self.layer  = parent.layer+1
            parent.kids += (self,)
        self.setupGraphics()

    def x(s, val=0) : return s.pos[0]+val*s.scale
    def y(s, val=0) : return s.pos[1]+val*s.scale

    def align(s,myCon,pivotCon, xoff, yoff) :
        # Align so that seperation of 2 connectors is (xoff,yoff)
        pivX, pivY = pivotCon.pos
        oldX, oldY = myCon.pos
        xoff *= s.scale ; yoff *= s.scale
        newX = pivX+xoff; newY = pivY+yoff
        xmov = newX-oldX; ymov = newY-oldY
        s.scootOver(xmov, ymov)

    def encapsulated(s) :
        return s.layer == set.CmdEncapsuleLayer

    def hidden(s) :
        return s.layer > set.CmdEncapsuleLayer

    def scaleM(self, *args) :      # scale multiple args
        return map(self.scale1, args)

    def scale1(s, arg) :       # transform single point or scalar
        if   type(arg) == type(5) :
            return arg*s.scale
        elif type(arg) == type((4,)) or type(arg)==type([4]) :
            return posAdd(s.pos,posMult(arg,s.scale))

    def sendOutput(self) :
        self.output.sendOutput()   # between connectors

    def checkClicked(self, clicked) :
        if abs(clicked[0]-self.pos[0]) <= 15 :
            if abs(clicked[1]-self.pos[1]) <= 15 :
                self.takeClick()

    def takeClick(self) :          # default action
        if set.Debug : print self.name, "was clicked"

    def scootOver (self, xmov, ymov, nest="") :
        # not only yourself but everything inside too
        self.pos = posAdd(self.pos, (xmov,ymov))
        for kid in self.kids :
            # kid is either an inner component or a connector
            kid.scootOver (xmov, ymov, nest+"  ")

    def __repr__ (s) :
        par = s.parent
        if par : par = par.name
        return "<Comp: %s.%s %s %s>" % (par,s.name,s.pos,s.layer)

def posMult(pos,factor) :                # position math
    return (pos[0]*factor,pos[1]*factor)

def posAdd(pos1, pos2) :
    return (pos1[0]+pos2[0],pos1[1]+pos2[1])

