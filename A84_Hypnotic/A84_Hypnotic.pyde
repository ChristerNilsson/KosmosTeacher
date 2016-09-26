# http://funprogramming.org/113-Array-of-objects-hypnotic-animation-part-II.html

from Bug import Bug
bugs = []

def setup():
  size(450, 450)
  noStroke()
  for i in range(200):
    x = width/2  + cos(i/2.0) * i
    y = height/2 + sin(i/2.0) * i
    bugs.append(Bug(x, y, 0.05 + i/1000.0))

def draw():
  background(150, 0, 0)
  for bug in bugs: bug.draw()