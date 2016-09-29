from Assert import fc,sc,sw,rd,circle,bg,push,col

def lektion6(ass):

    with ass.check("whiteTriangle"):
        if ass.errors(): return
        fc(1)
        triangle(20,40, 160,100, 100,140)
        
    with ass.check("yellowQuad"):
        if ass.errors(): return
        fc(1,1,0)
        quad(150,100, 180,20, 40,20, 100,140)
        
    with ass.check("pacMan"):
        if ass.errors(): return
        fc(1,1,0)
        arc(100,100, 80,80, radians(-135),radians(135), PIE)
        