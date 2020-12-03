from random import randint

def ordena(v):
    if len(v) < 2:
        return v
    l, p, h = [ ], [ ], [ ]
    ch = v[randint(0, len(v) - 1)]
    for x in v:
        if x < ch:
            l.append(x)
        elif x == ch:
            p.append(x)
        elif x > ch:
            h.append(x)
    return ordena(l) + p + ordena(h)

v = [1,2,3,4,5,667,67,78,89,90,0,56,76,78]
ordena(v)
print(ordena(v))