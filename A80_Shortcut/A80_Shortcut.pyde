from Shortcut import Shortcut

def setup():
    global shortcut
    size(600,300)
    textSize(24)
    textAlign(CENTER,CENTER)
    shortcut = Shortcut()

def draw():
    background(0)
    shortcut.draw()
    
def keyPressed():
    shortcut.update(key)