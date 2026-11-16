# -*- coding: utf-8 -*-
"""Classeur Excel de la version alpha — profil, catalogue, face-à-face.

Le classeur reprend les données du document, une feuille par usage :
1) le profil opposable, 2) le catalogue des quinze machines, 3) le face-à-face
des tarifs Intel / AMD, 4) les repères de calcul, 5) la méthode.
Aucun prix n'est calculé ici : les montants viennent des relevés du document.
"""
from __future__ import annotations

import os

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

from profil_catalogue_alpha import (CONFORT, ENTREE, F2F, PROFIL_ROWS, REPERES,
                                    STANDARD, TVA)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.environ.get("LIVRABLES_DIR", "livrables")
BASE = "Postes_fixes_profil_cible_et_catalogue_Intel_AMD_alpha"

BLEU = "1F3B63"
GRIS_TXT = "555B66"
FILL = {
    "g": PatternFill("solid", fgColor="D8EDCB"),
    "y": PatternFill("solid", fgColor="FAEBB8"),
    "o": PatternFill("solid", fgColor="F8CDB6"),
    "n": PatternFill("solid", fgColor="E6E8EC"),
}
TXT = {"g": "1E6B33", "y": "7A5E12", "o": "A23B1A", "n": "555B66"}
FILL_INTEL = PatternFill("solid", fgColor="E3ECF7")
FILL_AMD = PatternFill("solid", fgColor="EDE3F2")
THIN = Side(style="thin", color="D0D7E2")
BORDER = Border(bottom=THIN)

EUR = '#,##0.00\\ "€"'
FCFA = '#,##0\\ "FCFA"'

GAMMES = [("Entrée de gamme", ENTREE, "entree"),
          ("Standard", STANDARD, "standard"),
          ("Confort", CONFORT, "confort")]


def _sheet(ws, headers, widths, freeze="B2"):
    for c, (h, w) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=1, column=c, value=h)
        cell.fill = PatternFill("solid", fgColor=BLEU)
        cell.font = Font(color="FFFFFF", bold=True, size=9, name="Calibri")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = BORDER
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.row_dimensions[1].height = 34
    ws.freeze_panes = freeze
    ws.sheet_properties.tabColor = BLEU


def _body(ws, row, values, widths_centre=(), money=()):
    for j, v in enumerate(values, 1):
        cell = ws.cell(row=row, column=j, value=v)
        cell.font = Font(size=9, name="Calibri")
        cell.alignment = Alignment(wrap_text=True, vertical="top",
                                   horizontal="center" if j in widths_centre else "left")
        cell.border = BORDER
        if j in money:
            cell.number_format = EUR
            cell.alignment = Alignment(horizontal="right", vertical="top")
    return row + 1


def _link(cell, url):
    cell.hyperlink = url
    cell.font = Font(size=9, name="Calibri", color="1155CC", underline="single")


def build_xlsx(path):
    wb = Workbook()

    # ---------------------------------------------------------------- 1 profil
    ws = wb.active
    ws.title = "1 Profil"
    _sheet(ws, ["Gamme", "Usage", "Millésime", "CPU Intel", "CPU AMD", "Mémoire",
                "Stockage", "GPU", "Garantie"],
           [20, 34, 11, 34, 24, 24, 14, 22, 10])
    for i, row in enumerate(PROFIL_ROWS, start=2):
        _body(ws, i, row, widths_centre=(3, 9))
    ws.freeze_panes = "B2"

    # ------------------------------------------------------------- 2 catalogue
    ws = wb.create_sheet("2 Catalogue")
    heads = ["Gamme", "Constructeur", "Voie", "Modèle", "État", "CPU", "Cœurs / threads",
             "Fréq. base", "Fréq. turbo", "RAM — capacité · type · fréquence",
             "Disque — capacité · interface · type", "Revendeur", "Prix livré €",
             "Prix FCFA", "Conformité au profil", "Lien"]
    widths = [17, 12, 7, 34, 14, 20, 13, 10, 10, 30, 30, 20, 13, 14, 52, 30]
    _sheet(ws, heads, widths, freeze="E2")
    r = 2
    for nom, jeu, _key in GAMMES:
        for m in jeu:
            if m["voie"] == "AMD" and m["modele"] == "—":
                continue
            vals = [nom, m["constructeur"], m["voie"], m["modele"], m["etat"], m["cpu"],
                    m["coeurs"], m["fbase"], m["fturbo"], m["ram"], m["disque"],
                    m["revendeur"],
                    m["prix"] if m["prix"] else "—",
                    int(round(m["prix"] * TVA)) if m["prix"] else "—",
                    m["conformite"], m["lien"].split("](")[-1].rstrip(")")]
            _body(ws, r, vals, widths_centre=(2, 3, 5, 7, 8, 9), money=(13,))
            ws.cell(row=r, column=14).number_format = FCFA
            ws.cell(row=r, column=14).alignment = Alignment(horizontal="right", vertical="top")
            code = m["code"]
            for col in (5, 15):
                ws.cell(row=r, column=col).fill = FILL[code]
                ws.cell(row=r, column=col).font = Font(size=9, name="Calibri", color=TXT[code])
            ws.cell(row=r, column=3).fill = FILL_AMD if m["voie"] == "AMD" else FILL_INTEL
            ws.cell(row=r, column=4).font = Font(size=9, name="Calibri", bold=True)
            if m["lien"].startswith("["):
                _link(ws.cell(row=r, column=16), vals[15])
            r += 1
    ws.auto_filter.ref = "A1:P%d" % (r - 1)

    # ------------------------------------------------------------ 3 face-à-face
    ws = wb.create_sheet("3 Face-à-face")
    heads = ["Gamme", "Constructeur", "Voie Intel — modèle", "Prix Intel €",
             "Voie AMD — modèle", "Prix AMD €", "Écart AMD − Intel €",
             "Écart %", "Ce que l'écart achète"]
    _sheet(ws, heads, [17, 12, 34, 13, 34, 13, 15, 9, 58], freeze="C2")
    r = 2
    for nom, _jeu, key in GAMMES:
        for cons, mi, pi, ma, pa, verdict in F2F[key]:
            ecart = round(pa - pi, 2) if (pi and pa) else "n. c."
            pct = (pa - pi) / pi if (pi and pa) else None
            _body(ws, r, [nom, cons, mi, pi if pi else "—", ma, pa if pa else "—",
                          ecart, pct, verdict],
                  widths_centre=(2, 8), money=(4, 6, 7))
            for col in (4, 6, 7):
                ws.cell(row=r, column=col).number_format = EUR
            if isinstance(pct, float):
                c = ws.cell(row=r, column=8)
                c.number_format = '+0.0%;-0.0%'
                c.fill = FILL["g"] if pct < 0 else FILL["o"]
                c.font = Font(size=9, name="Calibri",
                              color=TXT["g"] if pct < 0 else TXT["o"], bold=True)
            else:
                ws.cell(row=r, column=8).fill = FILL["n"]
            ws.cell(row=r, column=2).fill = FILL_INTEL
            ws.cell(row=r, column=5).fill = FILL_AMD
            r += 1
    ws.auto_filter.ref = "A1:I%d" % (r - 1)

    # --------------------------------------------------------------- 4 repères
    ws = wb.create_sheet("4 Repères de calcul")
    _sheet(ws, ["Gamme", "Processeur", "Cœurs", "Threads", "Turbo",
                "Carte graphique intégrée", "Ce que la puce sait faire de mieux"],
           [17, 24, 12, 9, 11, 24, 72])
    r = 2
    for nom, _jeu, key in GAMMES:
        for row in REPERES[key]:
            _body(ws, r, [nom] + row, widths_centre=(3, 4, 5))
            r += 1
    ws.auto_filter.ref = "A1:G%d" % (r - 1)

    # --------------------------------------------------------------- 5 méthode
    ws = wb.create_sheet("5 Méthode")
    _sheet(ws, ["Point", "Règle appliquée"], [26, 120])
    notes = [
        ["Objet", "Spécifier le profil technique des postes fixes à approvisionner, puis le "
                  "confronter au marché : quinze machines, trois constructeurs, deux plateformes."],
        ["Source des prix", "Relevés du 5 novembre 2026 sur Amazon.fr, Fnac, Cdiscount, LDLC et "
                            "Materiel.net, rapprochés des fiches constructeur HP, Dell et Lenovo."],
        ["Valeur des prix", "Illustrative : de quoi arbitrer entre deux voies techniques, pas de quoi "
                            "contractualiser. Un devis constructeur ou grossiste décalera ces montants "
                            "de 15 à 25 % à la baisse sur volume."],
        ["Conversion", "1 € = 655,957 FCFA, parité fixe. Les francs sont exacts, les euros ne le sont pas."],
        ["État", "Chaque ligne porte Neuf ou Reconditionné. Treize lignes sur quinze sont neuves (87 %)."],
        ["n. c.", "Information absente de l'annonce, jamais déduite d'une autre source."],
        ["« — »", "Le produit n'existe pas au catalogue du constructeur — cas de l'AMD chez Dell, "
                  "qui n'a pas d'offre OptiPlex AMD."],
        ["Garantie", "Trois ans sur site chez les constructeurs, absente en reconditionné : garantie "
                     "légale de conformité côté vendeur, au mieux douze mois d'extension en atelier."],
        ["Repères de calcul", "Cœurs, threads, fréquence et classe de graphique : aucune note de "
                              "benchmark n'est affichée, ces machines n'ayant pas été mesurées."],
        ["Réserve d'achat", "Sur Amazon et Fnac, vérifier la mention « vendu et expédié par » : les "
                            "mêmes machines circulent en import, en clavier QWERTZ, avec une garantie "
                            "constructeur parfois inapplicable en France."],
        ["Prix manquants", "M70q Gen 5, M90q Gen 5, M75q Gen 5 en 32 Go / 1 To, et le devis Dell du "
                           "confort. Signalés « à chiffrer », jamais estimés."],
        ["Version", "Version alpha — structure et arbitrage arrêtés, relevés à compléter à la commande."],
    ]
    for i, (k, v) in enumerate(notes, start=2):
        _body(ws, i, [k, v])
        ws.cell(row=i, column=1).font = Font(size=9, name="Calibri", bold=True)
    ws.freeze_panes = "A2"

    wb.properties.title = ("Postes fixes — profil ciblé, catalogue et face-à-face Intel / AMD "
                           "(version alpha)")
    wb.properties.creator = "GED-SERVICES"
    wb.properties.lastModifiedBy = "GED-SERVICES"
    wb.save(path)
    return path


if __name__ == "__main__":
    out = os.path.join(ROOT, OUTDIR)
    os.makedirs(out, exist_ok=True)
    print(build_xlsx(os.path.join(out, BASE + ".xlsx")))
