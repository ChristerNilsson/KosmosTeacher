class Segment7:
    
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.col0 = color(150) # background
        self.col1 = color(100,0,0) # off
        self.col2 = color(255,0,0) # on
        self.clear()
        self.leds = []
        t = (w+h)/20 # tjockleken
        x0 = t
        x1 = 2*t
        x2 = w-2*t
        y0 = t
        y1 = 2*t
        y2 = h/2-t/2
        y3 = y2+t
        y4 = h-2*t
        hw = w-4*t
        hh = t
        vw = t
        vh = h/2-2.5*t
        self.leds.append([x1,y0,hw,hh])
        self.leds.append([x2,y1,vw,vh])
        self.leds.append([x2,y3,vw,vh])
        self.leds.append([x1,y4,hw,hh])
        self.leds.append([x0,y3,vw,vh])
        self.leds.append([x0,y1,vw,vh])
        self.leds.append([x1,y2,hw,hh])

    def on(self,i):
        self.state[i] = 1
        
    def off(self,i):
        self.state[i] = 0
    
    def clear(self):        
        self.state = [0,0,0,0,0,0,0]

    def draw(self):
        with pushMatrix():
            noStroke()
            rectMode(CORNER)
            fill(self.col0)
            rect(self.x,self.y,self.w,self.h)
            for i in range(7):
                x,y,w,h = self.leds[i]
                if self.state[i]==0:
                    fill(self.col1)
                else:
                    fill(self.col2)
                rect(self.x+x,self.y+y,w,h)