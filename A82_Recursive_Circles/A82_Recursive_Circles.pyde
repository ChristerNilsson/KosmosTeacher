def setup():
    size(800,800)

def circles(x,y,r,col):
    fill(col)
    stroke(255)
    ellipse(x,y,2*r,2*r)
    if r < 10: return
    circles(x-r/2,y,r/2,col/2)
    circles(x+r/2,y,r/2,3*col/4)
    
def draw():
    circles(width/2,height/2,width/2,255)