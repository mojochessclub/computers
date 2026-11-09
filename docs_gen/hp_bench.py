# -*- coding: utf-8 -*-
"""Benchmark HP — classeur filtrable (.xlsx) et rapport paysage (.docx + .pdf)."""
import os
import re
import sys

from hp_data import MACHINES, VERDICT, LIEN, TVA

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables", "HP")
BASE = "Benchmark_postes_fixes_HP_750_1250_euros"

# année de lancement du processeur (et non du châssis)
ANNEE = {
    "i3-14100": 2024, "i5-14400": 2024, "i5-14400T": 2024, "i5-13500": 2023, "i5-14500": 2024,
    "i5-14500T": 2024, "i7-14700T": 2024, "i7-13700T": 2023, "i3-13100T": 2023, "i3-1315U": 2023,
    "i5-1335U": 2023, "Ryzen 5 7520U": 2023, "Ryzen 5 8500G": 2024, "Ryzen 5 220": 2025,
    "Ryzen 3 210": 2025, "Core Ultra 5 225": 2025, "Core Ultra 5 235T": 2025,
    "Core Ultra 7 265": 2025, "Xeon W-2125": 2017,
}

TRANCHE = {"g": "Conforme au socle", "b": "À compléter", "c": "Hors cible en l'état"}


def euro(n):
    return f"{n:,.2f}".replace(",", "\u00a0").replace(".", ",") + "\u00a0€"


def fcfa(n):
    return f"{round(n * TVA):,}".replace(",", "\u00a0") + "\u00a0FCFA"


def freq_pair(f):
    """'2,6 – 5,0 GHz' -> ('2,6', '5,0') ; sinon (n. c., n. c.)."""
    nums = re.findall(r"\d+,\d+", f)
    if len(nums) >= 2:
        return nums[0], nums[1]
    if len(nums) == 1:
        return nums[0], nums[0]
    return "n. c.", "n. c."


def ligne(m):
    """Dictionnaire complet d'une machine (colonnes du classeur)."""
    (mid, modele, fmt, cpu, gen, cores, freq, ram, ram_t, disque, disque_t, os, lic, ecran,
     periph, reseau, garantie, prix, port, asin, verdict, motif) = m
    total = prix + port
    return {
        "id": mid, "désidératas": "Fixe", "tranche": TRANCHE[verdict], "fabricant": "HP",
        "modèle": modele.replace("**", ""), "os": os, "année": ANNEE.get(cpu, "n. c."),
        "prix": prix, "prix_fcfa": round(prix * TVA), "port": port,
        "port_fcfa": round(port * TVA), "livré": total, "livré_fcfa": round(total * TVA),
        "cpu": cpu, "gén": gen, "cœurs": cores, "fréquence": freq, "ram": ram, "ram_type": ram_t,
        "disque": disque, "disque_type": disque_t, "écran": ecran, "périph": periph,
        "réseau": reseau, "garantie": garantie, "licence": lic, "format": fmt,
        "verdict": TRANCHE[verdict], "motif": motif, "lien": LIEN.format(asin=asin), "asin": asin,
        "vcode": verdict,
    }


LIGNES = sorted((ligne(m) for m in MACHINES), key=lambda r: r["livré"])
for i, r in enumerate(LIGNES, 1):
    r["id"] = f"M{i:02d}"

CAND = next(r for r in LIGNES if r["asin"] == "B0D76M6T6R")
RANG = [r["id"] for r in LIGNES].index(CAND["id"]) + 1
COMPLETES = [r for r in LIGNES if r["ram"] != "n. c." and r["disque"] != "n. c."
             and r["cpu"] != "n. c."]
RANG_COMPLET = [r["id"] for r in COMPLETES].index(CAND["id"]) + 1
NB_INCOMPLET = len(LIGNES) - len(COMPLETES)


# --------------------------------------------------------------------------- #
def build_xlsx(path):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.table import Table, TableStyleInfo

    cols = [
        ("ID", 7, "id"), ("Désidératas", 12, "désidératas"), ("Tranche", 20, "verdict"),
        ("Fabricant", 10, "fabricant"), ("Modèle", 38, "modèle"), ("OS", 20, "os"),
        ("Année processeur", 11, "année"), ("Tarif € TTC", 11, "prix"),
        ("Tarif FCFA", 15, "prix_fcfa"), ("Frais de port €", 11, "port"),
        ("Frais de port FCFA", 15, "port_fcfa"), ("Total livré €", 12, "livré"),
        ("Total livré FCFA", 16, "livré_fcfa"), ("Processeur", 24, "cpu"),
        ("Génération", 11, "gén"), ("Cœurs / threads", 12, "cœurs"),
        ("Fréquence min (GHz)", 10, "fmin"), ("Fréquence max (GHz)", 10, "fmax"),
        ("RAM", 8, "ram"), ("Type de mémoire", 13, "ram_type"), ("Disque", 16, "disque"),
        ("Type de disque", 12, "disque_type"), ("Écran", 20, "écran"),
        ("Clavier / souris", 14, "périph"), ("Wi-Fi", 18, "réseau"), ("Ethernet", 10, "eth"),
        ("Garantie annoncée", 18, "garantie"), ("Licence", 10, "licence"),
        ("Format", 8, "format"), ("Verdict", 22, "verdict"), ("Motif / réserve", 42, "motif"),
        ("Lien Amazon", 44, "lien"),
        ("FCFA Amazon", 16, "livré_fcfa"), ("FCFA Fnac", 12, None), ("FCFA Cdiscount", 12, None),
        ("FCFA LDLC", 12, None), ("FCFA Materiel.net", 12, None), ("FCFA Top Achat", 12, None),
    ]

    wb = Workbook()
    ws = wb.active
    ws.title = "Benchmark HP"

    head_fill = PatternFill("solid", fgColor="1F3B63")
    head_font = Font(color="FFFFFF", bold=True, size=9, name="Calibri")
    thin = Side(style="thin", color="D0D7E2")

    for c, (label, width, _key) in enumerate(cols, 1):
        cell = ws.cell(row=1, column=c, value=label)
        cell.fill = head_fill
        cell.font = head_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = Border(bottom=thin)
        ws.column_dimensions[get_column_letter(c)].width = width
    ws.row_dimensions[1].height = 34

    fills = {"b": PatternFill("solid", fgColor="FBF3D0"), "c": PatternFill("solid", fgColor="FBE0CE")}

    for r, row in enumerate(LIGNES, start=2):
        fmin, fmax = freq_pair(row["fréquence"])
        values = {
            "fmin": fmin, "fmax": fmax, "eth": row["réseau"].split("+")[-1].strip()
            if "GbE" in row["réseau"] else "n. c.",
        }
        for c, (_label, _w, key) in enumerate(cols, 1):
            if key is None:
                val = "non relevé"
            elif key in values:
                val = values[key]
            else:
                val = row[key]
            cell = ws.cell(row=r, column=c, value=val)
            cell.font = Font(size=9, name="Calibri")
            cell.border = Border(bottom=thin)
            if key in ("prix", "port", "livré"):
                cell.number_format = '# ##0.00 "€"'
                cell.alignment = Alignment(horizontal="right")
            elif key in ("prix_fcfa", "port_fcfa", "livré_fcfa"):
                cell.number_format = '# ##0 "FCFA"'
                cell.alignment = Alignment(horizontal="right")
            elif key == "lien":
                cell.hyperlink = val
                cell.font = Font(size=9, name="Calibri", color="1155CC", underline="single")
            elif key in ("motif", "modèle", "écran"):
                cell.alignment = Alignment(wrap_text=True, vertical="top")
            elif key == "verdict":
                cell.fill = fills.get(row["vcode"], fills["b"])
                cell.font = Font(size=9, bold=True, name="Calibri")
            elif key == "id":
                cell.font = Font(size=9, bold=True, name="Calibri")

    ref = f"A1:{get_column_letter(len(cols))}{len(LIGNES) + 1}"
    t = Table(displayName="BenchmarkHP", ref=ref)
    t.tableStyleInfo = TableStyleInfo(name="TableStyleLight9", showRowStripes=True)
    ws.add_table(t)
    ws.freeze_panes = "F2"
    ws.auto_filter.ref = ref

    # seconde feuille : légende et méthode (courte)
    ws2 = wb.create_sheet("Méthode")
    notes = [
        ("Source", "Page de résultats Amazon.fr fournie par le destinataire — « ordinateur de bureau », "
                   "marque HP, état Neuf, prix 750 à 1 250 € — relevée le 5 novembre 2026."),
        ("Périmètre", "28 machines fixes HP avec prix affiché. Sont écartées : les annonces sans prix "
                      "(options non choisies), les portables, les clients légers et le matériel réseau."),
        ("Prix", "Prix TTC affichés, hors frais de port ; le port annoncé est indiqué séparément et "
                 "additionné dans la colonne « Total livré ». Les montants bougent chaque semaine."),
        ("Conversion", "1 € = 655,957 FCFA, parité fixe : les colonnes FCFA sont exactes, les prix non."),
        ("Année", "Année de lancement du processeur, déduite de sa référence — et non année du châssis."),
        ("n. c.", "Information non communiquée dans l'annonce : elle n'a pas été complétée par déduction."),
        ("Distributeurs", "Seuls les prix Amazon ont été relevés. Les colonnes Fnac, Cdiscount, LDLC, "
                          "Materiel.net et Top Achat restent vides : elles n'ont pas été vérifiées et "
                          "aucun montant n'a été estimé."),
        ("Verdict", "« Conforme au socle » : 32 Go, Windows 11 Pro et garantie 3 ans sur site réunis. "
                    "« À compléter » : 16 Go et/ou licence Famille. « Hors cible » : 8 Go, "
                    "reconditionné, plateforme ancienne ou annonce sans données techniques."),
        ("Liens", "URL directes /dp/ de la page source ; trois ont été ouvertes le 5 novembre 2026 et "
                  "répondent, dont celle du candidat (1 061,20 € + 78,98 € de port)."),
    ]
    ws2.column_dimensions["A"].width = 16
    ws2.column_dimensions["B"].width = 110
    for r, (k, v) in enumerate(notes, start=1):
        a = ws2.cell(row=r, column=1, value=k)
        a.font = Font(bold=True, size=9)
        b = ws2.cell(row=r, column=2, value=v)
        b.font = Font(size=9)
        b.alignment = Alignment(wrap_text=True, vertical="top")

    wb.save(path)
    return path


# --------------------------------------------------------------------------- #
def build_doc():
    from render import Doc

    doc = Doc(
        base=BASE,
        title="Benchmark — postes fixes HP",
        subtitle="Vingt-huit machines fixes HP neuves, 750 à 1 250 €, relevées sur Amazon.fr",
        meta=[],
        doc_ref="GED-BENCH-2026-11 · Confidentiel — usage interne",
        footer="GED-SERVICES · benchmark postes fixes HP",
    )

    doc.cover(
        eyebrow="Benchmark — postes fixes",
        title="Postes fixes HP\n750 à 1 250 €",
        subtitle="Vingt-huit machines fixes HP neuves relevées sur Amazon.fr : prix, "
                 "caractéristiques, liens et conformité à la cible GED-SERVICES.",
        meta_rows=[
            ["Destinataire", "**M. Jad, directeur général — ADCHIM**"],
            ["Émetteur", "**Joël MBA OYONE — GED-SERVICES**"],
            ["Source", "Page de résultats Amazon.fr fournie (« ordinateur de bureau », marque HP, "
                       "état Neuf, 750 à 1 250 €), relevée le **5 novembre 2026**"],
            ["Périmètre", "28 machines fixes avec prix affiché ; annonces sans prix, portables, "
                          "clients légers et matériel réseau écartés"],
            ["Prix", "TTC, hors frais de port ; port annoncé indiqué à part et ajouté au « total "
                     "livré ». 1 € = 655,957 FCFA, parité fixe"],
            ["Fiabilité", "Caractéristiques reprises des annonces ; **n. c.** = non communiqué, "
                          "jamais déduit. Année = lancement du processeur, non du châssis. "
                          "Seuls les prix Amazon sont relevés — aucun montant estimé ailleurs"],
            ["Liens", "URL canoniques `amazon.fr/dp/ASIN`. **Trois fiches rouvertes** (M03, M21, "
                      "M22 le 5 novembre) : même produit, même prix ; les 25 autres sont les "
                      "liens de la page de résultats"],
            ["Lecture", "Trois tableaux liés par l'identifiant **M01 à M28**, classés par total "
                        "livré croissant ; **ligne bleue** = HP Elite 800 G9 Mini, le poste examiné "
                        "dans la note d'arbitrage"],
            ["Livrables", "Word (.docx) et PDF identiques, plus le classeur `.xlsx` filtrable"],
        ],
        pagebreak=False,
    )

    doc.landscape(True)

    # ---- tableau A
    rows, cf = [], {}
    for i, r in enumerate(LIGNES):
        rows.append([r["id"], r["modèle"], r["format"], euro(r["prix"]), euro(r["port"]),
                     euro(r["livré"]), fcfa(r["livré"]), f"[ouvrir]({r['lien']})"])
        if r is CAND:
            for c in range(8):
                cf[(i, c)] = {"bg": "EAF0F7", "b": True}
    doc.table(
        ["ID", "Machine", "Format", "Prix TTC", "Port", "Total livré", "Total FCFA", "Lien"],
        rows, widths=[1.1, 6.4, 1.5, 2.2, 1.8, 2.3, 3.0, 1.9], font=7.6,
        aligns=["c", "l", "c", "r", "r", "r", "r", "c"], cell_fmt=cf,
        caption="Tableau 1 — Identification et prix, classés par total livré croissant. Prix TTC du "
                "5 novembre 2026 ; les frais de port sont ceux annoncés par le vendeur.",
    )

    doc.pagebreak()

    # ---- tableau B
    rows, cf = [], {}
    for i, r in enumerate(LIGNES):
        rows.append([r["id"], r["cpu"], str(r["année"]), r["cœurs"], r["fréquence"], r["ram"],
                     r["disque"], r["écran"]])
        if r is CAND:
            for c in range(8):
                cf[(i, c)] = {"bg": "EAF0F7", "b": True}
    doc.table(
        ["ID", "Processeur", "Année", "Cœurs", "Fréquences", "RAM", "Disque", "Écran"],
        rows, widths=[1.1, 5.4, 1.4, 2.0, 2.9, 2.0, 3.2, 7.9], font=7.6,
        aligns=["c", "l", "c", "c", "c", "c", "l", "l"], cell_fmt=cf,
        caption="Tableau 2 — Caractéristiques techniques reprises des annonces. Année = lancement du "
                "processeur, non du châssis ; n. c. = non communiqué.",
    )

    doc.pagebreak()

    # ---- tableau C
    rows, cf = [], {}
    for i, r in enumerate(LIGNES):
        code = r["vcode"]
        rows.append([r["id"], r["modèle"], r["os"], r["réseau"], r["garantie"],
                     r["verdict"], r["motif"]])
        cf[(i, 5)] = {"bg": {"b": "FBF3D0", "c": "FBE0CE"}[code],
                      "color": {"b": "806000", "c": "A8480C"}[code], "b": True}
        if r is CAND:
            cf[(i, 1)] = {"bg": "EAF0F7", "b": True}
    doc.table(
        ["ID", "Machine", "Système", "Réseau", "Garantie annoncée", "Verdict", "Motif / réserve"],
        rows, widths=[1.1, 5.0, 3.0, 2.8, 3.0, 3.1, 7.9], font=7.5,
        aligns=["c", "l", "l", "l", "l", "c", "l"], cell_fmt=cf,
        caption="Tableau 3 — Conformité à la cible GED-SERVICES (32 Go, Windows 11 Pro, garantie 3 ans "
                "sur site) et réserves à lever avant commande.",
    )

    doc.landscape(False)

    doc.p("**Trois constats.** Aucune des {0} machines n'est livrée à 32 Go : l'extension est à prévoir "
          "partout, entre 336 € la barrette et 594 € le kit, quel que soit le châssis. Le classement "
          "suit le prix, pas la performance : de {1} à {2}, l'écart atteint {3} pour la même dotation "
          "de 16 Go et 512 Go. Enfin, **{4} annonces sur {0} ne donnent pas la totalité des "
          "caractéristiques** — c'est le premier filtre à appliquer avant de comparer des prix."
          .format(len(LIGNES), euro(LIGNES[0]["livré"]), euro(LIGNES[-1]["livré"]),
                  euro(LIGNES[-1]["livré"] - LIGNES[0]["livré"]), NB_INCOMPLET), small=True)

    doc.h1_plain("Le candidat dans le classement")
    p400 = next(r for r in LIGNES if r["asin"] == "B0FW5CD247")
    p260 = next(r for r in LIGNES if r["asin"] == "B0F3PSJX34")
    doc.p("Le **HP Elite 800 G9 Mini** ({0}, ligne bleue des tableaux) arrive à **{1}**, port compris "
          "— soit **{2}** — à la **{3}e position sur {4}** par le prix, et {5}e des {6} machines "
          "complètement documentées. À équipement comparable, il coûte {7} de plus que le Pro 400 G9 "
          "Mini ({8}, {9}) et {10} de plus que le Pro Mini 260 G9 ({11}, {12}), qui n'a que 8 Go et "
          "256 Go. Il reste le seul à loger un i5-14500 en un litre."
          .format(CAND["id"], euro(CAND["livré"]), fcfa(CAND["livré"]), RANG, len(LIGNES),
                  RANG_COMPLET, len(COMPLETES), euro(CAND["livré"] - p400["livré"]), p400["id"],
                  euro(p400["livré"]), euro(CAND["livré"] - p260["livré"]), p260["id"],
                  euro(p260["livré"])), small=True)

    doc.p("**Prix du jour.** L'annonce affichait 1 140,18 € la veille et 1 061,20 € le 5 novembre, "
          "port à 78,98 € : c'est exactement ce que la note de la veille annonçait — un prix de place "
          "de marché bouge d'une semaine à l'autre. La comparaison doit donc se faire sur le "
          "**total livré**, jamais sur le prix d'appel.", small=True)

    doc.p("**Ce que le classeur ajoute.** Le fichier `.xlsx` joint reprend les mêmes lignes avec les "
          "colonnes du modèle demandé — tarifs par distributeur, licence, garantie, type de disque — "
          "et un **filtre actif sur chaque colonne** : il permet de trier par prix, par mémoire, par "
          "format ou par verdict, puis de ne garder que les machines conformes.", small=True)

    doc.save(OUT)

    import docx as _docx
    path = os.path.join(OUT, BASE + ".docx")
    _d = _docx.Document(path)
    cp = _d.core_properties
    cp.author = "GED-SERVICES"
    cp.last_modified_by = "GED-SERVICES"
    cp.comments = ""
    cp.keywords = ""
    cp.category = ""
    cp.subject = "Benchmark des postes fixes HP, 750 à 1 250 €"
    cp.title = "Benchmark — postes fixes HP"
    _d.save(path)
    return OUT


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    p = build_xlsx(os.path.join(OUT, BASE + ".xlsx"))
    print("xlsx:", p)
    print("docx+pdf:", build_doc())
