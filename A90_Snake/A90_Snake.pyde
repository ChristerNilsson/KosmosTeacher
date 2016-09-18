from Snake import Snake

def init():
    global snakes
    snakes = []
    snakes.append(Snake(10,10,15,color(255,0,0),  'a','s'))
    snakes.append(Snake(30,30,15,color(0,255,0),  'k','l'))

def setup():
    size(600,600)
    init()

def draw():
    background(0)
    for i in range(len(snakes)):
        snakes[i].draw()
        snakes[i].update()
        for j in range(len(snakes)):
            if snakes[i].collision(snakes[j]):
                snakes.remove(snakes[i])
                return

def keyPressed():
    if key == ' ' and len(snakes) <= 1: 
        init()
    else:
        for snake in snakes:
            snake.turn(key)            