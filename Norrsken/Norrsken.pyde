from Bean import Bean

beans = []

def setup():
    size(1920,1080)
    background(0)
    colorMode(HSB, 360, 100, 100)

def draw():
    x_off = frameCount * 0.0003
    if frameCount % 8 == 0: beans.append(Bean(noise(x_off) * width, noise(x_off+20) * height, x_off, x_off+20))
    for bean in beans: bean.draw()    