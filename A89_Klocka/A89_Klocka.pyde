SIZE = 250

def setup():
    size(600,600)
    rectMode(CENTER)
    noStroke()
    
def urtavla():
    fill(255)
    ellipse(0,0,2*SIZE+10,2*SIZE+10)
    fill(0)
    for i in range(60):
        if i%5==0: rect(SIZE-25,0,40,10)
        else:      rect(SIZE-5,0,5,1)
        rotate(radians(6))
        
def visare(v,w,l,c):
    with pushMatrix():
        rotate(radians(v-90))
        translate(l/2,0)
        fill(c)
        rect(0,0,l,w)

def draw():
    background(0)
    translate(width/2,height/2)
    urtavla()
    visare((hour()+minute()/60.0)*30, 12,SIZE-70,color(255,0,0,128))
    visare((minute()+second()/60.0)*6, 9,SIZE,   color(0,255,0,128))
    visare(second()*6,                 6,SIZE,   color(0,0,255,128))    