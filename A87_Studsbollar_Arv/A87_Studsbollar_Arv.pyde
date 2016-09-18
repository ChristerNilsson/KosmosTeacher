from Ball import Ball
from Square import Square

def setup():
    size(600,600)
    rectMode(CENTER)
    global balls
    balls = []
    for i in range(5):
        x = 10+random(width-20)
        y = 100+random(height-200)
        xvel = 1+random(5)
        yvel = 1+random(5)
        if i%2==0:
            balls.append(Ball(x,y,xvel,yvel))
        else:
            balls.append(Square(x,y,xvel,yvel))
             
def draw():
    background(255,255,0)
    for ball in balls:
        ball.draw()
        ball.update()