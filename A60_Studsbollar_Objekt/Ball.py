class Ball:
    
    def __init__(self):
        self.x = 100 + random(width - 200)
        self.y = 100 + random(height - 200)
        self.vx = random(1,5)
        self.vy = random(1,5)
        self.col = random(255)
        self.r = random(10,50)
        
    def draw(self):
        fill(self.col)
        ellipse(self.x, self.y, 2*self.r, 2*self.r)
        
    def update(self):
        r = self.r
        if self.x - r < 0: self.vx = -self.vx
        elif self.x + r > width: self.vx = -self.vx
        self.x += self.vx
    
        if self.y + r > height: self.vy =- self.vy
        else: self.vy += 1
        self.y += self.vy
        