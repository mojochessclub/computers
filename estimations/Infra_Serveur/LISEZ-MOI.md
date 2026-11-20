# ADCHIM — rapatriement de l'hyperviseur (dossier V1, novembre 2026)

**Fichiers** :
`ADC_Infra_Serveur_Essentiel_V1_2026-11-20.pdf` (2 pages) et
`ADC_Infra_Serveur_Dossier_Technique_V1_2026-11-20.pdf` (7 pages), avec leurs `.docx`
modifiables. Émetteur : Joël MBA OYONE — GED-SERVICES.

## Deux documents, deux usages

| Document | Pages | À qui | Ce qu'il sert à |
|---|---|---|---|
| **Essentiel** | 2 | Comité de direction | Décider : existant, socle, familles HPE, budget, décision sollicitée |
| **Dossier technique** | 7 | Comité et revendeur | Instruire : méthode, mesures, comparatif AMD / Intel, encombrement, budget complet, risques, questions à poser |

L'essentiel se lit seul. Le dossier technique le démontre et fournit les tableaux de
consultation à envoyer aux revendeurs.

## Structure du dossier technique

| Section | Ce qu'elle apporte |
|---|---|
| Synthèse et guide de lecture | Quatre constats, codes couleur, cheminement |
| 1. Objet, périmètre et méthode | Les quatre étapes : mesurer, spécifier, consulter, arbitrer |
| 2. État de l'existant | Relevés, limites des mesures, mesures à produire sur 30 jours |
| 3. Besoin cible | Hypothèses de dimensionnement et exigences minimales |
| 4. Comparatif HPE AMD / Intel | Six processeurs candidats, face-à-face des deux voies |
| 5. Encombrement et architecture | Dimensions, poids, colis, contraintes de baie, couches Proxmox |
| 6. Cotations et budget | Repères de prix, postes du coût complet, grille de pondération |
| 7. Risques, questions et suite | Six risques, huit questions au revendeur, calendrier |
| 8. Vocabulaire et fiches | Quatorze tableaux indexés, fiche de cotation à remplir |

## Codes couleur

| Couleur | Sens |
|---|---|
| Vert | Point tenu, ou donnée adossée à une fiche constructeur |
| Orange | À vérifier, à confirmer au devis |
| Rouge | Risque, hors profil, donnée à ne pas extrapoler |
| Bleu | Montant ou poste encore à chiffrer |
| Gris | Simple repère de prix, non retenu |

## Trois chiffres

- **Mémoire** : 64 Go occupés à **88,4 %** — c'est la ressource qui décide, pas le CPU (15 %).
- **Cible** : 128 Go DDR5 ECC, ≥ 2 To utiles après RAID1, 12 à 16 cœurs, 2 × 10 GbE, 3 ans.
- **Budget** : de **8 900 à 13 900 €** HT pour la cible équipée (5,8 à 9,1 M FCFA), hors fret,
  douane, réseau, onduleur, licences et intégration.

## Régénération

```bash
python docs_gen/adc_infra_essentiel_v1.py
python docs_gen/adc_infra_dossier_v1.py
```

Les deux scripts écrivent dans `estimations/Infra_Serveur/` (surchargeable par la variable
d'environnement `LIVRABLES_DIR`). Les montants FCFA sont calculés au taux de 655,957 ; aucun
prix n'est saisi à la main.
