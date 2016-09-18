def setup():
    size(600,600)
    global x,y,xvel,yvel 
    x = width/2
    y = 50
    xvel = 3
    yvel = 5
        
def draw():
    global x,y,xvel,yvel 
    background(255,255,0)
    ellipse(x,y,50,50)

    if x-25<0: xvel=-xvel
    if x+25>width: xvel=-xvel
    x+=xvel

    if y+25>height: yvel=-yvel
    else: yvel+=1
    y+=yvel