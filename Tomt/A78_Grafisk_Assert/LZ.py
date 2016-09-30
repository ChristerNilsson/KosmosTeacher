from Assert import bg,fc,sc,sw,rd,circle,push,col

def lektionZ(ass):

    with ass.check("chessRow"):
        if ass.errors(): return

                        
    with ass.check("chessBoard"):
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
        rectMode(CENTER)

                        


                        
    with ass.check("manyDices"):
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
        
    with ass.check("hypnoticA"):
        if ass.errors(): return
        hypnoticA()

    
    with ass.check("hypnoticB_1"):
        if ass.errors(): return
        hypnoticB(1)
        
    with ass.check("hypnoticB_5"):
        if ass.errors(): return
        hypnoticB(5)