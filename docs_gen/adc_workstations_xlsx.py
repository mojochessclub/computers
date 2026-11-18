# -*- coding: utf-8 -*-
"""Classeur Excel de la note d'arbitrage ADCHIM — postes fixes Intel / AMD.

Le classeur reprend mot pour mot les données du document Word : une feuille par
gamme, puis le face-à-face, les processeurs et la méthode. Aucun prix n'est
calculé ici, sauf la conversion FCFA qui reste une formule (1 € = 655,957 FCFA),
pour que le lecteur puisse vérifier ou rectifier un taux.
"""
from __future__ import annotations

import os

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

from adc_workstations import (CONFORT, CPU_ROWS, DUREE, ENTREE, EQUIV_ROWS,
                              SEUILS, STANDARD, TVA, VIGILANCE)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, os.environ.get("LIVRABLES_DIR",
                                           "estimations/ADC_Workstations 2026-11-18"))
BASE = "ADC_Workstations_2026-11-18_Catalogue_et_face_a_face"

BLEU = "1F3B63"
GRIS_TXT = "555B66"
FILL = {
    "v": PatternFill("solid", fgColor="D8EDCB"),
    "o": PatternFill("solid", fgColor="FAEBB8"),
    "r": PatternFill("solid", fgColor="F8CDB6"),
    "n": PatternFill("solid", fgColor="E9EBEF"),
}
TXT = {"v": "1E6B33", "o": "7A5E12", "r": "9B2C12", "n": "4A5058"}
CONF_LABEL = {"v": "Conforme", "o": "Partielle", "r": "Non conforme", "n": "Sans objet"}
FILL_INTEL = PatternFill("solid", fgColor="E3ECF7")
FILL_AMD = PatternFill("solid", fgColor="EDE3F2")
FILL_TETE = PatternFill("solid", fgColor="EDF1F7")
THIN = Side(style="thin", color="D0D7E2")
BORDER = Border(bottom=THIN)

EUR = '#,##0.00\\ "€"'
FCFA = '#,##0\\ "FCFA"'

GAMMES = [("Entrée de gamme", ENTREE, "Entrée de gamme"),
          ("Standard entreprise", STANDARD, "Standard entreprise"),
          ("Confort", CONFORT, "Confort")]

COLS = ["Constructeur", "Modèle", "Voie", "État", "Processeur", "Année de sortie",
        "Obsolescence présumée", "Mémoire · stockage", "Prix livré (€)",
        "Équivalent FCFA", "Conformité au profil", "Commentaire", "Fiche produit"]
WIDTHS = [13, 32, 8, 14, 22, 10, 12, 34, 13, 15, 14, 52, 12]


def _sheet(ws, headers, widths, freeze="B2", header_row=1):
    for c, (h, w) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=header_row, column=c, value=h)
        cell.fill = PatternFill("solid", fgColor=BLEU)
        cell.font = Font(color="FFFFFF", bold=True, size=9, name="Calibri")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = BORDER
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.row_dimensions[header_row].height = 34
    ws.freeze_panes = freeze
    ws.sheet_properties.tabColor = BLEU


def _gamme_sheet(wb, nom, rows):
    ws = wb.create_sheet(nom if len(nom) <= 31 else nom[:31])
    _sheet(ws, COLS, WIDTHS, freeze="B5", header_row=4)
    for i, r in enumerate(rows, start=5):
        vals = [r["constructeur"], r["modele"], r["plateforme"], r["etat"], r["cpu"],
                r["annee"], "%d — %d ans de détention" % (r["obso"], DUREE),
                r["config"],
                r["prix"] if r["prix"] is not None else "à chiffrer",
                None, CONF_LABEL[r["conf"]], r["commentaire"],
                "fiche produit" if r["lien"] else "—"]
        for j, v in enumerate(vals, 1):
            cell = ws.cell(row=i, column=j, value=v)
            cell.font = Font(size=9, name="Calibri")
            cell.border = BORDER
            cell.alignment = Alignment(wrap_text=True, vertical="top")
        ws.cell(row=i, column=6).alignment = Alignment(horizontal="center", vertical="top")
        ws.cell(row=i, column=7).alignment = Alignment(horizontal="center", vertical="top")
        # prix
        pc = ws.cell(row=i, column=9)
        if r["prix"] is None:
            pc.value = "à chiffrer"
            pc.font = Font(size=9, name="Calibri", italic=True, color=TXT["o"])
            pc.alignment = Alignment(horizontal="right", vertical="top")
        else:
            pc.number_format = EUR
            pc.alignment = Alignment(horizontal="right", vertical="top")
        # FCFA : formule, pour que le taux reste vérifiable
        fc = ws.cell(row=i, column=10, value="=IF(ISNUMBER($I%d),ROUND($I%d*%s,0),\"—\")"
                                           % (i, i, TVA))
        fc.number_format = FCFA
        fc.alignment = Alignment(horizontal="right", vertical="top")
        # voie
        vc = ws.cell(row=i, column=3)
        vc.font = Font(size=9, name="Calibri", bold=True)
        vc.fill = FILL_AMD if r["plateforme"] == "AMD" else FILL_INTEL
        vc.alignment = Alignment(horizontal="center", vertical="top")
        # conformité
        cc = ws.cell(row=i, column=11)
        cc.fill = FILL[r["conf"]]
        cc.font = Font(size=9, name="Calibri", bold=True, color=TXT[r["conf"]])
        cc.alignment = Alignment(horizontal="center", vertical="top", wrap_text=True)
        # constructeur en gras
        ws.cell(row=i, column=1).font = Font(size=9, name="Calibri", bold=True)
        # lien
        lc = ws.cell(row=i, column=13)
        if r["lien"]:
            lc.hyperlink = r["lien"]
            lc.font = Font(size=9, name="Calibri", color="1155CC", underline="single")
            lc.alignment = Alignment(horizontal="center", vertical="top")
    ws["A1"] = "%s — deux références par constructeur et par voie" % nom
    ws["A1"].font = Font(size=13, bold=True, color=BLEU, name="Calibri")
    ws["A2"] = ("Deux références par constructeur et par voie. Prix TTC relevés le "
                "18 novembre 2026 ; « à chiffrer » signale une machine réelle dont aucun "
                "distributeur ne publie le prix. 1 € = 655,957 FCFA.")
    ws["A2"].font = Font(size=9, italic=True, color=GRIS_TXT, name="Calibri")
    return ws


def _synthese(wb):
    ws = wb.active
    ws.title = "Synthèse"
    ws.sheet_properties.tabColor = "C05621"
    ws["A1"] = "Postes fixes ADCHIM — benchmark Intel / AMD"
    ws["A1"].font = Font(size=15, bold=True, color=BLEU, name="Calibri")
    ws["A2"] = ("Note d'arbitrage du 18 novembre 2026 — Joël MBA OYONE, GED-SERVICES, "
                "à l'attention de Jad SAID, directeur général d'ADCHIM.")
    ws["A2"].font = Font(size=9, italic=True, color=GRIS_TXT, name="Calibri")

    lignes = [
        ("Enveloppe par poste", "650 € à 1 350 €, écran, clavier et livraison non compris"),
        ("Gammes", "Entrée de gamme (650–850 €) · Standard entreprise (850–1 200 €) · "
                   "Confort (1 200–1 350 €)"),
        ("Références par gamme", "6 Intel + 6 AMD : deux HP, deux Dell, deux Lenovo par voie. "
                                 "Pas d'offre AMD chez Dell — fait de catalogue, pas un oubli."),
        ("Prix", "TTC, port compris quand il est connu. Illustratifs : ils servent à arbitrer, "
                 "pas à contractualiser."),
        ("Conversion", "1 € = 655,957 FCFA, parité fixe — les formules FCFA des feuilles gammes "
                       "la recalculent."),
        ("Obsolescence présumée", "Année de sortie du processeur + %d ans de détention." % DUREE),
        ("Recommandation", "Lenovo ThinkCentre M75q Gen 5 en AMD (1 139,49 €) comme standard "
                           "d'achat ; HP Elite 800 G9 Mini en Intel (1 140,18 €) comme repli."),
        ("Point d'arbitrage", "La cible 32 Go porte le poste à ≈ 1 389,49 €, soit ≈ 39 € au-dessus "
                              "du plafond."),
    ]
    r = 4
    for lib, val in lignes:
        a = ws.cell(row=r, column=1, value=lib)
        a.font = Font(size=9, bold=True, color=BLEU, name="Calibri")
        a.alignment = Alignment(vertical="top")
        b = ws.cell(row=r, column=2, value=val)
        b.font = Font(size=9, name="Calibri")
        b.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[r].height = 30
        r += 1

    r += 1
    ws.cell(row=r, column=1, value="Code couleur").font = Font(size=10, bold=True, color=BLEU,
                                                               name="Calibri")
    r += 1
    for key, txt in (("v", "Conforme au profil : tout y est, dans l'enveloppe"),
                     ("o", "Partielle, ou prix non relevé"),
                     ("r", "Non conforme, ou hors enveloppe")):
        c = ws.cell(row=r, column=1, value=CONF_LABEL[key])
        c.fill = FILL[key]
        c.font = Font(size=9, bold=True, color=TXT[key], name="Calibri")
        c.alignment = Alignment(horizontal="center")
        d = ws.cell(row=r, column=2, value=txt)
        d.font = Font(size=9, name="Calibri")
        r += 1

    r += 1
    ws.cell(row=r, column=1, value="Comptage par gamme").font = Font(size=10, bold=True,
                                                                     color=BLEU, name="Calibri")
    r += 1
    for j, h in enumerate(["Gamme", "Références", "dont chiffrées", "Conformes", "Partielles",
                           "Non conformes"], 1):
        c = ws.cell(row=r, column=j, value=h)
        c.fill = FILL_TETE
        c.font = Font(size=9, bold=True, color=BLEU, name="Calibri")
        c.border = BORDER
    r += 1
    for nom, rows, _ in GAMMES:
        vals = [nom, len(rows), sum(1 for x in rows if x["prix"]),
                sum(1 for x in rows if x["conf"] == "v"),
                sum(1 for x in rows if x["conf"] == "o"),
                sum(1 for x in rows if x["conf"] == "r")]
        for j, v in enumerate(vals, 1):
            c = ws.cell(row=r, column=j, value=v)
            c.font = Font(size=9, name="Calibri")
            c.border = BORDER
            c.alignment = Alignment(horizontal="left" if j == 1 else "center")
        r += 1
    ws.column_dimensions["A"].width = 22
    ws.column_dimensions["B"].width = 92
    for col in "CDEF":
        ws.column_dimensions[col].width = 14


def _f2f(wb):
    ws = wb.create_sheet("Face-à-face")
    headers = ["Gamme", "Constructeur", "Voie Intel — modèle", "Prix Intel (€)",
               "Voie AMD — modèle", "Prix AMD (€)", "Écart AMD − Intel (€)",
               "Écart en %", "Lecture"]
    width = [16, 13, 34, 13, 34, 13, 15, 10, 52]
    _sheet(ws, headers, width, freeze="C2")
    paires = [
        ("Entrée", "Lenovo", "M70q Gen 5 — i5-13500T", 840.00, "M75q Gen 5 — R5 PRO 8500GE",
         763.67, "AMD 76,33 € moins cher, en DDR5, avec six cœurs contre quatorze."),
        ("Entrée", "HP", "Pro 400 G9 SFF — i5-13500", 1039.22, "ProDesk 2 G1a — R5 8500G",
         827.52, "AMD 211,70 € moins cher, mais châssis tour et vendeur tiers."),
        ("Standard", "HP", "Elite 800 G9 Mini — i5-14500", 1140.18,
         "Elite 805 G9 SFF — R7 8700G", 1528.34,
         "AMD 388,16 € plus cher : l'écart paie le SFF et la Radeon 780M."),
        ("Standard", "Lenovo", "M90q Gen 5 — i5-14500T", 1532.86,
         "M75q Gen 5 — R7 PRO 8700GE", 1139.49,
         "AMD 393,37 € moins cher, à 16 Go des deux côtés."),
        ("Confort", "HP", "Pro Mini 400 G9 — i7-14700T", 1286.14,
         "Elite 805 G9 SFF — R7 8700G", 1528.34,
         "AMD 242,20 € plus cher, et seulement 16 Go / 512 Go."),
    ]
    for i, (g, c, mi, pi, ma, pa, lect) in enumerate(paires, start=2):
        ws.cell(row=i, column=1, value=g)
        ws.cell(row=i, column=2, value=c).font = Font(size=9, bold=True, name="Calibri")
        ws.cell(row=i, column=3, value=mi)
        ws.cell(row=i, column=4, value=pi).number_format = EUR
        ws.cell(row=i, column=5, value=ma)
        ws.cell(row=i, column=6, value=pa).number_format = EUR
        ec = ws.cell(row=i, column=7, value="=F%d-D%d" % (i, i))
        ec.number_format = '+#,##0.00\\ "€";-#,##0.00\\ "€"'
        pc = ws.cell(row=i, column=8, value="=ROUND(G%d/D%d*100,1)" % (i, i))
        pc.number_format = '+0.0"%";-0.0"%"'
        ws.cell(row=i, column=9, value=lect)
        for j in range(1, 10):
            cell = ws.cell(row=i, column=j)
            cell.border = BORDER
            cell.alignment = Alignment(wrap_text=True, vertical="top",
                                       horizontal="right" if j in (4, 6, 7, 8) else "left")
            if cell.font.size is None or j != 2:
                cell.font = Font(size=9, name="Calibri")
        ws.cell(row=i, column=2).font = Font(size=9, name="Calibri", bold=True)
        ws.cell(row=i, column=3).fill = FILL_INTEL
        ws.cell(row=i, column=5).fill = FILL_AMD
        # couleur de l'écart : vert si l'AMD est moins cher
        ec.fill = FILL["v"] if pa < pi else FILL["r"]
        ec.font = Font(size=9, bold=True, name="Calibri", color=TXT["v" if pa < pi else "r"])
    i = len(paires) + 3
    ws.cell(row=i, column=1, value="L'écart est calculé AMD moins Intel, à configuration "
                                  "équivalente : même mémoire, même stockage, même millésime. "
                                  "Il est vert quand l'AMD est moins cher.").font = Font(
        size=9, italic=True, color=GRIS_TXT, name="Calibri")


def _cpu(wb):
    ws = wb.create_sheet("Processeurs")
    headers = ["Année de sortie", "Intel", "Cœurs / threads Intel", "AMD",
               "Cœurs / threads AMD", "Gamme visée"]
    _sheet(ws, headers, [15, 34, 18, 34, 18, 22], freeze="B2")
    r = 2
    for row in CPU_ROWS:
        for j, v in enumerate(row, 1):
            c = ws.cell(row=r, column=j, value=v)
            c.font = Font(size=9, name="Calibri")
            c.border = BORDER
            c.alignment = Alignment(wrap_text=True, vertical="top",
                                    horizontal="center" if j == 1 else "left")
        r += 1
    r += 2
    ws.cell(row=r, column=1, value="Équivalences d'architecture").font = Font(
        size=11, bold=True, color=BLEU, name="Calibri")
    r += 1
    for j, h in enumerate(["Famille AMD", "Architecture", "Contemporain Intel", "Année",
                           "Lecture"], 1):
        c = ws.cell(row=r, column=j, value=h)
        c.fill = PatternFill("solid", fgColor=BLEU)
        c.font = Font(size=9, bold=True, color="FFFFFF", name="Calibri")
        c.alignment = Alignment(horizontal="center", wrap_text=True)
        c.border = BORDER
    r += 1
    for row in EQUIV_ROWS:
        for j, v in enumerate(row, 1):
            c = ws.cell(row=r, column=j, value=v)
            c.font = Font(size=9, name="Calibri")
            c.border = BORDER
            c.alignment = Alignment(wrap_text=True, vertical="top")
        r += 1
    r += 1
    ws.cell(row=r, column=1, value="Une comparaison n'a de sens qu'à époque comparable. "
                                  "L'obsolescence présumée se lit à partir de l'année de sortie "
                                  "du processeur, majorée de %d ans." % DUREE).font = Font(
        size=9, italic=True, color=GRIS_TXT, name="Calibri")


def _methode(wb):
    ws = wb.create_sheet("Seuils et méthode")
    ws["A1"] = "Seuils matériels retenus, et méthode de relevé"
    ws["A1"].font = Font(size=13, bold=True, color=BLEU, name="Calibri")
    r = 3
    for j, h in enumerate(["Critère", "Entrée de gamme", "Standard entreprise", "Confort"], 1):
        c = ws.cell(row=r, column=j, value=h)
        c.fill = PatternFill("solid", fgColor=BLEU)
        c.font = Font(size=9, bold=True, color="FFFFFF", name="Calibri")
        c.alignment = Alignment(horizontal="center", wrap_text=True, vertical="center")
        c.border = BORDER
    r += 1
    for row in SEUILS:
        for j, v in enumerate(row, 1):
            c = ws.cell(row=r, column=j, value=v)
            c.font = Font(size=9, name="Calibri", bold=(j == 1))
            c.border = BORDER
            c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[r].height = 28
        r += 1
    r += 2
    ws.cell(row=r, column=1, value="Sources, date et limites").font = Font(
        size=11, bold=True, color=BLEU, name="Calibri")
    r += 1
    for txt in (
        "Sources : relevés du marché français — Amazon.fr en référence principale, puis "
        "Cdiscount, Fnac, LDLC, Materiel.net, les sites constructeur HP, Dell et Lenovo, et "
        "deux distributeurs informatiques français.",
        "Date des relevés : 18 novembre 2026. Un prix d'enseigne bouge en quelques jours, "
        "surtout en reconditionné et sur les fins de série.",
        "Nature des prix : TTC, port compris quand il est connu. Ils sont illustratifs : un "
        "devis constructeur ou grossiste les décalera de 15 à 25 % à la baisse sur volume.",
        "Conversion : 1 € = 655,957 FCFA, parité fixe. Les francs sont exacts, les euros ne le "
        "sont pas — ils changent chaque semaine.",
        "Conformité : jugée sur la mémoire, le stockage, la puce et l'enveloppe. Une case orange "
        "n'est pas un avis, c'est un fait : un point manque, ou le prix n'est pas connu.",
        "Ce que le classeur ne fait pas : aucun benchmark mesuré, aucune volumétrie de parc, "
        "aucun devis ferme.",
    ):
        c = ws.cell(row=r, column=1, value=txt)
        c.font = Font(size=9, name="Calibri")
        c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
        ws.row_dimensions[r].height = 26
        r += 1
    ws.column_dimensions["A"].width = 24
    for col in "BCD":
        ws.column_dimensions[col].width = 34


def build_xlsx():
    wb = Workbook()
    _synthese(wb)
    for nom, rows, feuille in GAMMES:
        _gamme_sheet(wb, nom, rows)
    _f2f(wb)
    _cpu(wb)
    _methode(wb)
    os.makedirs(OUTDIR, exist_ok=True)
    path = os.path.join(OUTDIR, BASE + ".xlsx")
    wb.save(path)
    return path


if __name__ == "__main__":
    print(build_xlsx())
