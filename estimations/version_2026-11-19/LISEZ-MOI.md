# ADCHIM — note de synthèse Comité de direction, version 2026-11-19 (v2)

**Fichiers** : `ADC_Workstations_CODIR_v2_2026-11-19.pdf` (8 pages, pour la séance) et
`.docx` (modifiable). Émetteur : Joël MBA OYONE — GED-SERVICES. Destinataire : comité de
direction d'ADCHIM.

## Ce qu'est cette version

Une synthèse de trois choses : la note technique du 19 novembre, le relevé d'incohérences
interne, et la revue externe du même jour. Les tableaux et la logique d'arbitrage sont
conservés ; les raccords entre prix, écarts, générations et conversions ont été repris.

Elle est bâtie pour une réunion, pas pour une lecture en profondeur :

| Section | Ce qu'elle apporte |
|---|---|
| 1. Philosophie | Les trois principes (usages, pérennité, neutralité) et la précaution sur les prix |
| 2. Cibles techniques | Le référentiel de conformité, gamme par gamme — et les trois points de vigilance corrigés |
| 3. Cibles retenues | Les trois tableaux de gamme, cibles surlignées en vert, avec l'orientation proposée |
| 4. Processeurs | Le face-à-face Intel / AMD par génération, architecture, date de sortie et cœurs |
| 5. Châssis | Mini / SFF / Tour : ce que chacun pourra recevoir pendant cinq ans |
| 6. Arbitrages | Six décisions, le coût réel de la cible 32 Go, et la décision sollicitée |
| Annexe A | Les 18 corrections apportées par rapport à la note du 19 novembre |

Chaque tableau est suivi d'un encadré **« À quoi sert ce tableau »** : en une phrase, ce
qu'il permet de trancher en séance.

## Les trois chiffres à retenir

- **Standard d'achat** : Lenovo ThinkCentre M75q Gen 5 en AMD, **1 112,92 €**
  (730 028 FCFA), avec le HP Elite 800 G9 Mini en Intel à **1 055,99 €** comme seconde
  source.
- **Entrée de gamme** : M75q Gen 5 à **849,00 €** et M70q Gen 5 à **840,00 €** — même
  châssis, un seul jeu de pièces.
- **Cible 32 Go** : livrée en 2 × 8 Go (double canal), elle coûte ≈ **1 612,92 €** avec le
  kit 2 × 16 Go, soit **262,92 € au-dessus du plafond**. C'est l'arbitrage de la séance.

## Règle de cohérence

Tous les montants FCFA et tous les écarts sont calculés par le générateur
(`docs_gen/adc_codir_v2.py`), jamais saisis : 1 € = 655,957 FCFA. Si un prix change dans
le script, les tableaux, les conversions et les écarts suivent ensemble.

```bash
.venv/bin/python docs_gen/adc_codir_v2.py   # régénère le .docx et le .pdf
```
