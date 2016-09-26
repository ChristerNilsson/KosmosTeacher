import sys
from Area import Area,BACKGR
    
EXT = ".png"
WIDTH = 200
HEIGHT = 200
GAP = 3

def push():
    return pushMatrix()

def bg(*params):
    noStroke()
    fc(*params)
    rect(0,0,WIDTH+1,HEIGHT+1)

def rd(degrees):
    rotate(radians(degrees))
        
def circle(x,y,r):
    ellipse(x,y,2*r,2*r)

def col(*params):
    if len(params)==1:
        return color(255*params[0])
    elif len(params)==2:
        return color(255*params[0], 255*params[0], 255*params[0], 255*params[1])
    elif len(params)==3:
        return color(255*params[0], 255*params[1], 255*params[2])
    elif len(params)==4:
        return color(255*params[0], 255*params[1], 255*params[2], 255*params[3])
        
def fc(*params):
    if len(params)==0:
        noFill()
    elif len(params)==1:
        fill(255*params[0])
    elif len(params)==2:
        fill(255*params[0], 255*params[0], 255*params[0], 255*params[1])
    elif len(params)==3:
        fill(255*params[0], 255*params[1], 255*params[2])
    elif len(params)==4:
        fill(255*params[0], 255*params[1], 255*params[2], 255*params[3])
        
def sc(*params):
    if len(params)==0:
        noStroke()
    elif len(params)==1:
        stroke(255*params[0])
    elif len(params)==2:
        stroke(255*params[0],255*params[0],255*params[0],255*params[1])
    elif len(params)==3:
        stroke(255*params[0],255*params[1],255*params[2])
    elif len(params)==4:
        stroke(255*params[0],255*params[1],255*params[2],255*params[3])

def sw(n):
    strokeWeight(n)                

class Assert:
    
    def __init__(self):
        self.images = {}
        self.result = {}
        self.area1 = Area(GAP,GAP,                  WIDTH,HEIGHT)
        self.area2 = Area(GAP,1*(GAP+HEIGHT+1)+GAP, WIDTH,HEIGHT)
        self.area3 = Area(GAP,2*(GAP+HEIGHT+1)+GAP, WIDTH,HEIGHT)
        self.area4 = Area(GAP+WIDTH,2*(GAP+HEIGHT+1)+GAP, WIDTH,HEIGHT)
        self.area5 = Area(GAP+WIDTH,1*(GAP+HEIGHT+1)+GAP, WIDTH,HEIGHT)
        self.count = 0
        self.mousex = 0
        self.mousey = 0
        self.img2 = None
        self.img3 = None
        self.img4 = None
        self.nr = 0

    def check(self,filename): # missing ext
        if self.count == 0:
            background(255)
            self.filename = filename
            if filename in self.images:
                self.img2 = self.images[filename]
            else:
                self.img2 = loadImage(filename + EXT)
            a = self.area2
            if self.img2 == None:
                fill(BACKGR)
                strokeWeight(1)
                stroke(0)
                rect(a.x,a.y,a.w+1,a.h+1)
            else: 
                self.images[filename] = self.img2
                image(self.img2, a.x, a.y)
            
        if self.img3:
            self.area3.myset(self.img3)        

        self.showText()
                                                                        
        return self
        
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, tb):
        if self.filename not in self.result:
            self.nr += 1
            count = self.compare()
            self.result[self.filename] = count==0
            print(str(self.nr) + " " + self.filename + " " + str(millis())+" ms")
        resetMatrix()
        rectMode(CORNER)
        colorMode(RGB,255,255,255,255)
        textAlign(LEFT,BOTTOM)
            
    def showOneColor(self,color,value,y):
        fill(color)
        textAlign(RIGHT,BOTTOM)
        text("{0:3d}".format(value),        GAP+3*WIDTH/2-10,y)
        textAlign(LEFT,BOTTOM)
        text("{0:.3f}".format(value/255.0), GAP+3*WIDTH/2+10,y)

    def showText(self):
        self.area4.clear(255)        
        textAlign(CENTER,BOTTOM)
        textSize(16)
        strokeWeight(1)
        fill(0)
        text(self.filename, 3*WIDTH/2, 440)
        
        mghg = (self.mousey-GAP) % (HEIGHT+1+GAP)
        if 0 <= self.mousex-GAP <= WIDTH and mghg <= HEIGHT and self.mousey<3*180+4*GAP:
            s = "x,y = "+str(self.mousex-GAP) + ","+str(mghg) 
            text(s,GAP+3*WIDTH/2,460)
            
        if self.count==0: fill(0,128,0)
        else:             fill(255,0,0)
        text(str(self.count) + " pixel errors",GAP+3*WIDTH/2,480)
        
        pixel = self.img2.get(self.mousex-GAP, mghg)
        r,g,b = self.split(pixel)
        self.showOneColor(color(255,0,0), r, 520)
        self.showOneColor(color(0,255,0), g, 540)
        self.showOneColor(color(0,0,255), b, 560)

    def split(self,c):
        b = c & 0xFF
        c = c >> 8; g = c & 0xFF 
        c = c >> 8; r = c & 0xFF 
        return [r,g,b]
    
    def compare(self):
        self.count = 0
        
        img1 = self.area1.myget()
        img2 = self.area2.myget()
        self.img3 = self.area3.myget()
        
        for i in range(WIDTH+1):
            for j in range(HEIGHT+1):
                r1,g1,b1 = self.split(img1.get(i,j))
                r2,g2,b2 = self.split(img2.get(i,j))
                r,g,b = abs(r1-r2), abs(g1-g2), abs(b1-b2) # somewhat nicer diff
                c = color(r,g,b)
                self.img3.set(i,j,c) 
                if r+g+b > 9: # t ex whiteTriangle i motsatt riktning
                    self.count += 1
                    if self.count < 10: print i,j,":",r,g,b
        self.area3.myset(self.img3)        
        if self.count > 0: 
            self.filename2 = self.filename
            print self.filename2, ":", self.count, "errors in", str(millis())+ " millis"
        return self.count
   
    def errors(self):
        if self.count==0: 
            self.area1.coords()
            translate(self.area1.x,self.area1.y)
        return self.count!=0
    
    def keyPressed(self):
        if key == "!": 
            self.area1.save(self.filename + EXT)

    def mousePressed(self):
        self.mousex = mouseX
        self.mousey = mouseY
        
    def mouseMoved(self):
        loadPixels()
        #n,m = 3,20
        n,m = 5,12
         
        x0,y0 = GAP,HEIGHT
        x1,y1 = 100+GAP+WIDTH,100+HEIGHT
        for dx in range(-m,m):
            x = mouseX+dx
            for dy in range(-m,m):
                y = mouseY+dy
                pixel = pixels[x + width*y]
                for i in range(n):
                    xi = x1+n*dx+i-2
                    for j in range(n):
                        yi = y1+n*dy+j-1
                        pixels[xi + width*yi] = pixel 
        updatePixels()
        stroke(255)
        strokeWeight(1)
        x1=x1-1+1
        y1=y1+1
        line(x1,     y1-100, x1,     y1+100)       
        line(x1-100, y1,     x1+100, y1)       