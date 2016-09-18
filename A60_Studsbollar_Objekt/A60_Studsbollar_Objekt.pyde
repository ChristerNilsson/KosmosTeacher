from Ball import Ball

balls = []

def setup():
    size(600,600)
    for i in range(5):
        balls.append(Ball())
             
def draw():
    #background(255,0,0,)
    for ball in balls:
        ball.draw()
        ball.update()
        