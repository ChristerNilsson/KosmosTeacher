# Graphic operations

squares = []
assert len(squares) == 0
squares.append([100,100,10])
assert len(squares) == 1
assert len(squares[0]) == 3
assert dist(0,0,5,0) == 5
assert dist(0,0,0,5) == 5
assert dist(1,0,1,5) == 5
assert dist(0,0,3,4) == 5

#===================================

def L3():
    circles = []                 ###
    circles.append([100,100,50]) ###
    circles.append([150,150,50]) ###
    
    def g(xm,ym,circles):
        res = []
        for circle in circles:
            x,y,r = circle
            if dist(xm,ym,x,y) <= r:
                res.append(circle) 
        return res

    def f(xm,ym,circles):
        return [[x,y,r] for x,y,r in circles if dist(xm,ym,x,y) <= r]

    assert f(0,0,circles) == []
    assert f(110,110,circles) == [[100,100,50]]
    assert f(125,125,circles) == [[100,100,50], [150,150,50]]
    assert f(140,140,circles) == [[150,150,50]]