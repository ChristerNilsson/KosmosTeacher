b = 0
n = 2

def setup():
    size(1024,1024)
    #colorMode(HSB,256,256,256)

def draw():
    global b
    background(0)
    c = 255.0/(n-1)
    d = 1.0*width/n
    for r in range(n):
        for g in range(n):
            fill(r*c,g*c,b*c)
            rect(r*d,g*d,d,d)

    #r = 255*int(mouseX/d)/(n-1)
    #g = 255*int(mouseY/d)/(n-1)
    #print n,":",r,g,int(b*c),'(',n*n*n,')'           
            
def keyPressed():
    global b,n
    if keyCode==LEFT : n -= 1
    if keyCode==RIGHT: n += 1
    n = constrain(n,2,256)
    if keyCode==DOWN : b -= 1
    if keyCode==UP   : b += 1
    b = constrain(b,0,n-1)
    