# Livrables du 16 novembre 2026

Trois fichiers, un seul contenu : **le profil ciblé, le catalogue des quinze postes et le
face-à-face des tarifs Intel / AMD** (version alpha, référence GED-POSTES-2026-11-C).

| Fichier | Format | Ce qu'il sert à faire |
|---|---|---|
| `Postes_fixes_profil_cible_et_catalogue_Intel_AMD_alpha.docx` | Word | Relire, commenter, modifier le texte et les tableaux |
| `Postes_fixes_profil_cible_et_catalogue_Intel_AMD_alpha.pdf` | PDF | Diffuser tel quel : 9 pages, dont trois planches A3 paysage |
| `Postes_fixes_profil_cible_et_catalogue_Intel_AMD_alpha.xlsx` | Excel | Trier, filtrer, recalculer : cinq feuilles, liens actifs |

## Ce que contient le classeur

1. **Profil** — les trois seuils opposables : entrée de gamme, standard de référence, confort,
   avec le seuil Intel et le seuil AMD de chaque gamme.
2. **Catalogue** — les quinze machines, une ligne par voie : gamme, constructeur, plateforme,
   modèle, état (neuf ou reconditionné), processeur, cœurs et threads, fréquences, mémoire et
   disque détaillés, revendeur, **prix livré en euros et en francs CFA**, conformité colorée,
   lien actif. Filtre automatique sur toutes les colonnes, volets figés.
3. **Face-à-face** — pour chaque gamme et chaque constructeur, la voie Intel et la voie AMD
   côte à côte, l'**écart en euros et en pourcentage** (vert quand l'AMD est moins cher, orange
   quand il l'est plus), et ce que l'écart achète.
4. **Repères de calcul** — cœurs, threads, fréquence, classe de graphique, et ce que chaque puce
   sait faire de mieux. Aucun score de benchmark n'est affiché : ces machines n'ont pas été
   mesurées.
5. **Méthode** — source et date des prix, conversion à 655,957 FCFA, sens de « n. c. » et de
   « — », réserve sur la garantie en reconditionné, précaution « vendu et expédié par ».

## À savoir avant de s'en servir

Les prix sont **réellement relevés le 5 novembre 2026**, mais ils n'ont qu'une **valeur
illustrative** : ils servent à arbitrer entre deux voies techniques, pas à contractualiser.
Un devis constructeur ou grossiste décalera ces montants de 15 à 25 % à la baisse sur volume.

Trois prix manquent encore — M70q Gen 5, M90q Gen 5, M75q Gen 5 en 32 Go / 1 To — et le devis
Dell du confort. Ils sont signalés « à chiffrer », jamais estimés.

## Régénérer les trois fichiers

```bash
cd docs_gen
LIVRABLES_DIR=livrables-2026-11-16 ../.venv/bin/python profil_catalogue_alpha.py   # Word + PDF
LIVRABLES_DIR=livrables-2026-11-16 ../.venv/bin/python alpha_xlsx.py                 # Excel
```
