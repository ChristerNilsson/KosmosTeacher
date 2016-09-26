########################################################
def draw():                                            #
########################################################

    with ass.check("whiteBackground"): 
        if ass.errors(): return
        bg(1)
        
    with ass.check("grayBackground"): 
        if ass.errors(): return
        bg(0.5)
        
    with ass.check("redBackground"): 
        if ass.errors(): return
        bg(1,0,0)
        
    with ass.check("greenBackground"): 
        if ass.errors(): return
        bg(0,1,0)
        
    with ass.check("yellowBackground"): 
        if ass.errors(): return
        bg(1,1,0)
        
    with ass.check("point"): 
        if ass.errors(): return
        point(10,30)

    with ass.check("redPoint"): 
        if ass.errors(): return
        sc(1,0,0)
        point(20,40)

    with ass.check("greenPoint"): 
        if ass.errors(): return
        sc(0,1,0)
        point(30,10)
        
    with ass.check("horizontalLine"): 
        if ass.errors(): return
        sc(1,0,1)
        line(10,70, 190,70) 

    with ass.check("verticalLine"): 
        if ass.errors(): return
        sc(1,1,0)
        sw(10)
        line(110,30, 110,170)
        
    with ass.check("yellowLine"): 
        if ass.errors(): return
        sc(1,1,0)
        line(20,30, 140,160)

    with ass.check("whiteCircle"): 
        if ass.errors(): return
        fc(1)
        circle(60,80,30)

    with ass.check("whiteEmptyCircle"): 
        if ass.errors(): return
        sc(1)
        fc()
        sw(2)
        circle(70,90,40)
        
    with ass.check("greenEllipse"): 
        if ass.errors(): return
        fc(0,1,0)
        ellipse(120,60, 60,40) 

    with ass.check("greenRect"): 
        if ass.errors(): return
        fc(0,1,0)
        rect(60,80, 40,50) 

    with ass.check("redRect"):
        if ass.errors(): return
        fc(1,0,0)
        rect(80,70, 40,100)

    with ass.check("whiteTriangle"):
        if ass.errors(): return
        fc(1)
        triangle(20,40, 160,100, 100,140)
        
    with ass.check("yellowQuad"):
        if ass.errors(): return
        fc(1,1,0)
        quad(150,100, 180,20, 40,20, 100,140)
        
    with ass.check("twoDiscsA"):
        if ass.errors(): return
        fc(1,0,0)
        circle(80,100,40)
        fc(0,1,0)
        circle(100,120,50)

    with ass.check("twoDiscsB"):
        if ass.errors(): return
        fc(0,1,0)
        circle(140,120,60)
        fc(1,0,0)
        circle(60,80,50)
        
    with ass.check("twoDiscsC"):
        if ass.errors(): return
        fc(1,0,0)
        circle(80,100,40)
        fc(0,1,0, 0.5)
        circle(120,100,50)
        
    with ass.check("twoDiscsD"):
        if ass.errors(): return
        fc(1,0,0, 0.5)
        circle(80,90,60)
        fc(0,1,0)
        circle(110,120,50)

    with ass.check("twoDiscsE"):
        if ass.errors(): return
        fc(1,0,0, 0.5)
        circle(70,90,50)
        fc(0,1,0, 0.5)
        circle(100,130,70)

    with ass.check("twoDiscsF"):
        if ass.errors(): return
        fc(0,1,0, 0.5)
        circle(120,140,40)
        fc(1,0,0)
        circle(80,70,50)
        
    with ass.check("twoDiscsG"):
        if ass.errors(): return
        fc(0,1,0)
        circle(110,120,40)
        fc(1,0,0, 0.5)
        circle(80,100,60)

    with ass.check("twoDiscsH"):
        if ass.errors(): return
        fc(0,1,0, 0.5)
        circle(120,100,40)
        fc(1,0,0, 0.5)
        circle(80,90,60)

    with ass.check("cross"):
        if ass.errors(): return
        fc(1,0,0)
        sc()
        rect(85,70, 70,10)
        rect(115,40, 10,100)
                    
    with ass.check("squareHole"):
        if ass.errors(): return
        fc(0,1,1)
        sc()
        rect(60,60, 80,20)
        rect(60,120, 80,20)
        rect(60,60, 20,80)
        rect(120,60, 20,80)
        sc(0)
        fc()
        sc(1,0,0)
        sw(3)
        rect(60,60, 80,80)
        rect(80,80, 40,40)
        
    def colorCube(n,b):
        bg(0)
        d = 200.0/n
        m = n-1.0
        for r in range(n):
            for g in range(n):
                fc(r/m,g/m,b/m)
                rect(r*d,g*d,d,d)
        
    with ass.check("colorCube_2_0"):
        if ass.errors(): return
        colorCube(2,0)
        
    with ass.check("colorCube_2_1"):
        if ass.errors(): return
        colorCube(2,1)
        
    with ass.check("colorCube_3_0"):
        if ass.errors(): return
        colorCube(3,0)
        
    with ass.check("colorCube_3_1"):
        if ass.errors(): return
        colorCube(3,1)
        
    with ass.check("colorCube_3_2"):
        if ass.errors(): return
        colorCube(3,2)
        
    def korg(n,w,c1,c2):
        bg(0)
        fill(c1)
        stroke(c2)
        sw(w)
        q = 2*n+1
        d = 200.0/q
        for i in range(n): # hor
            rect(d+i*2*d,0,d,q*d)
        for j in range(n): # ver
            rect(0,d+j*2*d,q*d,d)
        for i in range(n): # chessbooard
            for j in range(n):
                if (i+j) % 2 == 1:
                    rect(i*2*d,d+j*2*d,3*d,d)
                else:
                    rect(d+i*2*d,j*2*d,d,3*d)
                    
    with ass.check("korg_1"): 
        if ass.errors(): return
        colorMode(RGB,1,1,1,1)
        korg(1,5,color(1,0,0),color(1,1,0))
    
    with ass.check("korg_2"): 
        if ass.errors(): return
        colorMode(RGB,1,1,1,1)
        korg(2,4,color(0.5),color(1))
        
    with ass.check("korg_3"): 
        if ass.errors(): return
        colorMode(RGB,1,1,1,1)
        korg(3,3,color(1,1,0),color(1,0,0))
        
    with ass.check("korg_4"): 
        if ass.errors(): return
        colorMode(RGB,1,1,1,1)
        korg(4,2,color(1),color(0.5))
        
    with ass.check("korg_5"): 
        if ass.errors(): return
        colorMode(RGB,1,1,1,1)
        korg(5,1,color(1,0,0),color(1,1,0))
        
    with ass.check("textPythonA"):
        if ass.errors(): return
        fc(1,1,0)
        textSize(50)
        text("Python",100,100)
        
    with ass.check("textPythonB"):
        if ass.errors(): return
        fc(1,1,0)
        textSize(50)
        textAlign(CENTER,CENTER)
        text("Python",100,100)
        
    with ass.check("textPythonC"):
        if ass.errors(): return
        fc(1,1,0)
        textSize(50)
        textAlign(CENTER,CENTER)
        translate(100,100)
        rd(90)
        text("Python",0,0)
        
    with ass.check("textPythonD"):
        if ass.errors(): return
        fc(1,1,0)
        textSize(50)
        textAlign(CENTER,CENTER)
        translate(100,100)
        rd(180)
        text("Python",0,0)

    with ass.check("rotatedEllipse"):
        if ass.errors(): return
        fc(1,0,0)
        sc()
        translate(100,100)
        rd(45)
        ellipse(0,0, 80,40)

    with ass.check("rotatedRectA"):
        if ass.errors(): return
        fc(1,0,0)
        rect(60,100, 40,40)
        fc(0,1,0)
        rect(140,100, 40,40)
        
    with ass.check("rotatedRectB"):
        if ass.errors(): return
        with push():
            fc(1,0,0)
            translate(60,100)
            rd(45)
            rect(0,0, 40,40)
        
        with push():
            fc(0,1,0)
            translate(140,100)
            rd(45)
            rect(0,0, 40,40)
    
    with ass.check("rotatedRectC"):
        if ass.errors(): return
        rectMode(CENTER)
        with push():
            fc(1,0,0)
            translate(80,120)
            rd(45)
            rect(0,0, 40,40)
        
        with push():
            fc(0,1,0)
            translate(160,120)
            rd(45)
            rect(0,0, 40,40)
            
    with ass.check("pacMan"):
        if ass.errors(): return
        fc(1,1,0)
        arc(100,100, 80,80, radians(-135),radians(135), PIE)
        
    # Termin 2        
        
    with ass.check("chessRow"):
        if ass.errors(): return
        for i in range(8):
            if i%2==0:
                fc(1)
            else:
                fc(0.5)
            rect(20+20*i,20, 20,20)
            
    with ass.check("chessBoard"):
        if ass.errors(): return
        for i in range(1,9):
            for j in range(1,9):
                if (i+j)%2 == 0:
                    fc(1)
                else:
                    fc(0.5)
                rect(20*i,20*j, 20,20)
        
    with ass.check("dices"):
        if ass.errors(): return
        fc(0)
        point(10,10)
        
        point(28,8)
        point(32,12)

        point(48,8)
        point(50,10)
        point(52,12)

        point(68,8)
        point(68,12)
        point(72,8)
        point(72,12)

        point(88,8)
        point(88,12)
        point(90,10)
        point(92,8)
        point(92,12)

        point(108,8)
        point(108,10)
        point(108,12)
        point(112,8)
        point(112,10)
        point(112,12)

    def dots(x,y,dots):
        for dot in dots:
            if dot==1: point(x+8,y+8)
            if dot==2: point(x+8,y+10)
            if dot==3: point(x+8,y+12)
            if dot==4: point(x+10,y+10)
            if dot==5: point(x+12,y+8)
            if dot==6: point(x+12,y+10)
            if dot==7: point(x+12,y+12)

    def dice(x,y,d):
        if d==1: dots(x,y,[4])
        if d==2: dots(x,y,[1,7])
        if d==3: dots(x,y,[1,4,7])
        if d==4: dots(x,y,[1,3,5,7])
        if d==5: dots(x,y,[1,3,4,5,7])
        if d==6: dots(x,y,[1,2,3,5,6,7])
            
    with ass.check("manyDices"):
        if ass.errors(): return
        fc(0)
        for i in range(10):
            for j in range(10):
                dice(20*i,20*j,1+(i+j)%6)
                
    with ass.check("skislope"):
        if ass.errors(): return
        bg(0)
        sc(1,0,0)
        for i in range(0,210,10):
            line(i,0,200,i)
            
    with ass.check("sunshine"):
        if ass.errors(): return
        bg(0)
        sc(1,1,0)
        for i in range(0,220,20):
            line(i,0,200-i,200)
            line(0,i,200,200-i)

    def urtavla():
        fc(0)
        sc(1)
        circle(0,0,90)
        fc(1)
        for i in range(60):
            if i%5==0: circle(85,0,2)
            else:      point(85,0)
            rd(6)
            
    def visare(v,w,l,r,g,b):
        with push():
            rd(v-90)
            translate(l/2,0)
            fc(r,g,b)
            rect(0,0,l,w)

    def klocka(h,m,s):
        rectMode(CENTER)            
        translate(100,100)
        urtavla()
        visare((h+m/60.0)*30, 7, 60, 1,0,0)
        visare((m+s/60.0)*6,  5, 80, 0,1,0)
        visare(s*6,           2, 80, 0,0,1)
    
    with ass.check("klocka"):
        if ass.errors(): return
        klocka(10,9,30)
        
    with ass.check("klockaB"):
        if ass.errors(): return
        klocka(11,30,15)
        
    def circles(x,y,r):
        circle(x,y,r)
        if r < 10: return
        circles(x-r/2,y,r/2)
        circles(x+r/2,y,r/2)
        
    with ass.check("recursiveCircles"):
        if ass.errors(): return
        sc(1)
        circles(100,100,100)                            

##########################################################
from Assert import Assert,fc,sc,sw,rd,circle,bg,push,col #
def setup():                                             #
    size(407,616)                                        #
    global ass                                           #
    ass = Assert()                                       #
def keyPressed(): ass.keyPressed()                       #
def mousePressed(): ass.mousePressed()                   #
def mouseMoved(): ass.mouseMoved()                       #
##########################################################    