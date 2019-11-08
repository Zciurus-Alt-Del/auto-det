import numpy as np
#"■8(1&2&3@4&5&6@7&8&9)"
s = str(input("Enter determinant in MS-Office-Format:\n"))

def form(raw):
    raw = raw[2:]
    while raw[-1:] == ")":  # evtl. klammern entfernen
        raw = raw[1:-1]

    m = raw.split("@")
    m = [x.split("&") for x in m]

    for row in range(len(m[0])):
        for col in range(len(m)):
            m[row][col] = int(m[row][col])

    return m

def det(raw):
    m = form(raw)

    m = np.array(m)
    D = np.linalg.det(m)

    return D

print("> ",det(s))
x=input()