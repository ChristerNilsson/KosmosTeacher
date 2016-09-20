from Exercise import Exercise

exercise = Exercise()

def setup():
    size(400,400)
    fill(0)
    textAlign(CENTER,CENTER)
    
def draw():
    exercise.draw()
    
def keyPressed():
    exercise.keyPressed()