class Bean:
    def __init__(self,x,y,x_off,y_off):
        self.x = x
        self.y = y
        self.x_off = x_off
        self.y_off = y_off
        self.vel = 3
        self.accel = -0.003
        
    def draw(self):
        if self.vel <= 0: return
        self.x_off += 0.0007
        self.y_off += 0.0007
        self.vel += self.accel
        self.x += noise(self.x_off) * self.vel - self.vel/2
        self.y += noise(self.y_off) * self.vel - self.vel/2
        #colorMode(HSB, 360, 100, 100)
        h = noise((self.x_off + self.y_off)/2) * 360
        stroke(h,100,100,4)
        point(self.x,self.y)