def setup():
    size(600,400)
    background(0)
    textSize(24)

def draw():
    background(255)
    fill(0)
    stroke(255)
    text(mouseX,40,30)    
    text(mouseY,40,50)    
    text(frameCount,40,70)    

    stroke(255,0,0)
    for x in range(0,width,100):
        line(x, 0, x, height)
    stroke(0,255,0)
    for y in range(0,height,100):
        line(0, y, width, y)

def mousePressed():
    stroke(0)
    noFill()
    rect(0,0,width-1,height-1)   
    saveFrame()             
                