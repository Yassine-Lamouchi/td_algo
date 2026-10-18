# exercice 2 : probleme de transport avec recherche tabou
# 2 depots, 3 magasins

import random

# couts de transport
C = [[5,3,4],[6,7,2]]
# capacites des depots
S = [8,9]
# demandes des magasins
D = [4,5,8]

def cout(x):
    r = 0
    for i in range(2):
        for j in range(3):
            r += C[i][j]*x[i][j]
    return r

def init():
    # glouton : on remplit par cout croissant
    x = [[0,0,0],[0,0,0]]
    s = S[:]
    d = D[:]
    cellules = [(C[i][j],i,j) for i in range(2) for j in range(3)]
    cellules.sort()
    for c,i,j in cellules:
        q = min(s[i],d[j])
        x[i][j] = q
        s[i] -= q
        d[j] -= q
    return x

def voisins(x):
    # mouvements 2x2 : on deplace 1 unite d'une colonne a une autre
    v = []
    for j1 in range(3):
        for j2 in range(3):
            if j1 != j2 and x[0][j1] > 0 and x[1][j2] > 0:
                y = [x[0][:], x[1][:]]
                y[0][j1] -= 1
                y[0][j2] += 1
                y[1][j2] -= 1
                y[1][j1] += 1
                v.append((y,j1,j2))
    return v

def tabou():
    x = init()
    best = [x[0][:], x[1][:]]
    bc = cout(x)
    tl = []
    for it in range(50):
        vs = voisins(x)
        if not vs:
            break
        bm = None
        bv = 999999
        for y,j1,j2 in vs:
            if (j1,j2) in tl:
                continue
            c = cout(y)
            if c < bv:
                bv = c
                bm = (y,j1,j2)
        if bm is None:
            bm = vs[0]
        x = bm[0]
        tl.append((bm[2],bm[1]))  # on interdit le retour
        if len(tl) > 3:
            tl.pop(0)
        if cout(x) < bc:
            bc = cout(x)
            best = [x[0][:], x[1][:]]
    return best, bc

if __name__ == "__main__":
    x0 = init()
    print("solution initiale :", x0)
    print("cout initial :", cout(x0))
    b,c = tabou()
    print("meilleure solution :", b)
    print("cout final :", c)

#Résultat obtenu : [[3,5,0],[1,0,8]] avec coût 52 (c'est l'optimum)