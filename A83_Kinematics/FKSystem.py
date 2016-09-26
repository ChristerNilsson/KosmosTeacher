class FKSystem:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.arms = []
        self.t = 0
        self.last = []

    def addArm(self,size,a,b):
        self.arms.append([size,a,b])        
        
    def update(self):
        x = self.x
        y = self.y
        for size,a,b in self.arms:
            angle = sin(self.t * a) * b
            x += size * cos(angle) 
            y += size * sin(angle)
        if self.last != []: line(x,y, self.last[0], self.last[1])
        self.last = [x,y]
        self.t += 0.05

        