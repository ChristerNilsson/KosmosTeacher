import random
import time
from Circle import Circle

class Game:
    def __init__(self,width,height):
        self.level = 1
        self.width = width
        self.height = height
        self.init(0)
        self.start = time.time()
        self.stopp = time.time()

    def init(self,dlevel):
        self.level += dlevel
        self.level=constrain(self.level,1,20)
        self.circles = []
        self.marked = None # Marked Circle
        
        self.select_colors()

        self.stopp = time.time()
        
    def select_colors(self):
        if self.level <= 27:
            n=3
        else:
            n=4
        radius = width/(1+self.level)
        colors = []
        for i in range(n):
            r = (i+0.5)/n
            for j in range(n):
                g = (j+0.5)/n
                for k in range(n):
                    b = (k+0.5)/n
                    colors.append(color(255*r,255*g,255*b,128))
        for i in range(self.level):
            col = random.choice(colors)
            colors.remove(col)
            self.circles.append(Circle(col,radius, self.circles))
            self.circles.append(Circle(col,radius, self.circles))

    def mousePressed(self):
        # You must only mark one circle
        # The second circle must have the same color as the first one.
        n = len(self.circles)
        for c in self.circles:
            if c.within(mouseX,mouseY):
                cc = c 
                self.circles.remove(c)                
        if  n != len(self.circles)+1:
            self.init(-1)
            return

        if self.marked == None:
            self.marked = cc.col
        elif cc.col == self.marked:
            self.marked = None
            if len(self.circles)==0:
                self.init(1) # Win
        else: 
            self.init(-1) # Lose
            
    def draw(self):
        for c in self.circles: c.draw()
        fill(255,255,255,128)
        text("Level %d in %.3f seconds" % (self.level, self.stopp-self.start) ,width/2,height-50)