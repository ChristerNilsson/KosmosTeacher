import random
from QA import QA

class Exercise(QA):
    def makeLongList(self):
        n = self.level + 1
        return [ [random.randint(0,self.width-1), random.randint(0,self.height-1)] for i in range(n) ]
            
    def displayQuestion(self,answer,x,y,w,h):
        fill(255);     text("Select a Point!",x+5,y+30)
        text("Level: "+str(self.level),x+5,y+80)
        fill(255,0,0); text("Width="+str(self.width),self.width-150,30)
        fill(0,255,0); text("Height="+str(self.height),5,self.height-15)
        xa,ya = answer
        stroke(255,0,0); line(xa, 0, xa, self.height)
        stroke(0,255,0); line(0, ya, self.width, ya)
    
    def displayAnswer(self,answer,x,y,w,h):
        xa,ya = answer
        fill(255,0,0); text(xa, x,     y+30)
        fill(0,255,0); text(ya, x+100, y+30)

def setup():
    size(800,400)
    textSize(24)
    global exercise
    exercise = Exercise(width,height)

def draw():
    background(128)
    exercise.draw()
        
def mousePressed():
    exercise.mousePressed()