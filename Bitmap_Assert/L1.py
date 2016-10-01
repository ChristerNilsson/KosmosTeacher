from Assert import fc,sc,sw,rd,circle,bg,push,col

def lektion1(ass):
    
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
    