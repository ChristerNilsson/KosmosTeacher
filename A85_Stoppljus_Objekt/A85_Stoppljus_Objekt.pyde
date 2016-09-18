from Stoppljus import Stoppljus

lysen = []

def setup():
    background(128)
    size(300,300)
    lysen.append(Stoppljus(100, 50, 50, [2000,500,2000,500]))
    lysen.append(Stoppljus(200, 50, 50, [1000,250,1000,250]))
    
def draw():
    for lyse in lysen: lyse.update()