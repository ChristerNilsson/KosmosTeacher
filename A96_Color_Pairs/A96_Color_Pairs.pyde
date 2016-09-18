from Game import Game

def setup():
    size(1900,1040)
    level = 1
    global game
    game = Game(width,height)
    textSize(48)
    textAlign(CENTER,CENTER)

def draw():
    #background(128)
    background(0)
    game.draw()
        
def mousePressed():
    game.mousePressed()