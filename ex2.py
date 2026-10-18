# Exercice 2 : probleme de transport - recherche tabou
# 2 depots (D1, D2), 3 magasins (M1, M2, M3)

import random

# cout de transport depot i -> magasin j
cout_transport = [
    [5, 3, 4],   # D1
    [6, 7, 2]    # D2
]

# capacites des depots
capacite = [8, 9]

# demandes des magasins
demande = [4, 5, 8]

nb_depots = 2
nb_magasins = 3


def calculer_cout(x):
    """calcul du cout total"""
    total = 0
    for i in range(nb_depots):
        for j in range(nb_magasins):
            total += cout_transport[i][j] * x[i][j]
    return total


def verifier_contraintes(x):
    """verifie si la solution respecte les contraintes"""
    # contrainte capacite
    for i in range(nb_depots):
        if sum(x[i]) > capacite[i]:
            return False
    # contrainte demande
    for j in range(nb_magasins):
        s = sum(x[i][j] for i in range(nb_depots))
        if s != demande[j]:
            return False
    return True


def solution_initiale():
    """solution gloutonne : remplir par cout croissant"""
    x = [[0]*nb_magasins for _ in range(nb_depots)]
    cap = capacite[:]
    dem = demande[:]
    # trier les cellules par cout croissant
    cellules = []
    for i in range(nb_depots):
        for j in range(nb_magasins):
            cellules.append((cout_transport[i][j], i, j))
    cellules.sort()
    for c, i, j in cellules:
        q = min(cap[i], dem[j])
        x[i][j] = q
        cap[i] -= q
        dem[j] -= q
    return x


def generer_voisins(x):
    """voisinage par mouvement 2x2 : deplacer 1 unite"""
    voisins = []
    for j1 in range(nb_magasins):
        for j2 in range(nb_magasins):
            if j1 == j2:
                continue
            # on deplace 1 unite : D1[j1] -> D1[j2] et D2[j2] -> D2[j1]
            if x[0][j1] > 0 and x[1][j2] > 0:
                y = [x[0][:], x[1][:]]
                y[0][j1] -= 1
                y[0][j2] += 1
                y[1][j2] -= 1
                y[1][j1] += 1
                # verifier capacites
                if sum(y[0]) <= capacite[0] and sum(y[1]) <= capacite[1]:
                    voisins.append((y, j1, j2))
    return voisins


def recherche_tabou(max_iter=50, taille_tabou=3):
    """recherche tabou pour le probleme de transport"""
    # s_init <- Glouton(Pb)
    s = solution_initiale()
    # s* <- s_init
    best = [s[0][:], s[1][:]]
    best_cout = calculer_cout(s)
    # liste tabou
    liste_tabou = []
    k = 0

    print("Solution initiale (glouton) :", s)
    print("Cout initial :", calculer_cout(s))
    print()

    # boucle principale
    while k < max_iter:
        k += 1
        vs = generer_voisins(s)
        if not vs:
            break

        # chercher le meilleur voisin non tabou
        meilleur = None
        meilleur_cout = float('inf')

        for y, j1, j2 in vs:
            # verifier si le mouvement est tabou
            if (j1, j2) in liste_tabou:
                continue
            c = calculer_cout(y)
            if c < meilleur_cout:
                meilleur_cout = c
                meilleur = (y, j1, j2)

        # si tous les voisins sont tabous, on prend le premier
        if meilleur is None:
            meilleur = (vs[0][0], vs[0][1], vs[0][2])
            meilleur_cout = calculer_cout(vs[0][0])

        # s <- s'
        s = meilleur[0]

        # ajouter le mouvement inverse a la liste tabou
        liste_tabou.append((meilleur[2], meilleur[1]))
        if len(liste_tabou) > taille_tabou:
            liste_tabou.pop(0)

        # si s' est meilleur que s* alors s* <- s'
        if meilleur_cout < best_cout:
            best_cout = meilleur_cout
            best = [s[0][:], s[1][:]]

    return best, best_cout


if __name__ == "__main__":
    print("=" * 40)
    print("Exercice 2 : Probleme de transport")
    print("Methode : Recherche Tabou")
    print("=" * 40)
    print()

    sol, c = recherche_tabou()

    print()
    print("Meilleure solution trouvee :")
    print("  D1 -> M1={}, M2={}, M3={}".format(sol[0][0], sol[0][1], sol[0][2]))
    print("  D2 -> M1={}, M2={}, M3={}".format(sol[1][0], sol[1][1], sol[1][2]))
    print("Cout total :", c)
