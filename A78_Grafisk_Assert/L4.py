from Assert import fc,sc,sw,rd,circle,bg,push,col

def lektion4(ass):

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
        