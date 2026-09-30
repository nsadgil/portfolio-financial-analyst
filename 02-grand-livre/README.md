# 02 Diagnostic Financier - Grand Livre Multi-devises

> Analyse de performance financière et opérationnelle d'une structure multi-départements

### 📁 Structure
    02-afritech/
    ├── analysis_general_ledger.xlsx 
    ├── compte_resultat_usd.xlsx
    ├── rapport_grand_livre.md
    └── README.md

**Dataset :** [General-Ledger.xlsx](https://github.com/Jrtoby/General-Ledger-Financial-Analysis) - 2000 écritures, 2023-2025, 5 devises

### 📌 Contexte
Mission Afritech : Transformer un export comptable USD en outil de pilotage pour la direction.

## Objectifs
1. Contrôler l'équilibre Débit/Crédit
2. Valider la conversion multi-devises
3. Construire le P&L consolidé
4. Analyser les charges par département
5. Investiguer la variation de CA sur 2025

### 🔧 Méthodologie - 4 axes
**1. P&L Consolidé [P&L_Consolide]**
- Modèle réconcilié et auditable
**2. Analyse Annuelle [P&L_Annuel]**
- Lecture : Croissance 2023-2024 saine, mais compression de marge nette
**3. Analyse de Saisonnalité [Saisonnalite]**
- Enseignement : Forte saisonnalité, Q1 et Q4 tirent l'année, Q3 faible
**4. Performance par Département [Par_Dept]**
- Total charges op : 927 563$ réconcilié avec P&L consolidé

### 📄 Rapports
- `rapport_afritech_gestion.md` : Recommandations opérationnelles - optimiser HR/IT, capitaliser sur saisonnalité
- `rapport_due_diligence.md` : Risques (dépendance saisonnière, concentration charges) et leviers de marge

### 🛠️ Stack
Excel, P&L Analysis, Saisonnalité, Analyse par département, Financial Modeling

### 💡 Valeur
J'ai transformé 4 onglets bruts en diagnostic complet : rentabilité à 79.8%, saisonnalité expliquée, et départements benchmarkés pour décision.

## Fichiers
- `analysis_general_ledger.ipynb` : code complet
- `compte_resultat_usd.xlsx` : 4 onglets (P&L_Consolide, P&L_Annuel, Saisonnalite, Par_Dept)
- `rapport_grand_livre.md` : rapport final

## Lancer le projet
```bash
pip install pandas openpyxl
jupyter notebook analysis_general_ledger.ipynb
```