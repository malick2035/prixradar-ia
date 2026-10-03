"""
Prépare toutes les données et tous les résultats de PrixRadar.IA.

Usage :  python scripts/preparer_donnees.py
Entrée : data/brut/wfp_food_prices_{ben,tgo,ner,sen}.csv (téléchargés sur HDX)
Sorties : data/prix_nettoyes_2019_2026.csv.gz, data/valeurs_ecartees.csv,
          resultats/resultats_cles.json, resultats/synthese_produits.csv
"""
import json, sys, pathlib, hashlib
from datetime import date
import pandas as pd
RACINE = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE))
from prixradar import calculs as C

def main():
    sources = {}
    for code in C.PAYS:
        f = RACINE / "data/brut" / f"wfp_food_prices_{code}.csv"
        sources[f.name] = {"sha256": hashlib.sha256(f.read_bytes()).hexdigest(), "octets": f.stat().st_size}
    brut = C.charger_brut(RACINE / "data/brut")
    propre, ecartes = C.nettoyer(brut)
    propre.to_csv(RACINE / "data/prix_nettoyes_2019_2026.csv.gz", index=False, compression="gzip")
    ecartes.to_csv(RACINE / "data/valeurs_ecartees.csv", index=False)

    res = {"meta": {"date_calcul": date.today().isoformat(), "version_methode": "1.0",
                    "releves_bruts_retenus": int(len(propre) + len(ecartes)), "releves_utilises": int(len(propre)),
                    "valeurs_ecartees": int(len(ecartes)),
                    "fin_des_donnees": {p: propre.loc[propre.pays == p, "date"].max().strftime("%Y-%m") for p in C.PAYS.values()},
                    "marches": {p: int(propre.loc[propre.pays == p, "marche"].nunique()) for p in C.PAYS.values()},
                    "fichiers_sources": sources, "source": "PAM via HDX, licence CC BY-IGO"},
           "produits": {}, "communes": {}, "comparaison": []}
    synth = []
    for pays, dp in propre.groupby("pays"):
        res["produits"][pays] = {}
        cnt = dp["produit"].value_counts()
        for prod in sorted(cnt[cnt >= 300].index):
            x = dp[dp["produit"] == prod]
            s, n_s = C.saisonnalite(x)
            h, n_h, a0, a1 = C.hausse_panel(x)
            nat = C.serie_nationale(x)
            prec = nat[nat.index <= nat.index[-1] - pd.DateOffset(months=12)]
            e = C.economie(s) if s else (None, None, None)
            zones = C.prix_par_zone(x)
            q25, q75 = C.saisonnalite_dispersion(x)
            r = {"unite": C.unite_de(x), "saison": s, "saison_q25": q25, "saison_q75": q75, "marches_saison": n_s,
                 "fiabilite_saison": C.niveau_fiabilite(n_s),
                 "economie": e[0], "mois_moins_cher": e[1], "mois_plus_cher": e[2],
                 "hausse": h, "hausse_marches": n_h, "hausse_debut": a0, "hausse_fin": a1,
                 "chocs": C.chocs(x), "dernier_prix": round(float(nat.iloc[-1])), "date_dernier": nat.index[-1].strftime("%Y-%m"),
                 "evolution_12_mois": None if prec.empty else round((nat.iloc[-1] / prec.iloc[-1] - 1) * 100),
                 "serie": [[t.strftime("%Y-%m"), round(float(v))] for t, v in nat[nat.index.year >= 2020].items()],
                 "zones": [[z.region, round(z.prix), int(z.marches)] for z in zones.itertuples()],
                 "test_tendance": C.test_tendance(x)}
            res["produits"][pays][prod] = r
            synth.append({"pays": pays, "produit": prod, "unite": r["unite"], "economie_pct": r["economie"],
                          "mois_moins_cher": r["mois_moins_cher"], "mois_plus_cher": r["mois_plus_cher"],
                          "hausse_pct": h, "periode_hausse": f"{a0}-{a1}", "marches_hausse": n_h, "chocs_pct": r["chocs"],
                          "dernier_prix": r["dernier_prix"], "date_dernier": r["date_dernier"]})
            if pays == "Bénin":
                pc = C.prix_par_commune(x)
                figes = {m: C.prix_figes_recents(xm) for m, xm in x.groupby("marche")}
                res["communes"][prod] = {reg: [[t.commune, t.marche, round(t.moyenne), round(t.dernier_prix), t.date_dernier.strftime("%Y-%m"),
                                                int(t.releves), figes.get(t.marche, 0)]
                                               for t in g.itertuples()] for reg, g in pc.groupby("region")}
    res["comparaison"] = C.comparaison_cereales(propre).to_dict("records")
    (RACINE / "resultats").mkdir(exist_ok=True)
    json.dump(res, open(RACINE / "resultats/resultats_cles.json", "w"), ensure_ascii=False, separators=(",", ":"))
    pd.DataFrame(synth).to_csv(RACINE / "resultats/synthese_produits.csv", index=False)
    print("Relevés utilisés :", len(propre), "| écartés :", len(ecartes))

if __name__ == "__main__":
    main()
