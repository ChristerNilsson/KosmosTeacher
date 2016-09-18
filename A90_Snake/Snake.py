class Snake:

    def __init__(self,x,y,size,col,left,right):
        self.size = size
        self.col = col
        self.left = left
        self.right = right

        self.n = width/self.size
        self.dir = 0
        self.body = [PVector(x,y)] # square numbers
        self.dirs = [PVector(1,0),PVector(0,-1),PVector(-1,0),PVector(0,1)]

    def collision(self,other):
        head = self.body[-1]
        if self==other:
            return head in self.body[:-1]
        else:
            return head in self.body[:-1] or head in other.body
        
    def draw(self):
        fill(self.col)
        for item in self.body:
            n = self.size
            rect(item.x*n, item.y*n, n, n)

    def turn(self, key):
        if key == self.left:  self.dir = (self.dir+1) % 4
        if key == self.right: self.dir = (self.dir-1) % 4
        
    def update(self):
        if frameCount % 5 != 0: return
        head = self.body[-1]
        d = self.dirs[self.dir]
        p = PVector((head.x+d.x) % self.n, (head.y+d.y) % self.n) 
        self.body.append(p)
        if frameCount % 50 != 0: self.body.pop(0)

        