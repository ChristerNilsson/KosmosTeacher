import random

class QA:
    def __init__(self,width,height):
        self.level = 1
        self.width = width
        self.height = height
        self.longList = self.makeLongList()
        self.shortList = self.makeShortList()
        
    def makeShortList(self):
        self.n = self.level+1
        self.index = random.randint(0, self.n-1)
        self.guess_index = -1
        return random.sample(self.longList, self.n)

    def mousePressed(self):
        if mouseX < width/2: return
        self.guess_index = mouseY/(height/self.n)
        self.level += 1 if self.guess_index == self.index else -1
        self.level = constrain(self.level, 1, 10)
        self.longList = self.makeLongList()
        self.shortList = self.makeShortList()

    def draw(self):
        if self.index >= len(self.shortList): return
        self.displayQuestion(self.shortList[self.index], 0, 0, width/2, height)
        h = height/self.n
        for i in range(len(self.shortList)): 
            self.displayAnswer(self.shortList[i], width/2, i*h, width/2, h)