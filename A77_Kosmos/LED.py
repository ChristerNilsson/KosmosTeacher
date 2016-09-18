class LED:
    
    def __init__(self,x,y,size):
        self.x = x
        self.y = y
        self.size = size
        self.col0 = color(150) # background
        self.col1 = color(100) # off
        self.col2 = color(200,200,0) # on
        self.state = 0
        
    def on(self):
        self.state = 1
    def off(self):
        self.state = 0

    def draw(self):
        if self.state==0:
            fill(self.col1)
        else:
            fill(self.col2)
        with pushMatrix():
            rectMode(CENTER)
            ellipse(self.x,self.y,self.size,self.size)

    