"""
AfriTech Distribution — Analyse commerciale et financiere consolidee (2024-2025)
Script corrige et complet : correction, agregation, jointures, sous-requete, fonctions de fenetrage.
"""
import sqlite3
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# ── 1. Connexion et corrections de donnees (A) ──────────────────────────────
DB_PATH = "./data/afritech_distribution_v2.db"
OUT = "./outputs"
Path(OUT).mkdir(parents=True, exist_ok=True)

connexion = sqlite3.connect(DB_PATH)

connexion.execute("DELETE FROM ventes WHERE produit_id = 7")
connexion.execute(
    "INSERT OR IGNORE INTO produits(produit_id, nom_produit, categorie, prix_vente_base, prix_achat) "
    "VALUES (16, 'Webcam HD', 'Accessoires', 22000, 12000)"
)
connexion.execute("UPDATE ventes SET remise_pct = 0 WHERE produit_id = 14")
connexion.commit()

# Rechargement APRES corrections : indispensable pour travailler sur des donnees a jour
ventes = pd.read_sql_query("SELECT * FROM ventes", connexion)
produits = pd.read_sql_query("SELECT * FROM produits", connexion)
objectifs = pd.read_sql_query("SELECT * FROM objectifs_mensuels", connexion)

ventes["date_vente"] = pd.to_datetime(ventes["date_vente"])
ventes["mois"] = ventes["date_vente"].dt.strftime("%Y-%m")
ventes["CA"] = ventes["quantite"] * ventes["prix_unitaire"] * (1 - ventes["remise_pct"] / 100)

# ── 2. CA par pays et par categorie (B, corrige : /100.0) ───────────────────
ca_pays = ventes.groupby("pays")["CA"].sum().sort_values(ascending=False)

ventes_cat = ventes.merge(produits, on="produit_id", how="left")
ca_categorie = ventes_cat.groupby("categorie")["CA"].sum().sort_values(ascending=False)

# Version SQL corrigee (division flottante), utilisee pour validation croisee
requete_categorie = """
SELECT p.categorie, SUM((v.quantite * v.prix_unitaire) * (1 - v.remise_pct / 100.0)) AS CA
FROM ventes v
LEFT JOIN produits p ON v.produit_id = p.produit_id
GROUP BY p.categorie
ORDER BY CA DESC
"""
ca_categorie_sql = pd.read_sql_query(requete_categorie, connexion)

requete_top_pays = """
SELECT pays, SUM((quantite * prix_unitaire) * (1 - remise_pct / 100.0)) AS CA
FROM ventes
GROUP BY pays
HAVING CA > 150000000
ORDER BY CA DESC
"""
top_pays = pd.read_sql_query(requete_top_pays, connexion)

# ── 3. Classification des ventes par tranche (D) ────────────────────────────
requete_classement = """
WITH ventes_calc AS (
    SELECT id_vente, (quantite * prix_unitaire) * (1 - remise_pct / 100.0) AS CA
    FROM ventes
)
SELECT id_vente, CA,
    CASE WHEN CA < 100000 THEN 'Petite vente'
         WHEN CA < 500000 THEN 'Vente moyenne'
         ELSE 'Grosse vente' END AS classement_CA
FROM ventes_calc
"""
classement = pd.read_sql_query(requete_classement, connexion)
repartition_tranches = classement["classement_CA"].value_counts()

# ── 4. Sous-requete corrigee (E) : produits au-dessus du prix catalogue moyen
requete_produits_top = """
SELECT nom_produit, prix_vente_base
FROM produits
WHERE prix_vente_base > (SELECT AVG(prix_vente_base) FROM produits)
ORDER BY prix_vente_base DESC
"""
produits_top = pd.read_sql_query(requete_produits_top, connexion)

ca_produits_top = (
    ventes_cat[ventes_cat["nom_produit"].isin(produits_top["nom_produit"])]
    .groupby("nom_produit")["CA"].sum()
    .sort_values(ascending=False)
)

# ── 5. Ecart budgetaire reel vs objectif (C) ────────────────────────────────
ca_mensuel_pays = ventes.groupby(["pays", "mois"])["CA"].sum().reset_index()
ecart_budget = ca_mensuel_pays.merge(objectifs, on=["pays", "mois"], how="left")
ecart_budget["ecart_pct"] = ecart_budget["CA"] / ecart_budget["objectif_ca"]

# Investigation Ghana (objectifs manquants avant juillet 2024)
ghana_sans_objectif = ecart_budget[
    (ecart_budget["pays"] == "Ghana") & (ecart_budget["objectif_ca"].isna())
]
nb_mois_ghana_sans_objectif = ghana_sans_objectif.shape[0]
ca_ghana_sans_objectif = ghana_sans_objectif["CA"].sum()
ca_ghana_total = ecart_budget[ecart_budget["pays"] == "Ghana"]["CA"].sum()

# ── 6. Fonctions de fenetrage — evolution mensuelle (F) ─────────────────────
requete_variation = """
WITH calcul AS (
    SELECT STRFTIME('%Y-%m', date_vente) AS mois,
           SUM((quantite * prix_unitaire) * (1 - remise_pct / 100.0)) AS ca_total
    FROM ventes GROUP BY mois
)
SELECT mois, ca_total,
    LAG(ca_total, 1) OVER (ORDER BY mois) AS ca_precedent,
    ca_total - LAG(ca_total, 1) OVER (ORDER BY mois) AS variation_absolue,
    ROUND((ca_total - LAG(ca_total,1) OVER (ORDER BY mois)) * 100.0
          / NULLIF(LAG(ca_total,1) OVER (ORDER BY mois), 0), 2) AS variation_pct,
    SUM(ca_total) OVER (ORDER BY mois ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS ca_cumule,
    ROUND(AVG(ca_total) OVER (ORDER BY mois ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS moyenne_mobile_3m
FROM calcul ORDER BY mois
"""
evolution_mensuelle = pd.read_sql_query(requete_variation, connexion)

requete_rang = """
WITH calcul AS (
    SELECT pays, SUM((quantite * prix_unitaire) * (1 - remise_pct / 100.0)) AS ca_total
    FROM ventes GROUP BY pays
)
SELECT pays, ca_total, RANK() OVER (ORDER BY ca_total DESC) AS rang
FROM calcul ORDER BY ca_total DESC
"""
rang_pays = pd.read_sql_query(requete_rang, connexion)

connexion.close()

# ── 7. Graphiques ────────────────────────────────────────────────────────────
plt.style.use("seaborn-v0_8-whitegrid")

plt.figure(figsize=(6, 6))
plt.pie(ca_pays.values, labels=ca_pays.index, autopct="%1.1f%%", colors=sns.color_palette("viridis", 5))
plt.title("Repartition du chiffre d'affaires par pays (2024-2025)", fontweight="bold")
plt.tight_layout()
plt.savefig(f"{OUT}/ca_par_pays.png", dpi=150)
plt.close()

plt.figure(figsize=(8, 5))
sns.barplot(x=ca_categorie.values, y=ca_categorie.index, hue=ca_categorie.index, palette="mako", legend=False)
plt.title("Chiffre d'affaires par categorie de produits", fontweight="bold")
plt.xlabel("Chiffre d'affaires (EUR)")
plt.ylabel("")
plt.tight_layout()
plt.savefig(f"{OUT}/ca_par_categorie.png", dpi=150)
plt.close()

fig, ax1 = plt.subplots(figsize=(11, 5))
ax1.plot(evolution_mensuelle["mois"], evolution_mensuelle["ca_total"], marker="o", label="CA mensuel", color="steelblue")
ax1.plot(evolution_mensuelle["mois"], evolution_mensuelle["moyenne_mobile_3m"], linestyle="--", label="Moyenne mobile 3 mois", color="darkorange")
ax1.set_xticks(range(0, len(evolution_mensuelle), 2))
ax1.set_xticklabels(evolution_mensuelle["mois"][::2], rotation=45, ha="right")
ax1.set_ylabel("Chiffre d'affaires (EUR)")
ax1.set_title("Evolution mensuelle du chiffre d'affaires (2024-2025)", fontweight="bold")
ax1.legend()
plt.tight_layout()
plt.savefig(f"{OUT}/evolution_mensuelle_ca.png", dpi=150)
plt.close()

plt.figure(figsize=(7, 4.5))
sns.barplot(x=rang_pays["ca_total"], y=rang_pays["pays"], hue=rang_pays["pays"], palette="crest", legend=False)
plt.title("Classement des pays par chiffre d'affaires total", fontweight="bold")
plt.xlabel("Chiffre d'affaires (EUR)")
plt.ylabel("")
plt.tight_layout()
plt.savefig(f"{OUT}/classement_pays.png", dpi=150)
plt.close()

# ── 8. Export Excel corrige (feuille "Ca par produit" recalculee) ──────────
with pd.ExcelWriter(f"{OUT}/rapport_ventes_afritech_corrige.xlsx") as writer:
    ca_pays.to_excel(writer, sheet_name="CA par pays")
    rang_pays.to_excel(writer, sheet_name="TOP pays", index=False)
    ca_categorie.to_excel(writer, sheet_name="CA par categorie")
    ecart_budget.to_excel(writer, sheet_name="Ecart budgetaire", index=False)
    ca_produits_top.to_excel(writer, sheet_name="CA produits premium")
    evolution_mensuelle.to_excel(writer, sheet_name="Evolution mensuelle CA", index=False)
    repartition_tranches.to_excel(writer, sheet_name="Repartition tranches CA")
    produits_top.to_excel(writer, sheet_name="Produits prix superieur moy", index=False)

# ── 9. Sorties pour le rapport ───────────────────────────────────────────────
print("=== CA par pays ===")
print(ca_pays)
print("\n=== CA par categorie (pandas) ===")
print(ca_categorie)
print("\n=== CA par categorie (SQL corrige) ===")
print(ca_categorie_sql)
print("\n=== Top pays > 150M (SQL corrige) ===")
print(top_pays)
print("\n=== Repartition tranches ===")
print(repartition_tranches)
print("\n=== Produits au-dessus du prix moyen catalogue ===")
print(produits_top)
print("\n=== CA genere par ces produits premium ===")
print(ca_produits_top)
print("\n=== Ghana - mois sans objectif ===", nb_mois_ghana_sans_objectif)
print("CA Ghana sans objectif :", ca_ghana_sans_objectif, "/ CA Ghana total :", ca_ghana_total,
      f"({ca_ghana_sans_objectif/ca_ghana_total:.1%})")
print("\n=== Evolution mensuelle (extrait) ===")
print(evolution_mensuelle.head(6))
print("\n=== Classement pays (rang) ===")
print(rang_pays)

ca_total_global = ca_pays.sum()
print("\nCA TOTAL GLOBAL:", ca_total_global)
