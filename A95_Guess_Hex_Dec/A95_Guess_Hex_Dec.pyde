import random
from QA import QA

class Exercise(QA):
    def makeLongList(self):
        n = self.level + 1
        return [ 10+i for i in range(2**self.level) ]
            
    def displayQuestion(self,answer,x,y,w,h):
        fill(255);
        text("Select a Number!",                       x+5, y+30)
        text("Level: " + str(self.level),              x+5, y+80)
        text("Hexadecimal " + hex(answer).lstrip('0'), x+5, y+130)
    
    def displayAnswer(self,answer,x,y,w,h):
        fill(0); text(answer, x, y+30)

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