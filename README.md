<img width="1200" height="600" alt="image" src="https://github.com/user-attachments/assets/a9d49e18-d1af-4676-8190-1c3bad662b30" />

# Portfolio Financial Analyst - Data - Reporting & Due Diligence 

> De la donnée brute à la décision financière : Analyse commerciale, Comptabilité & Due Diligence

📍 Cotonou, Bénin - Remote 🌍 | 🕒 Réponse < 12h

---

## 📊 Projets phares

### 1. P&L Bridge - Volume / Prix / Mix / COGS / FX
Explication d'une variation de marge brute entre N et N-1.
- Construction du bridge complet
- Visualisation Waterfall

→ Voir le projet : [03-bridge/ - Bridge de Marge](./03-bridge/)

### 2. Dashboard Finance
Dashboard interactif pour pilotage mensuel.
- P&L / Bilan / TFT
- BFR / Trésorerie

→ Voir le projet : [04-kossou/ - Audit & Reporting](./04-kossou/)

---

## 📈 Cas pratique : Analyse de saisonnalité (Données réelles)

Analyse de 12 mois pour identifier pics, creux et leviers de marge.

**Insights clés :**
- **Mars :** Pic d'activité +32,87% MoM (CA 177 631€, Résultat 61 191€)
- **Septembre :** Anomalie critique - Résultat net chute à 4 802€ (-85%)
- **Q4 :** 38% du CA annuel concentré sur Oct-Nov-Dec = forte saisonnalité fin d'année
- **Marge moyenne :** ~31% avec volatilité liée au COGS

**Méthodologie :** Nettoyage balance -> Calcul MoM% -> Visualisation bi-axes CA/Résultat vs Variation

**Fichiers :** `data/` contient les sources Excel nettoyées.

---

## 🛠️ Stack
Excel Avancé | Power BI (DAX, Power Query) | Python (Pandas) | P&L, Budget vs Actual, Bridge

## 📬 Contact - **Disponible pour missions FP&A / Contrôle de gestion**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gildasnk/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:nsadgil@gmail.com)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/22968175942)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/gildasnk)

---

<details>
<summary>🔍 Voir le détail technique complet (SQL, Python, IQR, Window Functions)</summary>

    Ce repository regroupe 3 projets complets réalisés sur données réelles (2024-2025) : analyse commerciale 360°, comptabilité générale et due diligence commerciale par bridge de marge.
    
---

## 📁 Structure du Repository
    ├── 01-afritech/              # Analyse 360° AfriTech
    │   ├── data/
    │   │   ├── afritech_v1_raw.db
    │   │   └── afritech_v2_clean.db
    │   ├── outputs/
    │   │   ├── ca_par_pays.png
    │   │   ├── ca_par_categorie.png
    │   │   ├── dispersion_ca.png
    │   │   └── correlation_prix_ca.png
    │   ├── sql/
    │   │   ├── afritech_analysis.xlsx
    │   │   ├── analyse_commerciale.py
    │   │   └── rapport_ventes_afritech.md
    │   ├── stats/
    │   │   ├── afritech_stats.xlsx
    │   │   ├── analyse_statistique.py
    │   │   └── rapport_stats_afritech.md
    │   ├── viz_plt_sns.py        # Visualisation avec Matplotlib & Seaborn
    │   │
    │   └── README.md
    │
    ├── 02-grand-livre/            # P&L & Saisonnalité
    │   ├── analysis_general_ledger.ipynb
    │   ├── compte_resultat_usd.xlsx
    │   ├── rapport_grand_livre.md
    │   └── README.md
    │
    ├── 03-bridge/                 # Bridge de Marge - Due Diligence
    │   ├── bridge_assets/
    │   │   ├── bridge_cascade_pays.png
    │   │   └── bridge_cascade_produits.png
    │   ├── bridge_afritech_analyse.xlsx
    │   ├── rapport_afritech_gestion.md
    │   ├── rapport_due_diligence.md
    │   └── README.md
    │
    ├── 04-kossou/                 # Audit & Reporting Financier
    │   ├── data/
    │   │   └── balance_comptable_brute.xlsx
    │   ├── kossou_reporting_financier.xlsx
    │   ├── rapport_mission.md
    │   └── README.md
    │
    └── README.md   


## 🚀 Accès rapide
| Projet | Dossier | Fichiers clés |
| :--- | :--- | :--- |
| **AfriTech** | [01-afritech/](./01-afritech/) | [SQL](./01-afritech/sql/) · [Stats](./01-afritech/stats/) · [Outputs](./01-afritech/outputs/) |
| **Grand-Livre** | [02-grand-livre/](./02-grand-livre/) | [P&L Excel](./02-grand-livre/compte_resultat_usd.xlsx) · [Notebook](./02-grand-livre/analysis_general_ledger.ipynb) |
| **Bridge** | [03-bridge/](./03-bridge/) | [Excel N1-N4](./03-bridge/bridge_afritech_analyse.xlsx) · [Waterfalls](./03-bridge/bridge_assets/) |
| **Kossou** | [04-kossou/](./04-kossou/) | [Balance](./04-kossou/data/balance_comptable_brute.xlsx) · [Reporting](./04-kossou/kossou_reporting_financier.xlsx) |

## 01 - AfriTech - Analyse Commerciale 360°

**SQL & Data Cleaning :**
- Correction base : `DELETE` produit_id 7, `INSERT` Webcam HD, `UPDATE` remises
- Jointures ventes + produits, agrégation CA avec correction `/100.0`
- CTE + `CASE WHEN` pour classification ventes, sous-requête produits premium
- Window Functions : `LAG()` variation MoM, `SUM() OVER` cumulé, `AVG() OVER ROWS 2 PRECEDING` MM3M, `RANK()` classement pays

**Statistiques Python :**
- Tendance : mean vs median, écart % par pays
- Volatilité : `std()` global + par catégorie
- Outliers : méthode IQR (Q1-1.5*IQR / Q3+1.5*IQR) + poids sur CA
- Corrélations : qté/CA, prix/CA + par catégorie

## 02 - Grand-Livre - Finance

**Finance :**
- P&L consolidé 2.18M$, marge 79.8%, RN 571k$ (IS 30%)
- Analyse annuelle 2023->2024 +7.78%, saisonnalité 12 mois, performance par département

## 03 - Bridge - Due Diligence Commerciale

- Décomposition variance marge brute Niveau 1 à 4
- Effets Volume / Prix / Remise / COGS avec réconciliation à 0€
- Bridge par Produit (Amarilla, Paseo...) et par Pays (Canada, France...)
- 2 waterfalls + matrice de contrôle

## 04 - Kossou - Audit Comptable

- Nettoyage balance brute, mapping plan comptable
- Construction P&L + Bilan + BFR + TFT + Dashboard
- Retraitements IFRS
- Reporting financier final pour direction

### 📈 Résultats clés
- CA total : **822 552 683 €** | 4 pays > 150M€ | 61% Informatique
- Bridge réconcilié : 8 546 824€ d'effet volume, -5 648 141€ effet COGS
- 14 onglets Excel audités + 8 visualisations

</details>
