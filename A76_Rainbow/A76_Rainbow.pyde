# Rainbow
def setup():
    size(256,256)
    noStroke()
    colorMode(HSB, 256)

def draw():
    for i in range(256):
        stroke(i, 255, 255)
        line(i,0,i,255)