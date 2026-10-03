"""
Fonctions de calcul de PrixRadar.IA.

Toutes les applications (Streamlit, démonstration, documents) utilisent ces
fonctions, pour garantir des chiffres identiques partout.
"""
from __future__ import annotations
import pandas as pd

PAYS = {"ben": "Bénin", "tgo": "Togo", "ner": "Niger", "sen": "Sénégal"}
ANNEE_DEBUT_ANALYSE = 2020          # 2019 exclue : collecte incomplète au Bénin
SEUIL_ABERRANT = 3.0                # prix > 3 x ou < 1/3 de la médiane du mois
SEUIL_CHOC = 10.0                   # variation mensuelle (%) considérée comme un choc
FRAICHEUR_MAX_JOURS = 60            # au-delà, la donnée est signalée comme ancienne

PRODUITS_FR = {
    "Millet": "Mil", "Rice (imported)": "Riz importé", "Sorghum": "Sorgho", "Rice (local)": "Riz local",
    "Maize (white)": "Maïs blanc", "Cassava meal (gari)": "Gari", "Beans (white)": "Haricots blancs",
    "Soybeans": "Soja", "Sorghum (red)": "Sorgho rouge", "Beans (red)": "Haricots rouges", "Maize": "Maïs",
    "Tomatoes": "Tomates", "Onions": "Oignons", "Oil (groundnut)": "Huile d'arachide", "Oil (palm)": "Huile de palme",
    "Peppers (red, dry)": "Piment rouge sec", "Cassava meal (tapioca)": "Tapioca", "Groundnuts (Bambara)": "Voandzou",
    "Fish (fresh, silvi)": "Poisson frais", "Oranges": "Oranges", "Okra (fresh)": "Gombo frais",
    "Groundnuts (small, unshelled)": "Arachide (petite, en coque)", "Lemons": "Citrons",
    "Wheat flour (imported)": "Farine de blé importée", "Beans (niebe)": "Niébé", "Coconut (dried)": "Noix de coco sèche",
    "Leafy vegetables": "Légumes-feuilles", "Cassava meal (gari, fine)": "Gari fin", "Maize (local)": "Maïs local",
    "Yam": "Igname", "Yam (white)": "Igname blanche", "Sweet potatoes": "Patate douce", "Carrots": "Carottes",
    "Rice (ordinary, first quality)": "Riz ordinaire", "Papaya": "Papaye", "Potatoes": "Pommes de terre", "Wheat": "Blé",
    "Maize (imported)": "Maïs importé", "Cabbage": "Chou", "Groundnuts (shelled)": "Arachide décortiquée",
    "Yam (flour)": "Farine d'igname", "Peas (green, dry)": "Pois secs", "Fish (tilapia)": "Tilapia",
    "Maize (yellow)": "Maïs jaune", "Groundnuts (unshelled)": "Arachide en coque", "Cassava (cossette)": "Cossettes de manioc",
    "Yam (dry)": "Igname sèche", "Oil (palm nut)": "Huile de palmiste", "Cassava flour": "Farine de manioc",
    "Cassava (fresh)": "Manioc frais", "Rice (Broken, local)": "Riz brisé local", "Shrimps": "Crevettes",
    "Rice (milled, local)": "Riz décortiqué local", "Beans (black)": "Haricots noirs", "Rice (paddy)": "Riz paddy",
    "Oil (vegetable)": "Huile végétale", "Salt": "Sel", "Plantains": "Banane plantain", "Snail": "Escargots",
    "Sorghum (imported)": "Sorgho importé", "Taro": "Taro", "Yam (yellow)": "Igname jaune"}

COMMUNES_FR = {"Kerou": "Kérou", "Kobli": "Cobly", "Pehonko": "Péhunco", "Tanguieta": "Tanguiéta", "Ouake": "Ouaké",
    "Abomey-calavi": "Abomey-Calavi", "Ze": "Zè", "So-ava": "Sô-Ava", "Bembereke": "Bembèrèkè", "Kalale": "Kalalé",
    "Sinende": "Sinendé", "Glazoue": "Glazoué", "Ouesse": "Ouèssè", "Aplahoue": "Aplahoué", "Dogbo-tota": "Dogbo",
    "Klouekanme": "Klouékanmè", "Come": "Comé", "Porto-novo": "Porto-Novo", "Adja-ouere": "Adja-Ouèrè", "Ketou": "Kétou",
    "Pobe": "Pobè", "Sakete": "Sakété", "Cove": "Covè", "Zogbodome": "Zogbodomey", "Dassa": "Dassa-Zoumè"}
REGIONS_FR = {"Atakora": "Atacora", "Oueme": "Ouémé"}

# Céréales comparables entre pays (même source, noms harmonisés)
CEREALES = {"Maïs": {"Bénin": "Maïs blanc", "Togo": "Maïs blanc", "Niger": "Maïs", "Sénégal": "Maïs local"},
            "Mil": {p: "Mil" for p in PAYS.values()},
            "Sorgho": {"Bénin": "Sorgho", "Togo": "Sorgho rouge", "Niger": "Sorgho", "Sénégal": "Sorgho"},
            "Riz local": {p: "Riz local" for p in PAYS.values()},
            "Riz importé": {p: "Riz importé" for p in PAYS.values()}}


def charger_brut(dossier: str) -> pd.DataFrame:
    """Lit les fichiers bruts du PAM (wfp_food_prices_xxx.csv) des 4 pays."""
    morceaux = []
    for code, nom in PAYS.items():
        t = pd.read_csv(f"{dossier}/wfp_food_prices_{code}.csv", low_memory=False)
        if str(t.iloc[0, 0]).startswith("#"):          # ligne d'étiquettes HXL éventuelle
            t = t.iloc[1:]
        t["pays"] = nom
        morceaux.append(t)
    return pd.concat(morceaux, ignore_index=True)


def nettoyer(brut: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Garde les prix de détail 2019+, harmonise les noms, écarte les valeurs aberrantes.

    Retourne (données propres, valeurs écartées avec le motif)."""
    d = brut.copy()
    d["date"] = pd.to_datetime(d["date"])
    d["price"] = pd.to_numeric(d["price"], errors="coerce")
    d = d[(d["pricetype"] == "Retail") & (d["date"].dt.year >= 2019) & d["commodity"].isin(PRODUITS_FR)
          & d["price"].gt(0)].copy()
    d["produit"] = d["commodity"].map(PRODUITS_FR)
    d["region"] = d["admin1"].replace(REGIONS_FR)
    d["commune"] = d["admin2"].map(lambda x: COMMUNES_FR.get(x, x))
    d = d.rename(columns={"market": "marche", "price": "prix", "unit": "unite"})
    d = d[["date", "pays", "region", "commune", "marche", "produit", "unite", "prix"]]
    med = d.groupby(["pays", "produit", "date"])["prix"].transform("median")
    ratio = d["prix"] / med
    aberrant = (ratio > SEUIL_ABERRANT) | (ratio < 1 / SEUIL_ABERRANT)
    ecartes = d[aberrant].assign(mediane_du_mois=med[aberrant].round(1), rapport=ratio[aberrant].round(2),
                                 motif="Prix à plus de 3 fois ou moins du tiers de la médiane du mois")
    return d[~aberrant].reset_index(drop=True), ecartes.reset_index(drop=True)


def unite_de(x: pd.DataFrame) -> str:
    return "litre" if (x["unite"] == "L").mean() > 0.5 else "kg"


def derniere_annee_complete(x: pd.DataFrame) -> int:
    fin = x["date"].max()
    return fin.year - 1 if fin.month < 12 else fin.year


def saisonnalite(x: pd.DataFrame) -> tuple[list | None, int]:
    """Indice saisonnier (100 = moyenne de l'année), calculé marché par marché.

    Pour chaque marché et chaque année complète depuis 2020, l'indice d'un mois est
    le prix du mois divisé par la moyenne de l'année. On prend ensuite la médiane
    de tous les marchés et de toutes les années. Retourne (12 valeurs, nb de marchés)."""
    a1 = derniere_annee_complete(x)
    y = x[(x["date"].dt.year >= ANNEE_DEBUT_ANALYSE) & (x["date"].dt.year <= a1)].copy()
    y["annee"], y["mois"] = y["date"].dt.year, y["date"].dt.month
    m = y.groupby(["marche", "annee", "mois"])["prix"].mean().reset_index()
    n_mois = m.groupby(["marche", "annee"])["mois"].transform("count")
    m = m[n_mois >= 10]                                  # années presque complètes seulement
    if m.empty:
        return None, 0
    m["indice"] = m["prix"] / m.groupby(["marche", "annee"])["prix"].transform("mean") * 100
    s = m.groupby("mois")["indice"].median().reindex(range(1, 13))
    if s.notna().sum() < 12:
        return None, int(m["marche"].nunique())
    return [round(v, 1) for v in s], int(m["marche"].nunique())


def saisonnalite_dispersion(x: pd.DataFrame) -> tuple[list | None, list | None]:
    """Quartiles (25 % et 75 %) des indices mensuels entre marchés et années : mesure de l'incertitude."""
    a1 = derniere_annee_complete(x)
    y = x[(x["date"].dt.year >= ANNEE_DEBUT_ANALYSE) & (x["date"].dt.year <= a1)].copy()
    y["annee"], y["mois"] = y["date"].dt.year, y["date"].dt.month
    m = y.groupby(["marche", "annee", "mois"])["prix"].mean().reset_index()
    m = m[m.groupby(["marche", "annee"])["mois"].transform("count") >= 10]
    if m.empty:
        return None, None
    m["indice"] = m["prix"] / m.groupby(["marche", "annee"])["prix"].transform("mean") * 100
    q = m.groupby("mois")["indice"].quantile([0.25, 0.75]).unstack().reindex(range(1, 13))
    if q.isna().any().any():
        return None, None
    return [round(v, 1) for v in q[0.25]], [round(v, 1) for v in q[0.75]]


def niveau_fiabilite(nb_marches: int) -> str:
    """Fiabilité selon le nombre de marchés : forte (10 et plus), moyenne (3 à 9), faible (1 ou 2)."""
    return "forte" if nb_marches >= 10 else ("moyenne" if nb_marches >= 3 else "faible")


def economie(s: list) -> tuple[int, int, int]:
    """(économie possible en %, mois le moins cher 1-12, mois le plus cher 1-12)."""
    mn, mx = min(s), max(s)
    return round((mx - mn) / mx * 100), s.index(mn) + 1, s.index(mx) + 1


def hausse_panel(x: pd.DataFrame) -> tuple[int | None, int, int, int]:
    """Évolution entre 2020 et la dernière année complète, sur les marchés suivis les deux années.

    Retourne (hausse en %, nb de marchés, année de départ, année d'arrivée)."""
    a0, a1 = ANNEE_DEBUT_ANALYSE, derniere_annee_complete(x)
    y = x[x["date"].dt.year.isin([a0, a1])].assign(annee=lambda t: t["date"].dt.year)
    nb = y.groupby(["marche", "annee"])["prix"].count().unstack()
    moy = y.groupby(["marche", "annee"])["prix"].mean().unstack()
    if a0 not in moy or a1 not in moy:
        return None, 0, a0, a1
    ok = (nb[a0] >= 6) & (nb[a1] >= 6)
    r = (moy.loc[ok, a1] / moy.loc[ok, a0]).dropna()
    if len(r) < 3:
        return None, int(len(r)), a0, a1
    return round((r.median() - 1) * 100), int(len(r)), a0, a1


def serie_nationale(x: pd.DataFrame) -> pd.Series:
    return x.groupby("date")["prix"].median().sort_index()


def chocs(x: pd.DataFrame) -> int | None:
    """Part des mois (depuis 2020) où le prix médian varie de plus de 10 % en un mois."""
    s = serie_nationale(x[x["date"].dt.year >= ANNEE_DEBUT_ANALYSE])
    if len(s) < 24:
        return None
    v = s.pct_change().dropna() * 100
    return round((v.abs() > SEUIL_CHOC).mean() * 100)


def prix_par_zone(x: pd.DataFrame, niveau: str = "region", mois: int = 12) -> pd.DataFrame:
    """Moyenne de chaque marché sur les derniers mois, puis médiane par zone."""
    fin = x["date"].max()
    r = x[x["date"] > fin - pd.DateOffset(months=mois)]
    pm = r.groupby([niveau, "marche"])["prix"].mean().reset_index()
    z = pm.groupby(niveau)["prix"].agg(prix="median", marches="count").reset_index()
    return z.sort_values("prix").reset_index(drop=True)


def prix_par_commune(x: pd.DataFrame, mois: int = 3) -> pd.DataFrame:
    """Par marché : moyenne des derniers mois, dernier prix et sa date."""
    fin = x["date"].max()
    r = x[x["date"] > fin - pd.DateOffset(months=mois)].sort_values("date")
    g = r.groupby(["region", "commune", "marche"])
    out = g["prix"].agg(moyenne="mean", releves="count").reset_index()
    der = g.tail(1)[["region", "commune", "marche", "prix", "date"]].rename(columns={"prix": "dernier_prix", "date": "date_dernier"})
    return out.merge(der, on=["region", "commune", "marche"]).sort_values("moyenne").reset_index(drop=True)


def comparaison_cereales(d: pd.DataFrame, mois: int = 12) -> pd.DataFrame:
    lignes = []
    for cer, noms in CEREALES.items():
        for pays, nom in noms.items():
            x = d[(d["pays"] == pays) & (d["produit"] == nom)]
            if x.empty:
                continue
            fin = d.loc[d["pays"] == pays, "date"].max()
            r = x[x["date"] > fin - pd.DateOffset(months=mois)]
            if len(r) < 30:
                continue
            lignes.append({"cereale": cer, "pays": pays, "prix": round(r.groupby("marche")["prix"].mean().median()),
                           "marches": int(r["marche"].nunique()), "periode_fin": fin.strftime("%Y-%m")})
    return pd.DataFrame(lignes)


def test_tendance(x: pd.DataFrame, horizon: int = 3) -> dict | None:
    """Teste la « tendance saisonnière » sur la dernière année complète.

    Profil saisonnier appris sur les années précédentes ; prévision du prix national
    à +horizon mois = prix actuel x (indice futur / indice actuel). Comparée à la
    méthode naïve (« le prix ne bouge pas »). Erreur moyenne absolue en %."""
    a1 = derniere_annee_complete(x)
    appris, _ = saisonnalite(x[x["date"].dt.year < a1])
    if appris is None:
        return None
    s = serie_nationale(x)
    err_s, err_n = [], []
    for t in s.index[(s.index.year == a1)]:
        cible = t + pd.DateOffset(months=horizon)
        if cible not in s.index:
            continue
        prev = s[t] * appris[cible.month - 1] / appris[t.month - 1]
        err_s.append(abs(prev - s[cible]) / s[cible] * 100)
        err_n.append(abs(s[t] - s[cible]) / s[cible] * 100)
    if len(err_s) < 6:
        return None
    return {"annee_testee": a1, "horizon_mois": horizon, "n": len(err_s),
            "erreur_tendance": round(sum(err_s) / len(err_s), 1), "erreur_naive": round(sum(err_n) / len(err_n), 1)}


SEUIL_FIGE = 4    # même prix au moins 4 mois de suite : valeur probablement reconduite


def plus_longue_serie_identique(prix: pd.Series) -> int:
    """Nombre maximal de mois consécutifs avec exactement le même prix (série mensuelle triée)."""
    if prix.empty:
        return 0
    meilleur = courant = 1
    valeurs = prix.round(2).tolist()
    for a, b in zip(valeurs, valeurs[1:]):
        courant = courant + 1 if a == b else 1
        meilleur = max(meilleur, courant)
    return meilleur


def prix_figes_recents(x: pd.DataFrame, mois: int = 12) -> int:
    """Pour un marché et un produit : plus longue série de prix identiques sur les derniers mois."""
    fin = x["date"].max()
    r = x[x["date"] > fin - pd.DateOffset(months=mois)]
    return plus_longue_serie_identique(r.groupby("date")["prix"].mean().sort_index())


def age_jours(date, reference) -> int:
    return int((pd.Timestamp(reference) - pd.Timestamp(date)).days)
