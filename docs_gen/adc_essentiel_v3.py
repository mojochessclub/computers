# -*- coding: utf-8 -*-
"""ADCHIM — « L'essentiel à retenir » (version 3) : synthèse de deux pages.

Vocabulaire de la version longue du courriel, sans les marques d'un message.
Trois tableaux numérotés (TAB-01 à TAB-03), codes couleur, décision sollicitée.
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
BASE = "ADC_Essentiel_a_retenir_v3_2026-11-19"

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
    r.font.size = DPt(20)
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
        "bti", fontName="DJ-B", fontSize=20, leading=24, textColor=hexc(BLEU),
        spaceAfter=3)))
    doc.story.append(Paragraph(subtitle, ParagraphStyle(
        "bsu", fontName="DJ", fontSize=10.5, leading=14.5, textColor=hexc(GRIS_T),
        spaceAfter=6)))
    doc.story.append(HLine())


def sous_titre(doc, text):
    """Sous-titre qui alimente le signet PDF au premier niveau (pas de h1 préalable)."""
    p = doc.doc.add_heading(text, level=2)
    for r in p.runs:
        r.font.size = DPt(12.5)
    st = ParagraphStyle("h1", parent=doc.ps["h2"])
    doc.story.append(Paragraph(_rich(text), st))


def tab_titre(doc, num, titre):
    """Intitulé de tableau placé au-dessus de celui-ci."""
    d = doc.doc
    p = d.add_paragraph()
    r = p.add_run("%s — %s" % (num, titre))
    r.bold = True
    r.font.size = DPt(8.5)
    r.font.color.rgb = DRGB.from_string(BLEU)
    p.paragraph_format.space_before = DPt(6)
    p.paragraph_format.space_after = DPt(2)
    p.paragraph_format.keep_with_next = True
    doc.story.append(Paragraph("%s — %s" % (num, titre), ParagraphStyle(
        "tab", fontName="DJ-B", fontSize=8.4, leading=11, textColor=hexc(BLEU),
        spaceBefore=4, spaceAfter=3, keepWithNext=1)))


# --------------------------------------------------------------------------- #
PROFIL_HEADERS = ["Critère", "Entrée de gamme", "Standard entreprise", "Confort"]
PROFIL_WIDTHS = [2.6, 4.75, 5.05, 4.7]
PROFIL_ROWS = [
    ["Statut", "Illustration : pas notre cible",
     "**La cible : standard du parc**", "À chiffrer sur devis"],
    ["Usage", "Bureautique légère :\nAccueil, saisie, consultation",
     "Bureautique soutenue :\ncommerciaux, comptabilité, transit",
     "Usages plus lourds :\nCalculs lourds, CAO légère, au cas où"],
    ["Processeur",
     "**Intel i5-13500 / 13500T** — 13ᵉ gén., 2023\n**AMD** Ryzen 5 8500G — Zen 4, 2024",
     "**Intel i5-14500 / 14500T** — 14ᵉ gén., 2024\n**AMD** Ryzen 7 8700G — Zen 4, "
     "2024\n**AMD** Ryzen 7 PRO 8700GE",
     "**Intel i7-14700** — 14ᵉ gén., 2024\n**AMD** Ryzen 7 8700G · 9700X — "
     "Zen 4 / 5\n**AMD** Ryzen 7 PRO 8700GE"],
    ["Mémoire", "16 Go minimum livrés\n1 × 16 Go en simple canal toléré",
     "16 Go minimum livrés\n**32 Go préférés**, en 2 × 16 Go, double canal (débit et "
     "évolutivité)",
     "**32 Go en cible**, ≥ 2 emplacements"],
    ["Stockage", "SSD 512 Go NVMe", "SSD 512 Go NVMe", "SSD 512 Go à 1 To NVMe"],
    ["Châssis", "Tous châssis éligibles :\nMFF / Mini, SFF, tour",
     "Mini ou SFF ; tour si une extension PCIe est prévue",
     "Tour de préférence ; SFF possible sous réserve de compatibilité avec la carte "
     "graphique envisagée"],
    ["Enveloppe", "**650 – 850 €**", "**850 – 1 200 €**", "**1 200 – 1 350 €**"],
]

EXIG_HEADERS = ["Exigence", "Ce qu’elle impose, quelle que soit la gamme"]
EXIG_WIDTHS = [3.2, 13.9]
EXIG_ROWS = [
    ["Mémoire", "16 Go minimum **livrés** ; extension à 32 Go pour ≈ 250 €, selon la "
                "gamme. Le double canal (2 × 16 Go) est à privilégier pour le débit et "
                "l’évolutivité."],
    ["Processeur", "**Intel** 13ᵉ génération minimum (2023) ; **AMD** Ryzen 5 8500G / "
                   "8600G (Zen 4) minimum. Rien en dessous."],
    ["Stockage", "SSD 512 Go NVMe minimum. Ni disque SATA, ni eMMC."],
    ["Système et garantie", "Windows 11 Professionnel, licence incluse ; garantie 3 ans "
                            "sur site, pièces et main-d’œuvre."],
]

MOD_HEADERS = ["Gamme", "Constructeur", "Modèle", "Plateforme",
               "Prix catalogue relevé", "Fiche"]
MOD_WIDTHS = [2.2, 2.55, 4.35, 2.05, 4.6, 1.3]
MOD_ROWS = [
    ["Entrée de gamme", "HP", "Pro 400 G9 SFF\n(référence comparative : prix supérieur au plafond)", "Intel", 943.61, "o",
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
        subtitle="Projet d’approvisionnement des postes informatiques",
        meta=[],
        doc_ref="ADCHIM · projet d’approvisionnement des postes · novembre 2026",
        footer="GED-SERVICES · ADCHIM · projet d’approvisionnement des postes · "
               "novembre 2026",
    )

    band(doc, "ADCHIM · projet d’approvisionnement des postes informatiques",
         "L’essentiel à retenir",
         "Synthèse de deux pages : profils, exigences et modèles de référence.")

    doc.p("Cette synthèse présente les principaux éléments à prendre en compte pour "
          "l’approvisionnement des postes informatiques. Elle reprend **cinq grands "
          "critères d’arbitrage** — profils matériels, processeurs, mémoire, stockage et "
          "enveloppes tarifaires — et s’appuie sur une étude comparative portant sur plus "
          "d’une vingtaine de modèles.", small=True)
    doc.p("La **note technique complète**, distincte, constitue la base de travail "
          "comparative : détail des seize références recensées, comparatif des processeurs "
          "Intel et AMD, formats de châssis et arbitrage mémoire. Elle apporte les "
          "précisions absentes de cette synthèse : réserves, écarts constatés, options et "
          "éléments de justification.", small=True)

    # ------------------------------------------------------------------ 1
    doc.spacer(0.12)
    sous_titre(doc, "1.  Les enveloppes tarifaires")
    doc.ul([
        "Les trois tranches (**650–850 €, 850–1 200 €, 1 200–1 350 €**) ne sont pas des "
        "orientations budgétaires prédéfinies, ni définitives a priori.",
        "Elles ont été établies dans l’ordre inverse : à partir des configurations "
        "techniques de chaque niveau d’usage, puis des prix catalogues relevés sur le "
        "marché français en novembre 2026.",
        "Ces montants sont indicatifs et destinés à faciliter les arbitrages, techniques "
        "comme budgétaires ; ils restent à confirmer après consultation. L’enveloppe "
        "découle du profil technique, et non l’inverse.",
    ], small=True)

    # ------------------------------------------------------------------ 2
    doc.spacer(0.12)
    sous_titre(doc, "2.  Les comparaisons et le code couleur")
    doc.ul([
        "L’étude s’est concentrée sur **HP, Lenovo et Dell**, en plateformes **Intel et "
        "AMD**, à partir des caractéristiques techniques et des prix catalogues "
        "disponibles.",
        "Les prix relevés constituent des **repères de marché** ; seul un devis "
        "fournisseur permet de confirmer les conditions commerciales.",
        "**Code couleur** — vert : retenu ; orange : illustration ou vérification "
        "nécessaire ; rouge : hors profil ou hors enveloppe ; gris : référence de prix.",
    ], small=True)

    # ------------------------------------------------------------------ 3
    doc.spacer(0.05)
    sous_titre(doc, "3.  L’essentiel à retenir, en trois volets")
    doc.p("Les trois tableaux ci-dessous récapitulent les profils, les exigences et les "
          "modèles. La gamme **Standard entreprise** est la cible du parc.", small=True)

    doc.h2("3.1  Profils matériels retenus, en trois gammes")
    tab_titre(doc, "TAB-01", "Profils matériels cibles et enveloppes tarifaires par gamme")
    fmt = {(0, 1): {"bg": ORANGE, "color": ORANGE_T, "b": True},
           (0, 2): {"bg": VERT, "color": VERT_T, "b": True},
           (0, 3): {"bg": BLEU_F, "color": BLEU_T, "b": True}}
    doc.table(PROFIL_HEADERS, PROFIL_ROWS, PROFIL_WIDTHS, font=7.5,
              aligns=["l", "l", "l", "l"], first_col_bold=True, header_bg=BLEU,
              zebra=False, cell_fmt=fmt)

    doc.pagebreak()
    doc.h2("3.2  Exigences transverses")
    doc.p("**Critères transverses non négociables, quelle que soit la gamme** : toute "
          "offre ne respectant pas ces exigences minimales est écartée, quel que soit le "
          "niveau de remise proposé.", small=True)
    tab_titre(doc, "TAB-02",
              "Exigences techniques transverses et minimales du parc informatique")
    doc.table(EXIG_HEADERS, EXIG_ROWS, EXIG_WIDTHS, font=8.2,
              aligns=["l", "l"], first_col_bold=True, header_bg=BLEU)

    doc.spacer(0.25)
    doc.h2("3.3  Modèles de référence, par gamme")
    doc.p("Les références présentées ne constituent pas une liste restrictive. Elles "
          "permettent de disposer de points de comparaison concrets, avec accès direct aux "
          "fiches des modèles recensés.", small=True)
    tab_titre(doc, "TAB-03",
              "Références de matériels recensées et comparatif tarifaire par gamme")

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
    doc.table(MOD_HEADERS, body, MOD_WIDTHS, font=7.7,
              aligns=["l", "l", "l", "c", "r", "c"], first_col_bold=True, header_bg=BLEU,
              row_bg=greens, cell_fmt=cells)

    doc.p("Deux sources par gamme, en Intel et en AMD ; les quatre modèles d’entrée de "
          "gamme restent cités pour mémoire. Prix relevés en novembre 2026, hors écran et "
          "clavier, sous réserve des conditions de livraison, de fiscalité et des remises "
          "commerciales.", small=True, italic=True)

    # ------------------------------------------------------------------ clôture
    doc.spacer(0.25)
    doc.callout(
        "Décision sollicitée",
        "Valider les trois profils et leurs enveloppes ; retenir le ThinkCentre M75q "
        "Gen 5 en AMD comme standard du parc, avec l’Elite 800 G9 Mini en seconde source ; "
        "arrêter la mémoire en 1 × 16 Go, les 32 Go en option chiffrée ; ne passer commande "
        "qu’au vu des devis.", kind="warn")

    doc.spacer(0.15)
    doc.p("Joël MBA OYONE — GED-SERVICES, services informatiques · novembre 2026",
          small=True)

    return doc.save(OUTDIR)


if __name__ == "__main__":
    print(build_doc())
