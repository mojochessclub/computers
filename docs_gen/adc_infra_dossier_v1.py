# -*- coding: utf-8 -*-
"""ADCHIM — Infra_Serveur : dossier technique d'arbitrage (version 1).

Rapatriement de l'hyperviseur : méthode, existant, besoin cible, comparatif HPE AMD / Intel,
encombrement, budget complet, risques et consultation.
"""
from __future__ import annotations

import os

from adc_infra_common import BLEU, FMT, band, sous_titre, tab_titre
from render import Doc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, os.environ.get("LIVRABLES_DIR",
                                           "estimations/Infra_Serveur"))
BASE = "ADC_Infra_Serveur_Dossier_Technique_V1_2026-11-20"


# --------------------------------------------------------------------------- #
METHODE_HEADERS = ["Étape", "Travail attendu", "Résultat"]
METHODE_WIDTHS = [2.4, 9.6, 4.5]
METHODE_ROWS = [
    ["Mesurer", "Relevés actuels et pics CPU / RAM, SWAP par VM, IOPS, latence, croissance",
     "Besoin confirmé"],
    ["Spécifier", "Socle minimum et configurations AMD / Intel comparables",
     "Cahier de consultation"],
    ["Consulter", "Au moins trois devis sur une nomenclature identique",
     "Offres recevables"],
    ["Arbitrer", "Coût livré, garantie, délais, évolution et support", "Décision DG"],
]

EXIST_HEADERS = ["Indicateur", "Capacité", "Occupation", "Interprétation et action"]
EXIST_WIDTHS = [2.8, 4.0, 2.3, 8.0]
EXIST_ROWS = [
    ["CPU", "8 cœurs / 2,5 GHz", "≈ 15 %", "Pas de tension CPU démontrée", "v"],
    ["RAM", "64 Go", "88,4 %", "Marge insuffisante ; usage par VM à relever", "o"],
    ["Disque", "≈ 960 Go", "89,9 %", "Peu de réserve pour les snapshots et la croissance", "o"],
    ["SWAP", "Non précisé", "≈ 100 %", "Distinguer manque de RAM, surallocation ou fuite", "r"],
]

MES_HEADERS = ["Domaine", "Mesure à produire", "Période"]
MES_WIDTHS = [3.4, 10.9, 2.8]
MES_ROWS = [
    ["CPU", "Moyenne, pics, p95, temps d’attente en file (ready) par VM", "30 jours"],
    ["Mémoire", "Allouée contre consommée, ballooning, cache, SWAP par VM", "30 jours"],
    ["Stockage", "IOPS, latence p95, débit, croissance mensuelle", "30 jours"],
    ["Disponibilité", "Incidents, fenêtres de service, RTO et RPO attendus", "Atelier IT"],
]

BESOIN_HEADERS = ["Composant", "Minimum demandé", "À préciser au devis"]
BESOIN_WIDTHS = [2.9, 5.4, 8.8]
BESOIN_ROWS = [
    ["Mémoire", "128 Go DDR5 ECC", "RDIMM, fréquence, nombre de DIMM, slots libres, "
                                   "extension à 256 Go"],
    ["Stockage", "≥ 2 To utiles après RAID1", "2 × 1,92 To + disque de rechange ; "
                                              "contrôleur, endurance, garantie"],
    ["Processeur", "12 à 16 cœurs", "Référence, base / turbo, TDP, socket, support HPE"],
    ["Réseau", "2 × 10 GbE souhaités", "BASE-T ou SFP+, DAC ou optiques, ports libres"],
    ["Châssis", "Rackable, avec rails", "U, profondeur, poids machine et poids du colis"],
    ["Énergie", "Alimentations redondantes", "Puissance, cordons, consommation mesurée"],
    ["Gestion", "HPE iLO", "Version et licence, fonctions distantes"],
    ["Garantie", "3 ans constructeur", "Couverture au Gabon, procédure RMA, délais"],
]

FAM_HEADERS = ["Famille", "Processeur candidat", "Cœurs / fréquence", "Châssis à faire coter"]
FAM_WIDTHS = [1.9, 4.4, 3.4, 7.4]
FAM_ROWS = [
    ["AMD", "EPYC 9124", "16C / 3,00 GHz", "DL325 Gen11 8SFF", "v"],
    ["AMD", "EPYC 9125", "16C / 2,60 GHz", "DL325 Gen11 — compatibilité à confirmer", "o"],
    ["AMD", "EPYC 9224", "24C / 2,40 GHz", "DL325 Gen11 — compatibilité à confirmer", "o"],
    ["Intel", "Xeon Silver 4510", "12C / 2,40 GHz", "DL380 Gen11 — compatibilité à confirmer",
     "o"],
    ["Intel", "Xeon Silver 4410Y", "12C / 2,00 GHz", "DL320 Gen11 — compatibilité à confirmer",
     "o"],
    ["Intel", "Xeon Gold 6426Y", "16C / 2,40 GHz", "ML110 Gen11 — compatibilité à confirmer",
     "o"],
]

FACE_HEADERS = ["Critère de comparaison", "Voie AMD — EPYC sur DL325 Gen11",
                "Voie Intel — Xeon sur DL320 / DL380 / ML110"]
FACE_WIDTHS = [3.6, 6.7, 6.8]
FACE_ROWS = [
    ["Cœurs par socket", "16 à 24 cœurs sur un seul socket",
     "12 à 16 cœurs, deux sockets possibles"],
    ["Mémoire", "128 Go DDR5 ECC, extension à 256 Go à exiger",
     "128 Go DDR5 ECC, extension à 256 Go à exiger"],
    ["Format en baie", "1U court, 8 baies SFF, 4,29 × 43,46 × 64,94 cm",
     "1U ou 2U selon modèle, encombrement à faire coter"],
    ["Ce que la voie apporte", "Densité de cœurs dans un 1U, une seule licence socket",
     "Choix de modèles et de revendeurs plus large, pièces courantes"],
    ["Ce qu’elle impose", "Châssis AMD uniquement, compatibilité à valider",
     "Plus de variantes, donc plus de risque de nomenclature différente"],
    ["Point à vérifier", "Validation HPE écrite châssis / CPU / mémoire",
     "Référence exacte du CPU et du socket"],
]

DIM_HEADERS = ["Modèle", "Dimensions H × L × P", "Poids", "Statut de la donnée"]
DIM_WIDTHS = [4.2, 5.6, 3.5, 3.8]
DIM_ROWS = [
    ["DL325 Gen11 8SFF", "4,29 × 43,46 × 64,94 cm", "12,56 – 15,54 kg", "HPE QuickSpecs",
     "v"],
    ["Colis DL325 8SFF", "24,2 × 60 × 91,6 cm", "À confirmer", "HPE QuickSpecs", "o"],
    ["DL320 / DL380 / ML110", "À joindre au devis", "À joindre au devis", "Ne pas extrapoler",
     "r"],
]

COUCHE_HEADERS = ["Couche", "Cible retenue", "Point de contrôle"]
COUCHE_WIDTHS = [2.6, 6.4, 8.1]
COUCHE_ROWS = [
    ["Hyperviseur", "Proxmox VE", "Version, support de stockage des VM"],
    ["Calcul", "1 socket, 12 à 16 cœurs, 128 Go", "Marge vCPU / RAM, slots libres"],
    ["Stockage", "2 × 1,92 To en RAID1 + rechange", "Contrôleur ou HBA, endurance"],
    ["Sauvegarde", "PBS + copie hors site", "RPO / RTO et tests de restauration"],
    ["Réseau", "2 × 10 GbE + port de gestion", "VLAN, switch, DAC / optiques"],
    ["Énergie", "Onduleur + PDU", "Autonomie et arrêt propre"],
]

PRIX_HEADERS = ["Référence et périmètre", "Prix HT", "FCFA", "Nature et réserve"]
PRIX_WIDTHS = [6.3, 3.2, 3.5, 4.1]
PRIX_ROWS = [
    ["DL325 Gen11, EPYC 9124, 64 Go, sans disques", "5 726 €", "3,8 M",
     "Relevé partiel ; pas la cible équipée", "n"],
    ["DL325 Gen11, 128 Go + RAID1 + spare", "8 900 – 12 900 €", "5,8 – 8,5 M",
     "Estimations variables ; devis requis", "o"],
    ["DL320 Gen11, Xeon Silver 4410Y, 128 Go", "≈ 11 800 €", "7,7 M",
     "Estimation de benchmark", "o"],
    ["DL380 Gen11, Xeon Silver 4510, 128 Go", "≈ 13 900 €", "9,1 M",
     "Estimation de benchmark", "o"],
    ["ML110 Gen11, Xeon Gold 6426Y", "≈ 9 676 €", "6,3 M", "Périmètre à vérifier", "o"],
    ["DL380 Gen10 reconditionné, 128 Go", "≈ 3 200 €", "2,1 M",
     "Repère ; audit CPU, état et garantie", "r"],
]

COUT_HEADERS = ["Poste de coût", "Ce qu’il couvre", "Statut"]
COUT_WIDTHS = [3.6, 10.4, 3.2]
COUT_ROWS = [
    ["Serveur équipé", "Châssis, processeur, 128 Go, contrôleur, iLO, alimentations",
     "À chiffrer", "b"],
    ["Stockage", "2 × 1,92 To en RAID1 et un disque de rechange livré", "À chiffrer", "b"],
    ["Baie et énergie", "Rails, PDU, onduleur, autonomie et arrêt propre", "À chiffrer", "b"],
    ["Réseau", "Switch 10 GbE, DAC ou optiques, câblage, VLAN", "À chiffrer", "b"],
    ["Sauvegarde", "Cible PBS, copie hors site, bande passante", "À chiffrer", "b"],
    ["Licences", "Proxmox VE et PBS, support et mises à jour", "À valider", "o"],
    ["Fret et douane", "Transitaire, Incoterm, assurance, taxes à l’import", "À chiffrer", "b"],
    ["Intégration", "Installation, migration, documentation, formation", "À chiffrer", "b"],
]

POND_HEADERS = ["Critère de choix", "Poids", "Ce qu’il mesure"]
POND_WIDTHS = [4.6, 1.9, 10.6]
POND_ROWS = [
    ["Adéquation RAM et stockage", "30 %", "La ressource réellement contrainte aujourd’hui"],
    ["CPU et compatibilité", "15 %", "Référence validée, socket, support HPE écrit"],
    ["Réseau et entrées-sorties", "10 %", "10 GbE, contrôleur, disques, latence"],
    ["Garantie et support", "15 %", "3 ans, couverture au Gabon, procédure de retour"],
    ["Pérennité", "15 %", "Génération, extension mémoire, durée de vie"],
    ["Coût total livré", "15 %", "Serveur, options, fret, douane, intégration"],
]

RISK_HEADERS = ["Risque", "Impact", "Mesure de réduction"]
RISK_WIDTHS = [4.5, 3.6, 9.0]
RISK_ROWS = [
    ["CPU et châssis incompatibles", "Offre inutilisable",
     "Référence exacte et validation HPE écrite", "r"],
    ["64 Go livrés au lieu de 128 Go", "Saturation reconduite",
     "Contrôle à réception, clause au devis", "r"],
    ["Brut confondu avec utile", "Stockage insuffisant",
     "Capacité après RAID explicitée au devis", "o"],
    ["Garantie non applicable au Gabon", "Arrêt prolongé en cas de panne",
     "Conditions et procédure RMA vérifiées", "o"],
    ["Fret et douane sous-estimés", "Dépassement de budget",
     "Devis transitaire et Incoterm", "o"],
    ["Sauvegarde non restaurable", "Perte de données",
     "Test de restauration avant bascule, puis périodique", "r"],
]

QUEST_HEADERS = ["Rubrique", "Question à poser par écrit", "Pourquoi elle compte"]
QUEST_WIDTHS = [2.6, 8.3, 6.2]
QUEST_ROWS = [
    ["Références", "Numéro de pièce du serveur, du processeur, du contrôleur, des DIMM "
                   "et des SSD",
     "Une référence approchante change le prix et la garantie"],
    ["Mémoire", "128 Go livrés en combien de barrettes ? combien de slots restent libres ?",
     "L’extension à 256 Go se prépare à la commande"],
    ["Stockage", "Capacité utile après RAID1, endurance des disques, prix du disque de "
                 "rechange",
     "Brut et utile ne se confondent pas"],
    ["Réseau", "10 GbE en BASE-T ou SFP+ ? optiques ou DAC inclus ?",
     "Les optiques coûtent parfois plus que la carte"],
    ["Énergie et baie", "Puissance des alimentations, cordons, rails, profondeur, poids "
                        "du colis",
     "Baie, onduleur et transport en dépendent"],
    ["Garantie", "Trois ans sur site ? couverture au Gabon ? procédure RMA et délais ?",
     "Une garantie inapplicable ne protège de rien"],
    ["Livraison", "Incoterm, délai, transitaire, assurance, taxes à l’import",
     "Seul le coût livré est comparable"],
    ["Logiciel", "Compatibilité Proxmox VE et PBS, version de firmware, support HPE",
     "Éviter les surprises d’intégration"],
]

FICHE_HEADERS = ["Critère", "Offre A", "Offre B", "Offre C"]
FICHE_WIDTHS = [8.1, 3.0, 3.0, 3.0]
FICHE_ROWS = [
    "Référence serveur et processeur",
    "Mémoire livrée et slots libres",
    "Capacité utile après RAID1 et rechange",
    "Réseau 10 GbE et optiques",
    "Garantie, couverture et RMA",
    "Coût livré, Incoterm et délai",
    "Note pondérée sur 100",
]

VOCAB_HEADERS = ["Terme", "Ce qu’il désigne dans ce dossier"]
VOCAB_WIDTHS = [3.6, 13.5]
VOCAB_ROWS = [
    ["RAID1", "Deux disques en miroir : la même donnée écrite deux fois, capacité utile "
              "divisée par deux"],
    ["PBS", "Proxmox Backup Server : la sauvegarde dédupliquée des machines virtuelles"],
    ["RTO / RPO", "Durée d’arrêt admissible / quantité de données admissible à la perte"],
    ["iLO", "Gestion à distance du serveur, indépendante du système d’exploitation"],
    ["p95", "Niveau atteint ou dépassé pendant 5 % du temps : le pic qui compte vraiment"],
    ["Surallocation", "vCPU attribués au-delà des cœurs physiques ; tenable seulement si la "
                      "charge est mesurée"],
    ["Incoterm", "Qui paie le fret, l’assurance et la douane entre le vendeur et nous"],
    ["Disque de rechange", "Exemplaire identique prêt à remplacer un disque défaillant"],
]


def build_doc():
    doc = Doc(
        base=BASE,
        title="Dossier technique — rapatriement de l’hyperviseur",
        subtitle="Existant, besoin cible, comparatif HPE AMD / Intel, budget et risques",
        meta=[],
        doc_ref="ADCHIM · rapatriement de l’hyperviseur · novembre 2026",
        footer="GED-SERVICES · ADCHIM · rapatriement de l’hyperviseur · prix "
               "indicatifs à confirmer",
    )

    band(doc, "ADCHIM · rapatriement de l’hyperviseur · dossier technique",
         "Dossier technique d’arbitrage",
         "Existant, besoin cible, comparatif HPE AMD / Intel, budget complet et risques.")

    doc.p("Nous repartons des mesures observées et mettons en concurrence des "
          "nomenclatures comparables. **Aucun processeur, prix ou fournisseur n’est "
          "pré-validé** : les conclusions commerciales des études antérieures ne sont pas "
          "reconduites automatiquement.", small=True)

    doc.ul([
        "**La mémoire décide**, pas le processeur : 64 Go occupés à 88,4 % contre un CPU "
        "à 15 %.",
        "**Le stockage se juge en utile**, pas en brut : deux disques de 1,92 To en RAID1 "
        "donnent 1,92 To utiles.",
        "**Les deux voies se tiennent** — EPYC sur DL325 Gen11, Xeon sur DL320, DL380 ou "
        "ML110 — à condition de coter la même nomenclature.",
        "**Le prix du serveur n’est pas le coût du projet** : fret, douane, réseau, "
        "onduleur, licences et intégration pèsent autant que le châssis.",
    ], small=True)
    doc.p("**Utilité de cette liste.** Elle donne au comité les quatre constats qui "
          "commandent la décision ; le reste du dossier les démontre.", small=True)
    doc.p("**Comment lire ce dossier.** Les sections 1 et 2 établissent les faits ; les "
          "sections 3 et 4 fixent le besoin et mettent les deux voies techniques en "
          "parallèle ; les sections 5 et 6 traitent de l’installation et du budget complet ; "
          "la section 7 rassemble les risques, les questions à poser et la suite ; la "
          "section 8 traduit le vocabulaire employé.", small=True)
    doc.p("Les encadrés orange signalent une décision à prendre ou une précaution à "
          "respecter. Dans les tableaux, le vert marque un point tenu, l’orange un point à "
          "vérifier, le rouge un risque ou un hors-profil, le bleu un montant encore à "
          "chiffrer, le gris un simple repère.", small=True)

    # ------------------------------------------------------------------ 1
    doc.spacer(0.25)
    sous_titre(doc, "1.  Objet, périmètre et méthode")
    doc.p("Définir une plateforme locale pour reprendre les charges aujourd’hui hébergées "
          "chez un prestataire, sous Proxmox VE, avec une sauvegarde organisée autour de "
          "Proxmox Backup Server.", small=True)
    tab_titre(doc, "TAB-01", "Les quatre étapes de la démarche")
    doc.table(METHODE_HEADERS, METHODE_ROWS, METHODE_WIDTHS, font=8.2,
              aligns=["l", "l", "l"], first_col_bold=True, header_bg=BLEU)
    doc.p("**Utilité du tableau.** Il fixe l’ordre des choses : on ne consulte pas avant "
          "d’avoir mesuré, et l’on n’arbitre pas sur des nomenclatures différentes.",
          small=True)

    doc.p("**Mesurer.** Trente jours de relevés par machine virtuelle : CPU moyen et p95, "
          "temps d’attente, mémoire allouée contre consommée, SWAP, IOPS et latence, "
          "croissance mensuelle. Sans ces chiffres, tout dimensionnement reste une opinion.",
          small=True)
    doc.p("**Spécifier.** Un socle unique, le même pour tous les devis (TAB-04) : 128 Go "
          "DDR5 ECC, au moins 2 To utiles après RAID1, 12 à 16 cœurs, 2 × 10 GbE, iLO, "
          "alimentations redondantes, rails et garantie trois ans.", small=True)
    doc.p("**Consulter.** Trois revendeurs au moins, sur une nomenclature identique, un "
          "Incoterm identique et une même durée de garantie. Une ligne manquante rend "
          "l’offre non comparable.", small=True)
    doc.p("**Arbitrer.** Sur la grille de pondération (TAB-11), et non sur le prix "
          "affiché : la ressource contrainte pèse deux fois plus que le coût total livré.",
          small=True)
    doc.p("Les valeurs qui suivent sont des observations transmises, pas des mesures "
          "certifiées. Les prix cités sont des repères de novembre 2026 : ils ne "
          "constituent pas des engagements fournisseurs. Les dimensions ne sont reprises "
          "que lorsqu’une fiche constructeur est identifiée.", small=True)

    # ------------------------------------------------------------------ 2
    doc.spacer(0.25)
    sous_titre(doc, "2.  État de l’existant et limites des mesures")
    tab_titre(doc, "TAB-02", "Relevés disponibles et interprétation")
    cells, body = {}, []
    for i, (ind, cap, occ, lecture, st) in enumerate(EXIST_ROWS):
        f, t = FMT[st]
        cells[(i, 3)] = {"bg": f, "color": t, "b": True}
        body.append([ind, cap, occ, lecture])
    doc.table(EXIST_HEADERS, body, EXIST_WIDTHS, font=8.2,
              aligns=["l", "l", "c", "l"], first_col_bold=True, header_bg=BLEU,
              zebra=False, cell_fmt=cells)
    doc.p("**Utilité du tableau.** Il désigne la ressource qui décide du dimensionnement — "
          "ici la mémoire, à 88,4 %, et le stockage, à 89,9 % — et évite d’acheter des "
          "cœurs dont personne n’a besoin.", small=True)

    doc.p("**Lecture des deux chiffres qui comptent.** 88,4 % de 64 Go laissent environ "
          "7 Go réellement disponibles : c’est moins que ce qu’un hôte Proxmox, ses "
          "snapshots et une restauration demandent au même moment. De même, 89,9 % de "
          "960 Go laissent une centaine de gigaoctets, quand une seule sauvegarde "
          "complète peut en réclamer davantage.", small=True)

    doc.spacer(0.15)
    tab_titre(doc, "TAB-03", "Mesures complémentaires à demander avant l’arbitrage")
    doc.table(MES_HEADERS, MES_ROWS, MES_WIDTHS, font=8.2,
              aligns=["l", "l", "c"], first_col_bold=True, header_bg=BLEU)
    doc.p("**Utilité du tableau.** Il transforme les relevés ponctuels en preuves : trente "
          "jours de mesures par machine virtuelle valent mieux qu’une capture d’écran.",
          small=True)

    doc.p("**Ce que ces relevés ne disent pas.**", small=True)
    doc.ul([
        "Le pic n’est pas la moyenne : 15 % de moyenne peut cacher des saturations courtes "
        "aux heures de pointe.",
        "L’occupation disque ne distingue ni les données utiles, ni les snapshots, ni les "
        "fichiers temporaires.",
        "Un SWAP à 100 % peut venir d’une machine mal réglée autant que d’un manque de "
        "mémoire physique.",
        "Aucune projection de croissance n’est fournie : la réserve se décide, elle ne se "
        "constate pas.",
    ], small=True)
    doc.callout(
        "Précaution",
        "Un SWAP à ≈ 100 % ne prouve pas à lui seul que la RAM physique est la cause. Il "
        "faut identifier les VM concernées et distinguer consommation réelle, mémoire "
        "réservée et défaut applicatif.", kind="warn")

    # ------------------------------------------------------------------ 3
    doc.spacer(0.25)
    sous_titre(doc, "3.  Besoin cible et exigences minimales")
    doc.p("Le socle ci-dessous est commun à toutes les offres : c’est lui qui rend les "
          "devis comparables. Il repose sur quatre hypothèses de travail.", small=True)
    doc.p("**Hypothèses retenues pour le dimensionnement.**", small=True)
    doc.ul([
        "128 Go aujourd’hui, 256 Go demain : les slots libres et le prix de l’extension "
        "sont exigés au devis.",
        "12 à 16 cœurs avec surallocation raisonnée ; les licences Proxmox se comptent par "
        "socket, pas par cœur.",
        "Une croissance de stockage projetée sur trente-six mois, et le disque de rechange "
        "livré avec la machine.",
        "Hors périmètre : postes de travail, cœur de réseau, climatisation de la salle et "
        "applications métier.",
    ], small=True)

    tab_titre(doc, "TAB-04", "Exigences minimales et points à faire préciser")
    doc.table(BESOIN_HEADERS, BESOIN_ROWS, BESOIN_WIDTHS, font=8.2,
              aligns=["l", "l", "l"], first_col_bold=True, header_bg=BLEU)
    doc.p("**Utilité du tableau.** Il sert de cahier de consultation : chaque ligne se "
          "retrouve telle quelle dans la demande de prix, et une offre qui n’y répond pas "
          "s’écarte sans discussion.", small=True)
    doc.p("Deux disques de 1,92 To en RAID1 donnent **1,92 To utiles**, non 3,84 To : "
          "exiger le niveau de RAID, la compatibilité contrôleur / ZFS et le disque de "
          "rechange.", small=True)

    doc.p("Le 10 GbE n’a de valeur que si le switch, les optiques et la cible de sauvegarde "
          "suivent ; RAID1 ne remplace ni PBS, ni la copie hors site, ni les tests de "
          "restauration.", small=True)

    # ------------------------------------------------------------------ 4
    doc.spacer(0.25)
    sous_titre(doc, "4.  Comparatif HPE AMD / Intel à consulter")
    tab_titre(doc, "TAB-05", "Processeurs candidats et châssis à faire coter")
    cells, body = {}, []
    for i, (fam, cpu, cœurs, châssis, st) in enumerate(FAM_ROWS):
        f, t = FMT[st]
        cells[(i, 3)] = {"color": t}
        body.append([fam, cpu, cœurs, châssis])
    doc.table(FAM_HEADERS, body, FAM_WIDTHS, font=8.2,
              aligns=["l", "l", "c", "l"], first_col_bold=True, header_bg=BLEU,
              cell_fmt=cells)
    doc.p("**Utilité du tableau.** Il met les deux voies sur la même ligne de départ : même "
          "mémoire, même stockage utile, même réseau, même garantie. Une seule référence est "
          "adossée à une fiche constructeur ; les autres restent à confirmer.", small=True)

    doc.spacer(0.15)
    tab_titre(doc, "TAB-06", "Les deux voies face à face")
    doc.table(FACE_HEADERS, FACE_ROWS, FACE_WIDTHS, font=8.2,
              aligns=["l", "l", "l"], first_col_bold=True, header_bg=BLEU)
    doc.p("**Utilité du tableau.** Il montre que le choix ne se joue pas sur le processeur "
          "seul : les deux voies répondent au même besoin, avec des risques de "
          "nomenclature différents.", small=True)

    doc.p("**Point de méthode.** Exiger la validation HPE écrite du triplet "
          "châssis / processeur / mémoire. Sous Proxmox, les licences se comptent par "
          "socket, non par cœur : ne pas réduire artificiellement les cœurs pour économiser "
          "une licence.", small=True)

    # ------------------------------------------------------------------ 5
    doc.spacer(0.25)
    sous_titre(doc, "5.  Encombrement, architecture et exploitation")
    tab_titre(doc, "TAB-07", "Dimensions et poids — données constructeur ou à confirmer")
    cells, body = {}, []
    for i, (mod, dim, poids, statut, st) in enumerate(DIM_ROWS):
        f, t = FMT[st]
        cells[(i, 3)] = {"color": t, "b": st == "v"}
        body.append([mod, dim, poids, statut])
    doc.table(DIM_HEADERS, body, DIM_WIDTHS, font=8.2,
              aligns=["l", "l", "l", "l"], first_col_bold=True, header_bg=BLEU,
              cell_fmt=cells)
    doc.p("**Utilité du tableau.** Il évite les mauvaises surprises de baie et de transport : "
          "le poids varie avec les disques, les DIMM, les alimentations et les options. "
          "Exiger les dimensions du colis final, les rails et le dégagement arrière.",
          small=True)

    doc.p("**Contraintes d’installation à vérifier avant commande.**", small=True)
    doc.ul([
        "Hauteur et profondeur de baie, dégagement arrière pour les câbles et la "
        "ventilation.",
        "Charge admissible sur les rails : 15,5 kg en haut de fourchette pour le DL325.",
        "Cheminement du colis de 91,6 cm de long et de 24,2 cm de haut : porte, monte-charge, "
        "escalier.",
        "Deux circuits d’alimentation ou, à défaut, un onduleur dimensionné pour l’arrêt "
        "propre.",
    ], small=True)

    doc.spacer(0.15)
    tab_titre(doc, "TAB-08", "Architecture cible, couche par couche")
    doc.table(COUCHE_HEADERS, COUCHE_ROWS, COUCHE_WIDTHS, font=8.2,
              aligns=["l", "l", "l"], first_col_bold=True, header_bg=BLEU)
    doc.p("**Utilité du tableau.** Il rappelle que le serveur n’est qu’une couche : sans "
          "sauvegarde testée, sans réseau et sans onduleur, la plateforme reste fragile.",
          small=True)
    doc.p("Un hôte unique reste un point de défaillance. Le RAID ne protège ni contre la "
          "panne serveur, ni contre le vol, ni contre l’incendie, ni contre un chiffrement "
          "malveillant : la restauration hors site doit être testée.", small=True)
    doc.p("**Exploitation courante.** Proxmox VE s’administre depuis une interface web : "
          "création et migration des machines virtuelles, instantanés, planification des "
          "sauvegardes vers PBS. Les mises à jour se font hôte par hôte et supposent un "
          "redémarrage planifié hors des heures de service.", small=True)
    doc.p("**Surveillance.** Les alertes à brancher dès la mise en service : température et "
          "ventilateurs, état RAID et disques, occupation mémoire, espace des sauvegardes, "
          "test de restauration mensuel. Sans cela, la panne se découvre au moment où l’on "
          "en a le plus besoin.", small=True)

    # ------------------------------------------------------------------ 6
    doc.spacer(0.25)
    sous_titre(doc, "6.  Cotations, budget complet et grille d’arbitrage")
    doc.p("Les montants ci-dessous sont des repères issus des documents communiqués. Ils sont "
          "indicatifs, à revalider, et aucun ne constitue un prix ferme.", small=True)
    doc.p("**Trois prix, trois périmètres.** Un relevé à 5 726 € sans disques, une estimation "
          "de 8 900 à 12 900 € pour la cible équipée et un reconditionné à 3 200 € ne "
          "mesurent pas la même chose. Toute offre est d’abord ramenée au même périmètre — "
          "mémoire, capacité utile, réseau, garantie — avant d’être chiffrée.", small=True)
    tab_titre(doc, "TAB-09", "Repères de prix HT et réserves associées")
    cells, body = {}, []
    for i, (ref, prix, fc, nature, st) in enumerate(PRIX_ROWS):
        f, t = FMT[st]
        cells[(i, 3)] = {"color": t}
        body.append([ref, prix, fc, nature])
    doc.table(PRIX_HEADERS, body, PRIX_WIDTHS, font=8.0,
              aligns=["l", "r", "r", "l"], header_bg=BLEU, cell_fmt=cells,
              caption="Montants HT ; FCFA en millions, au taux de 655,957.")
    doc.p("**Utilité du tableau.** Il montre l’écart entre un relevé partiel (5 726 €, "
          "64 Go, sans disques) et une machine réellement équipée : c’est le piège de "
          "comparaison le plus fréquent.", small=True)

    doc.spacer(0.15)
    tab_titre(doc, "TAB-10", "Postes à intégrer au coût complet du projet")
    cells, body = {}, []
    for i, (poste, couvre, statut, st) in enumerate(COUT_ROWS):
        f, t = FMT[st]
        cells[(i, 2)] = {"bg": f, "color": t, "b": True}
        body.append([poste, couvre, statut])
    doc.table(COUT_HEADERS, body, COUT_WIDTHS, font=8.2,
              aligns=["l", "l", "l"], first_col_bold=True, header_bg=BLEU,
              zebra=False, cell_fmt=cells)
    doc.p("**Utilité du tableau.** Il donne la liste exhaustive des lignes à faire chiffrer : "
          "un devis qui s’arrête au serveur laisse huit postes hors budget.", small=True)

    doc.spacer(0.15)
    tab_titre(doc, "TAB-11", "Grille de pondération proposée pour l’arbitrage")
    doc.table(POND_HEADERS, POND_ROWS, POND_WIDTHS, font=8.2,
              aligns=["l", "c", "l"], first_col_bold=True, header_bg=BLEU)
    doc.p("**Utilité du tableau.** Elle empêche que le prix tranche seul : 30 % vont à la "
          "ressource réellement contrainte, 15 % seulement au coût total livré.", small=True)

    doc.p("**Coût sur trois ans.** La garantie constructeur couvre les pièces, pas "
          "l’immobilisation : un serveur arrêté faute de disque de rechange coûte plus cher "
          "que le disque. Ajouter au prix d’achat le support, la consommation électrique de "
          "l’onduleur et du serveur, et le temps d’exploitation annuel.", small=True)
    doc.p("**Ce que change le reconditionné.** Un DL380 Gen10 à 3 200 € divise le prix par "
          "quatre, mais déplace le risque : génération antérieure, garantie plus courte, "
          "disques d’occasion, pièces plus difficiles à trouver. Il n’est retenu que si "
          "l’audit du processeur, l’état des disques et la couverture de garantie sont "
          "écrits noir sur blanc.", small=True)

    # ------------------------------------------------------------------ 7
    doc.spacer(0.25)
    sous_titre(doc, "7.  Risques, questions au revendeur et suite")
    tab_titre(doc, "TAB-12", "Risques identifiés et mesures de réduction")
    cells, body = {}, []
    for i, (risk, impact, mesure, st) in enumerate(RISK_ROWS):
        f, t = FMT[st]
        cells[(i, 1)] = {"color": t}
        body.append([risk, impact, mesure])
    doc.table(RISK_HEADERS, body, RISK_WIDTHS, font=8.2,
              aligns=["l", "l", "l"], first_col_bold=True, header_bg=BLEU,
              cell_fmt=cells)
    doc.p("**Utilité du tableau.** Il donne au comité les six points sur lesquels une "
          "économie mal placée se paie plus tard.", small=True)

    doc.spacer(0.15)
    tab_titre(doc, "TAB-13", "Questions à poser au revendeur, par écrit")
    doc.table(QUEST_HEADERS, QUEST_ROWS, QUEST_WIDTHS, font=8.2,
              aligns=["l", "l", "l"], first_col_bold=True, header_bg=BLEU)
    doc.p("**Utilité du tableau.** Il transforme une négociation orale en liste vérifiable : "
          "chaque réponse entre au dossier de comparaison, chaque absence de réponse devient "
          "une réserve.", small=True)

    doc.p("**Suite proposée.**", small=True)
    doc.ul([
        "**Sous quinze jours** — obtenir les relevés de trente jours et arrêter la liste "
        "des machines virtuelles à reprendre.",
        "**Sous un mois** — envoyer le cahier de consultation (TAB-04) et la grille de "
        "cotation à trois revendeurs.",
        "**À réception** — ramener chaque offre au coût livré et au coût sur trois ans, "
        "puis la noter sur la grille (TAB-11).",
        "**Au comité** — arbitrer, puis commander le disque de rechange avec le serveur, "
        "pas après la panne.",
    ], small=True)

    doc.spacer(0.2)
    doc.callout(
        "Décision sollicitée",
        "Valider le socle — 128 Go DDR5 ECC, ≥ 2 To utiles après RAID1, 12 à 16 cœurs, "
        "2 × 10 GbE, garantie 3 ans ; autoriser la mise en concurrence AMD / Intel sur au "
        "moins trois devis à nomenclature identique ; lancer les mesures par machine "
        "virtuelle ; revenir au comité avec le coût complet, les avantages, les limites et "
        "les écarts techniques de chaque offre.", kind="warn")

    # ------------------------------------------------------------------ 8
    doc.spacer(0.25)
    sous_titre(doc, "8.  Repères de vocabulaire pour la lecture")
    doc.p("Les termes techniques employés dans ce dossier, en une ligne chacun, pour une "
          "lecture sans spécialiste.", small=True)
    tab_titre(doc, "TAB-14", "Vocabulaire employé dans le dossier")
    doc.table(VOCAB_HEADERS, VOCAB_ROWS, VOCAB_WIDTHS, font=8.2,
              aligns=["l", "l"], first_col_bold=True, header_bg=BLEU)
    doc.p("**Utilité du tableau.** Il permet au comité de lire les tableaux précédents sans "
          "traduction et au revendeur de savoir de quel niveau de service on parle.",
          small=True)

    doc.p("**Limites de l’exercice.** Les prix cités sont des repères, non des offres. Les "
          "compatibilités processeur / châssis restent à confirmer par HPE, sauf la "
          "référence adossée à une fiche constructeur. Aucun délai de livraison n’est "
          "garanti à ce stade. Aucune mesure certifiée n’a encore été produite : le "
          "dimensionnement s’appuie sur les relevés transmis.", small=True)
    doc.p("**Documents à réunir pour le comité.**", small=True)
    doc.ul([
        "Les relevés de trente jours, par machine virtuelle et par ressource.",
        "Le cahier de consultation (TAB-04) complété et daté.",
        "Les trois devis, ramenés au coût livré, avec Incoterm et garantie identiques.",
        "La grille de pondération (TAB-11) notée offre par offre.",
    ], small=True)

    doc.spacer(0.15)
    tab_titre(doc, "TAB-15", "Fiche de cotation à remplir à réception des devis")
    doc.table(FICHE_HEADERS, [[c, "", "", ""] for c in FICHE_ROWS], FICHE_WIDTHS, font=8.2,
              aligns=["l", "c", "c", "c"], first_col_bold=True, header_bg=BLEU)
    doc.p("**Utilité du tableau.** Il donne au comité une feuille unique où chaque offre "
          "s’inscrit ligne à ligne : ce qui reste vide est un point à demander, non un "
          "détail.", small=True)

    doc.spacer(0.3)
    doc.p("Joël MBA OYONE — GED-SERVICES, services informatiques · novembre 2026",
          small=True)

    return doc.save(OUTDIR)


if __name__ == "__main__":
    print(build_doc())
