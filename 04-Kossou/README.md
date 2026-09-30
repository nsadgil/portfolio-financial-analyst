# 04 - KOSSOU Distribution - Mission Audit & Restructuration Financière

> De la balance brute inexploitable au pilotage financier : mission complète de diagnostic, nettoyage et modélisation.

## 📁 Structure
    04-Kossou/
    ├── data/
    │   └── balance_comptable_brute.xlsx   # données sources
    ├── kossou_reporting_financier.xlsx    # reporting construit (P&L, BS)
    ├── rapport_mission.md                 # rapport final de mission
    └── README.md

### 📌 Contexte
PME KOSSOU Distribution. Balance générale brute exportée du logiciel comptable, non équilibrée, avec erreurs de saisie et sans reporting. 
Objectif : fiabiliser et construire les états financiers pour pilotage.

### 🔧 Méthodologie - 5 étapes

**1. Audit & Nettoyage [Onglets Nettoyage, Anomalies]**
- Contrôle Débit = Crédit et calcul des soldes N-1 / N
- Journal des anomalies : 3 anomalies majeures détectées et corrigées
    - 613100: crédit-bail saisi à l'envers (-12 000 d'écart)
    - 601000: doublon (100800 + 67200) -> fusion SUMIF
    - 612000: compte à 0 en N-1 mal reporté
- Méthode : Power Query (extraction préfixe 3 chiffres)

**2. Structuration [Onglet Mapping]**
- Création d'un plan de mapping SYSCOHADA : Préfixe -> Bucket (Capitaux_Propres, Dettes_Financieres, Immo_Brut, etc.) -> Position Bilan / P&L
- Base pour automatiser la construction des états

**3. Construction des États Financiers [Balance, P&L, Bilan]**
- Balance nettoyée consolidée via SUMIFS
- P&L avec SIG : Chiffre d'Affaires (236M -> 279.5M, +18.4%), Marge Commerciale, Valeur Ajoutée, EBE/EBITDA Brut 37M -> 42.9M
- Bilan Actif/Passif avec ratios de liquidité générale (3.29 -> 3.06), DSO, DIO, DPO

**4. Retraitements Analytiques & Performance Réelle [Retraitements IFRS]**
- Normalisation de l'EBE : retraitement du crédit-bail 613 (Hypothèse 70% amort / 30% intérêts IFRS-like)
- EBITDA Ajusté : 43M -> 48.9M -> rentabilité opérationnelle pure à 17.5%

**5. Analyse du Cash [BFR, TFT, Dashboard]**
- BFR : Stocks 18.5M -> 22.3M, Créances 28.9M -> 35.6M, BFR en hausse de 3.7M
- Tableau de Flux de Trésorerie (méthode indirecte) : Résultat 26.4M + Dotations 9M - Var BFR 3.7M = Flux d'exploitation. Réconciliation Trésorerie 54M -> 57.5M (+3.45M) validée à 0 d'écart
- Dashboard final pour dirigeant

### 📦 Livrables
- `kossou_reporting_financier.xlsx` : Modèle 11 onglets automatisé et auditable
- `rapport_mission_1.md` : Diagnostic + recommandations (optimisation BFR, contrôle charges)

### 🛠️ Stack
Excel Avancé (Power Query, formules avancées, TCD, ...), SYSCOHADA, Analyse financière (SIG, BFR, TFT, DSO/DIO/DPO, ...), Retraitements IFRS

