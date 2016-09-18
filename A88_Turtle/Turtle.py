class Turtle:
    
    def __init__(self):
        self.pen = True
        self.history = []
        self.init()

    def init(self):
        background(128)
        w,h = width,height
        translate(w/2,h/2)
        stroke(0)
        for x in range(-w/2,w/2,w/10):
            strokeWeight(2 if x==0 else 1)
            line(x,-h,x,h)
        for y in range(-h/2,h/2,h/10):
            strokeWeight(2 if y==0 else 1)
            line(-w,y,w,y)

    def draw(self):
        stroke(255,0,0)
        for a,b in self.history:
            if a=='fd': 
                line(0,0,b,0)
                translate(b,0)
            if a=='lt': rotate(radians(-b))
            if a=='rt': rotate(radians(b))
            if a=='pu': noStroke()
            if a=='pd': stroke(255,0,0)
            
        fill(0,255,0,50)
        stroke(0)
        ellipse(0,0,50,50)
        #fill(255)
        ellipse(15,-10,7,7)
        ellipse(15, 10,7,7)
        
    def fd(self,d=1):
        self.history.append(['fd',50*d])
        
    def lt(self,vinkel=90):
        self.history.append(['lt',vinkel])
        
    def rt(self,vinkel=90):
        self.history.append(['rt',vinkel])
        
    def pu(self):
        self.history.append(['pu',0])

    def pd(self):
        self.history.append(['pd',0])
        
    def do(self,key):
        if key=='a': self.lt()
        if key=='d': self.rt()
        if key=='s': self.fd()
        if key=='r': self.history=[]
        if key=='z' and self.history!=[]: self.history.pop()
        if key=='0': self.pu()
        if key=='1': self.pd()
                