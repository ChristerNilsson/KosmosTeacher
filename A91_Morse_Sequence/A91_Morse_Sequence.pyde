def seq(sentence):
    res = ""
    for ch in list(sentence):
       if ch == "1": res += "1131313133"
       if ch == "3": res += "1111113133"
    return res

assert seq("1") =="1131313133"
assert seq("3")=="1111113133"
assert seq(seq("1")) == "1131313133113131313311111131331131313133111111313311313131331111113133113131313311111131331111113133"