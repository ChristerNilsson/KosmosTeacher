from Turtle import Turtle

def setup():
    size(500,500)
    global turtle
    turtle = Turtle()

    for i in range(5):
        turtle.fd(0.7)
        turtle.rt(72)
    turtle.pu()     
    
def draw():
    turtle.init()
    turtle.draw()
    
def keyPressed():
    turtle.do(key)            