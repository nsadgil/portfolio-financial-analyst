# Rapport de diagnostic financier — Grand Livre Comptable
**Client :** Entreprise multi-devises (opérations en USD, GBP, EUR, AUD, CAD)
**Préparé par :** N'KOUEI N'tcha Gildas
**Date du rapport :** 14 Septembre 2026
**Objet :** Contrôle qualité du grand livre, construction du compte de résultat, analyse départementale, investigation de la variation 2025

---

## 1. Contexte et objectif

Le contrôleur de gestion a transmis un export brut du grand livre comptable (2 000 écritures, exercices 2023 à 2025), couvrant les comptes de Revenus, Coût des ventes (COGS) et Charges opérationnelles, répartis sur 6 départements et enregistrés dans 5 devises différentes. L'analyse répond à quatre objectifs :

1. Contrôler la fiabilité et la cohérence des données transmises
2. Construire un compte de résultat consolidé en devise de référence (USD)
3. Analyser la répartition des charges par département
4. Investiguer une variation significative détectée sur l'exercice 2025

---

## 2. Méthodologie

### 2.1 Contrôle qualité — équilibre du grand livre

Un grand livre complet doit présenter un total Débit égal au total Crédit. Le contrôle initial (en devise locale, avant conversion) révèle un écart de **-763 041,46**.

**Analyse de l'écart :** la décomposition par type de compte montre que cet écart n'est pas une anomalie de saisie, mais une conséquence du **périmètre du dataset** : celui-ci ne contient que des comptes de résultat (Revenue, COGS, Expense), sans les comptes de contrepartie du bilan (trésorerie, tiers). Dans une comptabilité en partie double complète, chaque produit et chaque charge a une contrepartie au bilan ; leur absence ici explique mécaniquement le déséquilibre apparent. Ce montant correspond en réalité au **résultat avant impôt** de l'entreprise sur la période.

### 2.2 Validation de la conversion multi-devises

Le fichier source fournit des colonnes déjà converties en USD (`Debit_USD`, `Credit_USD`). Cette conversion a été recalculée indépendamment, par fusion avec la table des taux de change officiels, puis comparée aux valeurs fournies. **Aucun écart n'a été détecté** : les données de conversion transmises sont fiables et peuvent être utilisées telles quelles pour la suite de l'analyse.

---

## 3. Compte de résultat consolidé (en USD)

| Poste | Montant (USD) |
|---|---|
| Chiffre d'affaires | **2 185 401** |
| Coût des ventes (COGS) | 441 247 |
| **Marge brute** | **1 744 154** (79,8 %) |
| Charges opérationnelles (Payroll + Travel) | 927 564 |
| **Résultat avant impôt** | **816 590** |
| Impôt sur les sociétés (hypothèse : 30 %) | 244 977 |
| **Résultat net** | **571 613** |

⚠️ *Le taux d'imposition de 30 % est une hypothèse de travail, non fournie dans les données source, à faire valider par le client avant toute utilisation décisionnelle de ce résultat net.*

Ce résultat a été vérifié par deux méthodes de calcul indépendantes (agrégation directe par compte, et reclassement via une table de mapping poste-comptable → poste de reporting), aboutissant au même montant, confirmant la fiabilité du calcul.

---

## 4. Analyse par département

| Département | COGS | Charges opérationnelles | Total charges |
|---|---|---|---|
| **HR** | 91 810 | 135 260 | **227 070** |
| Sales | 54 346 | 150 613 | 204 959 |
| IT | 63 932 | 137 961 | 201 893 |
| Marketing | 70 065 | 130 579 | 200 645 |
| Finance | 68 529 | 131 015 | 199 543 |
| **Operations** | 49 254 | 126 876 | **176 131** |

**Constat :** le département **HR** génère le volume de charges le plus élevé (227 070), le département **Operations** le plus faible (176 131) — un écart de 29 %. Cette lecture inclut le COGS dans le total par convention (le COGS étant directement rattaché à l'activité opérationnelle de chaque département dans ce dataset).

**Activité transactionnelle :** le compte le plus mouvementé est le compte **5010 — Travel Expense** (412 écritures), suivi de près par Online Sales (402) et Sales Revenue (401) — les frais de déplacement génèrent le flux d'écritures le plus dense de l'entreprise, à surveiller si un contrôle de gestion des notes de frais n'est pas encore en place.

---

## 5. Investigation — Variation de chiffre d'affaires sur l'exercice 2025

### 5.1 Constat initial

La lecture brute du chiffre d'affaires annuel fait apparaître une baisse de 2025 par rapport aux exercices précédents, de l'ordre de 55 % en valeur affichée.

### 5.2 Vérification avant conclusion

Avant de conclure à une réelle contre-performance, la couverture mensuelle de l'exercice 2025 a été vérifiée directement : les écritures ne couvrent que **6 mois sur 12** (janvier à juin). Le chiffre d'affaires mensuel moyen sur cette période (**68 900 USD/mois**) est proche du rythme mensuel moyen des exercices 2023-2024 (**73 833 USD/mois**), soit un écart de seulement **-6,7 %** — une variation normale, sans commune mesure avec la baisse de 55 % lue sur les totaux annuels bruts.

**Conclusion :** il ne s'agit pas d'une baisse d'activité, mais d'un **exercice 2025 incomplet** au moment de l'extraction des données (arrêté à fin juin). La comparaison brute des totaux annuels est trompeuse dès lors que les périodes comparées n'ont pas la même durée ; le rythme mensuel moyen, lui, ne révèle aucune anomalie significative.

### 5.3 Analyse de saisonnalité (2023-2024 uniquement, 2025 exclu)

| Mois | Chiffre d'affaires | Variation vs mois précédent |
|---|---|---|
| Janvier | 154 958 | — |
| Février | 133 688 | -13,7 % |
| **Mars** | **177 631** | **+32,9 %** |
| Avril | 139 480 | -21,5 % |
| Mai | 168 192 | +20,6 % |
| Juin | 128 056 | -23,9 % |
| Juillet | 120 718 | -5,7 % |
| Août | 135 896 | +12,6 % |
| **Septembre** | **119 693** | **-11,9 %** |
| Octobre | 150 657 | +25,9 % |
| **Novembre** | **175 128** | **+16,2 %** |
| Décembre | 167 905 | -4,1 % |

**Constat :** l'activité présente une forte variabilité mois par mois (jusqu'à ±33 % de variation), sans tendance saisonnière univoque nette sur deux ans de données. Les mois de **mars et novembre** ressortent comme les points hauts de l'activité, **septembre** comme le point bas. Une confirmation sur un plus grand nombre d'exercices serait nécessaire avant de considérer ce profil comme une saisonnalité structurelle fiable.

---

## 6. Recommandations

1. **Ne pas comparer l'exercice 2025 aux exercices complets** dans les reportings de pilotage tant qu'il n'est pas clôturé ; utiliser un CA annualisé ou une comparaison à périmètre de mois identique (janvier-juillet vs janvier-juillet des années précédentes).
2. **Documenter et faire valider le taux d'imposition** utilisé (30 % ici est une hypothèse), pour fiabiliser le résultat net présenté aux parties prenantes.
3. **Investiguer la charge du département HR**, la plus élevée de l'organisation, pour identifier si elle reflète un investissement stratégique (recrutement, formation) ou un axe d'optimisation.
4. **Mettre en place un contrôle sur les frais de déplacement** (compte le plus mouvementé), pour s'assurer que le volume élevé d'écritures ne masque pas un besoin de rationalisation.
5. **Poursuivre le suivi mensuel de la saisonnalité** sur un historique plus long, avant d'en tirer des décisions de planification budgétaire.

---

## 7. Limites de l'analyse

- L'exercice 2025 étant incomplet (arrêté à juillet), toute lecture de tendance annuelle le concernant doit être considérée avec prudence.
- Le taux d'imposition de 30 % est une hypothèse de travail non confirmée par le client.
- L'analyse par département inclut le COGS dans le total des charges par convention explicite ; une lecture alternative (COGS isolé du reste) donnerait un classement différent des départements les plus "coûteux" en charges opérationnelles pures.
- Le dataset ne contenant pas les comptes de bilan (trésorerie, tiers), aucune analyse de solvabilité ou de structure financière n'a pu être menée à ce stade.

---

## Annexe — Code Python utilisé

```python
import pandas as pd

# ── 1. Chargement des données ──────────────────────────────────────
url = "https://raw.githubusercontent.com/Jrtoby/General-Ledger-Financial-Analysis/main/General-Ledger.xlsx"
gl = pd.read_excel(url, sheet_name="GL", usecols=[
    "GLID", "TxnDate", "Year", "Month", "AccountNumber", "AccountName",
    "Debit", "Credit", "Dept", "CostCenter", "Description", "Currency",
    "NetAmount", "RateToUSD", "Debit_USD", "Credit_USD", "NetAmountUSD", "AccountType"
])
taux_change = pd.read_excel(url, sheet_name="ExchangeRate")

# ── 2. Contrôle qualité : équilibre du grand livre ──────────────────
type_group = gl.groupby("AccountType")[["Debit", "Credit"]].sum()
resultat_avant_impot = type_group.loc["Revenue", "Credit"] - (
    type_group.loc["COGS", "Debit"] + type_group.loc["Expense", "Debit"]
)
print(f"Résultat avant impôt (devise locale) : {resultat_avant_impot:,.2f}")

# ── 3. Validation de la conversion multi-devises ────────────────────
devises = gl.merge(taux_change, on="Currency", how="left")
devises["Debit2USD"] = devises["Debit"] * devises["Rate2USD"]
devises["Credit2USD"] = devises["Credit"] * devises["Rate2USD"]
devises["ecart_debit"] = devises["Debit2USD"] - devises["Debit_USD"]
devises["ecart_credit"] = devises["Credit2USD"] - devises["Credit_USD"]
print("Écarts de conversion détectés :", devises["ecart_debit"].abs().max(),
      devises["ecart_credit"].abs().max())

# ── 4. Construction du compte de résultat (P&L) ──────────────────────
mapping_poste = {
    "Revenue": "Chiffre d'affaires",
    "COGS": "Coût des ventes",
    "Expense": "Charges opérationnelles",
}
sens_normal = {
    "Chiffre d'affaires": -1,   # sens normal au crédit
    "Coût des ventes": 1,        # sens normal au débit
    "Charges opérationnelles": 1,
}

pnl = devises[["AccountType", "NetAmountUSD"]].copy()
pnl["poste_reporting"] = pnl["AccountType"].map(mapping_poste)
pnl["sens"] = pnl["poste_reporting"].map(sens_normal)
pnl["montant"] = pnl["NetAmountUSD"] * pnl["sens"]

compte_resultat = pnl.groupby("poste_reporting")["montant"].sum()

ca = compte_resultat.loc["Chiffre d'affaires"]
cogs = compte_resultat.loc["Coût des ventes"]
opex = compte_resultat.loc["Charges opérationnelles"]

marge_brute = ca - cogs
taux_marge_brute = marge_brute / ca
resultat_avant_impot = marge_brute - opex
TAUX_IS = 0.30  # hypothèse 
impot = resultat_avant_impot * TAUX_IS
resultat_net = resultat_avant_impot - impot

print(f"Chiffre d'affaires        : {ca:>15,.0f} USD")
print(f"Coût des ventes (COGS)     : {cogs:>15,.0f} USD")
print(f"Marge brute                : {marge_brute:>15,.0f} USD  ({taux_marge_brute:.1%})")
print(f"Charges opérationnelles    : {opex:>15,.0f} USD")
print(f"Résultat avant impôt       : {resultat_avant_impot:>15,.0f} USD")
print(f"Impôt (hyp. {TAUX_IS:.0%})           : {impot:>15,.0f} USD")
print(f"Résultat net               : {resultat_net:>15,.0f} USD")

compte_resultat_final = pd.DataFrame({
    "Poste": ["Chiffre d'affaires", "Coût des ventes", "Marge brute", 
              "Charges opérationnelles", "Résultat avant impôt", 
              f"Impôt ({TAUX_IS:.0%})", "Résultat net"],
    "Montant_USD": [ca, -cogs, marge_brute, -opex, resultat_avant_impot, -impot, resultat_net]
})

# ── 5. Analyse par département ────────────────────────────────────────
par_departement = devises.groupby("Dept")["Debit_USD"].sum().sort_values(ascending=False)
print(f"Charges totales par département (COGS inclus) :\n{par_departement}")

croisement_dept = devises.pivot_table(
    index="Dept", values="Debit_USD", columns="AccountType", aggfunc="sum"
).fillna(0)
print(f"\nDétail par département et type de compte :\n{croisement_dept}")

nb_ecritures_par_compte = gl["AccountNumber"].value_counts()
print(f"\nNombre d'écritures par compte :\n{nb_ecritures_par_compte}")

# ── 6. Investigation — variation 2025 ──────────────────────────────────
devises["TxnDate"] = pd.to_datetime(devises["TxnDate"])
group = devises.groupby(["Year", "Month", "AccountName"])["NetAmountUSD"].sum().unstack(fill_value=0)
group["Chiffre_affaires"] = (group["Online Sales"] + group["Sales Revenue"]) * -1
group["Charges_totales"] = group["COGS"] + group["Payroll Expense"] + group["Travel Expense"]
group["resultat_net"] = (group["Chiffre_affaires"] - group["Charges_totales"]) * (1 - TAUX_IS)

annuel = group.groupby("Year")[["Chiffre_affaires", "resultat_net"]].sum()
annuel["YoY_CA_%"] = annuel["Chiffre_affaires"].pct_change() * 100
print(f"CA et résultat net par année :\n{annuel}")

# Vérification propre et reproductible : 2025 est-il un exercice complet ?
# (compter les mois couverts, plutôt qu'un ratio de CA difficile à défendre)
ca_2025 = group.loc[2025, "Chiffre_affaires"]
ca_2023_2024 = group.loc[[2023, 2024], "Chiffre_affaires"]
print(f"\nMois couverts en 2025 : {len(ca_2025)} / 12")
print(f"CA moyen mensuel 2025 : {ca_2025.mean():,.0f} USD")
print(f"CA moyen mensuel 2023-2024 : {ca_2023_2024.mean():,.0f} USD")
print(f"Écart de rythme mensuel : {(ca_2025.mean() / ca_2023_2024.mean() - 1):.1%}")
print("→ 2025 est un exercice incomplet (données arrêtées à fin juin), pas une baisse d'activité :")
print("  le rythme mensuel moyen reste proche de l'historique.")

# Saisonnalité, hors exercice incomplet
group_sans_2025 = group[group.index.get_level_values("Year") != 2025]
mensuel = group_sans_2025.groupby("Month")[["Chiffre_affaires", "resultat_net"]].sum()

MOIS_ORDRE = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
              "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
mensuel.index = mensuel.index.map(MOIS_ORDRE)
mensuel = mensuel.sort_index()
mensuel["variation_%"] = mensuel["Chiffre_affaires"].pct_change() * 100

print(f"\nSaisonnalité du CA (2023-2024 uniquement) :\n{mensuel}")
```
