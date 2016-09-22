from random import sample

ORIGKEYS = "aA iI lL oO 01 ,.'" + '"' + ":;[]{}()<>#%=+-*/" + BACKSPACE + TAB + ENTER 

class Exercise:
    def __init__(self):
        self.keys = ORIGKEYS[:]
        self.keys = self.keys.replace(" ","")
        self.index = len(self.keys)
        self.message = str(len(self.keys)) + " keys. Press space."
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
            textSize(32)
            text(ORIGKEYS[0:18],width/2,height/4)
            text(ORIGKEYS[18:36],width/2,height/3)
            text("Key:" + self.pretty(self.keys[self.index]),width/2,height/2)
            text(str(self.index) + " of " + str(len(self.keys)) + " keys",width/2,height - 40)
        else:
            textSize(20)
            text(self.message,width/2,height/2)
            
    def keyPressed(self):
        if key == 65535: return # AltGr, Shift    
        if key == " " and self.index == len(self.keys):
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
                    self.message = "You missed" + self.errors + " in " + str(millis()-self.start) + " ms"
        else:
            self.errors += self.pretty(self.keys[self.index])