# -*- coding: utf-8 -*-
"""Benchmark HP — version B : un tableau unique (PDF, Word, Excel) et quatre classes.

Les trois tableaux de la version A (prix et liens / technique / conformité) sont
réunis en un seul, chaque ligne portant sa classe :

    C  Conforme             socle tenu : 16 Go, 512 Go, Windows 11 Pro, plateforme 2023+
    M  Moyennement conforme socle tenu sauf un point, identifié et chiffrable
    I  Incertain            processeur, mémoire ou disque non communiqués
    N  Non conforme         socle manqué sur deux points ou plus, ou point rédhibitoire

La classe est calculée par `classer()` — quatre critères, aucun jugement caché — puis
la réserve est écrite à la main dans `RESERVE`.
"""
from __future__ import annotations

import os
import re

from hp_bench import BASE, LIGNES, OUT, euro, fcfa, freq_pair

BASE_B = BASE + "_version_B"

CLASSES = {
    "C": ("Conforme", "D8EDCB", "1E6B33"),
    "M": ("Moyennement conforme", "FAEBB8", "7A5E12"),
    "I": ("Incertain", "DCE6F2", "2C4E77"),
    "N": ("Non conforme", "F8CDB6", "A23B1A"),
}
ORDRE = ["C", "M", "I", "N"]

REGLE = {
    "C": "16 Go de RAM, 512 Go de disque, Windows 11 Pro, processeur 2023 ou plus récent",
    "M": "un seul de ces quatre points manque, ou une réserve matérielle est identifiée",
    "I": "le processeur, la mémoire ou le disque n'est pas annoncé : impossible de conclure",
    "N": "deux points manquent ou plus, ou un point rédhibitoire (reconditionné, plateforme 2021 ou avant, sans système)",
}


# --------------------------------------------------------------------------- #
def go(x):
    """« 16 Go » -> 16 ; « 1 To + 256 Go » -> 1024 ; « n. c. » -> None."""
    m = re.match(r"(\d+)\s*(Go|To)", str(x))
    if not m:
        return None
    v = int(m.group(1))
    return v * 1024 if m.group(2) == "To" else v


def court_freq(f):
    return str(f).replace(" – ", "–").replace(" GHz", "")


def classer(r):
    ram, disque, an = go(r["ram"]), go(r["disque"]), r["année"]
    if r["cpu"] == "n. c." or ram is None or disque is None:
        return "I"
    if "reconditionn" in r["modèle"].lower():
        return "N"
    if isinstance(an, int) and an <= 2021:
        return "N"
    pts = sum([ram >= 16, disque >= 512, r["os"] == "Windows 11 Pro",
               isinstance(an, int) and an >= 2023])
    if pts >= 4:
        clavier = str(r["périph"]).lower()
        return "M" if ("qwertz" in clavier or "allemand" in clavier) else "C"
    if pts == 3:
        return "M"
    return "N"


# réserve écrite à la main, par modèle (les identifiants M01…M28 bougent au tri)
RESERVE = [
    ("ProOne 440 G9", "4 cœurs seulement ; châssis AiO, ni mémoire ni disque à changer"),
    ("EliteDesk 8 Mini G1a R3", "processeur d'entrée de gamme, suffisant pour la bureautique"),
    ("Elite 800 G9 Mini", "candidat : 32 Go à ajouter, garantie à obtenir du vendeur"),
    ("Pro Mini 400 G9 i7", "i7 surdimensionné pour un poste de bureautique"),
    ("Pro 400 G9 SFF", "clavier allemand (QWERTZ) à remplacer, pas de Wi-Fi annoncé"),
    ("Z4 G4", "reconditionné, plateforme 2017 malgré 32 Go et Windows 11 Pro"),
    ("ProDesk 4 G1i Mini", "système non précisé ; haut de la fourchette de prix"),
]


def reserve_modele(r):
    for cle, txt in RESERVE:
        if cle.lower() in r["modèle"].lower():
            return txt
    return None


def reserve(r, code):
    fixe = reserve_modele(r)
    if fixe:
        return fixe
    if code == "I":
        manque = [n for n, v in (("processeur", r["cpu"]), ("mémoire", r["ram"]),
                                 ("disque", r["disque"])) if v == "n. c."]
        return "Annonce muette sur " + ", ".join(manque)
    if code == "C":
        return "Socle tenu sans réserve identifiée"
    return r["motif"]


def lignes_b():
    out = []
    for r in LIGNES:
        code = classer(r)
        out.append({**r, "code": code, "classe": CLASSES[code][0], "réserve": reserve(r, code)})
    return out


ROWS = lignes_b()
COMPTE = {c: sum(1 for r in ROWS if r["code"] == c) for c in ORDRE}
CAND = next(r for r in ROWS if r["asin"] == "B0D76M6T6R")


# --------------------------------------------------------------------------- #
def ecrire_machines(ws):
    """Remplit une feuille avec les 28 machines (24 colonnes), filtre et mise en page."""
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter

    cols = [
        ("ID", 7, "id"), ("Classe", 22, "classe"), ("Machine", 40, "modèle"),
        ("Format", 9, "format"), ("Processeur", 17, "cpu"), ("Année", 8, "année"),
        ("Cœurs / threads", 12, "cœurs"), ("Fréquence min (GHz)", 11, "fmin"),
        ("Fréquence max (GHz)", 11, "fmax"), ("RAM", 8, "ram"), ("Disque", 20, "disque"),
        ("Écran", 16, "écran"), ("Système", 20, "os"), ("Type de mémoire", 14, "ram_type"),
        ("Type de disque", 13, "disque_type"), ("Réseau", 18, "réseau"),
        ("Tarif € TTC", 12, "prix"), ("Frais de port €", 12, "port"),
        ("Total livré €", 12, "livré"), ("Total livré FCFA", 16, "livré_fcfa"),
        ("Garantie annoncée", 18, "garantie"), ("Licence", 10, "licence"),
        ("Réserve", 52, "réserve"), ("Lien Amazon", 42, "lien"),
    ]

    head_fill = PatternFill("solid", fgColor="1F3B63")
    head_font = Font(color="FFFFFF", bold=True, size=9, name="Calibri")
    thin = Side(style="thin", color="D0D7E2")

    for c, (label, width, _k) in enumerate(cols, 1):
        cell = ws.cell(row=1, column=c, value=label)
        cell.fill = head_fill
        cell.font = head_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = Border(bottom=thin)
        ws.column_dimensions[get_column_letter(c)].width = width
    ws.row_dimensions[1].height = 34

    band_fill = {c: PatternFill("solid", fgColor=CLASSES[c][1]) for c in ORDRE}

    def fl(x):
        try:
            return float(str(x).replace(",", "."))
        except ValueError:
            return x

    for i, r in enumerate(ROWS, start=2):
        fmin, fmax = freq_pair(r["fréquence"])
        values = {"fmin": fl(fmin), "fmax": fl(fmax), "ram": go(r["ram"]) or r["ram"]}
        for c, (_label, _w, key) in enumerate(cols, 1):
            val = r[key] if key not in values else values[key]
            cell = ws.cell(row=i, column=c, value=val)
            cell.font = Font(size=9, name="Calibri")
            cell.border = Border(bottom=thin)
            if key in ("prix", "port", "livré"):
                cell.number_format = '# ##0.00 "€"'
                cell.alignment = Alignment(horizontal="right")
            elif key == "livré_fcfa":
                cell.number_format = '# ##0 "FCFA"'
                cell.alignment = Alignment(horizontal="right")
            elif key in ("fmin", "fmax") and isinstance(val, float):
                cell.number_format = '0.0 "GHz"'
                cell.alignment = Alignment(horizontal="center")
            elif key == "ram" and isinstance(val, float):
                cell.number_format = '# ##0 "Go"'
                cell.alignment = Alignment(horizontal="center")
            elif key == "lien":
                cell.hyperlink = val
                cell.font = Font(size=9, name="Calibri", color="1155CC", underline="single")
            elif key in ("réserve", "modèle", "disque", "écran"):
                cell.alignment = Alignment(wrap_text=True, vertical="top")
            if cell.fill.fill_type is None:
                cell.fill = band_fill[r["code"]]
            if key == "classe":
                cell.font = Font(size=9, bold=True, name="Calibri", color=CLASSES[r["code"]][2])
            if key == "id":
                cell.font = Font(size=9, bold=True, name="Calibri")

    ref = f"A1:{get_column_letter(len(cols))}{len(ROWS) + 1}"
    ws.auto_filter.ref = ref
    ws.freeze_panes = "D2"
    ws.print_title_rows = "1:1"
    ws.print_options.horizontalCentered = True
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A3
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.sheet_view.zoomScale = 90
    ws.sheet_properties.tabColor = "1F3B63"


def build_xlsx(path):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font

    wb = Workbook()
    ws = wb.active
    ws.title = "Benchmark HP"
    ecrire_machines(ws)

    # ---- feuille Méthode
    wb.properties.creator = "GED-SERVICES"
    wb.properties.title = "Benchmark — postes fixes HP, 750 à 1 250 € (version B, tableau unique)"
    wb.properties.subject = "28 machines fixes HP relevées sur Amazon.fr le 5 novembre 2026"

    ws2 = wb.create_sheet("Méthode")
    ws2.column_dimensions["A"].width = 16
    ws2.column_dimensions["B"].width = 110
    notes = [("Filtrer", "Filtre automatique sur les 24 colonnes (flèche dans chaque en-tête) : "
                         "il fonctionne à l'identique dans Excel, LibreOffice Calc et Google Sheets. "
                         "Les colonnes ID, Classe et Machine restent visibles (volets figés).")]
    notes += [(f"Classe {c} — {CLASSES[c][0]} ({COMPTE[c]})", REGLE[c]) for c in ORDRE]
    notes += [
        ("Règle", "La classe ne juge que quatre points : 16 Go de RAM, 512 Go de disque, "
                  "Windows 11 Pro, processeur 2023 ou plus récent. Aucune note, aucun avis : "
                  "un point manquant donne « moyennement conforme », deux points ou un point "
                  "rédhibitoire donnent « non conforme »."),
        ("Source", "Page de résultats Amazon.fr fournie (« ordinateur de bureau », marque HP, "
                   "état Neuf, 750 à 1 250 €), relevée le 5 novembre 2026."),
        ("Prix", "TTC, hors frais de port ; le port annoncé est ajouté dans « Total livré ». "
                 "Les montants bougent chaque semaine. 1 € = 655,957 FCFA, parité fixe."),
        ("n. c.", "Information non communiquée dans l'annonce : jamais déduite, jamais estimée."),
        ("Année", "Année de lancement du processeur, non celle du châssis."),
        ("Liens", "URL directes /dp/. Trois fiches rouvertes le 5 novembre 2026 (M03, M21, M22 "
                  "de la version A) : même produit, même prix."),
    ]
    for r, (k, v) in enumerate(notes, start=1):
        a = ws2.cell(row=r, column=1, value=k)
        a.font = Font(bold=True, size=9)
        b = ws2.cell(row=r, column=2, value=v)
        b.font = Font(size=9)
        b.alignment = Alignment(wrap_text=True, vertical="top")

    wb.save(path)
    return path


def tableau_lignes(doc, prefix="Tableau"):
    """Légende des quatre classes + le tableau unique des 28 machines (A3 paysage)."""
    legend = []
    for c in ORDRE:
        legend.append(f"**{CLASSES[c][0]} · {COMPTE[c]}** — {REGLE[c]}")
    cell_fmt = {(0, j): {"bg": CLASSES[c][1], "color": CLASSES[c][2], "b": False}
                for j, c in enumerate(ORDRE)}
    doc.table([], [legend], [1, 1, 1, 1], font=7.4, header=False, zebra=False,
              cell_fmt=cell_fmt)

    headers = ["ID", "Machine", "Format", "Processeur", "Année", "Cœurs", "Fréq. GHz", "RAM",
               "Disque", "Écran", "Système", "Réseau", "Tarif €", "Total livré €", "FCFA",
               "Classe", "Réserve / motif", "Lien"]
    widths = [4.2, 12.8, 4.0, 8.8, 4.0, 4.6, 5.0, 4.6, 7.4, 6.2, 7.0, 5.0,
              5.6, 6.0, 6.4, 7.6, 13.4, 4.2]
    aligns = ["c", "l", "c", "l", "c", "c", "c", "c", "l", "l", "l", "l",
              "r", "r", "r", "l", "l", "c"]

    body, row_bg, cfmt = [], {}, {}
    for i, r in enumerate(ROWS):
        body.append([
            r["id"], r["modèle"], r["format"], r["cpu"], r["année"] or "n. c.", r["cœurs"],
            court_freq(r["fréquence"]), r["ram"], r["disque"],
            "—" if r["écran"] == "non inclus" else r["écran"],
            r["os"], r["réseau"],
            euro(r["prix"]), euro(r["livré"]), fcfa(r["livré"]),
            r["classe"], r["réserve"], "[ouvrir](%s)" % r["lien"],
        ])
        row_bg[i] = CLASSES[r["code"]][1]
        cfmt[(i, 15)] = {"color": CLASSES[r["code"]][2], "b": True}
        cfmt[(i, 0)] = {"b": True}
        if r["asin"] == CAND["asin"]:
            cfmt[(i, 1)] = {"b": True, "color": "1F3B63"}

    doc.table(headers, body, widths, font=6.9, header=True, zebra=False, aligns=aligns,
              row_bg=row_bg, cell_fmt=cfmt,
              caption=prefix + " — 28 machines fixes HP, classées par total livré croissant. "
                      "Prix TTC du 5 novembre 2026, frais de port compris dans le total livré ; "
                      "1 € = 655,957 FCFA. La couleur de la ligne donne la classe, la colonne "
                      "« Réserve » dit pourquoi. n. c. = non communiqué.")


def tableau_classes(doc, prefix="Tableau"):
    """Récapitulatif : une ligne par classe, avec la suite à donner."""
    recap = []
    actions = {
        "C": "retenir ; prévoir les 32 Go",
        "M": "corriger le point manquant (licence Pro, 512 Go, clavier, système à confirmer)",
        "I": "demander la fiche au vendeur avant de classer",
        "N": "écarter",
    }
    for c in ORDRE:
        membres = ", ".join(r["id"] for r in ROWS if r["code"] == c)
        recap.append([CLASSES[c][0], str(COMPTE[c]), membres, actions[c]])
    doc.table(["Classe", "Nb machines", "Machines", "Suite à donner"], recap,
              [3.6, 1.8, 6.0, 5.7], font=8.2, header=True, zebra=False, first_col_bold=True,
              row_bg={i: CLASSES[c][1] for i, c in enumerate(ORDRE)},
              aligns=["l", "c", "l", "l"],
              caption=prefix + " — Quatre classes, un seul critère de lecture : le nombre de points du socle "
                      "tenus (16 Go, 512 Go, Windows 11 Pro, processeur 2023 ou plus récent).")


# --------------------------------------------------------------------------- #
def build_doc():
    from render import Doc

    doc = Doc(
        base=BASE_B,
        title="Benchmark — postes fixes HP (tableau unique)",
        subtitle="Vingt-huit machines fixes HP neuves, 750 à 1 250 €, classées en quatre catégories",
        meta=[],
        doc_ref="GED-BENCH-2026-11-B · Confidentiel — usage interne",
        footer="GED-SERVICES · benchmark postes fixes HP",
    )

    doc.cover(
        eyebrow="Benchmark — postes fixes · version B",
        title="Postes fixes HP\n750 à 1 250 €",
        subtitle="Un tableau unique : prix, caractéristiques, lien et conformité sur la même ligne, "
                 "chaque machine rangée dans une des quatre classes.",
        meta_rows=[
            ["Destinataire", "**M. Jad, directeur général — ADCHIM**"],
            ["Émetteur", "**Joël MBA OYONE — GED-SERVICES**"],
            ["Source", "Page de résultats Amazon.fr fournie (« ordinateur de bureau », marque HP, "
                       "état Neuf, 750 à 1 250 €), relevée le **5 novembre 2026**"],
            ["Périmètre", "28 machines fixes avec prix affiché ; annonces sans prix, portables, "
                          "clients légers et matériel réseau écartés"],
            ["Tableau", "Une seule table de **28 lignes et 18 colonnes**, classée par total livré "
                        "croissant ; les trois tableaux de la version A y sont réunis"],
            ["Classes", "**%d conformes · %d moyennement conformes · %d incertaines · %d non conformes**"
                        % (COMPTE["C"], COMPTE["M"], COMPTE["I"], COMPTE["N"])],
            ["Prix", "TTC, frais de port inclus dans le « total livré » ; 1 € = 655,957 FCFA, "
                     "parité fixe"],
            ["Lecture", "**n. c.** = non communiqué, jamais déduit. Année = lancement du processeur, "
                        "non du châssis. Le candidat **HP Elite 800 G9 Mini (M21)** est en gras "
                        "dans la colonne Machine"],
            ["Livrables", "Word (.docx) et PDF identiques, plus le classeur `.xlsx` filtrable"],
        ],
        pagebreak=False,
    )

    doc.landscape3(True)
    tableau_lignes(doc)

    # --- retour au portrait, conclusion courte
    doc.landscape3(False)

    doc.h1_plain("Les quatre classes, et ce qu'il faut en faire")
    tableau_classes(doc)

    doc.h1_plain("Ce que le tableau dit")
    doc.p("**Quatre machines tiennent le socle** : %s. Aucune n'est livrée en 32 Go ; "
          "l'extension reste à prévoir partout, entre 335,95 € la barrette et 593,95 € le kit. "
          % ", ".join("%s %s" % (r["id"], r["modèle"]) for r in ROWS if r["code"] == "C"),
          small=True)
    doc.p("**Neuf machines ne manquent que d'un point** — le plus souvent la licence Pro "
          "(Windows 11 Famille) ou les 512 Go de disque : ce sont les seules à pouvoir rejoindre "
          "la classe « conforme » sans changer de modèle.", small=True)
    doc.p("**Dix annonces ne permettent pas de conclure** : processeur, mémoire ou disque non "
          "communiqués. Ce n'est pas un défaut de la machine mais de la fiche : une question au "
          "vendeur suffit à les classer.", small=True)
    doc.p("**Cinq sont hors cible** : 8 Go de RAM, plateforme 2017-2018, Windows 10 ou "
          "reconditionné. Le candidat reste le **HP Elite 800 G9 Mini** (%s, %s, %s livré, "
          "%s), seul poste conforme dont la note d'arbitrage a déjà établi le coût complet."
          % (CAND["id"], CAND["cpu"], euro(CAND["livré"]), fcfa(CAND["livré"])), small=True)

    doc.h1_plain("Méthode et réserves")
    doc.ul([
        "**Source** : page de résultats Amazon.fr fournie, « ordinateur de bureau », marque HP, "
        "état Neuf, 750 à 1 250 €, relevée le 5 novembre 2026 — 43 résultats, dont 28 machines "
        "fixes avec prix affiché.",
        "**Prix** : TTC affichés par le vendeur, port annoncé ajouté dans le « total livré ». "
        "1 € = 655,957 FCFA, parité fixe : les montants en francs sont exacts, les prix ne le "
        "sont pas — ils changent chaque semaine.",
        "**n. c.** : information absente de l'annonce ; elle n'a été ni déduite ni complétée pour "
        "un autre distributeur. Aucun montant estimé.",
        "**Année** : lancement du processeur, non du châssis — une machine neuve peut porter une "
        "plateforme de deux ans.",
        "**Liens** : URL canoniques `amazon.fr/dp/ASIN` ; trois fiches rouvertes le 5 novembre 2026 "
        "répondent avec le même produit et le même prix.",
        "**Classes** : calculées par la règle des quatre points, sans pondération ni note "
        "d'appréciation. Un point manquant suffit à sortir de « conforme ».",
    ], small=True)

    dpath, ppath = doc.save(OUT)

    # métadonnées Word : sans cela l'auteur reste « python-docx »
    import docx as _docx

    d = _docx.Document(dpath)
    cp = d.core_properties
    cp.author = "GED-SERVICES"
    cp.last_modified_by = "GED-SERVICES"
    cp.comments = ""
    cp.keywords = ""
    cp.category = ""
    cp.title = "Benchmark — postes fixes HP, tableau unique (version B)"
    cp.subject = "28 machines fixes HP, 750 à 1 250 €, classées en quatre catégories"
    cp.comments = ""
    d.save(dpath)
    return dpath, ppath


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print("xlsx :", build_xlsx(os.path.join(OUT, BASE_B + ".xlsx")))
    print("docx+pdf :", build_doc())
    print("classes :", COMPTE)
