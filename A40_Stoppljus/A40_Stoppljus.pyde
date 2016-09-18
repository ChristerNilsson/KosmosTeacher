def setup():
    size(100,300)
    global state,deadline
    state = 0
    deadline = 0
    
def stoppljus(red,yel,grn,d):
    global state,deadline
    fill(red*255,      0,0); ellipse(width/2,100,50,50)    
    fill(yel*255,yel*255,0); ellipse(width/2,150,50,50)    
    fill(      0,grn*255,0); ellipse(width/2,200,50,50)
    deadline = millis() + d    
    
def draw():
    global state,deadline
    if millis()>deadline:
        if state==0: stoppljus(1,0,0,2000)
        if state==1: stoppljus(1,1,0,500)
        if state==2: stoppljus(0,0,1,2000)
        if state==3: stoppljus(0,1,0,500)
        state += 1
        state %= 4