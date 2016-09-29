from Assert import fc,sc,sw,rd,circle,bg,push,col

def lektion5(ass):

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
                