"""Contrôles de cohérence sur les résultats réels (resultats/resultats_cles.json)."""
import json, pathlib
R = json.load(open(pathlib.Path(__file__).resolve().parents[1] / "resultats" / "resultats_cles.json", encoding="utf-8"))


def test_periode_analyse_sans_2019():
    for pays in R["produits"].values():
        for x in pays.values():
            assert x["hausse_debut"] == 2020


def test_indices_saisonniers_plausibles():
    for pays in R["produits"].values():
        for x in pays.values():
            if x["saison"]:
                assert 90 <= sum(x["saison"]) / 12 <= 110
                assert 0 <= x["economie"] < 100


def test_prix_positifs_et_dates_presentes():
    for pays in R["produits"].values():
        for x in pays.values():
            assert x["dernier_prix"] > 0 and len(x["date_dernier"]) == 7
            assert all(z[1] > 0 and z[2] >= 1 for z in x["zones"])


def test_comparaison_entre_pays():
    assert all(r["prix"] > 0 and r["marches"] >= 1 for r in R["comparaison"])


def test_valeurs_ecartees_minoritaires():
    m = R["meta"]
    assert m["valeurs_ecartees"] / m["releves_bruts_retenus"] < 0.05
