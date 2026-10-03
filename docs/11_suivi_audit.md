# 11 · Suivi des audits

## Audit 1 (1er octobre 2026)

L'audit du 1er octobre 2026 a relevé 24 failles (6 critiques, 12 majeures, 6 mineures). Ce tableau indique ce qui est corrigé dans la version 1.0.0 et ce qui reste à faire.

| ID | Faille | Statut | Correction apportée ou action restante |
|---|---|---|---|
| C1 | Évolution 2019-2025 biaisée par une collecte 2019 incomplète | ✅ Corrigé | Période 2020-2025, mêmes marchés, évolution marché par marché |
| C2 | Valeurs aberrantes non filtrées | ✅ Corrigé | Règle « 3 fois / un tiers de la médiane » ; 2 779 relevés écartés et listés |
| C3 | Indice saisonnier sensible aux changements de marchés | ✅ Corrigé | Indice marché par marché, années complètes, médiane |
| C4 | Pas de structure juridique | 🔴 À faire (porteur) | Options et prérequis : [10](10_structure_juridique_et_budget.md) |
| C5 | Données personnelles sans cadre | 🟡 Partiel | Politique de confidentialité publiée, aucune collecte réelle ; démarches auprès de l'autorité à faire avant lancement |
| C6 | Licences des données non vérifiées | ✅ Corrigé | Licence CC BY-IGO du PAM vérifiée, attribution ajoutée ; SIM-Agricole non utilisé sans autorisation |
| M1 | Démonstration plus riche que l'application | ✅ Corrigé | Statut de chaque fonction affiché ; onglet communes ajouté à l'application |
| M2 | Chiffres incohérents entre documents | ✅ Corrigé | Un module de calcul, un fichier de résultats, utilisés partout |
| M3 | Affirmations non sourcées | ✅ Corrigé | Affirmations sourcées ou retirées |
| M4 | Pas de budget chiffré | 🟡 Partiel | Postes définis ; chiffrage avec devis réels à faire |
| M5 | Tendances non testées | ✅ Corrigé | Test sur 2025 publié ; aucune prévision chiffrée sans test réussi |
| M6 | Accessibilité | 🟡 Partiel | Couleurs bleu/orange + libellés ▼▲ ; langues locales et audio prévus |
| M7 | Sécurité des comptes et paiements | 🟡 Partiel | Analyse des menaces et architecture cible documentées ; à construire |
| M8 | Risques de l'IA | 🟡 Partiel | Garde-fous définis ; à appliquer lors du développement |
| M9 | Gouvernance ouverte | ✅ Corrigé | CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, CHANGELOG, dictionnaire, licences |
| M10 | Inclusion et genre | 🟡 Partiel | Genre facultatif, approche documentée ; consultation des commerçantes au pilote |
| M11 | Risque de spéculation (« quoi stocker ») | ✅ Corrigé | Promesse reformulée, analyse « ne pas nuire » : [09](09_ne_pas_nuire_inclusion.md) |
| M12 | Données anciennes | ✅ Corrigé | Dates partout, alerte au-delà de 60 jours |
| m1 | Ressources externes dans la démonstration | ✅ Corrigé | Démonstration autonome (aucun appel extérieur) |
| m2 | Date des données peu visible | ✅ Corrigé | Bandeau daté en haut de la démonstration |
| m3 | Pas de tests, versions non fixées | ✅ Corrigé | 7 tests automatiques, versions fixées |
| m4 | Numéro de téléphone personnel publié | ✅ Corrigé | Numéro retiré ; adresse dédiée au projet recommandée |
| m5 | Nom non vérifié | 🔴 À faire (porteur) | Recherche d'antériorité et nom de domaine |
| m6 | Titre « UEMOA » imprécis | ✅ Corrigé | Pays cités explicitement |

**Bilan : 15 failles corrigées, 7 partiellement, 2 à traiter par le porteur.**


## Audit 2 (1er octobre 2026)

### Nature de ces audits
Ces audits sont des **revues internes structurées**, réalisées par l'équipe qui construit le projet, en s'inspirant de référentiels reconnus : critères des biens publics numériques (Digital Public Goods Standard), bonnes pratiques de sécurité des applications web (OWASP), principes de qualité des données statistiques, principe « ne pas nuire » de l'action humanitaire, et attentes usuelles des bailleurs (problème, preuve, cadre logique, durabilité). **Ils ne remplacent pas un audit indépendant** : avant un lancement public ou un financement important, une revue externe (méthode par un statisticien ou le PAM, sécurité par un spécialiste, conformité par un juriste) est recommandée.

### Nouvelles failles relevées et traitement

| ID | Faille | Statut | Traitement |
|---|---|---|---|
| N1 | Problème non formulé de façon stricte (pas d'arbre à problèmes) | ✅ Corrigé | [00](00_probleme_et_besoin.md) |
| N2 | Besoin régional et national non démontré par des sources institutionnelles | ✅ Corrigé | Cadre Harmonisé, FAO GIEWS, ECOWAP, ECOAGRIS, PAM : [00](00_probleme_et_besoin.md) |
| N3 | Besoin non confirmé par les utilisateurs (aucune enquête) | 🔴 À faire (porteur) | Protocole prêt : [14](14_protocole_enquete_besoin.md) |
| N4 | Pas de théorie du changement ni de cadre logique | ✅ Corrigé | [12](12_theorie_du_changement_cadre_logique.md) |
| N5 | Risque pour la sécurité des collecteurs (Atacora, Alibori) non traité | ✅ Corrigé | Protocole de sécurité : [09](09_ne_pas_nuire_inclusion.md) |
| N6 | Doublon possible avec ECOAGRIS, SIAR, SIM-AH | ✅ Corrigé | Plan de coordination : [13](13_durabilite_interoperabilite.md) |
| N7 | Pas de stratégie de sortie ni de plan de transfert | ✅ Corrigé | [13](13_durabilite_interoperabilite.md) |
| N8 | Interopérabilité non prévue (formats, API, HXL) | 🟡 Partiel | Prévue et documentée ; à construire |
| N9 | Dépendance à une seule personne | 🟡 Partiel | Plan de transmission documenté ; deuxième personne à former |
| N10 | Bénéfice par utilisateur non quantifié | 🟡 Partiel | Mesure prévue par l'enquête et le pilote |
| N11 | Méthode non validée par un tiers indépendant | 🔴 À faire (porteur) | Demander une revue au PAM (VAM) ou à un statisticien |
| N12 | Pas de contrôle de cohérence sur les résultats réels | ✅ Corrigé | 5 tests sur les résultats (12 tests au total) |

### Note globale (grille de préparation au financement)

| Critère | Poids | Note avant audit 2 | Note après audit 2 |
|---|---|---|---|
| Problème et preuve du besoin | 15 % | 6,5 | 7,5 |
| Solution et différenciation | 10 % | 8,0 | 8,5 |
| Qualité des données et de la méthode | 15 % | 8,5 | 8,5 |
| Produit et technique | 10 % | 7,5 | 7,5 |
| Sécurité et protection des données | 10 % | 6,0 | 6,5 |
| Éthique, inclusion, ne pas nuire | 10 % | 7,0 | 8,0 |
| Gouvernance ouverte | 5 % | 8,5 | 9,0 |
| Partenariats et alignement | 10 % | 5,5 | 6,5 |
| Modèle économique et durabilité | 10 % | 5,5 | 6,5 |
| Capacité de mise en œuvre, suivi-évaluation | 5 % | 6,0 | 7,0 |
| **Note globale** | | **6,9 / 10** | **7,6 / 10** |

### Ce qu'il faut pour atteindre 9,5 / 10
La documentation ne peut pas, à elle seule, dépasser environ **8 / 10**. Les points restants viennent de **preuves réelles**, que seul le porteur peut apporter :

1. **Enquête de besoin** auprès d'au moins 60 utilisateurs (N3) : +0,5
2. **Structure juridique** créée et **démarches de protection des données** engagées (C4, C5) : +0,4
3. **Lettres de soutien** d'associations de commerçants, de communes ou d'institutions : +0,3
4. **Budget chiffré** sur devis réels (M4) : +0,2
5. **Revue indépendante** de la méthode et de la sécurité (N11) : +0,3
6. **Résultats d'un premier test** avec de vrais utilisateurs (3 mois) : +0,4

Avec ces six éléments, la note visée de **9,5 / 10** devient atteignable.

## Audit 3 (1er octobre 2026)

### Nouvelles failles relevées et traitement

| ID | Faille | Statut | Traitement |
|---|---|---|---|
| T1 | Incertitude des profils saisonniers non montrée | ✅ Corrigé | Plage du 1er au 3e quartile affichée, explication en clair |
| T2 | Fiabilité des zones peu suivies non signalée | ✅ Corrigé | Niveaux forte / moyenne / faible ; alerte si 1 ou 2 marchés |
| T3 | Pas de preuve des fichiers sources utilisés | ✅ Corrigé | Empreinte SHA-256 de chaque fichier dans les résultats |
| T4 | Graphiques inaccessibles aux lecteurs d'écran | ✅ Corrigé | Résumé textuel et tableau « Voir les données » pour chaque graphique |
| T5 | Onglets non utilisables au clavier | ✅ Corrigé | Navigation par flèches, attributs d'accessibilité |
| T6 | Données d'inscription gardées par défaut sur l'appareil | ✅ Corrigé | Option « se souvenir de moi » décochée par défaut |
| T7 | Pas de politique de sécurité du contenu dans la démonstration | ✅ Corrigé | Politique stricte : aucune connexion extérieure possible |
| T8 | Promesse d'accueil supérieure aux preuves (« voir venir les hausses ») | ✅ Corrigé | Accroche reformulée : « Le bon moment et le bon endroit pour acheter » |
| T9 | Pas de tests automatiques à chaque modification | ✅ Corrigé | Intégration continue GitHub : tests et analyse des failles des dépendances |
| T10 | Documentation uniquement en français | ✅ Corrigé | Résumé en anglais (bailleurs internationaux, Indaba) |
| T11 | Pas d'analyse d'impact sur la protection des données | 🟡 Partiel | AIPD préliminaire ; validation juridique à faire |
| T12 | Pas de registre des risques consolidé | ✅ Corrigé | [16](16_registre_des_risques.md) |
| T13 | Conformité aux biens publics numériques non évaluée | ✅ Corrigé | Auto-évaluation : 7 critères sur 9 remplis, 2 partiels |
| T14 | Pas de règles de gouvernance ni de citation | ✅ Corrigé | GOVERNANCE.md, CITATION.cff |
| T15 | Prix courants seulement, sans correction de l'inflation générale | 🟡 Partiel | Limite annoncée ; correction prévue avec l'indice des prix de l'INStaD |
| T18 | Prix identiques plusieurs mois de suite (valeurs probablement reconduites), non détectés (signalé par le porteur) | ✅ Corrigé | Détection automatique (4 mois et plus), affichage « à confirmer sur le terrain », test ajouté, limite documentée |
| T17 | Communes présentées comme « non suivies » sans vérifier le SIM-Agricole ; valeur d'accès à l'information sous-estimée (signalé par le porteur) | ✅ Corrigé | Formulation précise : « aucun marché dans la base du PAM depuis 2014 », couverture SIM-Agricole à vérifier ; mission « rendre accessible ce qui existe » ajoutée |
| T16 | ECOAGRIS présenté comme « inactif depuis 2019 », information dépassée (signalée par le porteur) | ✅ Corrigé | Statut actualisé : réactivation en cours depuis 2024-2025 ; ajout du tableau de bord du commerce agricole de la CEDEAO |

### Note globale après l'audit 3

| Critère | Poids | Audit 2 | Audit 3 |
|---|---|---|---|
| Problème et preuve du besoin | 15 % | 7,5 | 7,5 |
| Solution et différenciation | 10 % | 8,5 | 8,5 |
| Qualité des données et de la méthode | 15 % | 8,5 | 9,0 |
| Produit et technique | 10 % | 7,5 | 8,0 |
| Sécurité et protection des données | 10 % | 6,5 | 7,0 |
| Éthique, inclusion, ne pas nuire | 10 % | 8,0 | 8,5 |
| Gouvernance ouverte | 5 % | 9,0 | 9,5 |
| Partenariats et alignement | 10 % | 6,5 | 6,5 |
| Modèle économique et durabilité | 10 % | 6,5 | 6,5 |
| Capacité de mise en œuvre, suivi-évaluation | 5 % | 7,0 | 7,5 |
| **Note globale** | | **7,6 / 10** | **7,8 / 10** |

**Lecture honnête** : les critères qui dépendent du travail technique et documentaire sont désormais entre 8 et 9,5. Les trois critères bloquants (preuve du besoin auprès des utilisateurs, partenariats, modèle économique) ne peuvent progresser qu'avec des **actions de terrain** : enquête, structure juridique, lettres de soutien, budget sur devis, revue indépendante, premier test de 3 mois (voir la fin de l'audit 2).
