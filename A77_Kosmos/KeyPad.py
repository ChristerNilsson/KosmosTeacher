class KeyPad:
    
    def __init__(self,x,y,size,W,H):
        self.x = x
        self.y = y
        self.size = size # en tangents storlek
        self.w = size*W+2
        self.h = size*H+2
        self.W = W # 3
        self.H = H # 4
        self.col0 = color(150) # background
        self.col1 = color(100) # off
        self.col2 = color(200,200,0) # on
        self.clear()
        self.text = "789456123*0#"
    
    def on(self,i,j):
        self.state[j][i] = 1
        
    def off(self,i,j):
        self.state[j][i] = 0
        
    def clear(self):
        self.state = []
        for i in range(self.H):
            self.state.append([0]*self.W)
    
    def draw(self):
        s = self.size
        noStroke()
        with pushMatrix():
            rectMode(CORNER)
            fill(self.col0)
            rect(self.x-s/2,self.y-s/2,self.w,self.h)
            rectMode(CENTER)
            for i in range(self.W):
                x = self.x+s*i
                for j in range(self.H):
                    y = self.y+s*j
                    if self.state[j][i] == 0:
                        fill(self.col1)
                    else:
                        fill(self.col2)
                    rect(x+1,y+1,s-2,s-2)
                    fill(255)
                    text(self.text[i+j*3],x+1,y+1)
            
    def mousePressed(self):
        with pushMatrix():
            rectMode(CENTER)
            s = self.size
            for i in range(self.W):
                x = self.x+s*i
                for j in range(self.H):
                    y = self.y+s*j
                    if x-s/2 < mouseX < x+s/2 and y-s/2 < mouseY < y+s/2:                    
                        self.handler(i+j*3)
                    
    