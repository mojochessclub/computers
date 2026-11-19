# ADCHIM — note de synthèse Comité de direction, version 2026-11-19 (v3)

**Fichiers** : `ADC_Workstations_CODIR_v3_2026-11-19.pdf` (8 pages, pour la séance) et
`.docx` (modifiable). Émetteur : Joël MBA OYONE — GED-SERVICES. Destinataire : comité de
direction d'ADCHIM. La v2 reste dans le dossier, pour comparer.

## Ce que la v3 change

Une seule chose, mais elle est structurante : **la recommandation mémoire est inversée**.
Le comité voit d'abord la contrainte budgétaire.

| | v2 | v3 |
|---|---|---|
| Configuration de commande du standard | 2 × 8 Go (double canal) | **1 × 16 Go, second emplacement libre** |
| Cible 32 Go | kit 2 × 16 Go, ≈ **1 612,92 €** | 1 barrette de 16 Go, ≈ **1 362,92 €** |
| Écart au plafond de 1 350 € | 262,92 € | **12,92 €** |
| Double canal à la commande | le défaut | **un supplément de 250 € / poste, arbitré poste par poste** |

Les sections 2, 3.2, 5 et 6, ainsi que l'annexe A, ont été réalignées : aucun passage ne
recommande plus le double canal par défaut. Tous les autres chiffres sont inchangés.

## Structure

| Section | Ce qu'elle apporte |
|---|---|
| 1. Philosophie | Les trois principes (usages, pérennité, neutralité) et la précaution sur les prix |
| 2. Cibles techniques | Le référentiel de conformité, gamme par gamme, et les points de vigilance |
| 3. Cibles retenues | Les trois tableaux de gamme, cibles surlignées en vert, avec l'orientation proposée |
| 4. Processeurs | Le face-à-face Intel / AMD par génération, architecture, date de sortie et cœurs |
| 5. Châssis | Mini / SFF / Tour : ce que chacun pourra recevoir pendant cinq ans |
| 6. Arbitrages | Six décisions, le coût réel de la cible 32 Go, la recommandation, la décision sollicitée |
| Annexe A | Les 18 corrections de la v1 → v2, et ce que la v3 change |

Chaque tableau est suivi d'un encadré **« À quoi sert ce tableau »** : en une phrase, ce
qu'il permet de trancher en séance.

## Les trois chiffres à retenir

- **Standard d'achat** : Lenovo ThinkCentre M75q Gen 5 en AMD, **1 112,92 €**
  (730 028 FCFA), livré en 1 × 16 Go, avec le HP Elite 800 G9 Mini en Intel à
  **1 055,99 €** comme seconde source.
- **Entrée de gamme** : M75q Gen 5 à **849,00 €** et M70q Gen 5 à **840,00 €** — même
  châssis, un seul jeu de pièces.
- **Cible 32 Go** : ≈ **1 362,92 €** avec une seconde barrette de 16 Go, soit **12,92 €
  au-dessus du plafond**. C'est l'arbitrage de la séance.

## Règle de cohérence

Tous les montants FCFA et tous les écarts sont calculés par le générateur
(`docs_gen/adc_codir_v3.py`), jamais saisis : 1 € = 655,957 FCFA. Si un prix change dans
le script, les tableaux, les conversions et les écarts suivent ensemble.

```bash
.venv/bin/python docs_gen/adc_codir_v3.py   # régénère le .docx et le .pdf
```
