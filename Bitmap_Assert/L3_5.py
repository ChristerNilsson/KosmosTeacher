from Assert import fc,sc,sw,rd,circle,bg,push,col

# for loops

def lektion3_5(ass):
    
    with ass.check("for01"): 
        if ass.errors(): return
        for i in range(10):
            rect(5+20*i,5, 10,10)
            
    with ass.check("for02"): 
        if ass.errors(): return
        for i in range(10):
            rect(5,5+20*i, 10,10)
            
    with ass.check("for03"): 
        if ass.errors(): return
        for i in range(10):
            rect(5+20*i,5+20*i, 10,10)
            
    with ass.check("for04"): 
        if ass.errors(): return
        for i in range(10):
            for j in range(10):
                rect(5+20*i,5+20*j, 10,10)
                          
    with ass.check("for05"): 
        if ass.errors(): return
        rectMode(CENTER)
        for i in range(10):
            rect(10+20*i,10, 2*i,2*i)

    with ass.check("for06"): 
        if ass.errors(): return
        rectMode(CENTER)
        for i in range(10):
            fc(i/10.0,0,0)
            rect(10+20*i,10, 2*i,2*i)

    with ass.check("for07"): 
        if ass.errors(): return
        for i in range(10):
            fc(i/10.0,0,0)
            circle(10+20*i,10, i)
            
    with ass.check("for08"): 
        if ass.errors(): return
        for i in range(10,0,-1):
            fc(i/10.0,0,0)
            circle(100,100, 10*i)
            
    with ass.check("for09"): 
        if ass.errors(): return
        for i in range(10,0,-1):
            fc(i/10.0,0,0)
            circle(10*i,10*i, 10*i)
            
    with ass.check("for10"): 
        if ass.errors(): return
        for i in range(10):
            for j in range(10):
                fc(i/10.0,j/10.0,0)
                circle(10+20*i,10+20*j, (i+j)/2)
                
    with ass.check("for11"): 
        if ass.errors(): return
        rectMode(CENTER)
        sc()
        for i in range(10):
            for j in range(10):
                with push():
                    translate(10+20*i,10+20*j)
                    rd(5*(i+j))
                    fc(i/9.0,j/9.0,0)
                    rect(0,0, 10,10)
                
                        