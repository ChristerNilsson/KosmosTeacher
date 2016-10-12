# range, comprehensions

def L5():
    
    assert range(4) == [0,1,2,3]
    assert range(10,15) == [10,11,12,13,14]
    assert range(0,50,10) == [0,10,20,30,40]
    assert range(50,0,-10) == [50,40,30,20,10]

    def f(): return range(1,5)
    assert f() == [1,2,3,4] 
    
    def g(): return range(10,30,5)
    assert g() == [10,15,20,25]     

    def h(): return range(25,5,-5)
    assert h() == [25,20,15,10]
         
    def i(): return range(-25,-5,5)
    assert i() == [-25,-20,-15,-10]     

    def j(): return range(-10,-30,-5)
    assert j() == [-10,-15,-20,-25]   
    
    assert [x   for x in range(10)] == [0,1,2,3,4,5,6,7,8,9]        
    assert [x+1 for x in range(10)] == [1,2,3,4,5,6,7,8,9,10]        
    assert [2*x for x in range(10)] == [0,2,4,6,8,10,12,14,16,18]        
    assert [x*x for x in range(10)] == [0,1,4,9,16,25,36,49,64,81]  

    def k(): return [-x for x in range(5)]       
    assert k() == [0,-1,-2,-3,-4]
    
    def l(): return [2*x+1 for x in range(5)]       
    assert l() == [1,3,5,7,9]    
    
    def m(): return [x*x*x for x in range(5)]       
    assert m() == [0,1,8,27,64]        
    
    def n(q): return [x*x + x for x in range(q)]       
    assert n(3) == [0,2,6]        
    assert n(5) == [0,2,6,12,20]            