from Ball import Ball

class Square(Ball):
    def draw(self):
        rect(self.x,self.y,50,50)