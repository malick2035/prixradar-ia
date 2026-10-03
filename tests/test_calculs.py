"""Tests des calculs de PrixRadar.IA (lancer : pytest)."""
import sys, pathlib
import pandas as pd
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from prixradar import calculs as C


def serie(marches=3, annees=(2020, 2021, 2022), profil=None, croissance=0.0):
    """Données synthétiques : prix = 100 x profil du mois x (1 + croissance) ** (année - 2020)."""
    profil = profil or [100] * 12
    lignes = []
    for m in range(marches):
        for a in annees:
            for mois in range(1, 13):
                p = profil[mois - 1] * (1 + croissance) ** (a - 2020) * (1 + m / 100)
                lignes.append({"date": pd.Timestamp(a, mois, 15), "pays": "Bénin", "region": "Atacora",
                               "commune": f"C{m}", "marche": f"M{m}", "produit": "Maïs blanc", "unite": "KG", "prix": p})
    return pd.DataFrame(lignes)


def test_saisonnalite_retrouve_le_profil():
    profil = [80, 90, 100, 110, 120, 120, 110, 100, 90, 80, 100, 100]
    s, n = C.saisonnalite(serie(profil=profil))
    moyenne = sum(profil) / 12
    assert n == 3
    for obtenu, attendu in zip(s, profil):
        assert abs(obtenu - attendu / moyenne * 100) < 0.2


def test_saisonnalite_insensible_a_l_inflation():
    profil = [90] * 6 + [110] * 6
    s1, _ = C.saisonnalite(serie(profil=profil))
    s2, _ = C.saisonnalite(serie(profil=profil, croissance=0.3))
    assert all(abs(a - b) < 0.2 for a, b in zip(s1, s2))


def test_economie():
    e, mn, mx = C.economie([100, 50] + [100] * 10)
    assert (e, mn, mx) == (50, 2, 1)


def test_hausse_panel_constant():
    h, n, a0, a1 = C.hausse_panel(serie(annees=(2020, 2021, 2022, 2023, 2024, 2025), croissance=0.10))
    assert n == 3 and a0 == 2020 and a1 == 2025
    assert abs(h - round((1.1 ** 5 - 1) * 100)) <= 1


def test_hausse_panel_ignore_les_marches_absents_au_depart():
    d = serie(annees=(2020, 2021, 2022, 2023, 2024, 2025), croissance=0.0)
    nouveau = d[d["marche"] == "M0"].assign(marche="M9", prix=lambda t: t["prix"] * 3)
    nouveau = nouveau[nouveau["date"].dt.year == 2025]
    h, n, _, _ = C.hausse_panel(pd.concat([d, nouveau]))
    assert h == 0 and n == 3


def test_valeurs_aberrantes_ecartees():
    d = serie()
    brut = pd.DataFrame({"date": d["date"].dt.strftime("%Y-%m-%d"), "admin1": "Atakora", "admin2": "Kobli",
                         "market": d["marche"], "commodity": "Maize (white)", "unit": "KG", "pricetype": "Retail",
                         "price": d["prix"], "pays": "Bénin"})
    brut.loc[0, "price"] = brut.loc[0, "price"] * 10
    propre, ecartes = C.nettoyer(brut)
    assert len(ecartes) == 1 and len(propre) == len(brut) - 1
    assert propre["commune"].iloc[0] == "Cobly" and propre["region"].iloc[0] == "Atacora"


def test_chocs():
    d = serie(marches=2, annees=(2020, 2021, 2022), profil=[100, 130] * 6)
    assert C.chocs(d) == 100


def test_dispersion_et_fiabilite():
    q25, q75 = C.saisonnalite_dispersion(serie(profil=[90] * 6 + [110] * 6))
    assert all(a <= b for a, b in zip(q25, q75))
    assert C.niveau_fiabilite(12) == "forte" and C.niveau_fiabilite(4) == "moyenne" and C.niveau_fiabilite(2) == "faible"


def test_prix_figes():
    assert C.plus_longue_serie_identique(pd.Series([100, 100, 100, 100, 90, 95])) == 4
    assert C.plus_longue_serie_identique(pd.Series([100, 101, 102])) == 1
