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

    r = 255*int(mouseX/d)/(n-1)
    g = 255*int(mouseY/d)/(n-1)
    print n,":",r,g,int(b*c),'(',n*n*n,')'           
            
def keyPressed():
    global b,n
    if keyCode==LEFT and n>2: n -= 1
    if keyCode==RIGHT and n<256: n += 1
    if keyCode==DOWN and b>0: b -= 1
    if keyCode==UP and b<n-1: b += 1
    if b<0:b=0
    if b>=n-1:b=n-1
    