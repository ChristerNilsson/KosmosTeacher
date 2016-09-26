class Bug:
  def __init__(self,x,y,speed):
    self.x = x
    self.y = y
    self.speed = speed

  def draw(self):
    sz = map(sin(frameCount*self.speed), -1, 1, 10, 20)
    ellipse(self.x, self.y, sz, sz)