"""
AfriTech Distribution -- Analyse statistique des ventes (2024-2025)
Script consolide (base : travail autonome de l'analyste, corrections mineures de forme appliquees)
"""
import sqlite3
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ── Accès aux data ─────────────────────────────────────────────
DB_PATH = "./data/afritech_distribution_v2.db"  
OUT = "./outputs" 
Path(OUT).mkdir(parents=True, exist_ok=True) 

connexion = sqlite3.connect(DB_PATH)

ventes = pd.read_sql_query("SELECT * FROM ventes", connexion)
produits = pd.read_sql_query("SELECT * FROM produits", connexion)
connexion.close()

ventes["date_vente"] = pd.to_datetime(ventes["date_vente"])
ventes["mois"] = ventes["date_vente"].dt.strftime("%Y-%m")
ventes["ca"] = ventes["quantite"] * ventes["prix_unitaire"] * (1 - ventes["remise_pct"] / 100.0)
ventes_produits = ventes.merge(produits, on="produit_id", how="left")

# ── A. Tendance centrale ─────────────────────────────────────────────
ca_total = ventes["ca"].sum()
ca_pays = ventes.groupby("pays")["ca"].sum()
ca_moyen = ventes["ca"].mean()
ca_median = ventes["ca"].median()

stats_pays = ventes.groupby("pays")["ca"].agg(["mean", "median"])
stats_pays["ecart_pct"] = (stats_pays["mean"] - stats_pays["median"]) / stats_pays["median"]

# ── B. Volatilite ─────────────────────────────────────────────────────
std_global = ventes["ca"].std()
std_categorie = ventes_produits.groupby("categorie")["ca"].std().sort_values(ascending=False)

# ── C. Detection d'anomalies ─────────────────────────────────────────
Q1 = ventes["ca"].quantile(0.25)
Q3 = ventes["ca"].quantile(0.75)
IQR = Q3 - Q1
seuil_bas = Q1 - 1.5 * IQR
seuil_haut = Q3 + 1.5 * IQR

outliers = ventes[(ventes["ca"] < seuil_bas) | (ventes["ca"] > seuil_haut)]
proportion_outliers = outliers["ca"].sum() / ventes["ca"].sum()

# ── D. Correlations / drivers ─────────────────────────────────────────
qte_ca = ventes["quantite"].corr(ventes["ca"])
prix_ca = ventes["prix_unitaire"].corr(ventes["ca"])

corr_cat_qte = ventes_produits.groupby("categorie").apply(lambda y: y["quantite"].corr(y["ca"]), include_groups=False)
corr_cat_prix = ventes_produits.groupby("categorie").apply(lambda y: y["prix_unitaire"].corr(y["ca"]), include_groups=False)

# ── Graphiques ─────────────────────────────────────────────────────────
sns.set_theme(style="darkgrid")

plt.figure(figsize=(15, 8))
plt.subplot(1, 2, 1)
sns.boxplot(y=ventes["ca"], color="skyblue", flierprops={"markerfacecolor": "red", "marker": "o"})
plt.title("Distribution globale du CA\n(points rouges = outliers)", fontsize=12, fontweight="bold")
plt.ylabel("Chiffre d'affaires (EUR)")

plt.subplot(1, 2, 2)
ordre_categories = ventes_produits.groupby("categorie")["ca"].median().sort_values(ascending=False).index
sns.boxplot(x="categorie", y="ca", data=ventes_produits, order=ordre_categories, hue="categorie", palette="Set2", legend=False)
plt.title("Dispersion du CA par categorie", fontsize=12, fontweight="bold")
plt.xlabel("Categorie")
plt.ylabel("")
plt.tight_layout()
plt.savefig(f"{OUT}/dispersion_ca.png", dpi=200)
plt.close()

plt.figure(figsize=(9, 6))
sns.regplot(x="prix_unitaire", y="ca", data=ventes, scatter_kws={"alpha": 0.5})
plt.title("Relation entre prix unitaire et chiffre d'affaires", fontsize=12, fontweight="bold")
plt.xlabel("Prix unitaire (EUR)")
plt.ylabel("Chiffre d'affaires (EUR)")
plt.tight_layout()
plt.savefig(f"{OUT}/correlation_prix_ca.png", dpi=200)
plt.close()

with pd.ExcelWriter(f"{OUT}/afritech_distribution_stats.xlsx") as writer:
    ca_pays.to_excel(writer, sheet_name="CA par pays")
    stats_pays.to_excel(writer, sheet_name="Tendance CA par pays")
    std_categorie.to_excel(writer, sheet_name="Volatilite par categorie")
    outliers.to_excel(writer, sheet_name="Ventes suspectes", index=False)
    corr_cat_prix.to_excel(writer, sheet_name="Correlation sectorielle prix")
    corr_cat_qte.to_excel(writer, sheet_name="Correlation sectorielle qte")

print("CA total:", ca_total)
print("moyenne/mediane:", ca_moyen, ca_median)
print(stats_pays)
print("std global:", std_global)
print(std_categorie)
print("Q1,Q3,IQR:", Q1, Q3, IQR, "seuils:", seuil_bas, seuil_haut)
print("nb outliers:", len(outliers), "proportion:", proportion_outliers)
print("corr qte/prix:", qte_ca, prix_ca)
print(corr_cat_qte)
print(corr_cat_prix)
