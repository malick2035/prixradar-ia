# 03 · Méthodologie

Toutes les méthodes sont codées dans [`prixradar/calculs.py`](../prixradar/calculs.py), testées dans [`tests/`](../tests/), et utilisées à l'identique par l'application, la démonstration et les documents.

## 1. Sources

| Source | Contenu | Fréquence | Statut |
|---|---|---|---|
| PAM (HDX), licence CC BY-IGO | Prix de détail par marché, produit et mois | Mensuelle | Intégré |
| SIM-Agricole (CT-SAGSA) | Prix par marché, analyses par commune | Mensuelle | Prévu, après autorisation |
| Réseau PrixRadar | Prix et disponibilité dans les communes non couvertes | Hebdomadaire | Prévu (pilote) |

Données intégrées (calcul du 1er octobre 2026) : Bénin et Sénégal jusqu'en juillet 2026, Togo et Niger jusqu'en août 2026 ; 50 marchés au Bénin, 119 au Togo, 68 au Niger, 60 au Sénégal.

## 2. Préparation des données

1. **Filtrage** : prix de **détail** uniquement (les prix de gros représentent moins de 1 % des relevés), années 2019 et suivantes, produits identifiés.
2. **Harmonisation** : noms de produits en français, regroupement des produits équivalents entre pays (voir le [dictionnaire des données](dictionnaire_des_donnees.md)).
3. **Valeurs aberrantes** : un prix supérieur à **3 fois** ou inférieur au **tiers** de la médiane du même produit, du même pays et du même mois est écarté. **2 779 relevés sur 217 775 (1,3 %)** ont été écartés ; ils sont tous listés dans [`data/valeurs_ecartees.csv`](../data/valeurs_ecartees.csv) avec le motif (exemple : riz paddy à 6 000 FCFA/kg à Bembèrèkè, probablement un prix par sac).
4. **Période d'analyse** : **2020 et après**. En 2019, la collecte au Bénin était incomplète (21 marchés de janvier à avril, 3 en mai et juin, 48 à partir de juillet) : l'utiliser comme référence fausserait les évolutions.

## 3. Calculs

| Indicateur | Méthode |
|---|---|
| **Indice saisonnier** | Pour chaque marché et chaque année complète (au moins 10 mois relevés) depuis 2020 : prix du mois ÷ prix moyen de l'année × 100. Puis médiane de tous les marchés et années. Neutralise l'inflation et les changements de marchés suivis. |
| **Écart entre mois** | (indice du mois le plus cher − indice du mois le moins cher) ÷ indice du mois le plus cher. |
| **Évolution des prix** | Marchés suivis au moins 6 mois en 2020 **et** en 2025 ; pour chacun, prix moyen 2025 ÷ prix moyen 2020 ; puis médiane. Prix courants (non corrigés de l'inflation). |
| **Prix par zone** | Prix moyen de chaque marché sur les 12 derniers mois ; puis médiane des marchés de la zone. Le nombre de marchés est affiché. |
| **Prix par commune** | Moyenne des 3 derniers mois et dernier prix relevé, avec sa date et le nombre de relevés. |
| **Chocs de prix** | Part des mois, depuis 2020, où le prix médian national varie de plus de 10 % en un mois. |
| **Comparaison entre pays** | Prix moyen de chaque marché sur les 12 derniers mois de chaque pays ; puis médiane. |

## 3 bis. Incertitude et fiabilité

- Pour chaque mois, l'application affiche la **plage où se situent la moitié des marchés et des années** (du 1er au 3e quartile des indices) : plus elle est large, moins le profil est régulier.
- **Niveau de fiabilité** selon le nombre de marchés : **forte** (10 et plus), **moyenne** (3 à 9), **faible** (1 ou 2). Les zones de fiabilité faible sont signalées.
- **Prix figés** : pour chaque marché et chaque produit, on mesure la plus longue série de mois consécutifs avec **exactement le même prix** sur les 12 derniers mois. À partir de **4 mois**, la valeur a probablement été reconduite d'un mois à l'autre ; l'application affiche alors « prix à confirmer sur le terrain ». C'est le cas d'environ **un couple marché-produit sur quatre** au Bénin (exemples : maïs blanc à Tanguiéta, 7 mois ; Kérou, 6 mois ; Natitingou, 4 mois). Ce constat justifie le contrôle par les collecteurs.
- **Traçabilité** : l'empreinte numérique (SHA-256) de chaque fichier source est enregistrée dans les résultats, pour prouver sur quelles données exactes les chiffres ont été calculés.

## 4. Test des tendances saisonnières

Avant d'utiliser le profil saisonnier pour anticiper, nous l'avons **testé sur 2025** : profil appris sur 2020-2024, prévision du prix à 3 mois, comparée à une méthode simple (« le prix ne bouge pas »).

| Produit | Erreur moyenne avec le profil | Erreur sans le profil | Conclusion |
|---|---|---|---|
| Tomates | 13,4 % | 41,4 % | Profil utile |
| Oignons | 18,8 % | 15,6 % | Profil indicatif seulement |
| Maïs blanc | 12,3 % | 12,0 % | Profil indicatif seulement |
| Riz importé | 5,0 % | 5,0 % | Prix stable, pas de saisonnalité |

**Règle adoptée** : l'application qualifie un profil de « testé » seulement si son erreur est au moins 20 % plus faible que celle de la méthode simple. **Aucune prévision chiffrée** n'est publiée tant que ce test n'est pas réussi.

## 5. Règles de qualité

- Afficher toujours la **source**, la **date** des données et le **nombre de marchés**.
- Signaler toute donnée de plus de **60 jours**.
- Ne jamais afficher de prix pour une zone ou un produit non couvert.
- Comparer des **périodes** et des **produits** comparables, issus d'une **même source**.

## 6. Limites

- Prix de **détail** uniquement ; prix courants, non corrigés de l'inflation générale.
- Les produits suivis diffèrent selon les pays ; la comparaison régionale porte sur les céréales.
- Le riz importé n'est plus suivi au Togo depuis 2022 ; le riz local est peu suivi au Niger (12 marchés récents).
- Certaines zones reposent sur peu de marchés (2 ou 3) : leurs résultats sont moins robustes.
- Données publiées avec un ou deux mois de décalage.
- Une partie des prix publiés semble reconduite d'un mois à l'autre (prix figés) : ils sont signalés, mais pas corrigés.
- Les profils saisonniers décrivent le passé ; ils ne garantissent pas les prix futurs.
- Transport, taxes et règles aux frontières ne sont pas pris en compte.

## 7. Reproductibilité

`python scripts/preparer_donnees.py` régénère toutes les données et tous les résultats ; `pytest` vérifie les calculs. L'analyse exploratoire d'origine est publique : [prix-alimentaires-uemoa](https://github.com/malick2035/prix-alimentaires-uemoa).
