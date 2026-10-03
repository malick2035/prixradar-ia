# Contribuer à PrixRadar.IA

Les contributions sont bienvenues : corrections, nouvelles sources de données, traductions, amélioration des méthodes.

1. Ouvrez une « issue » pour décrire votre proposition.
2. Créez une branche, faites vos modifications.
3. Toute modification des calculs passe par `prixradar/calculs.py`, avec un test dans `tests/`.
4. Lancez `pytest` et `python scripts/preparer_donnees.py` ; vérifiez que les résultats restent cohérents.
5. Proposez une « pull request » en expliquant le changement et son effet sur les chiffres.

Règles : toujours citer les sources, ne jamais ajouter de donnée personnelle au dépôt, ne jamais publier de clé secrète.
