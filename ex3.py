# Exercice 3 : Voyageur de commerce (TSP) - 8 villes
# Question 1 : Recherche Tabou (solution initiale : 1-2-3-4-5-6-7-8-1)
# Question 2 : Recuit Simule (5 iterations, variation empirique de T)

import random
import math

n = 8  # nombre de villes

# matrice des distances (999 = pas de lien direct)
INF = 999
dist = [
    #  1    2    3    4    5    6    7    8
    [0,   14,  15,  INF, INF, INF, INF, 17],   # ville 1
    [14,  0,   13,  14,  20,  INF, INF, 21],   # ville 2
    [15,  13,  0,   11,  21,  17,  9,   9],    # ville 3
    [INF, 14,  11,  0,   11,  10,  8,   20],   # ville 4
    [INF, 20,  21,  11,  0,   15,  18,  INF],  # ville 5
    [INF, INF, 17,  10,  15,  0,   9,   INF],  # ville 6
    [INF, INF, 9,   8,   18,  9,   0,   13],   # ville 7
    [17,  21,  9,   20,  INF, INF, 13,  0]     # ville 8
]


def cout_trajet(s):
    """cout total du circuit"""
    c = 0
    for i in range(n):
        c += dist[s[i]][s[(i+1) % n]]
    return c



# QUESTION 1 : Recherche Tabou
# Solution initiale : 1-2-3-4-5-6-7-8-1 (indices 0..7)


def recherche_tabou(max_iter=100, taille_tabou=5):
    # solution initiale comme demande dans l'enonce
    s = list(range(n))  # [0,1,2,3,4,5,6,7]
    best = s[:]
    best_cout = cout_trajet(s)
    liste_tabou = []
    k = 0

    print("Solution initiale : {}  cout = {}".format(
        [x+1 for x in s], cout_trajet(s)))

    while k < max_iter:
        k += 1
        # explorer tous les voisins (echange de 2 villes)
        meilleur_voisin = None
        meilleur_cout = float('inf')

        for i in range(n):
            for j in range(i+1, n):
                if (i, j) in liste_tabou:
                    continue
                # generer voisin par permutation
                ns = s[:]
                ns[i], ns[j] = ns[j], ns[i]
                c = cout_trajet(ns)
                if c < meilleur_cout:
                    meilleur_cout = c
                    meilleur_voisin = (ns, i, j)

        if meilleur_voisin is None:
            break

        # mettre a jour s
        s = meilleur_voisin[0]

        # ajouter le mouvement a la liste tabou
        liste_tabou.append((meilleur_voisin[1], meilleur_voisin[2]))
        if len(liste_tabou) > taille_tabou:
            liste_tabou.pop(0)

        # actualiser la meilleure solution
        if meilleur_cout < best_cout:
            best_cout = meilleur_cout
            best = s[:]

    return best, best_cout


# QUESTION 2 : Recuit Simule
# 5 paliers de temperature, variation empirique de T

def recuit_simule(T0=100, nb_paliers=5, iter_par_palier=50, alpha=0.5):
    # solution initiale aleatoire
    s = list(range(n))
    random.shuffle(s)
    best = s[:]
    best_cout = cout_trajet(s)
    T = T0

    print("Solution initiale : {}  cout = {}".format(
        [x+1 for x in s], cout_trajet(s)))

    for k in range(nb_paliers):
        for it in range(iter_par_palier):
            # generer un voisin (echange de 2 positions)
            i = random.randint(0, n-1)
            j = random.randint(0, n-1)
            while i == j:
                j = random.randint(0, n-1)

            ns = s[:]
            ns[i], ns[j] = ns[j], ns[i]

            # delta f
            delta = cout_trajet(ns) - cout_trajet(s)

            if delta <= 0:
                # amelioration -> on accepte
                s = ns
            else:
                # on accepte avec probabilite p = exp(-delta/T)
                p = math.exp(-delta / T)
                beta = random.random()
                if p > beta:
                    s = ns

            # maj meilleure solution
            if cout_trajet(s) < best_cout:
                best_cout = cout_trajet(s)
                best = s[:]

        # variation empirique de T (refroidissement geometrique)
        T = T * alpha

    return best, best_cout


if __name__ == "__main__":
    print("=" * 50)
    print("Exercice 3 : TSP - 8 villes")
    print("=" * 50)

    print()
    print("--- Question 1 : Recherche Tabou ---")
    sol_t, cout_t = recherche_tabou()
    print("Meilleure solution : {}".format([x+1 for x in sol_t]))
    print("Cout : {}".format(cout_t))

    print()
    print("--- Question 2 : Recuit Simule ---")
    sol_r, cout_r = recuit_simule()
    print("Meilleure solution : {}".format([x+1 for x in sol_r]))
    print("Cout : {}".format(cout_r))
