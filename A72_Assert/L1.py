# Fem matematiska operatorer

assert 1 + 2 == 3
assert 3 - 2 == 1
assert 3 * 2 == 6
assert 12 / 3 == 4 

assert 6 % 3 == 0 
assert 7 % 3 == 1 
assert 8 % 3 == 2

###################

def L1():

    def f(x): return 00 # Byt 00 mot det korrekta! 
    assert f(2) == 2 # heliga assert-rader!
    assert f(3) == 3 # heliga assert-rader!
    
    def g(x): return 00
    assert g(-4) == 4
    assert g(4) == -4
    
    def h(x): return 00
    assert h(7) == 8
    assert h(8) == 9
    
    def i(x): return 00
    assert i(5) == 10
    assert i(6) == 12
    
    def j(x): return 00
    assert j(5) == 25
    assert j(6) == 36
    
    def k(x): return 00
    assert k(7) == 5
    assert k(17) == 15
    
    def l(x): return 00
    assert l(8) == 4
    assert l(6) == 3
    
    def m(x): return 00
    assert m(8) == 0
    assert m(9) == 1
    assert m(10) == 0
    assert m(11) == 1
    
    def n(x,y): return 00
    assert n(3,4) == 12
    assert n(4,6) == 24
    
    def o(x,y): return 00
    assert o(3,4) == 7
    assert o(4,6) == 10
    
    def p(x,y): return 00
    assert p(3,4) == 1
    assert p(4,6) == 2
    
    def q(x,y): return 00
    assert q(8,4) == 2
    assert q(12,3) == 4
    
    # Skriv in hela raden som saknas!
    assert r(8,4) == 0
    assert r(9,4) == 1
    assert r(10,4) == 2
    assert r(11,4) == 3
    