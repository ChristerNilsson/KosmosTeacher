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
        bg (1,0,0)
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
        line(10,70,190,70)
        
    with ass.check("verticalLine"): 
        if ass.errors(): return
        sc(1,1,0)
        sw(10)
        line(110,30,110,170)
    
        
    with ass.check("yellowLine"): 
        if ass.errors(): return
        sc(1,1,0)
        line(20,30,140,160)

    with ass.check("whiteCircle"): 
        if ass.errors(): return
        fc(1)
        circle(60,80,30)

    with ass.check("whiteEmptyCircle"): 
        if ass.errors(): return
        fc()
        sw(2)
        circle(70,90,40)
    with ass.check("greenEllipse"): 
        if ass.errors(): return
        fc(0,1,0)
        ellipse(120,60,60,40)
        

    with ass.check("greenRect"): 
        if ass.errors(): return
        fc(0,1,0)
        rect(60,80,40,50)

    with ass.check("redRect"):
        if ass.errors(): return
        fc(1,0,0)
        rect(80,70,40,100)

    with ass.check("whiteTriangle"):
        if ass.errors(): return
        fc(1)
        triangle(20,40,160,100,100,140)
        
    with ass.check("yellowQuad"):
        if ass.errors(): return
        fc(1,1,0)
        quad(100,140,40,20,180,20,150,100)
    with ass.check("rotatedRectA"):
        if ass.errors(): return
        
    with ass.check("rotatedRectB"):
        if ass.errors(): return
    
    with ass.check("rotatedRectC"):
        if ass.errors(): return
            
    with ass.check("rotatedEllipse"):
        if ass.errors(): return

    with ass.check("twoDiscsA"):
        if ass.errors(): return

    with ass.check("twoDiscsB"):
        if ass.errors(): return
        
    with ass.check("twoDiscsC"):
        if ass.errors(): return
        
    with ass.check("twoDiscsD"):
        if ass.errors(): return

    with ass.check("twoDiscsE"):
        if ass.errors(): return

    with ass.check("twoDiscsF"):
        if ass.errors(): return
        
    with ass.check("twoDiscsG"):
        if ass.errors(): return

    with ass.check("twoDiscsH"):
        if ass.errors(): return

    with ass.check("cross"):
        if ass.errors(): return
                    
    with ass.check("textPythonA"):
        if ass.errors(): return
        
    with ass.check("textPythonB"):
        if ass.errors(): return
        
    with ass.check("textPythonC"):
        if ass.errors(): return
        
    with ass.check("textPythonD"):
        if ass.errors(): return

    with ass.check("pacMan"):
        if ass.errors(): return
        
    with ass.check("squareHole"):
        if ass.errors(): return
        
    # Termin 2        
        
    with ass.check("chessRow"):
        if ass.errors(): return
            
    with ass.check("chessBoard"):
        if ass.errors(): return
        
    with ass.check("dices"):
        if ass.errors(): return
            
    with ass.check("manyDices"):
        if ass.errors(): return
                
    with ass.check("skislope"):
        if ass.errors(): return
            
    with ass.check("sunshine"):
        if ass.errors(): return
    
    with ass.check("klocka"):
        if ass.errors(): return
        #klocka(10,9,30)
        
    with ass.check("klockaB"):
        if ass.errors(): return
        #klocka(11,30,15)
        
    with ass.check("recursiveCircles"):
        if ass.errors(): return

########################################################
from Assert import Assert,fc,sc,sw,rd,circle,bg        #
def setup():                                           #
    size(207,4*180-40)                                 #
    global ass                                         #
    ass = Assert()                                     #
def keyPressed(): ass.keyPressed()                     #
def mousePressed(): ass.mousePressed()                 #
########################################################    