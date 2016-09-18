def setup():
    size(360,360)
    rectMode(CENTER)
def draw():
    background(0)
    fill(255)
    translate(width/2,height/2)
    rotate(radians(mouseX))
    stroke(255,0,0)
    strokeWeight(mouseY)
    rect(0,0,50,50)    