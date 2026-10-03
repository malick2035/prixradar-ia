# 05 · Sécurité et confidentialité

## 1. Analyse des menaces

| Menace | Conséquence | Mesures prévues |
|---|---|---|
| Usurpation de PrixRadar.IA (faux numéros, faux messages) pour escroquer | Pertes d'argent pour les utilisateurs, perte de confiance | Canaux officiels uniques, message anti-arnaque partout, signalement simple |
| Faux paiement (capture d'écran falsifiée) | Abonnements frauduleux | Activation uniquement sur notification signée de l'agrégateur |
| Vol de données personnelles | Atteinte à la vie privée, spam, escroqueries | Données minimales, chiffrement, accès restreint, journaux |
| Prise de contrôle de comptes | Usurpation, accès payant détourné | Authentification sécurisée, limitation des tentatives |
| Fuite de clés secrètes (paiement, IA) | Fraude, coûts imprévus | Clés hors du code public, rotation, alertes de dépense |
| Injection de données ou de code | Résultats faussés, attaque du serveur | Validation des saisies, requêtes paramétrées, échappement de l'affichage |
| Relevés de terrain falsifiés | Information fausse | Photos, double relevé, contrôle automatique avec les sources officielles |
| Manipulation de l'assistant IA | Réponses trompeuses | Garde-fous décrits dans [04](04_architecture.md) |
| Indisponibilité ou perte de données | Service interrompu | Sauvegardes quotidiennes, procédure de restauration testée |

## 2. Données personnelles

- **Données minimales** : prénom, nom (facultatif), e-mail, numéro WhatsApp, profil, département, produits suivis, genre (facultatif). Jamais de pièce d'identité, de donnée bancaire ni de code Mobile Money.
- **Consentement** explicite, finalité indiquée, [politique de confidentialité](../POLITIQUE_DE_CONFIDENTIALITE.md) publiée.
- **Droits** : accès, rectification, suppression sur simple demande.
- **Aucune revente** ni cession.
- **Responsable de traitement** : la structure juridique porteuse du projet (à créer, voir [10](10_structure_juridique_et_budget.md)).
- **Conformité** : démarches auprès de l'autorité béninoise de protection des données personnelles **avant** toute collecte réelle.

*Le prototype actuel ne collecte aucune donnée réelle : le formulaire de démonstration garde les informations sur l'appareil de l'utilisateur.*

## 3. Sécurité technique (architecture cible)

| Mesure | Objectif |
|---|---|
| HTTPS partout | Chiffrer les échanges |
| Mots de passe hachés, jamais stockés en clair | Protéger les comptes |
| Clés secrètes dans un coffre de secrets, jamais sur GitHub | Éviter les fuites |
| Limitation des tentatives et des requêtes | Bloquer les attaques par force brute et les abus |
| Validation et échappement des saisies | Empêcher les injections |
| Sauvegardes chiffrées quotidiennes | Restaurer après incident |
| Journal des actions sensibles | Détecter les anomalies |
| Mises à jour régulières, analyse des dépendances | Corriger les failles connues |
| Revue de sécurité avant lancement public | Vérification indépendante |

## 4. Paiement Mobile Money

- Uniquement via un **agrégateur agréé** (KKiaPay ou FedaPay) ; MTN MoMo et Moov Money.
- PrixRadar.IA ne voit **jamais** le code secret : la validation se fait sur le téléphone de l'utilisateur.
- Abonnement activé **seulement** après notification signée et vérifiée ; référence unique par paiement ; doublons refusés ; reçu envoyé.

## 5. Message anti-arnaque (affiché partout)

> **PrixRadar.IA ne vous appellera jamais pour vous demander un code secret, un mot de passe ou un transfert d'argent.** Les abonnements se paient uniquement dans l'application. En cas de doute, écrivez à l'adresse officielle.

## 6. Signaler une faille

Voir [SECURITY.md](../SECURITY.md).
