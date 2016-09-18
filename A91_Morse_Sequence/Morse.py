class Morse():
    def __init__(self,params): # onoff,unit,x,y,r,c
        self.params = params
        self.index = 0
        self.deadline = 0 

    def draw(self):
        if millis() < self.deadline: return
        onoff,unit,x,y,r,c = self.params
        self.deadline = millis() + int(onoff[self.index]) * unit
        if self.index % 2 == 0: fill(c)
        else:                   fill(0)
        ellipse(x,y,2*r,2*r)
        self.index += 1
        self.index %= len(onoff)
        
        
        