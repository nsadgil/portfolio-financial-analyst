# 01 - AFRITECH Distribution - Analyse 360° (2024-2025)

> De la donnée brute SQLite à l'insight business : SQL avancé + Python + Stats appliquée + Finance

## 📁 Structure du projet

    01-afritech/
    ├── data/
    │   ├── afritech_v1_raw.db      # Base brute (12/09)
    │   └── afritech_v2_clean.db    # Base nettoyée (29/09) - utilisée pour l'analyse
    ├── outputs/
    │   ├── ca_par_categorie.png
    │   ├── ca_par_pays.png
    │   ├── correlation_prix_ca.png
    │   └── dispersion_ca.png
    ├── sql/
    │   ├── analyse_commerciale.py
    │   ├── afritech_analysis.xlsx
    │   └── rapport_ventes_afritech.md
    ├── stats/
    │   ├── analyse_statistique.py
    │   ├── afritech_stats.xlsx
    │   └── rapport_stats_afritech.md
    └── README.md

### 🔧 Stack & Méthodologie

    1. Data Cleaning & Correction [SQL]

    2. Agrégation & Jointures [SQL + Pandas]

    3. Analyse Avancée [SQL]

    4. Fonctions de Fenêtrage [Window Functions]

    5. Statistiques [Python]

    6. Finance [Excel P&L USD]

## 🗃️ Données
- **v1_raw** : données de départ, avec doublons et valeurs manquantes
- **v2_clean** : données nettoyées pour l'analyse finale

## 🔍 Analyses réalisées

### 1. Partie SQL (`/sql`)
- Requêtes sur le chiffre d'affaires par catégorie, pays
- Fichier : `analyse_sql.py` - auditable 

### 2. Partie Statistique (`/stats`)
- Corrélation prix / CA, dispersion
- Fichier : `analyse_stats.py` - auditable

## 📊 Visualisations
Graphiques dans `/outputs`

## 🛠️ Outils
Python, SQL (SQLite), Pandas, Matplotlib, Excel

### 💡 Valeur
J'ai corrigé la base, prouvé la rentabilité, détecté les outliers et expliqué la saisonnalité. Pas juste un reporting, mais une diagnostic pour pilotage.