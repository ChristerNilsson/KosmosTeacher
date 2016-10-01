from Assert import bg,fc,sc,sw,rd,circle,push,col

def lektionZ(ass):

    with ass.check("chessRow"):
        if ass.errors(): return
        bg(0.5)
        for i in range(8):
            fc(i%2)
            rect(20+20*i,20, 20,20)
            
    with ass.check("chessBoard"):
        if ass.errors(): return
        bg(0.5)
        for i in range(1,9):
            for j in range(1,9):
                fc((i+j)%2)
                rect(20*i,20*j, 20,20)
        
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
        
    def hypnoticA():
        bg(0.5, 0, 0)
        noStroke()
        fc(1)
        for i in range(100):
            x = 100 + cos(i) * i
            y = 100 + sin(i) * i
            circle(x, y, 5)
    
    with ass.check("hypnoticA"):
        if ass.errors(): return
        hypnoticA()

    def hypnoticB(t):
        bg(0.5, 0, 0)
        noStroke()
        fc(1)
        for i in range(100):
            x = 100 + cos(i) * i
            y = 100 + sin(i) * i
            speed = i/10.0
            r = map(sin(t*speed), -1, 1, 2, 5)
            circle(x, y, r)
    
    with ass.check("hypnoticB_1"):
        if ass.errors(): return
        hypnoticB(1)
        
    with ass.check("hypnoticB_5"):
        if ass.errors(): return
        hypnoticB(5)