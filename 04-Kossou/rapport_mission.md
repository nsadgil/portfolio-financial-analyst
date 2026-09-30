# Mission 1 — De la Balance Comptable au Suivi de Trésorerie
**Client :** KOSSOU DISTRIBUTION SARL (PME fictive, SYSCOHADA)
**Réalisé par :** N'KOUEI N'tcha Gildas
**Objet :** Automatisation Excel — Balance → Compte de Résultat (SIG) → Bilan → Retraitements analytiques → BFR → Tableau de flux de trésorerie → Tableau de bord direction
**Norme :** SYSCOHADA révisé (OHADA) 
**Retraitements :** Normalisation IFRS - Pour le pilotage
**Exercices couverts :** N-1 et N — Unité : milliers d'Euro (K €)

---

## 1. Contexte et objectif

À partir d'une balance générale brute (export logiciel comptable, deux exercices), reconstruction intégrale et automatisée — par formules, sans valeur figée — de la chaîne de reporting financier : nettoyage des données, construction des états financiers, normalisation de la rentabilité, analyse du besoin en fonds de roulement et de la trésorerie, jusqu'au tableau de bord de suivi pour la direction.

## 2. Architecture du classeur

| Onglet | Contenu |
|---|---|
| Balance_brute | Export brut, avec contrôle Débit = Crédit intégré |
| Anormalies | Journal des 3 anomalies détectées et corrigées |
| Nettoyage | Détection automatique (colonne Contrôle) avant correction |
| Mapping | Plan de reclassement compte → rubrique CR/Bilan |
| Balance | Balance consolidée et corrigée, prête pour le mapping |
| P&L | Compte de résultat en Soldes Intermédiaires de Gestion |
| Bilan | Actif/Passif avec ratios de liquidité et cycle de conversion cash |
| Retraitements | Normalisation EBE (crédit-bail, personnel intérimaire) |
| BFR | Besoin en fonds de roulement et Cash Gap (jours) |
| TFT | Tableau de flux de trésorerie, réconcilié au Bilan |
| Dashboard | Indicateurs clés commentés pour la direction |

## 3. Nettoyage — 3 anomalies détectées et documentées

1. **613100 (Redevances de crédit-bail)** : montant saisi en sens inverse (Débit/Crédit intervertis) sur l'exercice N — détecté par contrôle automatique de signe, corrigé par reclassement au débit.
2. **601000 (Achats de marchandises)** : compte apparaissant sur deux lignes suite à un export en deux lots — sans impact sur les totaux grâce à l'agrégation par bucket de mapping, mais à surveiller si la feuille `Balance` est réutilisée hors de ce classeur (une recherche directe par numéro de compte ignorerait la deuxième ligne).
3. **612000 (Entretien, réparations)** : nouveau compte non reporté dans le calcul du solde final lors d'une première version de la feuille de nettoyage — corrigé par extension de la formule de report.

## 4. Compte de Résultat (SIG)

| Indicateur | N-1 | N | Variation |
|---|---|---|---|
| Chiffre d'affaires | 236 000 | 279 500 | +18,4 % |
| Marge commerciale | 94 000 | 111 500 | +18,6 % |
| Valeur ajoutée | 69 600 | 80 000 | +14,9 % |
| EBE / EBITDA | 37 000 | 42 950 | +16,1 % |
| Résultat d'exploitation | 29 900 | 33 900 | +13,4 % |
| Résultat net | 23 050 | 26 450 | +14,8 % |

## 5. Bilan et structure financière

Total Actif = Total Passif vérifié sur les deux exercices (contrôle d'équilibre à 0).

| Ratio | N-1 | N | Lecture |
|---|---|---|---|
| Liquidité générale | 3,29 | 3,07 | Structure très solide, en léger repli |
| Liquidité réduite | 2,69 | 2,48 | Confortable (seuil d'alerte usuel : 1,0) |
| Liquidité immédiate | 1,75 | 1,53 | Bonne couverture des dettes court terme par le cash disponible |
| DSO / DIO / DPO | — | 46,5 / 48,4 / 58,2 jours | Cycle clients plus court que le cycle fournisseurs — situation favorable |

## 6. Retraitements analytiques

- **Crédit-bail** (hypothèse 70 % dotation / 30 % intérêt) : EBE retraité de 37 000 → 43 000 (N-1) et 42 950 → 48 950 (N). Résultat net retraité identique au résultat net publié (contrôle d'écart = 0), confirmant la neutralité de ce retraitement sur le résultat final.
- **Personnel intérimaire** : reclassement de 8 400 (N-1) et 12 600 (N) des consommations vers les charges de personnel — sans impact sur l'EBE, mais le "Ratio de Performance Opérationnelle" (charges de personnel réelles / CA) passe de 16,6 % à 17,0 %, révélant le vrai poids du travail (interne + externalisé) dans l'activité.

## 7. BFR et Trésorerie

BFR en hausse de 16 600 à 20 300 (+22,3 %), Cash Gap de 25,7 à 26,5 jours. Le tableau de flux de trésorerie, décomposé jusqu'aux 4 composantes du BFR (stocks, créances, fournisseurs, dettes sociales/fiscales), se réconcilie exactement avec la variation de trésorerie observée au bilan (54 050 → 57 500, écart de contrôle = 0).

## 8. Tableau de bord — synthèse direction

| Constat | Lecture |
|---|---|
| Trésorerie +6,4 % | Rentabilité qui se traduit en cash réel, pas seulement en résultat comptable |
| BFR +22,3 % | Point de vigilance : consommation croissante de ressources court terme |
| Rentabilité opérationnelle -0,7 pt | Légère baisse malgré la croissance du CA — coûts globalement maîtrisés |
| Dettes financières -25 % | Désendettement actif sur l'exercice |

## 9. Limites et hypothèses à documenter

- Ventilation crédit-bail (70 % dotation / 30 % intérêt) : hypothèse simplificatrice en l'absence du contrat détaillé.
- Distribution de dividendes dans le TFT déduite de la variation des capitaux propres (non observée directement) — à confirmer avec le procès-verbal d'affectation du résultat.
- Impôt repris tel que comptabilisé, non recalculé à un taux théorique.
- BFR simplifié (hors détail TVA et autres créances/dettes diverses).

---

*Classeur Excel disponible dans le dossier concerné du portfolio — toutes les feuilles construites par formule, sans valeur figée.*
