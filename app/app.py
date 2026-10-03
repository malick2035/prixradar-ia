"""
PrixRadar.IA : application Streamlit (prototype).

Lit les résultats calculés par scripts/preparer_donnees.py
(resultats/resultats_cles.json), pour que l'application affiche exactement
les mêmes chiffres que la documentation.
Source des données : Programme alimentaire mondial (PAM), via HDX, licence CC BY-IGO.
"""
import json
import pathlib
from datetime import date

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="PrixRadar.IA", page_icon="📡", layout="wide")

RACINE = pathlib.Path(__file__).resolve().parents[1]
MOIS = ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sep", "Oct", "Nov", "Déc"]
MOIS_LONG = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
             "septembre", "octobre", "novembre", "décembre"]
# Palette lisible par les personnes daltoniennes (bleu / orange), toujours doublée d'un libellé
MOINS_CHER, PLUS_CHER, NEUTRE = "#1B6FA8", "#C8572B", "#9AA8A3"
FRAICHEUR_MAX_JOURS = 60
COMMUNES_NON_SUIVIES = {"Atacora": ["Boukombé", "Kouandé", "Matéri", "Toucountouna"], "Donga": ["Copargo"]}


@st.cache_data
def charger():
    with open(RACINE / "resultats" / "resultats_cles.json", encoding="utf-8") as f:
        return json.load(f)


def mois_annee(aaaa_mm: str) -> str:
    a, m = aaaa_mm.split("-")
    return f"{MOIS_LONG[int(m) - 1]} {a}"


def virgule(n) -> str:
    """Nombre décimal à la française (13,4 au lieu de 13.4)."""
    return str(n).replace(".", ",")


def age_jours(aaaa_mm: str) -> int:
    return (date.today() - date(int(aaaa_mm[:4]), int(aaaa_mm[5:]), 15)).days


R = charger()

# ---------- Barre latérale ----------
st.sidebar.title("📡 PrixRadar.IA")
st.sidebar.caption("Le bon moment et le bon endroit pour acheter")
pays = st.sidebar.selectbox("Pays", ["Bénin", "Togo", "Niger", "Sénégal"])
produits = sorted(R["produits"][pays], key=str.lower)
produit = st.sidebar.selectbox("Produit", produits, index=produits.index("Tomates") if "Tomates" in produits else 0)
st.sidebar.markdown("---")
st.sidebar.caption(
    f"Prototype. Source : Programme alimentaire mondial (PAM), via HDX, licence CC BY-IGO. "
    f"Prix de détail en FCFA. Calcul du {R['meta']['date_calcul']}. "
    f"{R['meta']['valeurs_ecartees']:,} relevés aberrants écartés.".replace(",", " "))

x = R["produits"][pays][produit]
u = x["unite"]

# ---------- En-tête ----------
st.title("📡 PrixRadar.IA")
st.subheader(f"{produit} · {pays}")
st.caption(f"Prix de détail en FCFA par {u} · données jusqu'à {mois_annee(x['date_dernier'])}")
if age_jours(x["date_dernier"]) > FRAICHEUR_MAX_JOURS:
    st.warning(f"Le dernier prix connu date de {mois_annee(x['date_dernier'])}. "
               "Les données du PAM sont publiées avec un décalage : vérifiez sur le marché avant une décision importante.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Dernier prix connu", f"{x['dernier_prix']:,} FCFA".replace(",", " "), help="Médiane des marchés suivis")
if x["evolution_12_mois"] is not None:
    c2.metric("Sur 12 mois", f"{x['evolution_12_mois']:+d} %")
if x["saison"]:
    c3.metric("Mois habituellement le moins cher", MOIS_LONG[x["mois_moins_cher"] - 1])
    c4.metric("Écart moyen entre mois", f"{x['economie']} %", help="Entre le mois le plus cher et le moins cher")

onglets = ["📅 Quand acheter ?", "📍 Où acheter ?"]
if pays == "Bénin":
    onglets.append("🏘️ Départements et communes")
onglets += ["📈 Évolution des prix", "🌍 Comparer les pays"]
T = dict(zip(onglets, st.tabs(onglets)))

# ---------- Quand acheter ----------
with T["📅 Quand acheter ?"]:
    if not x["saison"]:
        st.info("Pas assez d'années complètes pour calculer la saisonnalité de ce produit.")
    else:
        s = pd.DataFrame({"Mois": MOIS, "Indice": x["saison"]})
        s["Repère"] = s["Indice"].apply(lambda v: "▼ Moins cher" if v < 97 else ("▲ Plus cher" if v > 103 else "Prix moyen"))
        if x.get("saison_q25"):
            s["Écart haut"] = [h - v for h, v in zip(x["saison_q75"], x["saison"])]
            s["Écart bas"] = [v - b for v, b in zip(x["saison"], x["saison_q25"])]
        fig = px.bar(s, x="Mois", y="Indice", color="Repère", text="Repère",
                     error_y="Écart haut" if "Écart haut" in s else None,
                     error_y_minus="Écart bas" if "Écart bas" in s else None,
                     color_discrete_map={"▼ Moins cher": MOINS_CHER, "▲ Plus cher": PLUS_CHER, "Prix moyen": NEUTRE})
        fig.add_hline(y=100, line_dash="dash", line_color="#555")
        fig.update_traces(textposition="outside", textfont_size=10)
        fig.update_layout(yaxis_title="Indice (100 = prix moyen de l'année)", xaxis_title="", height=460, legend_title="")
        st.plotly_chart(fig, width="stretch")
        st.success(f"Le prix est habituellement le plus bas en **{MOIS_LONG[x['mois_moins_cher'] - 1]}** et le plus haut "
                   f"en **{MOIS_LONG[x['mois_plus_cher'] - 1]}** (écart moyen : **{x['economie']} %**). "
                   "Planifiez vos achats en conséquence, sans constituer de stocks au-delà de vos besoins.")
        t = x.get("test_tendance")
        if t:
            if t["erreur_tendance"] <= 0.8 * t["erreur_naive"]:
                st.caption(f"✅ Profil testé sur {t['annee_testee']} : à 3 mois, erreur moyenne de {virgule(t['erreur_tendance'])} % "
                           f"contre {virgule(t['erreur_naive'])} % si l'on suppose que le prix ne bouge pas.")
            else:
                st.caption(f"⚠️ Profil indicatif : testé sur {t['annee_testee']}, il n'a pas mieux prévu les prix qu'une "
                           f"méthode simple ({virgule(t['erreur_tendance'])} % d'erreur contre {virgule(t['erreur_naive'])} %).")
        st.caption(f"Méthode : indice calculé marché par marché ({x['marches_saison']} marchés, fiabilité {x.get('fiabilite_saison', 'n.d.')}), "
                   "années complètes depuis 2020, médiane. Les traits verticaux montrent la plage où se situent la moitié des marchés et des années "
                   "(du 1er au 3e quartile) : plus ils sont longs, plus le profil varie d'un marché à l'autre.")

# ---------- Où acheter ----------
with T["📍 Où acheter ?"]:
    z = pd.DataFrame(x["zones"], columns=["Zone", "Prix", "Marchés"])
    if len(z) < 2:
        st.info("Pas assez de zones suivies récemment pour ce produit.")
    else:
        z["Repère"] = ["▼ Moins cher"] + ["Autres"] * (len(z) - 2) + ["▲ Plus cher"]
        fig = px.bar(z, x="Prix", y="Zone", orientation="h", text="Prix", color="Repère", hover_data=["Marchés"],
                     color_discrete_map={"▼ Moins cher": MOINS_CHER, "▲ Plus cher": PLUS_CHER, "Autres": NEUTRE})
        fig.update_layout(xaxis_title=f"Prix médian (FCFA/{u}), 12 derniers mois", yaxis_title="",
                          height=max(360, 40 * len(z)), legend_title="")
        st.plotly_chart(fig, width="stretch")
        st.success(f"**{z.Zone.iloc[0]}** : {z.Prix.iloc[0]} FCFA · **{z.Zone.iloc[-1]}** : {z.Prix.iloc[-1]} FCFA "
                   f"(**+{round((z.Prix.iloc[-1] / z.Prix.iloc[0] - 1) * 100)} %**).")
        faibles = z[z["Marchés"] <= 2]["Zone"].tolist()
        if faibles:
            st.warning("Fiabilité faible (1 ou 2 marchés suivis) pour : " + ", ".join(faibles) + ".")
        st.caption("Pour chaque marché : prix moyen des 12 derniers mois ; puis médiane par zone. "
                   "Le nombre de marchés par zone s'affiche au survol. Transport et taxes non compris.")

# ---------- Départements et communes (Bénin) ----------
if "🏘️ Départements et communes" in T:
    with T["🏘️ Départements et communes"]:
        par_dep = R["communes"].get(produit, {})
        deps = sorted(set(par_dep) | set(COMMUNES_NON_SUIVIES))
        dep = st.selectbox("Département", deps, index=deps.index("Atacora") if "Atacora" in deps else 0)
        lignes = par_dep.get(dep, [])
        manquantes = COMMUNES_NON_SUIVIES.get(dep, [])
        if not lignes:
            st.info(f"Pas de prix récents pour {produit} dans le département {dep}.")
        else:
            c = pd.DataFrame(lignes, columns=["Commune", "Marché", "Moyenne 3 mois", "Dernier prix", "Mois", "Relevés", "Prix identique (mois)"])
            c["Repère"] = ["▼ Moins cher"] + ["Autres"] * max(0, len(c) - 2) + (["▲ Plus cher"] if len(c) > 1 else [])
            fig = px.bar(c, x="Moyenne 3 mois", y="Commune", orientation="h", text="Moyenne 3 mois", color="Repère",
                         color_discrete_map={"▼ Moins cher": MOINS_CHER, "▲ Plus cher": PLUS_CHER, "Autres": NEUTRE})
            fig.update_layout(xaxis_title=f"FCFA/{u}, moyenne des 3 derniers mois", yaxis_title="",
                              height=max(260, 46 * len(c)), legend_title="")
            st.plotly_chart(fig, width="stretch")
            c["Mois"] = c["Mois"].map(mois_annee)
            st.dataframe(c.drop(columns="Repère"), hide_index=True, width="stretch")
            figes = c[c["Prix identique (mois)"] >= 4]
            if not figes.empty:
                st.warning("Prix à confirmer sur le terrain : le même prix a été publié plusieurs mois de suite à "
                           + ", ".join(f"{r.Commune} ({r['Prix identique (mois)']} mois)" for _, r in figes.iterrows())
                           + ". La valeur a peut-être été reconduite d'un mois à l'autre.")
        if manquantes:
            st.caption("Communes non suivies par le PAM dans ce département : " + ", ".join(manquantes)
                       + ". Elles seront couvertes par le réseau de collecteurs PrixRadar (pilote Atacora-Donga).")

# ---------- Évolution ----------
with T["📈 Évolution des prix"]:
    serie = pd.DataFrame(x["serie"], columns=["Mois", "Prix"])
    serie["Mois"] = pd.to_datetime(serie["Mois"])
    fig = px.line(serie, x="Mois", y="Prix")
    fig.update_traces(line_color="#16302B", line_width=3)
    fig.update_layout(xaxis_title="", yaxis_title=f"Prix médian national (FCFA/{u})", height=440)
    st.plotly_chart(fig, width="stretch")
    if x["hausse"] is not None:
        st.success(f"Entre **{x['hausse_debut']}** et **{x['hausse_fin']}**, sur les **{x['hausse_marches']} mêmes marchés**, "
                   f"le prix a évolué de **{x['hausse']:+d} %** (médiane des évolutions marché par marché, prix courants).")
    if x["chocs"] is not None:
        st.caption(f"Chocs de prix (variation de plus de 10 % en un mois) : {x['chocs']} % des mois depuis 2020.")

# ---------- Comparer les pays ----------
with T["🌍 Comparer les pays"]:
    comp = pd.DataFrame(R["comparaison"])
    cer = st.radio("Céréale", list(dict.fromkeys(comp["cereale"])), horizontal=True)
    cc = comp[comp["cereale"] == cer].copy()
    cc["Repère"] = ["▼ Moins cher" if v == cc["prix"].min() else "Autres" for v in cc["prix"]]
    fig = px.bar(cc, x="pays", y="prix", text="prix", color="Repère", hover_data=["marches", "periode_fin"],
                 color_discrete_map={"▼ Moins cher": MOINS_CHER, "Autres": NEUTRE})
    fig.update_layout(yaxis_title="Prix médian (FCFA/kg), 12 derniers mois", xaxis_title="", height=420, legend_title="")
    st.plotly_chart(fig, width="stretch")
    manq = {"Bénin", "Togo", "Niger", "Sénégal"} - set(cc["pays"])
    if manq:
        st.caption("Données insuffisantes pour : " + ", ".join(sorted(manq)) + ".")
    st.caption("Écarts indicatifs : transport, droits et règles aux frontières non compris.")

# ---------- Pied de page ----------
st.markdown("---")
st.markdown("**PrixRadar.IA** · prototype · [Code et documentation](https://github.com/malick2035/prixradar-ia) · "
            "Contact : data.malick9@gmail.com")
st.caption("PrixRadar.IA ne vous demandera jamais un code secret, un mot de passe ou un transfert d'argent. "
           "Les tendances passées ne garantissent pas les prix futurs.")
