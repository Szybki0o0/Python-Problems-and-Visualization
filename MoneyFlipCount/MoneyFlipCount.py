import random

APPEARANCE = 6
tab = []

def flip():
    result = random.randint(0,1)
    if result == 0:
        return "O"
    else:
        return "R"

for i in range(100):
    tab.append(flip())

def count(tab):
    c = 0
    C = 0
    prev = ""
    for i in tab:
        if i == prev:
            c += 1
        else:
            c = 0
            c += 1
            prev = i
        if c == APPEARANCE:
            C += 1
    return C

print(count(tab))