# Dictionnaire des données

## `data/prix_nettoyes_2019_2026.csv.gz`

| Colonne | Description |
|---|---|
| `date` | Mois du relevé (le 15 du mois, convention du PAM) |
| `pays` | Bénin, Togo, Niger, Sénégal |
| `region` | Département (Bénin) ou région, nom harmonisé (ex. Atacora) |
| `commune` | Commune (admin2 du PAM), accents restaurés pour le Bénin |
| `marche` | Nom du marché |
| `produit` | Nom du produit en français |
| `unite` | KG ou L |
| `prix` | Prix de détail en FCFA par unité |

## `data/valeurs_ecartees.csv`

Mêmes colonnes, plus `mediane_du_mois`, `rapport` (prix ÷ médiane) et `motif`.

## `resultats/synthese_produits.csv`

| Colonne | Description |
|---|---|
| `economie_pct` | Écart entre le mois le plus cher et le moins cher (%) |
| `mois_moins_cher`, `mois_plus_cher` | 1 = janvier … 12 = décembre |
| `hausse_pct`, `periode_hausse`, `marches_hausse` | Évolution sur les mêmes marchés et nombre de marchés |
| `chocs_pct` | Part des mois avec une variation de plus de 10 % |
| `dernier_prix`, `date_dernier` | Dernier prix médian national et son mois |

## Harmonisation des céréales entre pays

| Céréale | Bénin | Togo | Niger | Sénégal |
|---|---|---|---|---|
| Maïs | Maize (white) | Maize (white) | Maize | Maize (local) |
| Sorgho | Sorghum | Sorghum (red) | Sorghum | Sorghum |
| Mil, riz local, riz importé | même nom dans les 4 pays | | | |
