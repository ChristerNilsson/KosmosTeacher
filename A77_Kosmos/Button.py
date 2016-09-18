class Button:
    
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size=size
        self.col0 = color(150)
        self.col1 = color(100,0,0)
        self.col2 = color(255,0,0)
        self.state = 0
        self.text=""
        
    def draw(self):
        if self.state==0:
            fill(self.col1)
        else:
            fill(self.col2)
        rect(self.x,self.y,self.size,self.size)
        if self.text!="":
            stroke(255)
            fill(255)
            text(self.text,self.x,self.y)
        
    def text(t):
        self.text = t        

    def within(self):
        s = self.size/2
        return self.x-s < mouseX < self.x+s and self.y-s < mouseY < self.y+s
        
    def mousePressed(self):
        if self.within():
            self.state = 1
            self.handler()
                 
    def mouseReleased(self):
        if self.within():
            self.state = 0
        
        