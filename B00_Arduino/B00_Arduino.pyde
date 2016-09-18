add_library('arduino')

a = Arduino(this, "COM22", 57600)

def draw():
    a.digitalWrite(13,1)
    delay(500)
    a.digitalWrite(13,0)
    delay(500)