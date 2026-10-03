# 04 · Architecture

## 1. Prototype actuel

```
data/brut/ (fichiers du PAM)
      │  scripts/preparer_donnees.py  (utilise prixradar/calculs.py)
      ▼
data/prix_nettoyes_2019_2026.csv.gz  +  data/valeurs_ecartees.csv
      ▼
resultats/resultats_cles.json   ──►  app/app.py (Streamlit)
resultats/synthese_produits.csv ──►  demo/index.html (démonstration autonome)
                                ──►  documentation
```

Un seul module de calcul, un seul fichier de résultats : **tous les supports affichent les mêmes chiffres**.

## 2. Architecture cible (après le prototype)

```
 Sources                     Serveur PrixRadar (hébergé, sécurisé)            Utilisateurs
 PAM (mensuel)        ─┐     ┌───────────────────────────────────────┐
 SIM-Agricole (mensuel)─┼──► │ Collecte automatique, contrôle qualité │ ──► Application web
 Collecteurs (hebdo)  ─┘     │ Calculs (prixradar/calculs.py)         │ ──► WhatsApp, SMS
                             │ Base de données (comptes, abonnements) │ ──► Bulletins audio
 Agrégateur de paiement ◄──► │ API interne, journaux, sauvegardes     │
 (KKiaPay ou FedaPay)        │ Assistant IA encadré                   │
                             └───────────────────────────────────────┘
```

| Composant | Technologie envisagée |
|---|---|
| Collecte automatique mensuelle | Python, tâche planifiée (GitHub Actions ou serveur) |
| Lecture des bulletins SIM-Agricole | Extraction PDF, vérification manuelle des tableaux |
| Collecte de terrain | KoboToolbox (formulaires hors ligne, photos, coordonnées GPS) |
| Application | Interface web légère adaptée au téléphone ; Streamlit reste un outil de prototype |
| Comptes et abonnements | Base de données gérée (PostgreSQL), authentification sécurisée |
| Paiement | Agrégateur agréé, confirmation par notification signée |
| Diffusion | WhatsApp Business, SMS, fichiers audio pour radios |

**Streamlit Community Cloud** convient à la démonstration publique, mais **pas** aux comptes ni aux paiements : ces fonctions exigent un serveur et une base de données sécurisés (voir [05](05_securite_confidentialite.md)).

## 3. Assistant IA : garde-fous

1. **Les chiffres viennent du système, jamais de l'IA.** L'assistant reçoit les résultats calculés (prix, zone, date, source) et se limite à les formuler en langage simple.
2. **Réponse sourcée et datée** à chaque fois ; « je ne sais pas » si la donnée n'existe pas.
3. **Contenus extérieurs traités comme des données** : le texte des bulletins PDF est filtré et ne peut pas donner d'instructions à l'assistant (protection contre la manipulation).
4. **Pas de conseil financier ni de conseil de stockage spéculatif** (voir [09](09_ne_pas_nuire_inclusion.md)).
5. **Plafond de coût** mensuel, nombre de questions limité par utilisateur gratuit.
6. **Journal anonymisé** des questions et réponses, revue humaine régulière d'un échantillon.
7. **Tests** avant chaque mise en service : questions pièges, zones non couvertes, tentatives de manipulation.

## 4. État d'avancement

| Élément | Statut |
|---|---|
| Analyse et méthode (4 pays), tests automatiques | ✅ Fait |
| Application prototype et démonstration autonome | ✅ Fait |
| Mise en ligne publique du prototype | ⏳ Étape suivante |
| Collecte mensuelle automatique | ⏳ À faire |
| Comptes, abonnements, paiement | ⏳ À faire (après la structure juridique) |
| Assistant IA, alertes | ⏳ À faire |
| Réseau de collecteurs | ⏳ Pilote proposé |
