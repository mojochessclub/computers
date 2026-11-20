# -*- coding: utf-8 -*-
"""ADCHIM — Infra_Serveur : briques communes aux deux documents (essentiel et dossier).

Reprend la charte des documents « postes fixes » : bandeau, titres de tableau numérotés,
codes couleur vert / orange / rouge / gris, montants FCFA calculés.
"""
from __future__ import annotations

from docx.shared import Pt as DPt, RGBColor as DRGB
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

from render import HLine, hexc
from render import _rich_pdf as _rich

TVA = 655.957

VERT = "D8EDCB"
VERT_T = "1E6B33"
ORANGE = "FAEBB8"
ORANGE_T = "7A5E12"
ROUGE = "F8CDB6"
ROUGE_T = "9B2C12"
GRIS = "E9EBEF"
GRIS_T = "4A5058"
BLEU_F = "DCE6F2"
BLEU = "1F3B63"

FMT = {"v": (VERT, VERT_T), "o": (ORANGE, ORANGE_T),
       "r": (ROUGE, ROUGE_T), "n": (GRIS, GRIS_T),
       "b": (BLEU_F, BLEU)}


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


def eur0(x):
    """Montant rond, sans décimales (repères de budget)."""
    return _grp(int(round(x))) + "\u00A0€"


def fcfa(x, decimals=False):
    if x is None:
        return "—"
    n = int(round(x * TVA))
    if decimals:
        return _grp(n) + "\u00A0FCFA"
    return _grp(n) + "\u00A0FCFA"


def mfcfa(x):
    """Millions de FCFA, pour les ordres de grandeur."""
    m = x * TVA / 1e6
    return ("%.1f" % m).replace(".", ",") + "\u00A0M FCFA"


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


def sous_titre(doc, text, niveau=1):
    """Titre de section alimentant le signet PDF (niveau 1 par défaut)."""
    p = doc.doc.add_heading(text, level=2 if niveau == 2 else 1)
    for r in p.runs:
        r.font.size = DPt(12.5 if niveau == 2 else 15)
    style = "h2" if niveau == 2 else "h1"
    doc.story.append(Paragraph(_rich(text), ParagraphStyle(style, parent=doc.ps[style])))


def tab_titre(doc, num, titre):
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
        spaceBefore=6, spaceAfter=3, keepWithNext=1)))


def legende(doc, texte):
    doc.p(texte, small=True, italic=True)
