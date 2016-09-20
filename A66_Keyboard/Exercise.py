from random import sample

KEYS = "[]{}()<>,.'#%=+-*/:" + '"' + BACKSPACE + TAB + ENTER 

class Exercise:
    def __init__(self):
        self.keys = KEYS
        self.index = 0
        self.message = "Press space!"
        self.errors = ""
        self.start = 0

    def pretty(self,ch):
        if ch==BACKSPACE: return " BACKSPACE"
        if ch==TAB: return " TAB"
        if ch==ENTER: return " ENTER"
        return " " + ch        

    def draw(self):
        background(204)
        if self.message=="":
            textSize(60)
            text(self.pretty(self.keys[self.index]),width/2,height/2)
        else:
            textSize(20)
            text(self.message,width/2,height/2)
            
    def keyPressed(self):
        if key == 65535: return # AltGr, Shift    
        if key == " ":
            self.message = ""
            self.keys = sample(self.keys,len(self.keys))
            self.index = 0
            self.start = millis()
            self.errors = ""
        elif key == self.keys[self.index]:
            self.index += 1
            if self.index == len(self.keys):
                if self.errors == "":
                    self.message = "You made no mistakes in " + str(millis()-self.start) + " ms"
                else:
                    self.message = "You missed " + self.errors + " in " + str(millis()-self.start) + " ms"
        else:
            self.errors += self.pretty(self.keys[self.index])