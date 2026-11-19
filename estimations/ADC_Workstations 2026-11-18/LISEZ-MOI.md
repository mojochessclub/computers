# ADCHIM — postes fixes, benchmark Intel / AMD (19 novembre 2026)

Cinq fichiers, un seul jeu de données, arrêté au **19 novembre 2026**. Émetteur :
Joël MBA OYONE (GED-SERVICES) — destinataire : Jad SAID, directeur général d'ADCHIM.

| Fichier | Ce qu'il contient |
|---|---|
| `ADC_Workstations_2026-11-18_Note_comite_direction.pdf` / `.docx` | **Version comité de direction, 11 pages** : philosophie, cibles techniques, cibles retenues gamme par gamme (lignes vertes), face-à-face des processeurs par année et génération, formats de châssis, décision demandée. Chaque tableau est suivi d'un encadré « à quoi ça sert ». |
| `ADC_Workstations_2026-11-18_Releve_incoherences.pdf` / `.docx` | **Relecture de la note du 19 novembre** : 32 points relevés, dont 13 bloquants, avec la page, la gravité et la correction à appliquer. Se termine par un plan de correction en 4 étapes (≈ 1 h 10). |
| `ADC_Workstations_2026-11-18_Note_arbitrage_postes_fixes.pdf` | La note complète, 11 pages : seuils, processeurs par année, trois gammes en tableaux A3 paysage, face-à-face, recommandation, points à sécuriser, méthode. Version de lecture et de diffusion. |
| `ADC_Workstations_2026-11-18_Note_arbitrage_postes_fixes.docx` | Le même document, modifiable (Word). Mêmes tableaux, mêmes couleurs, mêmes chiffres. |
| `ADC_Workstations_2026-11-18_Catalogue_et_face_a_face.xlsx` | Le classeur de travail : synthèse, une feuille par gamme (36 références, filtrables), face-à-face avec écarts calculés, processeurs, seuils et méthode. |

## Le cadre

- **Enveloppe** : 650 € à 1 350 € par poste, écran, clavier et livraison non compris.
- **Gammes** : entrée de gamme (650–850 €), standard entreprise (850–1 200 €), confort
  (1 200–1 350 €).
- **Références** : deux par constructeur et par voie — 6 Intel + 6 AMD par gamme, soit
  36 lignes. Dell ne distribue pas d'AMD sur ce segment : c'est un fait de catalogue, pas
  un oubli, et il est écrit comme tel.
- **Colonnes** : année de sortie, obsolescence présumée (sortie + 5 ans), conformité au
  profil, commentaire, prix livré en euros, équivalent FCFA, lien vers la fiche produit.

## Trois précautions de lecture

1. Les prix sont **illustratifs et datés** : TTC, port compris quand il est connu. Un devis
   constructeur ou grossiste les décalera de 15 à 25 % à la baisse sur volume.
2. Une case **« à chiffrer »** n'est pas une omission : c'est une machine réelle dont aucun
   distributeur ne publie le prix au moment du relevé. Aucun prix n'a été estimé.
3. La conversion **1 € = 655,957 FCFA** est une parité fixe. Dans le classeur, les colonnes
   FCFA sont des formules : le taux reste vérifiable et rectifiable.

## Régénérer les fichiers

```bash
python3 -m venv .venv && .venv/bin/pip install python-docx reportlab openpyxl
.venv/bin/python docs_gen/adc_workstations.py        # .docx + .pdf
.venv/bin/python docs_gen/adc_workstations_xlsx.py   # .xlsx
```

Les données sources sont dans `docs_gen/adc_workstations.py` (`ENTREE`, `STANDARD`,
`CONFORT`, `CPU_ROWS`, `EQUIV_ROWS`, `SEUILS`, `VIGILANCE`). Corriger un prix dans ce
fichier et relancer les deux scripts suffit à mettre les trois livrables d'accord.
