# -*- coding: utf-8 -*-
"""Benchmark Dell — quatre tableaux, de la cible au classement.

Même architecture que le dossier HP (version C) :

    1. La cible : profil technique exigé, millésime compris
    2. La cible choisie : Dell Slim DS1265, critère par critère
    3. Les machines fixes Dell de la page, puis les annonces écartées
    4. Les quatre classes, et ce qu'il faut en faire

La règle de classement est celle du dossier HP, importée telle quelle : 16 Go,
512 Go, Windows 11 Pro, processeur 2023 ou plus récent.
"""
from __future__ import annotations

import os

from dell_data import ECARTEES, MACHINES
from hp_bench import euro, fcfa
from hp_bench_b import CLASSES, ORDRE, REGLE, classer, court_freq
from hp_bench_c import CIBLE, CIBLE_HEADERS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "livrables", "DELL")
BASE = "Benchmark_postes_fixes_DELL_750_1250_euros"

# Classe forcée quand la règle des quatre points conclurait « incertaine » alors
# que la plateforme, elle, est connue et disqualifiante.
FIXE = {
    "OptiPlex 3060": "N",
}

# Réserve courte, par modèle (les identifiants bougent au tri).
RESERVE = {
    "7010 Micro": "seule machine à réunir les quatre points, mais reconditionnée : "
                  "garantie du vendeur seulement",
    "3080 SFF": "8 Go et 256 Go seulement, plateforme 2020, système non précisé",
    "7070 Micro": "reconditionné, processeur 2019 (turbo 5,0 GHz) ; écran 27\" compris dans le prix",
    "3060 MFF": "plateforme 2018 (jeu H370) ; ni mémoire, ni disque, ni système annoncés",
    "EC24250": "mémoire et disque non annoncés ; Windows 11 Famille",
    "DS1265": "candidat : Windows 11 Famille, garantie à obtenir, processeur à confirmer",
}


def _reserve(r):
    for cle, txt in RESERVE.items():
        if cle.lower() in r["modèle"].lower():
            return txt
    return r["motif"]


def lignes():
    out = []
    for r in sorted(MACHINES, key=lambda x: x["livré"]):
        code = next((c for k, c in FIXE.items() if k.lower() in r["modèle"].lower()), None)
        code = code or classer(r)
        out.append({**r, "code": code, "classe": CLASSES[code][0], "réserve": _reserve(r)})
    for i, r in enumerate(out, 1):
        r["id"] = "D%02d" % i
    return out


ROWS = lignes()
COMPTE = {c: sum(1 for r in ROWS if r["code"] == c) for c in ORDRE}
CAND = next(r for r in ROWS if r["asin"] == "B0H9LKCN2T")

# --------------------------------------------------------------------------- #
# Tableau 2 — la cible choisie (Dell Slim DS1265)
G, Y, O = "g", "y", "o"
FMT = {
    "g": {"bg": "D8EDCB", "color": "1E6B33", "b": True},
    "y": {"bg": "FAEBB8", "color": "7A5E12", "b": True},
    "o": {"bg": "F8CDB6", "color": "A23B1A", "b": True},
}

CANDIDAT = [
    ("Millésime du processeur", "14ᵉ génération ou Core Ultra",
     "« Ryzen 5 150 » annoncé ; millésime non communiqué", "À confirmer", Y),
    ("Millésime du châssis", "Plateforme récente, encore fabriquée",
     "Dell Slim DS1265 — gamme lancée en 2025", "Conforme", G),
    ("Gamme", "Professionnelle",
     "Dell Slim : gamme grand public, ni OptiPlex ni Dell Pro", "Tolérable, à connaître", Y),
    ("Format", "Tour, SFF ou Mini", "Tour fine (slim), 3,7 litres", "Conforme", G),
    ("Processeur", "Core i5 13ᵉ/14ᵉ ou Core Ultra 5",
     "AMD Ryzen 5 150, équivalent Core i5", "Équivalent", Y),
    ("Nombre de cœurs", "6 minimum, 8 recommandés ou plus", "Non communiqué", "À confirmer", Y),
    ("Nombre de threads", "12 minimum", "Non communiqué", "À confirmer", Y),
    ("Fréquence de base", "≈ 2,5 GHz minimum", "Non communiquée", "À confirmer", Y),
    ("Fréquence Turbo", "4,0 GHz minimum, 4,5 recommandé", "Non communiquée", "À confirmer", Y),
    ("Enveloppe thermique", "Adaptée au châssis",
     "Non communiquée ; châssis slim, ventilation réduite", "Point de vigilance", Y),
    ("Mémoire vive", "16 Go minimum, 32 Go recommandé", "16 Go", "Sous la cible", Y),
    ("Type de mémoire", "DDR5 préférable", "DDR5 4800", "Conforme", G),
    ("Stockage", "SSD NVMe 512 Go minimum, 1 To idéal",
     "SSD M.2 NVMe 512 Go", "Minimum atteint", Y),
    ("Carte graphique", "Intégrée acceptable", "AMD Radeon 660M intégrée", "Conforme", G),
    ("Ethernet", "Gigabit minimum", "Non précisé", "À confirmer", Y),
    ("Wi-Fi / Bluetooth", "Wi-Fi 6 minimum", "Non précisé", "À confirmer", Y),
    ("Système", "Windows 11 Professionnel", "Windows 11 Famille",
     "Licence Pro à acheter", O),
    ("Sécurité", "TPM 2.0, Secure Boot, idéalement vPro",
     "Non communiqué", "À vérifier", Y),
    ("Écran", "Idéalement inclus dans le pack", "Non inclus — à chiffrer",
     "Coût à ajouter", Y),
    ("Clavier / souris", "Souhaités", "Clavier et souris Dell annoncés", "Inclus", G),
    ("Garantie", "3 ans sur site exigés", "Non précisée dans l'annonce",
     "À obtenir avant achat", O),
]
NB_G = sum(1 for r in CANDIDAT if r[4] == G)
NB_Y = sum(1 for r in CANDIDAT if r[4] == Y)
NB_O = sum(1 for r in CANDIDAT if r[4] == O)


# --------------------------------------------------------------------------- #
def _legend(doc):
    legend = []
    for c in ORDRE:
        legend.append(f"**{CLASSES[c][0]} · {COMPTE[c]}** — {REGLE[c]}")
    doc.table([], [legend], [1, 1, 1, 1], font=7.4, header=False, zebra=False,
              cell_fmt={(0, j): {"bg": CLASSES[c][1], "color": CLASSES[c][2], "b": False}
                        for j, c in enumerate(ORDRE)})


def tableau_machines(doc, prefix="Tableau 3"):
    _legend(doc)
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
            r["id"], r["modèle"], r["format"], r["cpu"], r["année"] if r["année"] else "n. c.",
            r["cœurs"], court_freq(r["fréquence"]), r["ram"], r["disque"],
            "—" if r["écran"] == "non inclus" else r["écran"],
            r["os"], r["réseau"], euro(r["prix"]), euro(r["livré"]), fcfa(r["livré"]),
            r["classe"], r["réserve"], "[ouvrir](%s)" % r["lien"],
        ])
        row_bg[i] = CLASSES[r["code"]][1]
        cfmt[(i, 15)] = {"color": CLASSES[r["code"]][2], "b": True}
        cfmt[(i, 0)] = {"b": True}
        if r["asin"] == CAND["asin"]:
            cfmt[(i, 1)] = {"b": True, "color": "1F3B63"}

    doc.table(headers, body, widths, font=6.9, header=True, zebra=False, aligns=aligns,
              row_bg=row_bg, cell_fmt=cfmt,
              caption=prefix + " — Les six postes fixes Dell de la page qui affichent un prix, "
                      "classés par total livré croissant. Prix TTC du 5 novembre 2026, frais de "
                      "port compris dans le total livré ; 1 € = 655,957 FCFA. La couleur de la "
                      "ligne donne la classe, la colonne « Réserve » dit pourquoi. "
                      "n. c. = non communiqué.")


def tableau_ecartees(doc, prefix="Tableau 3 bis"):
    rows = [[m, conf, prix, motif, "[fiche](https://www.amazon.fr/dp/%s)" % asin]
            for m, conf, prix, motif, asin in ECARTEES]
    doc.table(["Machine", "Configuration annoncée", "Prix affiché", "Motif d'exclusion", "Lien"],
              rows, [7.4, 12.4, 4.6, 12.0, 3.6], font=7.2, header=True, zebra=True,
              aligns=["l", "l", "r", "l", "c"],
              caption=prefix + " — Les huit autres annonces Dell de la page. Cinq n'affichent "
                      "aucun prix (« voir les options ») ; trois sortent du périmètre des "
                      "postes fixes. Elles restent utiles : la première est la seule Dell "
                      "annoncée en 16 Go / 512 Go / Windows 11 Pro.")


def tableau_classes(doc, prefix="Tableau 4"):
    actions = {
        "C": "retenir",
        "M": "corriger le point manquant (licence Pro, garantie) avant de commander",
        "I": "demander mémoire, disque et garantie au vendeur avant de classer",
        "N": "écarter",
    }
    recap = []
    for c in ORDRE:
        membres = ", ".join("%s %s" % (r["id"], r["modèle"]) for r in ROWS if r["code"] == c) \
            or "aucune"
        recap.append([CLASSES[c][0], str(COMPTE[c]), membres, actions[c]])
    doc.table(["Classe", "Nb machines", "Machines", "Suite à donner"], recap,
              [3.6, 1.8, 6.0, 5.7], font=8.2, header=True, zebra=False, first_col_bold=True,
              row_bg={i: CLASSES[c][1] for i, c in enumerate(ORDRE)},
              aligns=["l", "c", "l", "l"],
              caption=prefix + " — Quatre classes, un seul critère de lecture : le nombre de "
                      "points du socle tenus (16 Go, 512 Go, Windows 11 Pro, processeur 2023 ou "
                      "plus récent).")


# --------------------------------------------------------------------------- #
def build_doc():
    from render import Doc

    doc = Doc(
        base=BASE,
        title="Benchmark — postes fixes Dell (quatre tableaux)",
        subtitle="La cible, la cible choisie, les machines du marché, le classement",
        meta=[],
        doc_ref="GED-BENCH-2026-11-D · Confidentiel — usage interne",
        footer="GED-SERVICES · benchmark postes fixes Dell",
    )

    doc.cover(
        eyebrow="Benchmark — postes fixes · volet Dell",
        title="Postes fixes Dell\n750 à 1 250 €",
        subtitle="Quatre tableaux dans l'ordre de la décision : ce qu'il faut, ce que l'on "
                 "retient, ce que le marché propose, ce qu'il en reste.",
        meta_rows=[
            ["Destinataire", "**M. Jad, directeur général — ADCHIM**"],
            ["Émetteur", "**Joël MBA OYONE — GED-SERVICES**"],
            ["Source", "Page de résultats Amazon.fr fournie (« ordinateur de bureau », marques "
                       "Dell et HP, état Neuf, 750 à 1 250 €), relevée le **5 novembre 2026** — "
                       "48 annonces visibles sur 58"],
            ["Tableau 1", "**La cible** : profil technique exigé par profil d'usage, "
                          "**année de sortie comprise** (identique au dossier HP)"],
            ["Tableau 2", "**La cible choisie** : Dell Slim DS1265 confronté aux 21 points "
                          "du cahier des charges"],
            ["Tableau 3", "**Le marché** : les six postes fixes Dell qui affichent un prix, "
                          "puis les huit annonces écartées avec leur motif"],
            ["Tableau 4", "**Le classement** : %d conformes · %d moyennement conformes · "
                          "%d incertaine · %d non conformes"
                          % (COMPTE["C"], COMPTE["M"], COMPTE["I"], COMPTE["N"])],
            ["Prix", "TTC, frais de port compris dans le « total livré » ; 1 € = 655,957 FCFA, "
                     "parité fixe"],
            ["Lecture", "**n. c.** = non communiqué, jamais déduit. Année = lancement du "
                        "processeur, non du châssis"],
            ["Livrables", "Word (.docx) et PDF identiques, plus le classeur `.xlsx` à six "
                          "feuilles filtrables"],
        ],
        pagebreak=False,
    )
    doc.pagebreak()

    # ---------------------------------------------------------------- tableau 1
    doc.h1_plain("Tableau 1 — La cible : profil technique et millésime")
    doc.p("La cible se définit par l'usage, pas par un fabricant. Trois profils suffisent à "
          "couvrir les postes d'ADCHIM ; le profil **standard entreprise** est la référence "
          "d'achat. Elle ne change pas selon la marque : le tableau ci-dessous est celui du "
          "dossier HP, repris à l'identique pour que les deux relevés se comparent ligne à "
          "ligne.", small=True)
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
    doc.h1_plain("Tableau 2 — La cible choisie : Dell Slim DS1265")
    doc.p("Des six postes fixes Dell de la page qui affichent un prix, un seul annonce 16 Go et "
          "512 Go : le **Dell Slim DS1265** — Ryzen 5, 16 Go DDR5, SSD 512 Go, Windows 11 "
          "Famille, clavier et souris compris. Prix relevé le 5 novembre 2026 : **%s livré, "
          "soit %s**. [Fiche Amazon.fr](%s)."
          % (euro(CAND["livré"]), fcfa(CAND["livré"]), CAND["lien"]), small=True)
    doc.p("Les 21 points du cahier des charges, confrontés à l'annonce : **%d conformes ou "
          "meilleurs, %d à confirmer, %d bloquants** tant qu'ils ne sont pas levés."
          % (NB_G, NB_Y, NB_O), small=True)
    rows = [[c, cible, constate, ev] for c, cible, constate, ev, _ in CANDIDAT]
    cf = {(i, 3): FMT[CANDIDAT[i][4]] for i in range(len(CANDIDAT))}
    doc.table(["Critère", "Cahier des charges", "Constaté sur l'annonce", "Évaluation"],
              rows, [3.6, 4.4, 5.6, 3.5], font=7.6, aligns=["l", "l", "l", "c"], cell_fmt=cf,
              caption="Tableau 2 — Le candidat contre la cible. Le vert est tenu ou dépassé, "
                      "le jaune reste à confirmer ou atteint le plancher, l'orange manque.")
    doc.p("**Ce que le tableau dit.** Quatorze points ne sont pas documentés : la fiche vend "
          "une mémoire, un disque et une gamme, pas un processeur, un réseau ni une garantie. "
          "Deux points manquent franchement : la licence — Windows 11 Famille, quand le socle "
          "exige Pro — et la garantie, absente de l'annonce. Sur ce marché, une Dell conforme "
          "existe pourtant : le **Dell Pro Micro QCM1250** (i5-14500T, 16 Go, 512 Go, Windows 11 "
          "Pro) coche le socle entier, mais s'affiche « voir les options », sans prix. Il relève "
          "du devis, pas du panier.", small=True)

    # ---------------------------------------------------------------- tableau 3
    doc.landscape3(True)
    doc.h1_plain("Tableau 3 — Les postes fixes Dell de la page, prix affiché")
    tableau_machines(doc)
    doc.spacer(0.3)
    tableau_ecartees(doc)

    # ---------------------------------------------------------------- tableau 4
    doc.landscape3(False)
    doc.h1_plain("Tableau 4 — Les quatre classes, et ce qu'il faut en faire")
    tableau_classes(doc)
    doc.p("**Aucune machine Dell neuve ne tient le socle.** La seule qui réunisse les quatre "
          "points est l'**OptiPlex 7010 Micro reconditionnée** (%s, %s livré) : 16 Go, 512 Go, "
          "Windows 11 Pro, processeur 2023 — mais la garantie est celle du vendeur, pas celle de "
          "Dell. Le **Slim DS1265** (%s) n'échoue que sur la licence et la garantie : avec un "
          "Windows 11 Pro et un contrat trois ans, il deviendrait la référence Dell du segment "
          "bas. L'**AiO EC24250** ne peut pas être jugée : ni mémoire ni disque ne sont annoncés."
          % (euro(689.83), fcfa(689.83), euro(CAND["livré"])), small=True)

    doc.h1_plain("Méthode et réserves")
    doc.ul([
        "**Source** : page de résultats Amazon.fr fournie, « ordinateur de bureau », marques "
        "Dell et HP, état Neuf, 750 à 1 250 €, relevée le 5 novembre 2026. La page affiche "
        "« 1-48 sur 58 résultats » : **la page 2 n'a pas été fournie**, dix annonces manquent, "
        "dont d'éventuels postes fixes Dell. Le relevé porte sur les 48 annonces visibles.",
        "**Périmètre** : onze annonces Dell concernent un poste fixe ; six affichent un prix et "
        "figurent au tableau 3, cinq sont en « voir les options » et figurent au tableau 3 bis. "
        "Les portables et le client léger sont écartés du périmètre, sans jugement de valeur.",
        "**Fourchette** : trois annonces du tableau 3 sortent de la fourchette 750 à 1 250 € "
        "— l'OptiPlex 7010 (689,83 €), l'OptiPlex 7070 (790,91 €) et l'OptiPlex 3080 (723,47 €) "
        "— parce qu'elles éclairent la comparaison. Elles sont signalées par leur prix, non "
        "retenues comme achats.",
        "**État des annonces** : le filtre « Neuf » de la page laisse passer deux reconditionnés "
        "(OptiPlex 7010 et 7070). Ils sont classés non conformes, la règle le prévoit.",
        "**Prix** : TTC affichés par le vendeur, port annoncé ajouté dans le « total livré ». "
        "1 € = 655,957 FCFA, parité fixe : les montants en francs sont exacts, les prix ne le "
        "sont pas — ils changent chaque semaine.",
        "**n. c.** : information absente de l'annonce ; elle n'a été ni déduite ni complétée "
        "pour un autre distributeur. Aucun montant estimé.",
        "**Année** : lancement du processeur, non du châssis. Pour le DS1265, la gamme est "
        "annoncée en 2025 ; la référence exacte du processeur reste à confirmer avec le vendeur.",
        "**Liens** : URL canoniques `amazon.fr/dp/ASIN`, une par machine et par annonce écartée.",
        "**Classes** : règle des quatre points, identique au dossier HP, sans pondération. Le "
        "caractère reconditionné reste un point rédhibitoire, même quand les quatre points sont "
        "tenus.",
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
    cp.title = "Benchmark — postes fixes Dell, quatre tableaux"
    cp.subject = "Cible, cible choisie, postes fixes Dell de 750 à 1 250 €, classement"
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

    # ---- 1 cible
    ws = wb.active
    ws.title = "1 Cible"
    entetes(ws, CIBLE_HEADERS, [26, 38, 42, 42])
    for i, row in enumerate(CIBLE, start=2):
        for c, v in enumerate(row, 1):
            cell = ws.cell(row=i, column=c, value=v.replace("**", ""))
            cell.font = Font(size=9, bold=(c == 1), name="Calibri")
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = Border(bottom=thin)
            if i == 4:
                cell.fill = PatternFill("solid", fgColor="E6EDF5")
    ws.auto_filter.ref = "A1:D%d" % (len(CIBLE) + 1)
    ws.freeze_panes = "B2"
    ws.sheet_properties.tabColor = "1F3B63"

    # ---- 2 candidat
    ws2 = wb.create_sheet("2 Candidat Dell")
    entetes(ws2, ["Critère", "Cahier des charges", "Constaté sur l'annonce", "Évaluation"],
            [26, 40, 52, 22])
    for i, (crit, cible, constate, ev, code) in enumerate(CANDIDAT, start=2):
        for c, v in enumerate((crit, cible, constate, ev), 1):
            cell = ws2.cell(row=i, column=c, value=v)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = Border(bottom=thin)
            if c == 4:
                cell.fill = PatternFill("solid", fgColor=FMT[code]["bg"])
                cell.font = Font(size=9, bold=True, name="Calibri", color=FMT[code]["color"])
            else:
                cell.font = Font(size=9, bold=(c == 1), name="Calibri")
                if i % 2 == 0:
                    cell.fill = PatternFill("solid", fgColor="F5F7FA")
    ws2.auto_filter.ref = f"A1:D{len(CANDIDAT) + 1}"
    ws2.freeze_panes = "B2"
    ws2.sheet_properties.tabColor = "1E6B33"

    # ---- 3 machines
    ws3 = wb.create_sheet("3 Les 6 machines")
    cols = [
        ("ID", 7, "id"), ("Classe", 22, "classe"), ("Machine", 40, "modèle"),
        ("Format", 9, "format"), ("Processeur", 20, "cpu"), ("Année", 8, "année"),
        ("Cœurs / threads", 16, "cœurs"), ("Fréquence (GHz)", 14, "fréquence"),
        ("RAM", 8, "ram"), ("Type de mémoire", 14, "ram_type"), ("Disque", 10, "disque"),
        ("Type de disque", 16, "disque_type"), ("Écran", 22, "écran"), ("Système", 20, "os"),
        ("Réseau", 16, "réseau"), ("Garantie annoncée", 24, "garantie"),
        ("Périphériques", 28, "périph"), ("Tarif € TTC", 12, "prix"),
        ("Frais de port €", 12, "port"), ("Total livré €", 12, "livré"),
        ("Total livré FCFA", 16, "livré_fcfa"), ("Réserve", 56, "réserve"),
        ("Lien Amazon", 40, "lien"),
    ]
    entetes(ws3, [c[0] for c in cols], [c[1] for c in cols])
    band = {c: PatternFill("solid", fgColor=CLASSES[c][1]) for c in ORDRE}
    for i, r in enumerate(ROWS, start=2):
        for c, (_label, _w, key) in enumerate(cols, 1):
            val = r[key]
            cell = ws3.cell(row=i, column=c, value=val)
            cell.font = Font(size=9, name="Calibri")
            cell.border = Border(bottom=thin)
            cell.fill = band[r["code"]]
            if key in ("prix", "port", "livré", "livré_fcfa"):
                cell.number_format = '# ##0.00 "€"' if key != "livré_fcfa" else '# ##0 "FCFA"'
                cell.alignment = Alignment(horizontal="right")
            elif key == "lien":
                cell.hyperlink = val
                cell.font = Font(size=9, name="Calibri", color="1155CC", underline="single")
            elif key in ("réserve", "modèle", "écran"):
                cell.alignment = Alignment(wrap_text=True, vertical="top")
            if key == "classe":
                cell.font = Font(size=9, bold=True, name="Calibri", color=CLASSES[r["code"]][2])
            if key == "id":
                cell.font = Font(size=9, bold=True, name="Calibri")
    ws3.auto_filter.ref = "A1:%s%d" % (get_column_letter(len(cols)), len(ROWS) + 1)
    ws3.freeze_panes = "D2"
    ws3.print_title_rows = "1:1"
    ws3.page_setup.orientation = "landscape"
    ws3.page_setup.paperSize = ws3.PAPERSIZE_A3
    ws3.page_setup.fitToWidth = 1
    ws3.page_setup.fitToHeight = 0
    ws3.sheet_properties.pageSetUpPr.fitToPage = True
    ws3.sheet_properties.tabColor = "1F3B63"

    # ---- 4 classes
    ws4 = wb.create_sheet("4 Classes")
    entetes(ws4, ["Classe", "Nb machines", "Machines", "Suite à donner"], [24, 12, 56, 52])
    actions = {"C": "retenir",
               "M": "corriger le point manquant (licence Pro, garantie) avant de commander",
               "I": "demander mémoire, disque et garantie au vendeur avant de classer",
               "N": "écarter"}
    for i, c in enumerate(ORDRE, start=2):
        membres = ", ".join("%s %s" % (r["id"], r["modèle"]) for r in ROWS if r["code"] == c) \
            or "aucune"
        for j, v in enumerate((CLASSES[c][0], COMPTE[c], membres, actions[c]), 1):
            cell = ws4.cell(row=i, column=j, value=v)
            cell.font = Font(size=9, bold=(j == 1), name="Calibri")
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = Border(bottom=thin)
            cell.fill = PatternFill("solid", fgColor=CLASSES[c][1])
            if j == 1:
                cell.font = Font(size=9, bold=True, name="Calibri", color=CLASSES[c][2])
    ws4.freeze_panes = "A2"
    ws4.sheet_properties.tabColor = "A23B1A"

    # ---- 5 annonces écartées
    ws5 = wb.create_sheet("5 Annonces écartées")
    entetes(ws5, ["Machine", "Configuration annoncée", "Prix affiché", "Motif d'exclusion",
                  "ASIN", "Lien"], [30, 46, 16, 52, 14, 34])
    for i, (m, conf, prix, motif, asin) in enumerate(ECARTEES, start=2):
        lien = "https://www.amazon.fr/dp/%s" % asin
        for j, v in enumerate((m, conf, prix, motif, asin, lien), 1):
            cell = ws5.cell(row=i, column=j, value=v)
            cell.font = Font(size=9, name="Calibri")
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = Border(bottom=thin)
            if j == 6:
                cell.hyperlink = v
                cell.font = Font(size=9, name="Calibri", color="1155CC", underline="single")
    ws5.auto_filter.ref = "A1:F%d" % (len(ECARTEES) + 1)
    ws5.freeze_panes = "B2"
    ws5.sheet_properties.tabColor = "7A5E12"

    # ---- 6 méthode
    ws6 = wb.create_sheet("Méthode")
    ws6.column_dimensions["A"].width = 18
    ws6.column_dimensions["B"].width = 110
    notes = [
        ("Quatre tableaux", "1 la cible technique, 2 la cible choisie confrontée aux 21 points "
                            "du cahier des charges, 3 les six postes fixes Dell qui affichent un "
                            "prix puis les huit annonces écartées, 4 le classement en quatre "
                            "classes."),
        ("Filtrer", "Chaque feuille porte un filtre automatique sur ses colonnes (flèche dans "
                    "l'en-tête) : il fonctionne à l'identique dans Excel, LibreOffice Calc et "
                    "Google Sheets."),
    ] + [(f"Classe {c} — {CLASSES[c][0]} ({COMPTE[c]})", REGLE[c]) for c in ORDRE] + [
        ("Périmètre", "Onze annonces Dell de poste fixe sur la page : six avec prix (feuille 3), "
                      "cinq en « voir les options » (feuille 5). Portables et client léger "
                      "écartés."),
        ("Fourchette", "Trois machines du tableau sortent de 750 à 1 250 € (689,83 / 790,91 / "
                       "723,47 €) et restent au tableau pour la comparaison."),
        ("Candidat", "Dell Slim DS1265 — Ryzen 5, 16 Go DDR5, 512 Go, Windows 11 Famille : "
                     f"{euro(CAND['livré'])} livré, soit {fcfa(CAND['livré'])}. La configuration "
                     "Dell conforme existe (Pro Micro QCM1250, i5-14500T, 16 Go, 512 Go, "
                     "Windows 11 Pro) mais n'affiche pas de prix."),
        ("Source", "Page de résultats Amazon.fr fournie, relevée le 5 novembre 2026 : 48 "
                   "annonces visibles sur 58, la page 2 n'a pas été fournie."),
        ("Prix", "TTC, port compris dans le total livré ; 1 € = 655,957 FCFA, parité fixe."),
        ("n. c.", "Information non communiquée dans l'annonce : jamais déduite, jamais estimée."),
        ("Année", "Lancement du processeur, non du châssis."),
    ]
    for r, (k, v) in enumerate(notes, start=1):
        a = ws6.cell(row=r, column=1, value=k)
        a.font = Font(bold=True, size=9)
        b = ws6.cell(row=r, column=2, value=v)
        b.font = Font(size=9)
        b.alignment = Alignment(wrap_text=True, vertical="top")

    wb.properties.creator = "GED-SERVICES"
    wb.properties.title = "Benchmark — postes fixes Dell, quatre tableaux"
    wb.properties.subject = "Cible, candidat, postes fixes Dell de 750 à 1 250 €, classement"
    wb.save(path)
    return path


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print("xlsx :", build_xlsx(os.path.join(OUT, BASE + ".xlsx")))
    print("docx+pdf :", build_doc())
    print("classes :", COMPTE, "| candidat :", NB_G, NB_Y, NB_O)
