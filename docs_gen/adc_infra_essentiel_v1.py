# -*- coding: utf-8 -*-
"""ADCHIM — Infra_Serveur : « L'essentiel » (2 pages), version 1.

Rapatriement de l'hyperviseur : existant, socle à demander, familles HPE AMD / Intel,
budget indicatif et décision sollicitée.
"""
from __future__ import annotations

import os

from adc_infra_common import (BLEU, FMT, band, sous_titre, tab_titre)
from render import Doc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, os.environ.get("LIVRABLES_DIR",
                                           "estimations/Infra_Serveur"))
BASE = "ADC_Infra_Serveur_Essentiel_V1_2026-11-20"


# --------------------------------------------------------------------------- #
EXIST_HEADERS = ["Ressource", "Capacité", "Occupation", "Lecture"]
EXIST_WIDTHS = [2.6, 4.3, 2.4, 7.8]
EXIST_ROWS = [
    ["CPU", "8 cœurs / 2,5 GHz", "≈ 15 %", "Pas de tension CPU démontrée", "v"],
    ["RAM", "64 Go", "88,4 %", "Ressource prioritairement contrainte", "o"],
    ["Stockage", "≈ 960 Go", "89,9 %", "Capacité utile trop juste", "o"],
    ["SWAP", "—", "≈ 100 %", "Alerte à investiguer, VM par VM", "r"],
]

SOCLE_HEADERS = ["Élément", "Exigence minimum à faire coter"]
SOCLE_WIDTHS = [3.4, 13.7]
SOCLE_ROWS = [
    ["Mémoire", "**128 Go DDR5 ECC** livrés ; extension documentée à 256 Go et au-delà"],
    ["Stockage", "**≥ 2 To utiles après RAID1** ; 2 × 1,92 To + 1 disque identique de "
                 "rechange"],
    ["Processeur", "**12 à 16 cœurs** minimum ; AMD et Intel comparés à configuration "
                   "équivalente"],
    ["Réseau", "**2 × 10 GbE** natifs ; préciser BASE-T ou SFP+ (DAC, optiques, ports "
               "libres)"],
    ["Gestion, énergie", "HPE iLO ; doubles alimentations redondantes ; rails rack"],
    ["Garantie", "**3 ans constructeur**, couverture et procédure RMA au Gabon"],
    ["Sauvegarde", "Proxmox VE + PBS, copie hors site et tests de restauration"],
]

FAM_HEADERS = ["Famille", "Châssis à faire coter", "Processeurs candidats"]
FAM_WIDTHS = [2.3, 5.2, 9.6]
FAM_ROWS = [
    ["**AMD**", "DL325 Gen11, 1U / 8SFF",
     "EPYC 9124 (16C / 3,0 GHz) · 9125 (16C / 2,6) · 9224 (24C / 2,4)", "v"],
    ["**Intel**", "DL380 Gen11, DL320 Gen11 ou ML110 Gen11",
     "Xeon Silver 4510 (12C / 2,4) · 4410Y (12C / 2,0) · Gold 6426Y (16C / 2,4)", "v"],
]

BUDGET_HEADERS = ["Référence et périmètre", "Prix HT relevé", "Ordre de grandeur FCFA",
                  "Réserve"]
BUDGET_WIDTHS = [6.4, 3.6, 3.6, 3.5]
BUDGET_ROWS = [
    ["DL325 Gen11, EPYC 9124, 64 Go, sans disques", "5 726 €", "3,8 M", "Relevé partiel",
     "n"],
    ["DL325 Gen11, 128 Go + RAID1 + spare", "8 900 – 12 900 €", "5,8 – 8,5 M",
     "Estimation", "o"],
    ["DL320 Gen11, Xeon Silver 4410Y, 128 Go", "≈ 11 800 €", "7,7 M", "Benchmark", "o"],
    ["DL380 Gen11, Xeon Silver 4510, 128 Go", "≈ 13 900 €", "9,1 M", "Benchmark", "o"],
    ["ML110 Gen11, Xeon Gold 6426Y", "≈ 9 676 €", "6,3 M", "Périmètre à vérifier", "o"],
    ["DL380 Gen10 reconditionné, 128 Go", "≈ 3 200 €", "2,1 M", "Audit à faire", "r"],
]


def build_doc():
    doc = Doc(
        base=BASE,
        title="ADCHIM — l’essentiel du rapatriement de l’hyperviseur",
        subtitle="Existant, socle technique, familles HPE et budget",
        meta=[],
        doc_ref="ADCHIM · rapatriement de l’hyperviseur · novembre 2026",
        footer="GED-SERVICES · ADCHIM · rapatriement de l’hyperviseur · prix "
               "indicatifs à confirmer",
    )

    band(doc, "ADCHIM · rapatriement de l’hyperviseur · novembre 2026",
         "L’essentiel — rapatrier l’hyperviseur",
         "Deux pages pour décider : l’existant, le socle à demander, les familles à "
         "comparer, le budget.")

    doc.p("L’objectif n’est pas de choisir une marque ni un processeur par préférence, mais "
          "d’acheter une **capacité exploitable, évolutive et correctement garantie**. La "
          "méthode part des sollicitations réellement observées sur la plateforme actuelle, "
          "puis met les offres en concurrence sur une **nomenclature identique**.", small=True)
    doc.p("**Code couleur** — vert : maîtrisé ou conforme ; orange : sous surveillance ou à "
          "confirmer ; rouge : contrainte ou risque à traiter. Les prix sont des repères de "
          "novembre 2026, hors engagement fournisseur.", small=True)

    # ------------------------------------------------------------------ 1
    doc.spacer(0.1)
    sous_titre(doc, "1.  Ce que nous savons de l’existant")
    cells, bg = {}, {}
    body = []
    for i, (res, cap, occ, lecture, st) in enumerate(EXIST_ROWS):
        f, t = FMT[st]
        cells[(i, 3)] = {"bg": f, "color": t, "b": True}
        body.append([res, cap, occ, lecture])
    tab_titre(doc, "TAB-01", "État de l’existant et lecture des relevés")
    doc.table(EXIST_HEADERS, body, EXIST_WIDTHS, font=8.2,
              aligns=["l", "l", "c", "l"], first_col_bold=True, header_bg=BLEU,
              zebra=False, cell_fmt=cells)
    doc.p("Ces relevés donnent le sens du dimensionnement. Ils ne remplacent pas une mesure "
          "des pics, des IOPS, de la latence et de la consommation réelle par machine "
          "virtuelle : le SWAP peut traduire un manque de RAM, une surallocation ou un "
          "comportement applicatif.", small=True)

    doc.spacer(0.2)
    doc.p("**Ce qu’il faut mesurer avant d’arbitrer** — quatre relevés sur trente jours, "
          "par machine virtuelle :", small=True)
    doc.ul([
        "**CPU** : moyenne, pics, p95, temps d’attente en file (ready) par VM.",
        "**Mémoire** : allouée contre consommée, ballooning, cache, SWAP par VM.",
        "**Stockage** : IOPS, latence p95, débit et croissance mensuelle.",
        "**Disponibilité** : incidents, fenêtres de service, RTO et RPO attendus.",
    ], small=True)

    # ------------------------------------------------------------------ 2
    doc.spacer(0.2)
    sous_titre(doc, "2.  Le socle technique à demander")
    tab_titre(doc, "TAB-02", "Exigences minimales, identiques pour toutes les offres")
    doc.table(SOCLE_HEADERS, SOCLE_ROWS, SOCLE_WIDTHS, font=8.2,
              aligns=["l", "l"], first_col_bold=True, header_bg=BLEU)

    # ------------------------------------------------------------------ 3
    doc.pagebreak()
    sous_titre(doc, "3.  Les deux familles HPE à mettre en concurrence")
    tab_titre(doc, "TAB-03", "Familles, châssis et processeurs candidats")
    doc.table(FAM_HEADERS, [r[:3] for r in FAM_ROWS], FAM_WIDTHS, font=8.2,
              aligns=["l", "l", "l"], first_col_bold=True, header_bg=BLEU)
    doc.p("**Point de méthode.** Aucune référence n’est validée comme choix définitif : le "
          "revendeur doit confirmer par écrit la compatibilité châssis / processeur, la "
          "mémoire supportée, les ports, le contrôleur et la disponibilité. Sous Proxmox, "
          "les licences se comptent par socket, non par cœur — inutile de réduire les cœurs "
          "pour économiser une licence.", small=True)

    # ------------------------------------------------------------------ 4
    doc.spacer(0.25)
    sous_titre(doc, "4.  Le budget à prévoir")
    tab_titre(doc, "TAB-04", "Repères de prix HT et réserves associées")
    cells, body = {}, []
    for i, (ref, prix, fc, reserve, st) in enumerate(BUDGET_ROWS):
        f, t = FMT[st]
        cells[(i, 3)] = {"color": t}
        body.append([ref, prix, fc, reserve])
    doc.table(BUDGET_HEADERS, body, BUDGET_WIDTHS, font=8.0,
              aligns=["l", "r", "r", "l"], header_bg=BLEU, cell_fmt=cells)
    doc.p("Prix HT indicatifs, relevés de novembre 2026 ; aucun n’est un prix ferme. Le "
          "coût du projet ne s’arrête pas au serveur : disques et rechange, rails, réseau et "
          "optiques, onduleur, licences Proxmox / PBS, fret, assurance, douane, intégration "
          "et migration.", small=True)

    # ------------------------------------------------------------------ attention
    doc.spacer(0.2)
    doc.ul([
        "**Ne pas retenir une machine à 64 Go** au motif qu’elle est neuve : la mémoire est "
        "la ressource contrainte (88,4 %).",
        "**Brut n’est pas utile** : deux disques de 1,92 To en RAID1 donnent ≈ 1,92 To "
        "utiles, pas 3,84 To.",
        "**Un hôte unique reste un point de défaillance** : le RAID ne protège ni de la "
        "panne serveur, ni du vol, ni de l’incendie.",
        "**Vérifier la garantie au Gabon** et la procédure de retour avant de commander.",
    ], small=True)

    doc.spacer(0.2)
    doc.callout(
        "Décision sollicitée",
        "Valider le socle — 128 Go DDR5 ECC, ≥ 2 To utiles après RAID1, 12 à 16 cœurs, "
        "2 × 10 GbE, garantie 3 ans ; autoriser la mise en concurrence AMD / Intel sur au "
        "moins trois devis à nomenclature identique ; exiger dimensions, poids, garantie et "
        "Incoterm ; lancer les mesures par VM avant l’arbitrage final.", kind="warn")

    doc.spacer(0.15)
    doc.p("Joël MBA OYONE — GED-SERVICES, services informatiques · novembre 2026",
          small=True)

    return doc.save(OUTDIR)


if __name__ == "__main__":
    print(build_doc())
