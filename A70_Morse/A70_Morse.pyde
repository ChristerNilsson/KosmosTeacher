unit = 500 # millisekunder

onoff = "111113313133111117" # sos = "...---..."
index = 0
stopp = 0

def draw():
    
    global index,stopp
    if millis()/unit < stopp: 
        return

    siffra = onoff[index]
    tal = int(siffra)

    stopp = millis()/unit + tal

    if index % 2 == 0: 
        fill(255) # on
    else:              
        fill(0) # off

    ellipse(50,50,50,50)

    index = index + 1
    index = index % len(onoff)