##########################################################
from Assert import Assert                                #
def setup():                                             #
    #noSmooth()                                          #
    size(407,616)                                        #
    global ass                                           #
    ass = Assert()                                       #
def keyPressed(): ass.keyPressed()                       #
def mousePressed(): ass.mousePressed()                   #
def mouseMoved(): ass.mouseMoved()                       #
##########################################################
    
from L1 import lektion1
from L2 import lektion2
from L3 import lektion3
from L4 import lektion4
from L5 import lektion5
from L6 import lektion6
from LZ import lektionZ
        
def draw():
    
    lektion1(ass)
    #lektion2(ass)
    #lektion3(ass)
    #lektion4(ass)
    #lektion5(ass)
    #lektion6(ass)
    #lektionZ(ass)