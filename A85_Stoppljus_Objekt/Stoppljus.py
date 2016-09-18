class Stoppljus:

    def __init__(self, x, y, size, delays):
        self.x = x
        self.y = y
        self.size = size
        self.delays = delays
        self.delay = 0
        self.state = 0

    def one_lamp(self,villkor,col,y):
        fill(0)
        if villkor: fill(col) 
        ellipse(self.x, self.y+y, self.size, self.size)
        
    def update(self):
        if millis() > self.delay:
            
            self.state += 1
            self.state %= 4
            self.delay = millis() + self.delays[self.state]
            
            self.one_lamp(self.state <= 1, color(255,  0,0), 0)           # Red
            self.one_lamp(self.state%2==1, color(255,255,0), self.size)   # Yellow
            self.one_lamp(self.state == 2, color(  0,255,0), 2*self.size) # Green