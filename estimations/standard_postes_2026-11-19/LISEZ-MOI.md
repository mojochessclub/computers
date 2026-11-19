# ADCHIM — standardisation des postes fixes (note de décision, novembre 2026)

**Fichiers** : `ADC_Standard_Postes_Fixes_2026-11-19.pdf` (5 pages, pour la séance) et
`.docx` (modifiable). Émetteur : Joël MBA OYONE — GED-SERVICES.

## À qui il s'adresse

Deux lecteurs, un seul document :

- **le comité de direction**, qui décide — sections 1, 2, 7 et la décision sollicitée ;
- **le revendeur**, qui consulte et achète à l'étranger — les tableaux de modèles avec
  leurs liens, et le tableau « ce qu'on exige / ce qu'on refuse » de la section 7.

La section 7 tient sur une page : c'est le support de présentation en séance, et la base
de la demande de prix.

## Structure

| Section | Ce qu'elle apporte |
|---|---|
| 1. L'essentiel | Cinq points, dont le standard du parc et son prix |
| 2. Le profil de chaque gamme | Le référentiel d'achat : usage, processeurs, mémoire, stockage, garantie, enveloppe |
| 3. Les modèles retenus | Entrée, standard, confort : seize références, statut en couleur, lien vers la fiche |
| 4. Les processeurs | Face-à-face Intel / AMD par génération, architecture et date de sortie |
| 5. Les formats de châssis | Mini, SFF, tour : ce que chacun pourra recevoir pendant cinq ans |
| 6. La mémoire | Trois façons d'aller à 32 Go, chiffrées |
| 7. La commande | Récapitulatif par gamme, exigences de devis, réserves, décision sollicitée |

## Codes couleur

| Couleur | Sens |
|---|---|
| Vert | Référence retenue |
| Orange | À vérifier, ou sous réserve (reconditionné, 16 Go au lieu de 32) |
| Rouge | Hors profil ou hors enveloppe |
| Gris | Référence de prix, non retenue |

## Trois chiffres

- **Standard du parc** : Lenovo ThinkCentre M75q Gen 5 en AMD, **1 112,92 €**
  (730 028 FCFA) ; HP Elite 800 G9 Mini à **1 055,99 €** en seconde source.
- **Entrée de gamme** : M75q Gen 5 à **849,00 €**, M70q Gen 5 à **840,00 €**.
- **Cible 32 Go** : ≈ **1 362,92 €** par poste avec une seconde barrette, soit **12,92 €**
  au-dessus du plafond de 1 350 €.

## Règle de cohérence

Tous les montants FCFA et tous les écarts sont calculés par le générateur
(`docs_gen/adc_codir_v4.py`), jamais saisis : 1 € = 655,957 FCFA.

```bash
.venv/bin/python docs_gen/adc_codir_v4.py   # régénère le .docx et le .pdf
```

---

## Section « 1. L'essentiel à retenir » (2 pages)

`ADC_Essentiel_a_retenir_2026-11-19.pdf` et `.docx` — reprise mise en page de la section
fournie en PDF (texte des tableaux, codes couleur, cinq points). Contenu :

- **1.1 Un standard, trois gammes** : statut, usage, processeur, mémoire, stockage,
  châssis, enveloppe pour les trois gammes — vert = cible, orange = illustration,
  bleu = à chiffrer ;
- **1.2 Exigences transverses** : mémoire, processeur, stockage, système et garantie
  (les deux lignes restées vides dans le document d'origine sont renseignées) ;
- **1.3 Modèles de référence, par gamme** : 8 modèles, prix € + FCFA, colonne « fiche »
  cliquable ;
- **Les cinq points, en clair** et la **décision sollicitée**.

Générateur : `docs_gen/adc_essentiel.py` (même moteur que les autres documents).
