from Morse import Morse

morses = []

def setup():
    size(300,100)
    sos = "111113313133111117" 
    morses.append(Morse([sos, 500,  50, 50, 50, color(255,255,0)]))
    morses.append(Morse([sos, 400, 140, 40, 40, color(0,255,255)]))
    morses.append(Morse([sos, 300, 210, 30, 30, color(255,0,0)]))
    morses.append(Morse([sos, 200, 260, 20, 20, color(0,255,0)]))
    morses.append(Morse([sos, 100, 290, 10, 10, color(255)]))
    background(0)
    
def draw():
    for morse in morses:
        morse.draw()