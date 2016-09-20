from Game import Game

def setup():
    #size(1920-20,1080-40) # vaio 1920 x 1080
    #size(1600-20,900-40) # vaio 1600 x 900
    size(1280-20,800-40) # Dell M115HD 1280 x 800
    
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