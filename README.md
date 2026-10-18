# TP Optimisation - LSI3 2.1

**Yassine Lamouchi** - Groupe LSI3 2.1

## Fichiers

- `ex2.py` : Exercice 2 (problème de transport + recherche tabou)
- `ex3.py` : Exercice 3 (TSP 8 villes + recuit simulé et tabou)

## Exercice 2

Problème de transport avec 2 dépôts et 3 magasins.

|      | M1 | M2 | M3 | Capacité |
|------|----|----|----|----------|
| D1   | 5  | 3  | 4  | 8        |
| D2   | 6  | 7  | 2  | 9        |
| Dem. | 4  | 5  | 8  |          |

J'ai utilisé la recherche tabou avec des mouvements 2×2 (déplacer 1 conteneur d'une colonne à une autre).  
Solution trouvée : `[[3,5,0],[1,0,8]]` avec coût **52**.

## Exercice 3

TSP avec 8 villes. Les distances manquantes (les `-` du tableau) sont mises à 999.

**Recuit simulé** : 5 paliers de température (T0 = 100, division par 2 à chaque palier), 50 itérations par palier.

**Tabou** : 100 itérations, liste tabou de taille 5, voisinage par échange de deux villes.

Les deux méthodes trouvent des solutions avec un coût entre **86 et 95**.

## Lancer

```bash
python ex2.py
python ex3.py