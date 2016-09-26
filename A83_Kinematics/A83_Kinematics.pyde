# Youtube: Coding Math 43

from FKSystem import FKSystem

def setup():
    size(1000,1000)
    global system
    system = FKSystem(width/2,height/2)
    system.addArm(150, 1,    1.3)
    system.addArm(100, 1.2,  -0.9)
    system.addArm(80, 0.71, 4.12)
    system.addArm(60, 2.4, -0.7)
    background(0)
    stroke(255) 
    
def draw():
    system.update()

    