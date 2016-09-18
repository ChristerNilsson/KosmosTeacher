def setup():
    size(500,400)
    global r,g,b
    r,g,b = 128,128,128
    textSize(72)
    textAlign(CENTER,CENTER)
    
def draw():
    global r,g,b
    background(r,g,b)
    translate(width/2, height/2)
    fill(255,0,0); text(r,-180,0)
    fill(0,255,0); text(g,0,0)
    fill(0,0,255); text(b,180,0)

def keyPressed():
    global r,g,b
    if key=='R': r += 1    
    if key=='G': g += 1    
    if key=='B': b += 1    
    if key=='r': r -= 1    
    if key=='g': g -= 1    
    if key=='b': b -= 1        
    r = constrain(r,0,255)
    g = constrain(g,0,255)
    b = constrain(b,0,255)