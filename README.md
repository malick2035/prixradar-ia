# 📡 PrixRadar.IA

**Voir venir les hausses de prix alimentaires en Afrique de l'Ouest.**

PrixRadar.IA aide les commerçants, les ménages, les producteurs, les ONG et les décideurs publics du **Bénin**, du **Togo**, du **Niger** et du **Sénégal** à planifier leurs achats : **à quelle période** et **dans quelle zone** les produits alimentaires coûtent habituellement le moins cher, à partir des prix officiels du Programme alimentaire mondial (PAM).

> **Statut : prototype** (version 1.3, octobre 2026). *English summary: [README_EN.md](README_EN.md).* Démonstration interactive et application fonctionnelles ; comptes, paiement et assistant IA en préparation. Pilote proposé : **Atacora et Donga** (Bénin).

---

## Le constat (Bénin, données du PAM vérifiées)

| Constat | Résultat | Méthode |
|---|---|---|
| Hausse des prix entre 2020 et 2025 | de **+15 %** (maïs blanc) à **+57 %** (huile d'arachide) ; riz importé **+26 %** | Mêmes marchés en 2020 et 2025 (47 à 50 marchés), évolution marché par marché |
| Écart entre le mois le plus cher et le moins cher | **48 %** (tomates), **35 %** (oignons), **22 %** (maïs blanc) | Indice saisonnier calculé marché par marché, 2020-2025 |
| Écart entre départements | gari : **187 FCFA/kg** (Couffo) contre **460** (Alibori) | Médiane des marchés, 12 derniers mois |
| Instabilité | tomates : variation de plus de 10 % en un mois **55 %** des mois ; riz importé : **aucun** | Prix médian national, depuis 2020 |

Détail des calculs : [`resultats/synthese_produits.csv`](resultats/synthese_produits.csv) · Méthode : [`docs/03_methodologie.md`](docs/03_methodologie.md)

## Ce que fait PrixRadar.IA

| Service | Statut |
|---|---|
| **Quand acheter ?** Mois habituellement les moins chers et les plus chers | ✅ Fonctionnel |
| **Où acheter ?** Classement des départements, du moins cher au plus cher | ✅ Fonctionnel |
| **Départements et communes** (Bénin) | ✅ Fonctionnel |
| **Comparer les pays** (céréales) | ✅ Fonctionnel |
| **Radar du mois** et bulletin personnalisé | 🟡 Démonstration |
| **Inscription et compte** | 🟡 Démonstration (aucune donnée envoyée) |
| **Abonnements et paiement Mobile Money** | ⏳ Prévu |
| **Assistant IA** et **alertes WhatsApp** | ⏳ Prévu |

## Essayer

- **Démonstration** : télécharger [`demo/index.html`](demo/index.html) et l'ouvrir dans un navigateur. Elle fonctionne sans Internet.
- **Application** : voir « Lancer l'application » ci-dessous.

## Lancer l'application

```bash
pip install -r app/requirements.txt
streamlit run app/app.py
```

## Recalculer les résultats

```bash
# 1. Télécharger les fichiers du PAM dans data/brut/ (voir data/brut/README.md)
# 2. Recalculer
pip install -r requirements-dev.txt
python scripts/preparer_donnees.py
# 3. Vérifier les calculs
pytest          # 14 tests : méthodes et cohérence des résultats
```

## Documentation

| Document | Contenu |
|---|---|
| [00 · Le problème résolu et la preuve du besoin](docs/00_probleme_et_besoin.md) | **À lire en premier** : problème, preuves régionales et nationales, alignement |
| [01 · Pourquoi, et pourquoi maintenant](docs/01_pourquoi.md) | Le besoin dans les données |
| [02 · Existant et différence](docs/02_existant_et_difference.md) | SIM-Agricole, Ki@, AgroPrix, PAM |
| [03 · Méthodologie](docs/03_methodologie.md) | Sources, nettoyage, calculs, tests, limites |
| [04 · Architecture](docs/04_architecture.md) | Prototype et architecture cible |
| [05 · Sécurité et confidentialité](docs/05_securite_confidentialite.md) | Menaces, mesures, paiement, anti-arnaque |
| [06 · Modèle économique](docs/06_modele_economique.md) | Bien public et offres à bas prix |
| [07 · Impact et indicateurs](docs/07_impact_indicateurs.md) | Ce que nous mesurons |
| [08 · Feuille de route](docs/08_feuille_de_route.md) | 18 mois |
| [09 · Ne pas nuire, inclusion et genre](docs/09_ne_pas_nuire_inclusion.md) | Risques sociaux et mesures |
| [10 · Structure juridique et budget](docs/10_structure_juridique_et_budget.md) | Prérequis avant financement |
| [11 · Suivi des audits](docs/11_suivi_audit.md) | Failles relevées, corrections, note |
| [12 · Théorie du changement et cadre logique](docs/12_theorie_du_changement_cadre_logique.md) | Logique d'intervention et indicateurs |
| [13 · Durabilité et interopérabilité](docs/13_durabilite_interoperabilite.md) | Coordination, formats ouverts, sortie |
| [14 · Protocole d'enquête de besoin](docs/14_protocole_enquete_besoin.md) | Vérifier le besoin auprès des utilisateurs |
| [15 · Analyse d'impact sur la protection des données](docs/15_analyse_impact_donnees.md) | Risques pour les personnes et mesures |
| [16 · Registre des risques](docs/16_registre_des_risques.md) | Probabilité, impact, mesures |
| [17 · Critères des biens publics numériques](docs/17_biens_publics_numeriques.md) | Auto-évaluation |
| [Dictionnaire des données](docs/dictionnaire_des_donnees.md) | Colonnes et définitions |
| [Dossier de présentation (PDF)](docs/PrixRadar_IA_Dossier_de_presentation.pdf) | Pour les partenaires et bailleurs |

## Structure du dépôt

```
prixradar-ia/
├── app/                      Application Streamlit
├── demo/index.html           Démonstration autonome
├── prixradar/calculs.py      Toutes les méthodes de calcul (une seule source)
├── scripts/preparer_donnees.py
├── data/                     Données nettoyées et valeurs écartées
├── resultats/                Résultats utilisés partout
├── tests/                    Tests automatiques des calculs
└── docs/                     Documentation et dossier PDF
```

## Sources et licences

- Données : **Programme alimentaire mondial (PAM)**, via HDX, licence **CC BY-IGO**. Voir [SOURCES_ET_LICENCES.md](SOURCES_ET_LICENCES.md).
- Code : licence **MIT**. Documentation : licence **CC BY 4.0**.

## Contribuer, signaler une faille

[CONTRIBUTING.md](CONTRIBUTING.md) · [GOVERNANCE.md](GOVERNANCE.md) · [CITATION.cff](CITATION.cff) · [SECURITY.md](SECURITY.md) · [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) · [Politique de confidentialité](POLITIQUE_DE_CONFIDENTIALITE.md) · [Historique](CHANGELOG.md)

## Contact

**Malick OKASSE**, consultant Data Analytics & IA, Natitingou (Bénin) · data.malick9@gmail.com

Organisation, bailleur, association de commerçants ou institution : écrivez-nous pour une présentation du prototype.
