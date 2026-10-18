# exercice 3 : voyageur de commerce (8 villes)
# recuit simule + recherche tabou

import random
import math

# 999 = arete inexistante (les "-" du tableau)
INF = 999
d = [
    [0,   14,  15,  INF, INF, INF, INF, 17],
    [14,  0,   13,  14,  20,  INF, INF, 21],
    [15,  13,  0,   11,  21,  17,  9,   9],
    [INF, 14,  11,  0,   10,  8,   20,  5],
    [INF, 20,  21,  10,  0,   15,  18,  6],
    [INF, INF, 17,  8,   15,  0,   9,   7],
    [INF, INF, 9,   20,  18,  9,   0,   13],
    [17,  21,  9,   5,   6,   7,   13,  0]
]

def calc(s):
    r = 0
    for i in range(8):
        r += d[s[i]][s[(i+1)%8]]
    return r

def recuit():
    s = [0,1,2,3,4,5,6,7]
    bs = s[:]
    bc = calc(s)
    T = 100
    # 5 paliers de temperature
    for k in range(5):
        for it in range(50):
            i = random.randint(0,7)
            j = random.randint(0,7)
            while i == j:
                j = random.randint(0,7)
            ns = s[:]
            ns[i],ns[j] = ns[j],ns[i]
            delta = calc(ns) - calc(s)
            if delta <= 0:
                s = ns
            else:
                p = math.exp(-delta/T)
                if random.random() < p:
                    s = ns
            if calc(s) < bc:
                bc = calc(s)
                bs = s[:]
        T = T * 0.5
    return bs,bc

def tabou():
    s = [0,1,2,3,4,5,6,7]
    bs = s[:]
    bc = calc(s)
    tl = []
    for it in range(100):
        bm = None
        bv = 999999
        for i in range(8):
            for j in range(i+1,8):
                if (i,j) in tl:
                    continue
                ns = s[:]
                ns[i],ns[j] = ns[j],ns[i]
                v = calc(ns)
                if v < bv:
                    bv = v
                    bm = (ns,i,j)
        if bm is None:
            break
        s = bm[0]
        tl.append((bm[1],bm[2]))
        if len(tl) > 5:
            tl.pop(0)
        if calc(s) < bc:
            bc = calc(s)
            bs = s[:]
    return bs,bc

if __name__ == "__main__":
    print("=== recuit simule ===")
    b,c = recuit()
    print(b, c)
    print("=== tabou ===")
    b,c = tabou()
    print(b, c)

#Résultats typiques : les deux méthodes trouvent un coût autour de 86–95 (le meilleur cycle trouvé est [0,1,2,6,5,3,4,7] avec coût 86)