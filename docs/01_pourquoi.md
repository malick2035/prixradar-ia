# 01 · Pourquoi PrixRadar.IA, et pourquoi maintenant

## 1. Le besoin

Les prix alimentaires pèsent sur toute la chaîne : importateur, grossiste, semi-grossiste, supermarché, petit commerçant, producteur et ménage. L'analyse de **214 996 relevés de prix vérifiés** du Programme alimentaire mondial (PAM), au Bénin, au Togo, au Niger et au Sénégal, montre quatre réalités.

1. **Les prix augmentent.** Au Bénin, entre 2020 et 2025, sur les mêmes marchés, les prix ont évolué de **+15 %** (maïs blanc) à **+57 %** (huile d'arachide) ; le riz importé a pris **+26 %**. Au Togo, le maïs blanc a augmenté de **+87 %** sur la même période (37 marchés).
2. **Le moment d'achat compte.** L'écart moyen entre le mois le plus cher et le moins cher atteint **48 %** pour les tomates, **35 %** pour les oignons et **22 %** pour le maïs blanc.
3. **Le lieu d'achat compte.** Le gari coûte en médiane **187 FCFA/kg** dans le Couffo contre **460** dans l'Alibori ; dans l'Atacora, le maïs blanc coûtait **76 FCFA/kg** à Cobly contre **174** à Natitingou (moyenne de mai à juillet 2026).
4. **Les produits frais sont imprévisibles.** Le prix des tomates varie de plus de 10 % en un mois **55 %** des mois, celui des oignons **45 %** ; le riz importé, jamais depuis 2020.

*Toutes les valeurs proviennent de [`resultats/synthese_produits.csv`](../resultats/synthese_produits.csv), calculé par [`scripts/preparer_donnees.py`](../scripts/preparer_donnees.py).*

## 2. Le problème

Ces informations existent, mais elles atteignent rarement, et rarement à temps, les personnes qui décident :

- les données publiées prennent la forme de bases de données ou de rapports, difficiles à utiliser pour une décision rapide ;
- même là où les prix sont publiés, **très peu de commerçants ou de ménages vont les chercher** dans les bases de données du PAM ou dans les bulletins officiels ;
- plusieurs **communes rurales du Nord** (Boukombé, Kouandé, Matéri, Toucountouna dans l'Atacora ; Copargo dans la Donga) n'ont **aucun marché dans la base du PAM** depuis 2014 ; leur couverture par le SIM-Agricole reste à vérifier avec la CT-SAGSA ;
- la **disponibilité** des produits (abondant, moyen, rare) n'est pas mesurée de façon régulière.

## 3. Pourquoi maintenant

- **La sécurité alimentaire est une priorité.** En mai 2024, le Gouvernement a temporairement interdit l'exportation des produits vivriers (Conseil des Ministres du 8 mai 2024, rapporté dans le bulletin SIM-Agricole de mai 2024), signe de la sensibilité du sujet.
- **Les données officielles sont publiées chaque mois** : par le PAM (via HDX) et par le SIM-Agricole.
- **Les outils sont accessibles** : analyse, hébergement d'un prototype et diffusion par messagerie sont aujourd'hui à la portée d'une petite équipe.
- **L'intelligence artificielle** permet d'expliquer des données complexes en langage simple, puis en langues locales, à condition d'être encadrée (voir [04 · Architecture](04_architecture.md)).

*L'usage des messageries (WhatsApp, SMS) par les commerçants ciblés sera mesuré lors du pilote, pour choisir les bons canaux.*

## 4. Ce que PrixRadar.IA change

PrixRadar.IA répond à des questions de décision :

- **Quand acheter ?** Les mois habituellement les moins chers et les plus chers.
- **Où acheter ?** Le département ou la commune les moins chers.
- **Quels risques ?** Les produits dont le prix peut changer brutalement.

Pour les ONG, les bailleurs et les pouvoirs publics, le même outil montre **où et quand** les tensions sur les prix apparaissent.
