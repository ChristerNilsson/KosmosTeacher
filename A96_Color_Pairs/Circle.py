import random

class Circle:
    def __init__(self,col,radius,circles):
        count = 1
        while count>0:
            self.x = random.randint(0,width)
            self.y = random.randint(0,height)
            count = 0
            for c in circles:
                if dist(c.x,c.y,self.x,self.y) < radius*0.4: count += 1
                    
        self.col = col
        self.radius = radius
        self.marked = False

    def draw(self):
        fill(self.col)
        noStroke()
        strokeWeight(0.05*self.radius)
        ellipse(self.x,self.y,1.95*self.radius,1.95*self.radius)

        noFill()
        stroke(255,255,255,225)
        strokeWeight(0.05*self.radius)
        ellipse(self.x,self.y,2*self.radius,2*self.radius)

    def within(self,x,y):
        return dist(self.x,self.y, x,y) < self.radius        