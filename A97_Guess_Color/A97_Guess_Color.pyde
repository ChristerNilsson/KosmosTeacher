import random
from QA import QA

class Exercise(QA):

    def makeLongList(self):
        n = self.level + 1
        gap = 255.0/self.level
        return [[int(gap*r),int(gap*g),int(gap*b)] for r in range(n) for g in range(n) for b in range(n)]
            
    def displayQuestion(self,answer,x,y,w,h):
        fill(255)
        text("Select a Color!",x+50,y+h/2-120)
        text("Level: "+str(self.level),x+50,h/2-80)
        text("("+str((self.level+1)**3) + " colors)", x+50, h/2-40)
        r,g,b = answer
        fill(255); text("r = " + str(r), x+20, y+h/2+50);  fill(r,0,0); rect(x+150,y+h/2+25,100,40)
        fill(255); text("g = " + str(g), x+20, y+h/2+100); fill(0,g,0); rect(x+150,y+h/2+75,100,40)
        fill(255); text("b = " + str(b), x+20, y+h/2+150); fill(0,0,b); rect(x+150,y+h/2+125,100,40)

    def displayAnswer(self,answer,x,y,w,h):
        r,g,b = answer
        fill(r,g,b)
        rect(x+1,y+1,w-2,h-2)

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