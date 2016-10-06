# y = kx+m

###################

def L2():

    def d(x): return 1
    assert d(0) == 1 
    assert d(1) == 1 
    assert d(2) == 1 

    def e(x): return 100
    assert e(0) == 100 
    assert e(1) == 100 
    assert e(2) == 100 

    def f(x): return x
    assert f(0) == 0 
    assert f(1) == 1 
    assert f(2) == 2 
    
    def g(x): return x+1
    assert g(0) == 1
    assert g(1) == 2
    
    def h(x): return 2*x
    assert h(0) == 0
    assert h(1) == 2
    assert h(2) == 4
    
    def i(x): return 2*x+1
    assert i(0) == 1
    assert i(1) == 3
    assert i(2) == 5
    
    def j(x): return 10*x
    assert j(0) == 0
    assert j(1) == 10
    assert j(2) == 20
    
    def k(x): return 20*x+10
    assert k(0) == 10
    assert k(1) == 30
    assert k(2) == 50
    
    def l(x): return 11*x+11
    assert l(0) == 11
    assert l(1) == 22
    assert l(2) == 33
    
    def m(x): return x/2.0
    assert m(0) == 0
    assert m(1) == 0.5
    assert m(2) == 1
    
    def n(x): return 200 - 100*x
    assert n(0) == 200
    assert n(1) == 100
    assert n(2) == 0

    def o(x): return 200 - 20*x
    assert o(0) == 200
    assert o(1) == 180
    assert o(2) == 160