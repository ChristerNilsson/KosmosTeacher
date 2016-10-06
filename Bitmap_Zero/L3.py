from Assert import fc,sc,sw,rd,circle,bg,push,col

def lektion3(ass):


    with ass.check("horizontalLine"): 
        if ass.errors(): return


    with ass.check("verticalLine"): 
        if ass.errors(): return


    with ass.check("yellowLine"): 
        if ass.errors(): return


    with ass.check("skislope"):
        if ass.errors(): return


    with ass.check("sunshine"):
        if ass.errors(): return
