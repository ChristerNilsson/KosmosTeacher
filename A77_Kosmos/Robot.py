class Robot:

    def __init__(self,x,y,size,keys,col):
        self.x = x
        self.y = y
        self.size = size
        self.keys = keys
        self.col = col
        self.angle = 0
        self.speed = 0

    def draw(self):
        with pushMatrix():
            translate(self.x,self.y)
            rotate(radians(self.angle))
            scale(self.size/50.0)
            fill(self.col)
            ellipse(0,0,50,25)
            fill(0)
            ellipse(-5,0,25,12.5)
            rect(0,-15,20,4)
            rect(0,15,20,4)
        
    def update(self):
        self.x += self.speed * cos(radians(self.angle))
        self.y += self.speed * sin(radians(self.angle))
    
    def keyPressed(self):
        if   keyCode == self.keys[0]: self.angle -= 5
        elif keyCode == self.keys[1]: self.angle += 5
        elif keyCode == self.keys[2]: self.speed += 0.5
        elif keyCode == self.keys[3]: self.speed -= 0.5