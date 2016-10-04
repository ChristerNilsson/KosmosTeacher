from Assert import fc,sc,sw,rd,circle,bg,push,col

# for loops

def lektion3_5(ass):
    
    with ass.check("for01"): 
        if ass.errors(): return
        for i in range(10):
            x = 5+20*i
            rect(x,5, 10,10)
            
    with ass.check("for02"): 
        if ass.errors(): return
        for i in range(10):
            y = 5+20*i
            rect(5,y, 10,10)
            
    with ass.check("for03"): 
        if ass.errors(): return
        for i in range(10):
            x = 5+20*i
            y = 5+20*i
            rect(x,y, 10,10)
            
    with ass.check("for04"): 
        if ass.errors(): return
        for i in range(10):
            for j in range(10):
                x = 5+20*i
                y = 5+20*j
                rect(x,y, 10,10)
                          
    with ass.check("for05"): 
        if ass.errors(): return
        rectMode(CENTER)
        for i in range(10):
            x = 10+20*i
            y = 10
            w = 2*i
            h = 2*i
            rect(x,y, w,h)

    with ass.check("for06"): 
        if ass.errors(): return
        rectMode(CENTER)
        for i in range(10):
            fc(i/10.0,0,0)
            x = 10+20*i
            y = 10
            w = 2*i
            h = 2*i
            rect(x,y,w,h)

    with ass.check("for07"): 
        if ass.errors(): return
        for i in range(10):
            fc(i/10.0,0,0)
            x = 10+20*i
            y = 10
            r = i
            circle(x,y,r)
            
    with ass.check("for08"): 
        if ass.errors(): return
        for i in range(10,0,-1):
            fc(i/10.0,0,0)
            r = 10 * i
            circle(100,100, r)
            
    with ass.check("for09"): 
        if ass.errors(): return
        for i in range(10,0,-1):
            fc(i/10.0,0,0)
            x = 10*i
            y = 10*i
            r = 10*i
            circle(x,y,r)
            
    with ass.check("for10"): 
        if ass.errors(): return
        for i in range(10):
            for j in range(10):
                fc(i/10.0,j/10.0,0)
                x = 10+20*i
                y = 10+20*j
                r = (i+j)/2
                circle(x,y,r)
                
    with ass.check("for11"): 
        if ass.errors(): return
        rectMode(CENTER)
        sc()
        for i in range(10):
            for j in range(10):
                with push():
                    translate(10+20*i,10+20*j)
                    rd(5*(i+j))
                    r = i/9.0
                    g = j/9.0
                    b = 0 
                    fc(r,g,b)
                    rect(0,0, 10,10)
                
    with ass.check("for12"): 
        if ass.errors(): return
        rectMode(CENTER)
        sc(1)
        translate(100,100)
        for i in range(18,-1,-1):
            r = 1.0*i/18
            fc(r,0,0)
            w = 70+5*i
            h = 70+5*i
            rect(0,0, w,h)
            rd(5)
        
                                                