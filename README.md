# Travaux Dirigés & Rendu - Optimisation

**Yassine Lamouchi** — Groupe LSI3 2.1

---

## Structure des fichiers

```
├── ex2.py          # Exercice 2 : Problème de transport (Recherche Tabou)
├── ex3.py          # Exercice 3 : TSP 8 villes (Recuit Simulé + Tabou)
└── README.md       # Ce fichier
```

---

## Exercice 2 : Problème de transport

### Enoncé

Une entreprise dispose de 2 dépôts (D1, D2) contenant respectivement 8 et 9 containers.
3 magasins (M1, M2, M3) commandent respectivement 4, 5 et 8 containers.

**Coûts de transport :**

|      | M1 | M2 | M3 | Capacité |
|------|----|----|----|----------|
| D1   | 5  | 3  | 4  | 8        |
| D2   | 6  | 7  | 2  | 9        |
| Dem. | 4  | 5  | 8  |          |

### Méthode

- **Recherche Tabou** avec solution initiale gloutonne (remplissage par coût croissant)
- Voisinage par mouvement 2×2 (déplacement d'1 conteneur entre colonnes)
- Liste tabou de taille 3, 50 itérations max

### Résultat

```
Solution : D1 -> M1=3, M2=5, M3=0
           D2 -> M1=1, M2=0, M3=8
Coût total : 52
```

---

## Exercice 3 : Voyageur de commerce (TSP - 8 villes)

### Enoncé

Problème du voyageur de commerce avec 8 villes. Les distances manquantes (`-` dans le tableau) sont considérées comme très grandes (999).

### Question 1 : Recherche Tabou

- Solution initiale : 1-2-3-4-5-6-7-8-1 (comme demandé dans l'énoncé)
- Voisinage par échange de 2 villes
- Liste tabou de taille 5, 100 itérations

### Question 2 : Recuit Simulé

- 5 paliers de température (T0 = 100)
- Variation empirique de T : refroidissement géométrique (α = 0.5)
- 50 itérations par palier
- Acceptation probabiliste : p = exp(-Δf / T)

### Résultats typiques

Les deux méthodes convergent vers un coût autour de **98**.

---

## Exécution

```bash
python ex2.py
python ex3.py
```

> **Note :** Le recuit simulé est stochastique, les résultats peuvent varier légèrement à chaque exécution.
