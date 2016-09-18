def setup():
    size(500,500)
    rectMode(CENTER)

def draw():
    background(128)
    translate(width/2,height/2)
    strokeWeight(1)
    for i in range(-5,5):
        line(-250,i*50,250,i*50)
        line(i*50,250,i*50,-250)

    rotate(frameCount*0.005)

    noStroke()
    fill(255)
    ellipse(0,0,50,70)
    rotate(radians(45))
    
    pushMatrix()
    for i in range(2):
        rect(0,0,200,10)
        rotate(radians(90))
    popMatrix()
    
    stroke(0)
    for i in range(4):
        pushMatrix()
        translate(90,0)
        noFill()
        strokeWeight(1)
        ellipse(0,0,100,100)
        ellipse(0,0,2,2)
        popMatrix()
        rotate(radians(90))