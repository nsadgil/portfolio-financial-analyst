# 03 - BRIDGE - Analyse de Variance de Marge Brute
    
> Diagnostic financier - Du bridge simple au bridge matriciel par produit et pays

### 📁 Structure
    03-bridge/
    ├── bridge_assets/
    │ ├── bridge_cascade_pays.png
    │ └── bridge_cascade_produits.png
    ├── bridge_afritech_analyse.xlsx # Financial_Sample + 4 niveaux de bridge
    ├── rapport_afritech_gestion.md # Lecture gestion
    ├── rapport_due_diligence.md # Lecture investisseur
    └── README.md

### 📌 Contexte
Mission Afritech : Expliquer aux investisseurs pourquoi la marge brute bouge. Dataset Microsoft Financial Sample utilisé comme base réelle.

### 📊 Dataset
**Source :** [Microsoft Financial Sample - Power BI](https://learn.microsoft.com/en-us/power-bi/create-reports/sample-financial-download)
- Fichier : `Financial Sample.xlsx`
- Taille : ~700 lignes x 16 colonnes, 2013-2014
- Licence : Gratuit Microsoft pour démo / formation
- Contenu : 5 pays (Canada, France, Germany, Mexico, USA), 6 produits (Amarilla, Carretera, Montana, Paseo, Velo, VTT), 5 segments

### 🔧 Méthodologie - 4 Niveaux

**Niveau 1 - Bridge Global [Niveau 1]**
- Marge 326 400 -> 262 870 (-63 530 / -19.4%)
- Volume +46 080 | Prix -47 045 | Coût -29 100 | Remise -33 465 | Contrôle 0

**Niveau 2 - Bridge par Produit [Niveau 2]**
- 5 produits (Alpha, Beta, Gamma, Delta, Epsilon)
- Total 159 040 -> 150 901 (-8 139) avec détail volume/prix/remise/cogs

**Niveau 3 - Bridge Réel [Niveau 3] - Focus Produit Paseo**
- Marge 1 099 853 -> 3 697 584 (+2 597 731 / +236%)
- Effet volume +2 323 422, waterfall chart + synthèse investisseur

**Niveau 4 - Bridge Matriciel [Niv4. Produit & Niv4. Pays]**
- Par Produit : 3 878 464 -> 13 015 237 (+9 136 773)
- Par Pays : Canada +1 921 885, France +2 158 356, Germany +1 443 949, etc.
- Matrice de réconciliation à 0

### 📄 Rapports
- `rapport_afritech_gestion.md` : Lecture gestion - quels produits/pays tirent la perf
- `rapport_due_diligence.md` : Lecture investissement - risques (hausse cogs, pression remises) et leviers

### 🛠️ Stack
Excel (Bridge / Waterfall), Variance Analysis, Due Diligence, Contrôle à 0.

