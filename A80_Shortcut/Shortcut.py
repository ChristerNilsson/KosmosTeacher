import time

class Shortcut:
    def __init__(self):
        self.init()
        
    def init(self):
        self.history = [int(random(1,20))]
        self.target = int(random(1,20))
        self.start = time.time()

    def draw(self):
        a = self.history[-1]
        b = self.target
        text("a=/2   s=+2   d=*2   z=undo",width/2,50)
        if  a == b:
            antal = str(len(self.history)-1)
            tid = "%.3f" % (self.stopp-self.start)
            text("You used " + antal + " operations in "+ tid + " seconds", width/2,100)
            s = [str(tal) for tal in self.history]
            text(" ".join(s), width/2,150)
        else:    
            text(str(a) + " to " + str(b), width/2,100)
            
    def update(self,tangent):
        a = self.history[-1]
        next = a
        if tangent == ' ': 
            self.init()
        elif a != self.target:
            if tangent == 'a' and a%2==0: next = a / 2
            if tangent == 's': next = a + 2
            if tangent == 'd': next = a * 2
            if tangent == 'z' and len(self.history) > 1: self.history.pop()
            if next == self.target: self.stopp = time.time() 
            if next != a: self.history.append(next)