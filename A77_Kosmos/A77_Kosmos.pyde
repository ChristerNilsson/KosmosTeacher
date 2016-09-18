from LED import LED
from Segment7 import Segment7
from Matrix import Matrix
from Button import Button
from KeyPad import KeyPad
from Robot import Robot

led = LED(150,100,20)
s7a = Segment7(100,280,50,70)
s7b = Segment7(155,280,50,70)
m5x7a = Matrix(300,50,20,5,7)
m5x7b = Matrix(410,50,20,5,7)
button = Button(80,100,40)
keypad = KeyPad(300,240,30,3,4)
robot1 = Robot(50,200,50,[LEFT,RIGHT,UP,DOWN],color(255,0,0))
robot2 = Robot(50,250,40,[65,68,87,83],color(0,255,0))

counter = 0

def handleButton():
    global counter
    counter = counter+1

def handleKeyPad(i):
    ch = keypad.text[i]
    if ch == '0': s7b.state = [1,1,1,1,1,1,0]
    elif ch == '1': s7b.state = [0,1,1,0,0,0,0]
    elif ch == '2': s7b.state = [1,1,0,1,1,0,1]
    elif ch == '3': s7b.state = [1,1,1,1,0,0,1]
    elif ch == '4': s7b.state = [0,1,1,0,0,1,1]
    elif ch == '5': s7b.state = [1,0,1,1,0,1,1]
    elif ch == '6': s7b.state = [1,0,1,1,1,1,1]
    elif ch == '7': s7b.state = [1,1,1,0,0,0,0]
    elif ch == '8': s7b.state = [1,1,1,1,1,1,1]
    elif ch == '9': s7b.state = [1,1,1,1,0,1,1]
    else:s7b.state = [0,0,0,0,0,0,0]

def setup():
    size(600,400)
    textAlign(CENTER,CENTER)
    textSize(24)
    rectMode(CENTER)
    button.text = "Hi"
    button.handler = handleButton
    keypad.handler = handleKeyPad
    
def draw():
    background(128)
    led.off()

    s7a.state = [1,1,1,1,1,1,0]
    #s7b.state = [1,1,1,1,1,1,0]

    m5x7a.clear()
    m5x7a.on(1,1)

    m5x7b.state = [[0, 0, 1, 0, 0], 
                   [0, 1, 0, 1, 0], 
                   [1, 0, 0, 0, 1], 
                   [1, 1, 1, 1, 1], 
                   [1, 0, 0, 0, 1], 
                   [1, 0, 0, 0, 1], 
                   [1, 0, 0, 0, 1]]    

    led.state = button.state

    text(counter,200,100)

    s7a.draw()
    s7b.draw()
    m5x7a.draw()
    m5x7b.draw()
    led.draw()
    button.draw()   
    keypad.draw() 
    
    robot1.draw()
    robot1.update()
    robot2.draw()
    robot2.update()
    
def mousePressed():
    button.mousePressed()
    keypad.mousePressed()
    
def mouseReleased():
    button.mouseReleased()

def keyPressed():
    print keyCode
    robot1.keyPressed()
    robot2.keyPressed()                