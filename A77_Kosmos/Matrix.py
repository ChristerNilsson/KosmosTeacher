class Matrix:
    
    def __init__(self,x,y,size,W,H):
        self.x = x
        self.y = y
        self.size=size
        self.w = size*W+2
        self.h = size*H+2
        self.W = W # 5
        self.H = H # 7
        self.col0 = color(150) # background
        self.col1 = color(100) # off
        self.col2 = color(200,200,0) # on
        self.clear()
    
    def on(self,i,j):
        self.state[j][i] = 1
    def off(self,i,j):
        self.state[j][i] = 0
        
    def clear(self):
        self.state = []
        for i in range(self.H):
            self.state.append([0]*self.W)
    
    def draw(self):
        dx = self.size
        dy = self.size
        noStroke()
        with pushMatrix():
            rectMode(CORNER)
            fill(self.col0)
            rect(self.x-dx/2,self.y-dy/2,self.w,self.h)
        for i in range(self.W):
            x = self.x+dx*i
            for j in range(self.H):
                y = self.y+dy*j
                if self.state[j][i] == 0:
                    fill(self.col1)
                else:
                    fill(self.col2)
                ellipse(x+1,y+1,dx-2,dy-2)

        