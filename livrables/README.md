# Livrables — dossier « Rapatriement de l'hyperviseur »

Deux documents, chacun en **Word (.docx)** et **PDF (.pdf)**, produits depuis un même contenu
(`docs_gen/`) afin que les deux versions soient rigoureusement identiques.

| Fichier | Contenu | Volume |
|---|---|---|
| `A_Analyse_Joel_reformulee_qualite_prix_performance` | **Reformulation de l'analyse de Joël** sous l'angle qualité / prix / performance : existant, dimensionnement cible, Proxmox, comparaison des 7 configurations chiffrées, meilleure offre n°1 et n°2, neuf vs reconditionné, générations, 3 tranches de budget, coût complet, recommandation. | 14 pages · 18 tableaux · 7 graphiques |
| `D_Cinq_constructeurs_tableaux_comparatifs` | **Proposition D — cinq tableaux, un par constructeur** (HPE, Dell, Lenovo, Supermicro, ASUS). Chaque tableau reprend les lignes de la fiche de l'existant et décline 3 configurations (64 Go / 128 Go / gamme supérieure), avec Product Number, fournisseur, tarif et lien constructeur vérifié. Code couleur vert / jaune / orange selon la conformité aux exigences. | 10 pages · 10 tableaux · 5 pages en paysage |
| `B_Analyse_independante_benchmark_appro` | **Analyse indépendante construite de A à Z** (sans reprendre les conclusions initiales) : lecture critique des mesures, règles de dimensionnement, architecture Proxmox, nomenclature chiffrée, **4 recommandations HPE**, alternatives Dell / Lenovo / Supermicro, **4 circuits d'achat en France**, benchmark de 9 candidats, coût total, plan d'appro en 8 semaines, questions à poser aux revendeurs. | 14 pages · 18 tableaux · 5 graphiques |

## Ce que les deux documents démontrent

- L'existant est limité par la **mémoire (88 %) et le stockage (90 %)**, pas par le CPU (15 %).
- Le plancher technique défendable est **128 Go de RAM et 2 To utiles** — pas 64 Go.
- Sous **Proxmox VE** (licence par socket, 550 €/an), le nombre de cœurs n'a plus d'effet sur
  le coût : l'arbitrage redevient purement technique.
- Le **prix du serveur n'est pas le coût du projet** : réseau, onduleur, licences, fret, douane et
  migration ajoutent 40 à 50 %.
- Le rapatriement devient rentable si la facture de location actuelle dépasse **≈ 550 €/mois HT**.
- À exigences égales, **HPE, Lenovo et Supermicro se tiennent en 128 Go entre 8 200 et 8 500 € HT**,
  quand Dell (canal direct) affiche 16 411 € et le 2U HPE 16 861 €.

## Régénérer les documents

```bash
python3 -m venv .venv && .venv/bin/pip install python-docx matplotlib reportlab pillow
cd docs_gen
../.venv/bin/python charts.py      # graphiques -> docs_gen/assets
../.venv/bin/python doc_a.py       # livrables/A_*.docx + .pdf
../.venv/bin/python doc_b.py       # livrables/B_*.docx + .pdf
../.venv/bin/python doc_d.py       # livrables/D_*.docx + .pdf
```

Sources : `docs_gen/data.py` (données et hypothèses), `docs_gen/charts.py` (graphiques),
`docs_gen/render.py` (moteur de rendu Word + PDF), `docs_gen/doc_a.py`, `docs_gen/doc_b.py` (contenu).

## Avertissement

Les prix proviennent de relevés publics du 5 novembre 2026 et d'estimations construites par
analogie, signalées comme telles dans les documents. Ils ne constituent ni des offres fermes ni
des engagements de prix : ils servent à positionner une enveloppe budgétaire et une cible technique.
