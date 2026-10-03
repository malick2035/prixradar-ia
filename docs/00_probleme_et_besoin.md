# 00 · Le problème résolu et la preuve du besoin

*Document de référence pour répondre à la question d'un bailleur : « Quel problème PrixRadar.IA résout-il exactement, et le besoin existe-t-il vraiment ? »*

## 1. Le problème en une phrase

**Au Bénin et en Afrique de l'Ouest, les acteurs du commerce vivrier et les ménages prennent leurs décisions d'achat sans information de prix exploitable, alors que les prix varient fortement selon la saison et selon le lieu : ils paient plus cher qu'ils ne le devraient, et les alertes arrivent trop tard pour les zones rurales les plus fragiles.**

## 2. Arbre à problèmes

**Problème central** : décisions d'achat et d'approvisionnement alimentaires prises sans information de prix fiable, récente et compréhensible.

| Causes | Effets |
|---|---|
| Données officielles publiées sous forme de tableaux ou de rapports, peu exploitables pour une décision rapide, et rarement consultées par les commerçants et les ménages | Achats aux périodes et dans les zones les plus chères |
| Délai de publication d'un à deux mois | Pertes de marges pour les petits commerçants |
| Communes rurales sans marché dans la base du PAM (Boukombé, Kouandé, Matéri, Toucountouna, Copargo ; couverture par le SIM-Agricole à vérifier) | Budget alimentaire des ménages plus lourd |
| Disponibilité des produits non mesurée | Tensions locales repérées tardivement par les ONG et les pouvoirs publics |
| Information informelle (rumeurs, appels) non vérifiée | Exposition aux manipulations et à la spéculation |

## 3. Preuves du besoin

### 3.1 Au niveau régional (Afrique de l'Ouest, Sahel, CEDEAO)
- D'après l'actualisation du **Cadre Harmonisé** de juin 2026, plus de **54,8 millions de personnes** pourraient être en insécurité alimentaire aiguë (phase 3 ou plus) au Sahel, en Afrique de l'Ouest et au Cameroun pendant la soudure de juin à août 2026 [1].
- La FAO cite **la hausse des prix des denrées alimentaires** parmi les facteurs qui fragilisent les moyens de subsistance des populations les plus vulnérables, avec les conflits, les chocs climatiques et la baisse des financements humanitaires [2].
- La politique agricole de la CEDEAO (**ECOWAP**) inclut parmi ses objectifs la **lutte contre la volatilité des prix** [3]. Son système régional d'information agricole, **ECOAGRIS**, après plusieurs années d'inactivité, est **en cours de réactivation** : feuille de route validée en novembre 2024 [4], nouveau portail en développement depuis 2025 [8]. La CEDEAO prépare aussi un **tableau de bord du commerce et des marchés agricoles** (premier rapport annoncé pour 2025) [8]. L'information sur les marchés est donc une **priorité régionale en reconstruction**, que des outils ouverts et locaux peuvent alimenter.

### 3.2 Au niveau national (Bénin)
- Le Cadre Harmonisé projette environ **201 000 personnes** en insécurité alimentaire aiguë (phase 3 ou plus) pendant la soudure de juin à août 2026, dont environ **9 500 en phase 4 (urgence)** [5][6].
- Les départements de l'**Atacora** et de l'**Alibori** sont touchés par des violences de groupes armés, qui perturbent les moyens de subsistance ; environ **27 000 personnes** y étaient déplacées à la fin mars 2026 [6]. Le Bénin accueillait par ailleurs plus de **30 000 demandeurs d'asile et réfugiés** en novembre 2025 [7]. Ce sont précisément les zones du pilote PrixRadar.IA.
- En mai 2024, le Gouvernement a **temporairement interdit l'exportation des produits vivriers** (Conseil des Ministres du 8 mai 2024, rapporté par le bulletin SIM-Agricole de mai 2024), signe de la sensibilité des prix pour l'action publique.
- Les prix sont **volatils dans les deux sens** : selon la FAO, en avril 2026, les prix du maïs étaient de 25 à 35 % inférieurs à ceux d'avril 2025, après plusieurs années de hausse [6]. Savoir **quand** acheter compte autant que savoir **combien**.

### 3.3 Dans les données analysées par PrixRadar.IA
Voir [01 · Pourquoi](01_pourquoi.md) : hausses de +15 % à +57 % entre 2020 et 2025 au Bénin, écarts saisonniers jusqu'à 48 %, écarts entre zones du simple au double ou plus.

### 3.4 Ce qui n'est pas encore prouvé (et comment le prouver)
**La demande des utilisateurs eux-mêmes** (commerçantes, commerçants, ménages, ONG) n'a pas encore été mesurée par une enquête. C'est la première activité prévue : voir le [protocole d'enquête](14_protocole_enquete_besoin.md). Tant que cette enquête n'est pas faite, le besoin est **démontré par les données et les institutions**, mais **pas encore confirmé par les utilisateurs**.

## 4. Pourquoi PrixRadar.IA, alors que d'autres initiatives existent

Les systèmes existants (SIM-Agricole, SIM-AH/Ki@, AgroPrix, base du PAM, ECOAGRIS, SIAR de l'UEMOA) **collectent et publient des prix**. PrixRadar.IA ne les remplace pas ; il apporte la **couche manquante entre la donnée et la décision** :

1. **apporter l'information à ceux qui ne vont pas la chercher** : les données publiques existent, mais presque personne ne consulte les bases du PAM ou les bulletins ; PrixRadar.IA les transforme en **repères simples** (quand, où, quels risques), avec une méthode testée ;
2. couvrir les **communes rurales oubliées** du Nord et mesurer la **disponibilité** ;
3. diffuser par les **canaux du quotidien** (WhatsApp, SMS, radios, langues locales) ;
4. rester **ouvert et réutilisable** (bien public numérique) pour pouvoir **alimenter** les systèmes nationaux et régionaux plutôt que les concurrencer.

## 5. Alignement avec les cadres existants

| Cadre | Lien avec PrixRadar.IA |
|---|---|
| Objectif de développement durable 2 (« Faim zéro »), cible 2.c (limiter l'extrême volatilité des prix alimentaires, information sur les marchés) | Information sur les marchés accessible au plus grand nombre |
| ECOWAP (CEDEAO), lutte contre la volatilité des prix ; ECOAGRIS et tableau de bord du commerce agricole, en relance | Données ouvertes et méthode réutilisables par les systèmes régionaux |
| Système d'information agricole régional (SIAR) de l'UEMOA | Comparaison entre pays de l'UEMOA |
| Cadre Harmonisé et dispositif PREGEC | Indicateurs de prix par zone utiles à l'analyse de la soudure |
| Priorité nationale à la sécurité alimentaire | Information de proximité dans les zones vulnérables du Nord |

## Références

1. CILSS/AGRHYMET, Cadre Harmonisé, fiche de communication, situation projetée actualisée juin-août 2026 (juillet 2026). agrhymet.cilss.int
2. FAO, communiqué du Bureau sous-régional pour l'Afrique de l'Ouest sur les résultats du Cadre Harmonisé (janvier 2026), repris par AllAfrica.
3. FAO, chapitre « L'objectif politique : créer un marché ouest-africain unifié » (ECOWAP et volatilité des prix). fao.org/4/i4337f
4. CEDEAO, communiqué sur l'atelier de réactivation d'ECOAGRIS, Lagos, 4-8 novembre 2024. ecowas.int
5. CILSS/AGRHYMET, Cadre Harmonisé, fiche régionale décembre 2025 (situation projetée juin-août 2026).
6. FAO GIEWS, fiche pays Bénin, 10 juin 2026. fao.org/giews
7. PAM, note pays Bénin (données HCR, novembre 2025). docs.wfp.org
8. Programme FSRP (ARAA/CEDEAO) : atelier sur le tableau de bord du commerce et des marchés agricoles de la CEDEAO (Lomé, février 2025) et formation des informaticiens du CILSS/AGRHYMET au développement du portail ECOAGRIS (avril 2025). fsrp.araa.org

*Chiffres à réactualiser à chaque nouveau cycle du Cadre Harmonisé.*
