# -*- coding: utf-8 -*-
"""ADCHIM — « 1. L'essentiel à retenir » : reprise mise en page de la section fournie.

Trois tableaux (profil des trois gammes, exigences transverses, modèles de référence),
codes couleur vert / orange / bleu, et les trois phrases à retenir.
"""
from __future__ import annotations

import os

from docx.shared import Pt as DPt, RGBColor as DRGB
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

from render import Doc, HLine, hexc
from render import _rich_pdf as _rich

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, os.environ.get("LIVRABLES_DIR",
                                           "estimations/standard_postes_2026-11-19"))
BASE = "ADC_Essentiel_a_retenir_2026-11-19"

TVA = 655.957
VERT = "D8EDCB"
VERT_T = "1E6B33"
ORANGE = "FAEBB8"
ORANGE_T = "7A5E12"
BLEU_F = "DCE6F2"
BLEU_T = "1F3B63"
GRIS = "E9EBEF"
GRIS_T = "4A5058"
BLEU = "1F3B63"
ROUGE = "F8CDB6"
ROUGE_T = "9B2C12"


def _grp(n):
    out, i = "", 0
    for ch in reversed("%d" % n):
        if i and i % 3 == 0:
            out = "\u00A0" + out
        out = ch + out
        i += 1
    return out


def eur(x):
    if x is None:
        return "sur devis"
    ent, dec = ("%.2f" % x).split(".")
    return _grp(int(ent)) + "," + dec + "\u00A0€"


def fcfa(x):
    if x is None:
        return "—"
    return _grp(int(round(x * TVA))) + "\u00A0FCFA"


# --------------------------------------------------------------------------- #
def sous_titre(doc, text):
    """Sous-titre qui alimente le signet PDF au premier niveau (pas de h1 préalable)."""
    p = doc.doc.add_heading(text, level=2)
    for r in p.runs:
        r.font.size = DPt(12.5)
    st = ParagraphStyle("h1", parent=doc.ps["h2"])
    doc.story.append(Paragraph(_rich(text), st))


def band(doc, eyebrow, title, subtitle):
    d = doc.doc
    p = d.add_paragraph()
    r = p.add_run(eyebrow.upper())
    r.bold = True
    r.font.size = DPt(8.5)
    r.font.color.rgb = DRGB.from_string(ORANGE_T)
    p.paragraph_format.space_after = DPt(6)
    p = d.add_paragraph()
    r = p.add_run(title)
    r.bold = True
    r.font.size = DPt(22)
    r.font.color.rgb = DRGB.from_string(BLEU)
    p.paragraph_format.space_after = DPt(2)
    p = d.add_paragraph()
    r = p.add_run(subtitle)
    r.font.size = DPt(10.5)
    r.font.color.rgb = DRGB.from_string(GRIS_T)
    p.paragraph_format.space_after = DPt(10)

    doc.story.append(Paragraph(eyebrow.upper(), ParagraphStyle(
        "bey", fontName="DJ-B", fontSize=8.5, leading=11, textColor=hexc(ORANGE_T),
        spaceAfter=6)))
    doc.story.append(Paragraph(title, ParagraphStyle(
        "bti", fontName="DJ-B", fontSize=22, leading=26, textColor=hexc(BLEU),
        spaceAfter=3)))
    doc.story.append(Paragraph(subtitle, ParagraphStyle(
        "bsu", fontName="DJ", fontSize=10.5, leading=14.5, textColor=hexc(GRIS_T),
        spaceAfter=6)))
    doc.story.append(HLine())


# --------------------------------------------------------------------------- #
GAMMES_HEADERS = ["Critère", "Entrée de gamme", "Standard entreprise", "Confort"]
GAMMES_WIDTHS = [2.7, 4.7, 5.0, 4.7]
GAMMES_ROWS = [
    ["Statut", "Illustration : pas notre cible",
     "**La cible** : standard du parc", "À chiffrer sur devis"],
    ["Usage", "Bureautique légère — accueil, saisie, consultation",
     "Bureautique soutenue — commerciaux, comptabilité, transit",
     "Usages plus lourds — gros tableurs, CAO légère, au cas où"],
    ["Processeur",
     "Intel i5-13500 / 13500T — 13ᵉ gén., 2023\n"
     "AMD Ryzen 5 8500G — Zen 4, 2024",
     "Intel i5-14500 / 14500T — 14ᵉ gén., 2024\n"
     "AMD Ryzen 7 8700G — Zen 4, 2024",
     "Intel i7-14700 — 14ᵉ gén., 2024\n"
     "AMD Ryzen 7 8700G · 9700X — Zen 4 / 5"],
    ["Mémoire", "16 Go minimum livrés\n1 × 16 Go en simple canal toléré",
     "16 Go minimum livrés\n32 Go préférés : 2 × 16 Go, double canal (débit et évolutivité)",
     "32 Go en cible, deux emplacements"],
    ["Stockage", "SSD 512 Go NVMe", "SSD 512 Go NVMe", "SSD 512 Go à 1 To NVMe"],
    ["Châssis", "Tous châssis éligibles : MFF / Mini, SFF, tour",
     "Mini ou SFF ; tour si une extension PCIe est prévue",
     "Tour ou SFF — seule à garantir une carte graphique"],
    ["Enveloppe", "**650 – 850 €**", "**850 – 1 200 €**", "**1 200 – 1 350 €**"],
]

EXIG_HEADERS = ["Exigence", "Ce qu’elle impose, quelle que soit la gamme"]
EXIG_WIDTHS = [3.2, 13.9]
EXIG_ROWS = [
    ["Mémoire", "16 Go minimum **livrés** ; extension à 32 Go pour ≈ 250 €, selon la "
                "gamme. Le double canal (2 × 16 Go) se recherche pour le débit et "
                "l’évolutivité."],
    ["Processeur", "Intel 13ᵉ génération minimum (2023) ; AMD Ryzen 5 8500G / 8600G "
                   "(Zen 4) minimum. Rien en dessous."],
    ["Stockage", "SSD 512 Go NVMe minimum. Ni disque SATA, ni eMMC."],
    ["Système et garantie", "Windows 11 Professionnel, licence incluse ; garantie 3 ans "
                            "sur site, pièces et main-d’œuvre."],
]

MOD_HEADERS = ["Gamme", "Constructeur", "Modèle", "Plateforme", "Prix livré", "Fiche"]
MOD_WIDTHS = [2.35, 2.5, 4.3, 2.15, 4.4, 1.3]
MOD_ROWS = [
    ["Entrée de gamme", "HP", "Pro 400 G9 SFF", "Intel", 943.61, "o",
     "https://www.amazon.fr/dp/B0D4F6739P"],
    ["Entrée de gamme", "HP", "ProDesk 2 G1a (tour)", "AMD", 834.19, "o",
     "https://www.amazon.fr/dp/B0FR3R6P42"],
    ["Entrée de gamme", "Lenovo", "ThinkCentre M70q Gen 5", "Intel", 840.00, "o",
     "https://www.amazon.fr/dp/B0CR1YQ87P"],
    ["Entrée de gamme", "Lenovo", "ThinkCentre M75q Gen 5", "AMD", 849.00, "o",
     "https://www.cdiscount.com/Informatique/achat-pc-ordinateur/"
     "lenovo-thinkcentre-m75q-gen-5/f-1070853-aabod39488.html"],
    ["Standard entreprise", "HP", "Elite 800 G9 Mini", "Intel", 1055.99, "v",
     "https://www.amazon.fr/dp/B0D76M6T6R"],
    ["Standard entreprise", "Lenovo", "ThinkCentre M75q Gen 5", "AMD", 1112.92, "v",
     "https://www.cdiscount.com/informatique/achat-pc-ordinateur/mini-pc-lenovo/"
     "f-1070853-aabtn40622.html"],
    ["Confort", "Dell", "Pro Micro QCM1250 — 32 Go / 1 To", "Intel", None, "b",
     "https://www.dell.com/fr-fr/search/dell%20pro%20micro%20qcm1250"],
    ["Confort", "Lenovo", "ThinkCentre M75t Gen 5 — 32 Go / 1 To", "AMD", None, "b",
     "https://www.lenovo.com/fr/fr/search?text=ThinkCentre%20M75t%20Gen%205"],
]


# --------------------------------------------------------------------------- #
def build_doc():
    doc = Doc(
        base=BASE,
        title="ADCHIM — l’essentiel à retenir",
        subtitle="Trois gammes, un standard, un cahier des charges",
        meta=[],
        doc_ref="ADCHIM · standardisation des postes fixes · novembre 2026",
        footer="GED-SERVICES · ADCHIM · standard des postes fixes · novembre 2026",
    )

    band(doc, "ADCHIM · standardisation des postes fixes · novembre 2026",
         "1. L’essentiel à retenir",
         "Cinq points pour décider. S’il n’y avait qu’un tableau à consulter, ce serait "
         "celui-ci.")

    # ------------------------------------------------------------------ 1.1
    sous_titre(doc, "1.1  Un standard, trois gammes")
    doc.p("Un profil de poste ciblé pour tous, mais une évaluation par usage, sur trois "
          "étages. Le standard entreprise est la cible ; l’entrée de gamme est analysée pour "
          "illustration ; le confort reste à chiffrer.")

    fmt = {(0, 1): {"bg": ORANGE, "color": ORANGE_T, "b": True},
           (0, 2): {"bg": VERT, "color": VERT_T, "b": True},
           (0, 3): {"bg": BLEU_F, "color": BLEU_T, "b": True}}
    doc.table(GAMMES_HEADERS, GAMMES_ROWS, GAMMES_WIDTHS, font=8.6,
              aligns=["l", "l", "l", "l"], first_col_bold=True, header_bg=BLEU,
              zebra=False, cell_fmt=fmt,
              caption="Vert : la cible retenue. Orange : illustration, hors cible. Bleu : "
                      "à chiffrer avant toute commande.")

    # ------------------------------------------------------------------ 1.2
    doc.spacer(0.4)
    sous_titre(doc, "1.2  Exigences transverses")
    doc.p("Elles ne se renégocient pas d’une gamme à l’autre : une offre qui ne les tient "
          "pas ne s’instruit pas, quelle que soit sa remise.")
    doc.table(EXIG_HEADERS, EXIG_ROWS, EXIG_WIDTHS, font=8.9,
              aligns=["l", "l"], first_col_bold=True, header_bg=BLEU)

    # ------------------------------------------------------------------ 1.3
    doc.pagebreak()
    sous_titre(doc, "1.3  Modèles de référence, par gamme")
    doc.p("Modèles ciblés sur chaque gamme, à titre indicatif. Prix livrés, TTC, écran et "
          "clavier exclus ; FCFA au taux de 655,957. Les prix sont des relevés de marché de "
          "novembre 2026, hors remise constructeur : seul un devis fait foi.")

    cells, greens, body = {}, {}, []
    for i, (gamme, constr, modele, voie, prix, st, url) in enumerate(MOD_ROWS):
        if st == "v":
            greens[i] = VERT
            cells[(i, 0)] = {"color": VERT_T, "b": True}
        elif st == "o":
            cells[(i, 0)] = {"color": ORANGE_T}
        else:
            cells[(i, 0)] = {"color": BLEU_T}
        p = eur(prix) if prix is None else "%s\n%s" % (eur(prix), fcfa(prix))
        label = gamme if (i == 0 or MOD_ROWS[i - 1][0] != gamme) else ""
        body.append([label, constr, modele, voie, p, "[fiche](%s)" % url])
    doc.table(MOD_HEADERS, body, MOD_WIDTHS, font=8.6,
              aligns=["l", "l", "l", "c", "r", "c"], first_col_bold=True, header_bg=BLEU,
              row_bg=greens, cell_fmt=cells,
              caption="Deux sources par gamme : Intel chez HP ou Dell, AMD chez Lenovo. "
                      "Les quatre modèles d’entrée de gamme restent cités pour mémoire.")

    # ------------------------------------------------------------------ à retenir
    doc.spacer(0.5)
    sous_titre(doc, "Les cinq points, en clair")
    doc.ul([
        "**Un standard, trois gammes.** L’accueil, la bureautique soutenue, les usages "
        "lourds : un poste par usage, pas un poste pour tous.",
        "**Le standard du parc :** Lenovo ThinkCentre M75q Gen 5 en AMD, **1 112,92 €**, "
        "avec le HP Elite 800 G9 Mini à **1 055,99 €** comme seconde source.",
        "**L’entrée de gamme :** M75q Gen 5 à **849,00 €** ou M70q Gen 5 à **840,00 €** — "
        "même châssis, un seul jeu de pièces détachées.",
        "**La mémoire :** 16 Go livrés ; 32 Go pour ≈ 250 € de plus, soit **1 362,92 €** "
        "par poste — le seul arbitrage technique qui reste.",
        "**Le confort n’est pas chiffré.** Deux configurations conformes existent au "
        "catalogue ; aucune offre relevée ne tient l’enveloppe. Pas de commande avant devis.",
    ])

    doc.spacer(0.45)
    doc.callout(
        "Décision sollicitée",
        "Valider les trois profils et leurs enveloppes ; retenir le M75q Gen 5 en AMD comme "
        "standard du parc, avec l’Elite 800 G9 Mini en seconde source ; arrêter la mémoire en "
        "1 × 16 Go, les 32 Go en option chiffrée ; ne passer commande qu’au vu des devis.",
        kind="warn")

    doc.spacer(0.2)
    doc.p("Joël MBA OYONE — GED-SERVICES, services informatiques · novembre 2026",
          small=True)

    return doc.save(OUTDIR)


if __name__ == "__main__":
    print(build_doc())
