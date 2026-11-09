# -*- coding: utf-8 -*-
"""Benchmark HP — version C : quatre tableaux, de la cible au classement.

    1. La cible : profil technique exigé, millésime compris
    2. La cible choisie : HP Elite 800 G9 Mini, critère par critère
    3. Les 28 machines fixes relevées, classées en quatre catégories
    4. Les quatre classes, et ce qu'il faut en faire

Les tableaux 3 et 4 sont ceux de la version B, repris tels quels (`hp_bench_b`).
"""
from __future__ import annotations

import os

from hp_bench import BASE, OUT, euro, fcfa
from hp_bench_b import (CAND, CLASSES, COMPTE, ORDRE, ROWS, ecrire_machines,
                        tableau_classes, tableau_lignes)

BASE_C = BASE + "_version_C"

# --------------------------------------------------------------------------- #
# Tableau 1 — la cible
CIBLE_HEADERS = ["Exigence", "Entrée de gamme", "Standard entreprise (référence d'achat)",
                 "Confort longue durée"]
CIBLE = [
    ["Usage visé",
     "Accueil, saisie, consultation, poste nomade occasionnel",
     "Bureautique intensive, Sage, Teams, plusieurs applications ouvertes",
     "Utilisateurs exigeants, postes gardés cinq ans, CAO et gros tableurs"],
    ["Processeur",
     "Core i5 13ᵉ génération minimum",
     "Core i5 14ᵉ génération ou Core Ultra 5",
     "Core i5/i7 14ᵉ génération ou Core Ultra 5/7 série 2"],
    ["**Année de sortie exigée**",
     "**2023** ou plus récent",
     "**2024** ou plus récent",
     "**2024-2025**"],
    ["Cœurs / threads",
     "6 / 12 minimum",
     "10 / 16 minimum",
     "14 / 20 recommandé"],
    ["Mémoire",
     "16 Go DDR5, deux emplacements",
     "**32 Go** DDR5, deux emplacements, 64 Go maximum",
     "**32 Go** DDR5 extensible à 64 Go"],
    ["Stockage",
     "SSD NVMe 512 Go",
     "SSD NVMe 512 Go à 1 To",
     "SSD NVMe 1 To, emplacement libre"],
    ["Système",
     "Windows 11 Pro, licence comprise",
     "Windows 11 Pro, licence comprise",
     "Windows 11 Pro, licence comprise"],
    ["Réseau",
     "1 GbE et Wi-Fi 6",
     "1 GbE et Wi-Fi 6/6E",
     "1 GbE et Wi-Fi 6E"],
    ["Garantie",
     "3 ans sur site, pièces et main-d'œuvre",
     "3 ans sur site, pièces et main-d'œuvre",
     "3 ans sur site, pièces et main-d'œuvre"],
    ["Format",
     "Tour, SFF ou mini",
     "Tour, SFF ou mini, châssis encore fabriqué",
     "Tour, SFF ou mini, châssis encore suivi"],
]

# --------------------------------------------------------------------------- #
# Tableau 2 — la cible choisie
G, Y, O = "g", "y", "o"
FMT = {
    "g": {"bg": "D8EDCB", "color": "1E6B33", "b": True},
    "y": {"bg": "FAEBB8", "color": "7A5E12", "b": True},
    "o": {"bg": "F8CDB6", "color": "A23B1A", "b": True},
}

CANDIDAT = [
    ("Millésime du processeur", "14ᵉ génération ou Core Ultra",
     "i5-14500 — 14ᵉ génération, lancée en janvier 2024", "Conforme", G),
    ("Millésime du châssis", "Plateforme récente, encore fabriquée",
     "Elite 800 G9 — châssis de 2022, toujours au catalogue", "Tolérable, à connaître", Y),
    ("Gamme", "Professionnelle", "HP Elite 800 — gamme entreprise", "Très bien", G),
    ("Format", "Tour, SFF ou Mini", "Mini PC, 1 litre", "Conforme", G),
    ("Processeur", "Core i5 13ᵉ/14ᵉ ou Core Ultra 5", "Core i5-14500", "Très bien", G),
    ("Nombre de cœurs", "6 minimum, 8 recommandés ou plus",
     "14 cœurs (6 performance + 8 efficaces)", "Excellent", G),
    ("Nombre de threads", "12 minimum", "20 threads", "Excellent", G),
    ("Fréquence de base", "≈ 2,5 GHz minimum", "2,6 GHz sur les cœurs performance", "Conforme", G),
    ("Fréquence Turbo", "4,0 GHz minimum, 4,5 recommandé", "Jusqu'à 5,0 GHz", "Excellent", G),
    ("Enveloppe thermique", "Adaptée au châssis",
     "65 W de base, 154 W en pointe, dans 1 litre", "Point de vigilance", Y),
    ("Mémoire vive", "16 Go minimum, 32 Go recommandé", "16 Go", "Sous la cible", Y),
    ("Type de mémoire", "DDR5 préférable",
     "DDR5 SO-DIMM, 2 emplacements, 64 Go maximum", "Conforme", G),
    ("Stockage", "SSD NVMe 512 Go minimum, 1 To idéal", "SSD NVMe 512 Go",
     "Minimum atteint", Y),
    ("Carte graphique", "Intégrée acceptable", "Intel UHD Graphics 770", "Conforme", G),
    ("Ethernet", "Gigabit minimum", "1 GbE", "Conforme", G),
    ("Wi-Fi / Bluetooth", "Wi-Fi 6 minimum", "Wi-Fi 6E et Bluetooth 5.3", "Très bien", G),
    ("Système", "Windows 11 Professionnel", "Windows 11 Pro", "Conforme", G),
    ("Sécurité", "TPM 2.0, Secure Boot, idéalement vPro",
     "TPM 2.0 de série ; activation et vPro à confirmer", "À vérifier", Y),
    ("Écran", "Idéalement inclus dans le pack",
     "Non inclus — 84,95 € pour un 24\" Full HD", "Coût à ajouter", Y),
    ("Clavier / souris", "Souhaités", "Annoncés dans le carton", "Inclus", G),
    ("Garantie", "3 ans sur site exigés", "Non précisée dans l'annonce",
     "À obtenir avant achat", O),
]
NB_G = sum(1 for r in CANDIDAT if r[4] == G)
NB_Y = sum(1 for r in CANDIDAT if r[4] == Y)
NB_O = sum(1 for r in CANDIDAT if r[4] == O)


# --------------------------------------------------------------------------- #
def build_doc():
    from render import Doc

    doc = Doc(
        base=BASE_C,
        title="Benchmark — postes fixes HP (quatre tableaux)",
        subtitle="La cible, la cible choisie, les 28 machines du marché, le classement",
        meta=[],
        doc_ref="GED-BENCH-2026-11-C · Confidentiel — usage interne",
        footer="GED-SERVICES · benchmark postes fixes HP",
    )

    doc.cover(
        eyebrow="Benchmark — postes fixes · version C",
        title="Postes fixes HP\n750 à 1 250 €",
        subtitle="Quatre tableaux dans l'ordre de la décision : ce qu'il faut, ce que l'on retient, "
                 "ce que le marché propose, ce qu'il en reste.",
        meta_rows=[
            ["Destinataire", "**M. Jad, directeur général — ADCHIM**"],
            ["Émetteur", "**Joël MBA OYONE — GED-SERVICES**"],
            ["Source", "Page de résultats Amazon.fr fournie (« ordinateur de bureau », marque HP, "
                       "état Neuf, 750 à 1 250 €), relevée le **5 novembre 2026**"],
            ["Tableau 1", "**La cible** : profil technique exigé, par profil d'usage, "
                          "**année de sortie comprise**"],
            ["Tableau 2", "**La cible choisie** : HP Elite 800 G9 Mini confronté aux 21 points "
                          "du cahier des charges"],
            ["Tableau 3", "**Le marché** : 28 machines fixes, prix, caractéristiques, lien et "
                          "classe sur la même ligne"],
            ["Tableau 4", "**Le classement** : %d conformes · %d moyennement conformes · "
                          "%d incertaines · %d non conformes"
                          % (COMPTE["C"], COMPTE["M"], COMPTE["I"], COMPTE["N"])],
            ["Prix", "TTC, frais de port compris dans le « total livré » ; 1 € = 655,957 FCFA, "
                     "parité fixe"],
            ["Lecture", "**n. c.** = non communiqué, jamais déduit. Année = lancement du "
                        "processeur, non du châssis"],
            ["Livrables", "Word (.docx) et PDF identiques, plus le classeur `.xlsx` à quatre "
                          "feuilles filtrables"],
        ],
        pagebreak=False,
    )
    doc.pagebreak()

    # ---------------------------------------------------------------- tableau 1
    doc.h1_plain("Tableau 1 — La cible : profil technique et millésime")
    doc.p("La cible se définit par l'usage, pas par un budget. Trois profils suffisent à couvrir "
          "les postes d'ADCHIM ; le profil **standard entreprise** est celui qui sert de référence "
          "d'achat dans tout le dossier. La règle de millésime porte sur le processeur : "
          "**2023 ou plus récent**, jamais en dessous.", small=True)
    doc.table(CIBLE_HEADERS, CIBLE, [3.3, 4.2, 5.0, 4.6], font=8.0,
              aligns=["l", "l", "l", "l"], first_col_bold=True,
              cell_fmt={(i, 0): {"bg": "EDF1F7"} for i in range(len(CIBLE))},
              caption="Tableau 1 — Le seuil technique par profil d'usage. « Année de sortie "
                      "exigée » s'entend : année de lancement du processeur, non du châssis.")

    doc.p("**Quatre points éliminent une offre d'emblée**, sans discussion possible :", small=True)
    doc.ul([
        "**moins de 16 Go de mémoire** — un poste soudé à 8 Go ne s'étend pas : il sort du socle "
        "dès l'achat ;",
        "**plateforme 2021 ou antérieure** — suivi constructeur en fin de vie, pièces détachées "
        "incertaines ;",
        "**sans système, ou Windows Famille** — licence Pro à ajouter, 150 à 200 € selon le canal ;",
        "**reconditionné** — garantie constructeur non transférable, historique de la machine "
        "inconnu.",
    ], small=True)

    # ---------------------------------------------------------------- tableau 2
    doc.pagebreak()
    doc.h1_plain("Tableau 2 — La cible choisie : HP Elite 800 G9 Mini, i5-14500")
    doc.p("Le poste retenu : **HP Elite 800 G9 Mini** — Core i5-14500, 16 Go DDR5, SSD NVMe "
          "512 Go, Windows 11 Pro, format mini 1 litre. Prix relevé le 5 novembre 2026 : "
          "**%s livré, soit %s**. [Fiche Amazon.fr](%s)."
          % (euro(CAND["livré"]), fcfa(CAND["livré"]), CAND["lien"]), small=True)
    doc.p("Les 21 points du cahier des charges, confrontés à l'annonce : **%d conformes ou "
          "meilleurs, %d à surveiller ou au plancher, %d bloquant** tant qu'il n'est pas levé."
          % (NB_G, NB_Y, NB_O), small=True)
    rows = [[c, cible, constate, ev] for c, cible, constate, ev, _ in CANDIDAT]
    cf = {(i, 3): FMT[CANDIDAT[i][4]] for i in range(len(CANDIDAT))}
    doc.table(["Critère", "Cahier des charges", "Constaté sur l'annonce", "Évaluation"],
              rows, [3.6, 4.4, 5.6, 3.5], font=7.6, aligns=["l", "l", "l", "c"], cell_fmt=cf,
              caption="Tableau 2 — Le candidat contre la cible. Le vert est tenu ou dépassé, "
                      "le jaune atteint le plancher ou reste à confirmer, l'orange manque.")
    doc.p("**Deux points à retenir.** Le millésime : la puce est de janvier 2024, le châssis "
          "Elite 800 G9 de 2022 — configuration récente dans un boîtier de quatre ans, toujours "
          "suivi par HP. La garantie : l'annonce ne la mentionne pas ; c'est le seul point qui "
          "puisse, à lui seul, écarter l'offre. La mémoire est à 16 Go quand la cible standard "
          "en demande 32 : l'extension est chiffrée à 335,95 € la barrette, 593,95 € le kit.",
          small=True)

    # ---------------------------------------------------------------- tableau 3
    doc.landscape3(True)
    doc.h1_plain("Tableau 3 — Les 28 machines fixes HP de 750 à 1 250 €, classées en quatre catégories")
    tableau_lignes(doc, prefix="Tableau 3")

    # ---------------------------------------------------------------- tableau 4
    doc.landscape3(False)
    doc.h1_plain("Tableau 4 — Les quatre classes, et ce qu'il faut en faire")
    tableau_classes(doc, prefix="Tableau 4")
    doc.p("**Le candidat est dans les quatre conformes** (%s, %s, %s livré, %s) : c'est le seul "
          "dont le coût complet et le passage à 32 Go sont déjà chiffrés. Les neuf « moyennement "
          "conformes » ne manquent que d'un point — licence Pro, 512 Go, clavier ou système à "
          "confirmer — et pourraient rejoindre la première classe sans changer de modèle. Les dix "
          "« incertaines » ne sont pas des machines incomplètes mais des annonces muettes : une "
          "question au vendeur suffit à les classer."
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

    import docx as _docx

    d = _docx.Document(dpath)
    cp = d.core_properties
    cp.author = "GED-SERVICES"
    cp.last_modified_by = "GED-SERVICES"
    cp.comments = ""
    cp.keywords = ""
    cp.category = ""
    cp.title = "Benchmark — postes fixes HP, quatre tableaux (version C)"
    cp.subject = "Cible, cible choisie, 28 machines du marché, classement en quatre catégories"
    d.save(dpath)
    return dpath, ppath


# --------------------------------------------------------------------------- #
def build_xlsx(path):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter

    wb = Workbook()
    head_fill = PatternFill("solid", fgColor="1F3B63")
    head_font = Font(color="FFFFFF", bold=True, size=9, name="Calibri")
    thin = Side(style="thin", color="D0D7E2")

    def entetes(ws, headers, widths):
        for c, (h, w) in enumerate(zip(headers, widths), 1):
            cell = ws.cell(row=1, column=c, value=h)
            cell.fill = head_fill
            cell.font = head_font
            cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            cell.border = Border(bottom=thin)
            ws.column_dimensions[get_column_letter(c)].width = w
        ws.row_dimensions[1].height = 32

    # ---- feuille 1 : la cible
    ws = wb.active
    ws.title = "1 Cible"
    entetes(ws, CIBLE_HEADERS, [26, 38, 42, 42])
    for i, row in enumerate(CIBLE, start=2):
        for c, v in enumerate(row, 1):
            cell = ws.cell(row=i, column=c, value=v.replace("**", ""))
            cell.font = Font(size=9, bold=(c == 1), name="Calibri")
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = Border(bottom=thin)
            if i == 4:  # ligne « Année de sortie exigée »
                cell.fill = PatternFill("solid", fgColor="E6EDF5")
    ws.freeze_panes = "B2"
    ws.sheet_properties.tabColor = "1F3B63"

    # ---- feuille 2 : la cible choisie
    ws2 = wb.create_sheet("2 Candidat HP")
    entetes(ws2, ["Critère", "Cahier des charges", "Constaté sur l'annonce", "Évaluation"],
            [26, 40, 52, 22])
    for i, (crit, cible, constate, ev, code) in enumerate(CANDIDAT, start=2):
        for c, v in enumerate((crit, cible, constate, ev), 1):
            cell = ws2.cell(row=i, column=c, value=v)
            cell.font = Font(size=9, bold=(c == 4), name="Calibri")
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = Border(bottom=thin)
            if c == 4:
                cell.fill = PatternFill("solid", fgColor=FMT[code]["bg"])
                cell.font = Font(size=9, bold=True, name="Calibri",
                                 color=FMT[code]["color"])
            elif i % 2 == 0:
                cell.fill = PatternFill("solid", fgColor="F5F7FA")
    ws2.auto_filter.ref = f"A1:D{len(CANDIDAT) + 1}"
    ws2.freeze_panes = "B2"
    ws2.sheet_properties.tabColor = "1E6B33"

    # ---- feuille 3 : les 28 machines
    ws3 = wb.create_sheet("3 Les 28 machines")
    ecrire_machines(ws3)

    # ---- feuille 4 : les quatre classes
    ws4 = wb.create_sheet("4 Classes")
    entetes(ws4, ["Classe", "Nb machines", "Machines", "Suite à donner"],
            [24, 12, 52, 56])
    actions = {"C": "retenir ; prévoir les 32 Go",
               "M": "corriger le point manquant (licence Pro, 512 Go, clavier, système à confirmer)",
               "I": "demander la fiche au vendeur avant de classer",
               "N": "écarter"}
    for i, c in enumerate(ORDRE, start=2):
        membres = ", ".join(r["id"] for r in ROWS if r["code"] == c)
        vals = (CLASSES[c][0], COMPTE[c], membres, actions[c])
        for j, v in enumerate(vals, 1):
            cell = ws4.cell(row=i, column=j, value=v)
            cell.font = Font(size=9, bold=(j == 1), name="Calibri")
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = Border(bottom=thin)
            cell.fill = PatternFill("solid", fgColor=CLASSES[c][1])
            if j == 1:
                cell.font = Font(size=9, bold=True, name="Calibri",
                                 color=CLASSES[c][2])
    ws4.freeze_panes = "A2"
    ws4.sheet_properties.tabColor = "A23B1A"

    # ---- feuille 5 : méthode
    ws5 = wb.create_sheet("Méthode")
    ws5.column_dimensions["A"].width = 18
    ws5.column_dimensions["B"].width = 110
    notes = [
        ("Quatre tableaux", "1 la cible technique, 2 la cible choisie confrontée aux 21 points du "
                            "cahier des charges, 3 les 28 machines du marché, 4 le classement en "
                            "quatre catégories."),
        ("Filtrer", "Chaque feuille porte un filtre automatique sur ses colonnes (flèche dans "
                    "l'en-tête) : il fonctionne à l'identique dans Excel, LibreOffice Calc et "
                    "Google Sheets."),
    ] + [(f"Classe {c} — {CLASSES[c][0]} ({COMPTE[c]})", r) for c, r in
         zip(ORDRE, ["16 Go, 512 Go, Windows 11 Pro, processeur 2023 ou plus récent",
                     "un seul de ces quatre points manque, ou une réserve matérielle est identifiée",
                     "processeur, mémoire ou disque non communiqué : impossible de conclure",
                     "deux points manquent ou plus, ou un point rédhibitoire (reconditionné, "
                     "plateforme 2021 ou avant, sans système)"])] + [
        ("Candidat", "HP Elite 800 G9 Mini — i5-14500, 16 Go, 512 Go, Windows 11 Pro : "
                     f"{euro(CAND['livré'])} livré, soit {fcfa(CAND['livré'])}."),
        ("Source", "Page de résultats Amazon.fr fournie, relevée le 5 novembre 2026. Prix TTC, "
                   "port compris dans le total livré ; 1 € = 655,957 FCFA, parité fixe."),
        ("n. c.", "Information non communiquée dans l'annonce : jamais déduite, jamais estimée."),
        ("Année", "Lancement du processeur, non du châssis."),
    ]
    for r, (k, v) in enumerate(notes, start=1):
        a = ws5.cell(row=r, column=1, value=k)
        a.font = Font(bold=True, size=9)
        b = ws5.cell(row=r, column=2, value=v)
        b.font = Font(size=9)
        b.alignment = Alignment(wrap_text=True, vertical="top")

    wb.properties.creator = "GED-SERVICES"
    wb.properties.title = "Benchmark — postes fixes HP, quatre tableaux (version C)"
    wb.properties.subject = "Cible, candidat, 28 machines, classement"
    wb.save(path)
    return path


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print("xlsx :", build_xlsx(os.path.join(OUT, BASE_C + ".xlsx")))
    print("docx+pdf :", build_doc())
    print("classes :", COMPTE, "| candidat :", NB_G, NB_Y, NB_O)
