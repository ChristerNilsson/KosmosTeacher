# String operations

assert "0707496800".startswith("0707") == True
assert "0707496800".startswith("073") == False

assert "0707496800".find("49") == 4
assert "0707496800".find("0") == 0
assert "0707496800".find("3") == -1

assert "0707496800"[:3] == "070"
assert "0707496800"[3:] == "7496800"

assert len("0707496800") == 10

assert "0707496800".replace("0","*") == "*7*74968**" 

###################

def L2():
    def f(s): 
        # Rensa bort allt utom sifforna
        if s.startswith("+46"): s = s.replace("+46","0")
        if s.startswith("0046"): s = s.replace("0046","0")
        if s.startswith("46"): s = s.replace("46","0")
        s = s.replace(" ","").replace("-","")
        # Lagg till bindestreck och blanktecken 
        p = 2 if s.startswith('08') else 4
        if s.find('-') == -1: s = s[0:p] + "-" + s[p:] 
        s = s[0:-4] + " " + s[-4:] 
        s = s[0:-2] + " " + s[-2:] 
        return s  

    assert f("0780-45 23 46") == "0780-45 23 46"
    assert f("0702561234") == "0702-56 12 34"
    assert f("0752024061") == "0752-02 40 61"
    assert f("46730652211") == "0730-65 22 11"
    assert f("0730-6545899") == "0730-654 58 99"
    assert f("+46 8 25 46 78") == "08-25 46 78"
    assert f("+46708 45 12 14") == "0708-45 12 14"
    assert f("0046708 45 12 14") == "0708-45 12 14"