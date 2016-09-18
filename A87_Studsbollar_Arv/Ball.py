class Ball:
    
    def __init__(self,x,y,xvel,yvel):
        self.x=x
        self.y=y
        self.xvel=xvel
        self.yvel=yvel
        
    def draw(self):
        ellipse(self.x,self.y,50,50)
        
    def update(self):
        if self.x-25<0: self.xvel=-self.xvel
        elif self.x+25>width: self.xvel=-self.xvel
        self.x+=self.xvel
    
        if self.y+25>height: self.yvel=-self.yvel
        else: self.yvel+=1
        self.y+=self.yvel
        