########################################################
def draw():                                            #
########################################################

    with ass.check("whiteBackground"): 
        if ass.errors(): return
        
        
    with ass.check("grayBackground"): 
        if ass.errors(): return
        
        
    with ass.check("redBackground"): 
        if ass.errors(): return
        
        
    with ass.check("greenBackground"): 
        if ass.errors(): return

                
    with ass.check("yellowBackground"): 
        if ass.errors(): return

                
    with ass.check("point"): 
        if ass.errors(): return


    with ass.check("redPoint"): 
        if ass.errors(): return


    with ass.check("greenPoint"): 
        if ass.errors(): return

                
    with ass.check("horizontalLine"): 
        if ass.errors(): return


    with ass.check("verticalLine"): 
        if ass.errors(): return

                
    with ass.check("yellowLine"): 
        if ass.errors(): return


    with ass.check("whiteCircle"): 
        if ass.errors(): return


    with ass.check("whiteEmptyCircle"): 
        if ass.errors(): return

                
    with ass.check("greenEllipse"): 
        if ass.errors(): return


    with ass.check("greenRect"): 
        if ass.errors(): return


    with ass.check("redRect"):
        if ass.errors(): return


    with ass.check("whiteTriangle"):
        if ass.errors(): return

                
    with ass.check("yellowQuad"):
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

                                        
    with ass.check("squareHole"):
        if ass.errors(): return
                
        
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

                
    with ass.check("textPythonB"):
        if ass.errors(): return

                
    with ass.check("textPythonC"):
        if ass.errors(): return


                
    with ass.check("textPythonD"):
        if ass.errors(): return


    with ass.check("rotatedEllipse"):
        if ass.errors(): return


    with ass.check("rotatedRectA"):
        if ass.errors(): return

                
    with ass.check("rotatedRectB"):
        if ass.errors(): return

    
    with ass.check("rotatedRectC"):
        if ass.errors(): return

                        
    with ass.check("pacMan"):
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
        klocka(10,9,30)
        
    with ass.check("klockaB"):
        if ass.errors(): return
        klocka(11,30,15)
        

    with ass.check("recursiveCircles"):
        if ass.errors(): return
        sc(1)
        circles(100,100,100)                            

##########################################################
from Assert import Assert,fc,sc,sw,rd,circle,bg,push,col #
def setup():                                             #
    size(207,680)                                        #
    global ass                                           #
    ass = Assert()                                       #
def keyPressed(): ass.keyPressed()                       #
def mousePressed(): ass.mousePressed()                   #
##########################################################    