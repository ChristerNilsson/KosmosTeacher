def setup():
    size(600,600)
    global balls
    balls = []
    balls.append([width/2,0,3,5])
    balls.append([width/3,10,3,5])
             
def draw():
    global balls 
    background(255,255,0)
    for i in range(2):
        x,y,xvel,yvel = balls[i]
        ellipse(x,y,50,50)
    
        if x-25<0: xvel=-xvel
        elif x+25>width: xvel=-xvel
        x+=xvel
    
        if y+25>height: yvel=-yvel
        else: yvel+=1
        y+=yvel
        balls[i] = x,y,xvel,yvel