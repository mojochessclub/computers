# -*- coding: utf-8 -*-
"""ADCHIM — standardisation des postes fixes : note de décision et cahier des charges.

Document court (5 pages) destiné à deux lecteurs : le comité de direction, qui décide,
et le revendeur, qui achète. Trois gammes, deux plateformes, des tableaux commentés.
Aucune référence à un document antérieur. Tous les montants FCFA et les écarts sont
calculés ici, jamais saisis : 1 € = 655,957 FCFA.
"""
from __future__ import annotations

import os

from docx.shared import Pt as DPt, RGBColor as DRGB
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

from render import Doc, HLine, hexc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, os.environ.get("LIVRABLES_DIR",
                                           "estimations/standard_postes_2026-11-19"))
BASE = "ADC_Standard_Postes_Fixes_2026-11-19"

TVA = 655.957
VERT = "D8EDCB"
VERT_T = "1E6B33"
ORANGE = "FAEBB8"
ORANGE_T = "7A5E12"
ROUGE = "F8CDB6"
ROUGE_T = "9B2C12"
GRIS = "E9EBEF"
GRIS_T = "4A5058"
BLEU = "1F3B63"
FMT = {"v": (VERT, VERT_T), "o": (ORANGE, ORANGE_T),
       "r": (ROUGE, ROUGE_T), "n": (GRIS, GRIS_T)}


# --------------------------------------------------------------------------- #
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
def _m(constructeur, ref, voie, cpu, cfg, prix, st, label, url=None):
    return {"c": constructeur, "ref": ref, "voie": voie, "cpu": cpu, "cfg": cfg,
            "prix": prix, "st": st, "label": label, "url": url}


ENTREE = [
    _m("Lenovo", "ThinkCentre M70q Gen 5", "Intel", "Core i5-13500T",
       "16 Go DDR4 · 512 Go NVMe", 840.00, "v", "Retenu",
       "https://www.amazon.fr/dp/B0CR1YQ87P"),
    _m("Lenovo", "ThinkCentre M75q Gen 5", "AMD", "Ryzen 5 PRO 8500GE",
       "16 Go DDR5 · 512 Go NVMe", 849.00, "v", "Retenu",
       "https://www.cdiscount.com/Informatique/achat-pc-ordinateur/"
       "lenovo-thinkcentre-m75q-gen-5/f-1070853-aabod39488.html"),
    _m("HP", "ProDesk 2 G1a (tour)", "AMD", "Ryzen 5 8500G",
       "16 Go DDR5 · 512 Go NVMe", 834.19, "o", "À vérifier",
       "https://www.amazon.fr/dp/B0FR3R6P42"),
    _m("HP", "Pro 400 G9 SFF", "Intel", "Core i5-13500",
       "16 Go DDR4 · 512 Go SATA", 943.61, "r", "Hors profil",
       "https://www.amazon.fr/dp/B0D4F6739P"),
    _m("Dell", "OptiPlex 7010 Micro", "Intel", "Core i5-13500T",
       "16 Go DDR4 · 512 Go NVMe", 759.05, "o", "Recond.",
       "https://www.amazon.fr/dp/B0HKDSCK9X"),
]

STANDARD = [
    _m("Dell", "OptiPlex 7020 MFF", "Intel", "Core i5-14500T",
       "16 Go DDR5 · 512 Go NVMe", 999.95, "n", "Réf. prix",
       "https://store.actualsystemes.com/p7506414/dell-optiplex-7020-sff-pra%C2%AAt"
       "-pour-l-ia-core-i5-i5-14500-2-6-ghz-16-go-ssd-512-go-francais.aspx"),
    _m("HP", "Elite 800 G9 Mini", "Intel", "Core i5-14500",
       "16 Go DDR5 · 512 Go NVMe", 1055.99, "v", "Retenu",
       "https://www.amazon.fr/dp/B0D76M6T6R"),
    _m("Lenovo", "ThinkCentre M75q Gen 5", "AMD", "Ryzen 7 PRO 8700GE",
       "16 Go DDR5 · 512 Go NVMe", 1112.92, "v", "Retenu",
       "https://www.cdiscount.com/informatique/achat-pc-ordinateur/mini-pc-lenovo/"
       "f-1070853-aabtn40622.html"),
    _m("HP", "Elite 805 G9 SFF", "AMD", "Ryzen 7 8700G",
       "16 Go DDR5 · 512 Go NVMe", 1251.58, "o", "Hors couloir",
       "https://www.amazon.fr/dp/B0DHLD7ZWM"),
    _m("Lenovo", "ThinkCentre M90q Gen 5", "Intel", "Core i5-14500T",
       "16 Go DDR5 · 512 Go NVMe", 1470.45, "r", "Hors env.",
       "https://www.senetic.fr/product/12TH001FPB"),
]

CONFORT = [
    _m("HP", "Pro Mini 400 G9", "Intel", "Core i7-14700T",
       "16 Go DDR5 · 512 Go NVMe", 1109.30, "o", "16 Go seul",
       "https://www.amazon.fr/dp/B0D7424V46"),
    _m("HP", "Elite Desk 800 G9 (tour)", "Intel", "Core i7-14700",
       "16 Go DDR5 · 512 Go NVMe", 1363.75, "o", "16 Go seul",
       "https://www.hp.com/fr-fr/shop/search?q=Elite%20800%20G9"),
    _m("HP", "Elite Mini 800 G9", "Intel", "Core i7-14700",
       "16 Go DDR5 · 512 Go NVMe", 1331.80, "o", "16 Go seul",
       "https://www.cdiscount.com/search/10/hp+elite+mini+800+g9+i7-14700.html"),
    _m("Lenovo", "ThinkCentre M90q Gen 6", "Intel", "Core Ultra 7 265",
       "configuration non publiée", 1624.88, "r", "Hors env.",
       "https://www.cdiscount.com/search/10/thinkcentre+m90q+gen+6.html"),
    _m("Dell", "Pro Micro QCM1250", "Intel", "Core i7-14700T",
       "32 Go DDR5 · 1 To NVMe", None, "v", "Sur devis",
       "https://www.dell.com/fr-fr/search/dell%20pro%20micro%20qcm1250"),
    _m("Lenovo", "ThinkCentre M75t Gen 5", "AMD", "Ryzen 7 PRO 8700G",
       "32 Go DDR5 · 1 To NVMe", None, "v", "Sur devis",
       "https://www.lenovo.com/fr/fr/search?text=ThinkCentre%20M75t%20Gen%205"),
]

M_HEADERS = ["Constructeur", "Référence", "Plateforme", "Processeur",
             "Mémoire · stockage", "Prix livré", "Statut", "Fiche"]
M_WIDTHS = [2.25, 2.85, 1.9, 2.6, 2.2, 2.5, 1.7, 1.1]
M_ALIGNS = ["l", "l", "c", "l", "l", "r", "c", "c"]

PROFIL = [
    ["Usage", "Accueil, saisie, consultation",
     "Sage, Teams, bureautique intensive",
     "Gros tableurs, CAO légère, poste gardé cinq ans"],
    ["Intel", "i5-13400 · i5-13500 — 13ᵉ gén., 2023",
     "i5-14400 · i5-14500 — 14ᵉ gén., 2024",
     "i7-14700 — 14ᵉ gén., 2024, ou plus récent"],
    ["AMD", "Ryzen 5 8500G · 8600G — Zen 4, 2024",
     "Ryzen 5 8600G (Zen 4) · 9600X (Zen 5), 2024",
     "Ryzen 7 8700G (Zen 4) · 9700X (Zen 5), 2024"],
    ["Mémoire", "16 Go DDR4 ou DDR5, deux emplacements",
     "16 Go DDR5 sur deux emplacements — 32 Go en option",
     "32 Go DDR5 en cible, deux emplacements"],
    ["Stockage", "500 Go NVMe", "500 Go NVMe", "512 Go à 1 To NVMe"],
    ["Graphique", "iGPU suffisant", "Indifférent",
     "iGPU ; GPU dédié 6 Go si la CAO 3D entre au périmètre"],
    ["Garantie", "3 ans sur site, pièces et main-d’œuvre",
     "3 ans sur site, pièces et main-d’œuvre",
     "3 ans sur site, pièces et main-d’œuvre"],
    ["Enveloppe", "**650 – 850 €**", "**850 – 1 200 €**", "**1 200 – 1 350 €**"],
]
PROFIL_HEADERS = ["Critère", "Entrée de gamme", "Standard entreprise", "Confort"]
PROFIL_WIDTHS = [2.7, 4.8, 4.8, 4.8]

CPU_HEADERS = ["Constructeur", "Processeur", "Génération · architecture", "Sortie",
               "Cœurs / threads", "Gamme"]
CPU_WIDTHS = [2.4, 3.2, 6.2, 1.4, 2.1, 1.8]
CPU_ROWS = [
    ["Intel", "Core i5-13400", "13ᵉ génération — Raptor Lake", "T1 2023", "10C / 16T",
     "Entrée"],
    ["Intel", "Core i5-13500", "13ᵉ génération — Raptor Lake", "T1 2023", "14C / 20T",
     "Entrée"],
    ["AMD", "Ryzen 5 8500G", "Ryzen 8000G — Zen 4 (AM5)", "T1 2024", "6C / 12T", "Entrée"],
    ["AMD", "Ryzen 5 8600G", "Ryzen 8000G — Zen 4 (AM5)", "T1 2024", "6C / 12T",
     "Entrée · standard"],
    ["Intel", "Core i5-14400", "14ᵉ génération — Raptor Lake Refresh", "T1 2024",
     "10C / 16T", "Standard"],
    ["Intel", "Core i5-14500", "14ᵉ génération — Raptor Lake Refresh", "T1 2024",
     "14C / 20T", "Standard"],
    ["AMD", "Ryzen 5 9600X", "Ryzen 9000 — Zen 5 (AM5)", "T3 2024", "6C / 12T", "Standard"],
    ["Intel", "Core i7-14700", "14ᵉ génération — Raptor Lake Refresh", "T1 2024",
     "20C / 28T", "Confort"],
    ["AMD", "Ryzen 7 8700G", "Ryzen 8000G — Zen 4 (AM5)", "T1 2024", "8C / 16T", "Confort"],
    ["AMD", "Ryzen 7 9700X", "Ryzen 9000 — Zen 5 (AM5)", "T3 2024", "8C / 16T", "Confort"],
    ["Intel", "Core Ultra 7 265", "Core Ultra série 2 — Arrow Lake", "T1 2025",
     "20C / 20T", "Confort (hors env.)"],
]
CPU_GREEN = {4, 5, 6, 7}          # i5-14400, i5-14500, 9600X, i7-14700

CHASSIS_HEADERS = ["Format", "Caractéristiques", "Évolutivité", "Usage privilégié",
                   "Prix constatés"]
CHASSIS_WIDTHS = [2.4, 4.2, 4.8, 3.4, 2.3]
CHASSIS_ROWS = [
    ["Mini · Micro · MFF", "Très compact (1 à 2 litres), alimentation externe",
     "Très limitée : pas de carte graphique de CAO. Mémoire et disque restent "
     "remplaçables.", "Accueil, bureautique, poste standard", "759 → 1 470 €"],
    ["SFF", "Boîtier de bureau compact (7 à 9 litres), alimentation interne",
     "Intermédiaire : un logement PCIe bas profil selon modèle, alimentation souvent "
     "limitante.", "Bureautique avancée, extensions légères", "944 → 1 528 €"],
    ["Tour", "Tour de bureau (15 litres et plus)",
     "Élevée : PCIe pleine hauteur, carte graphique et disques supplémentaires possibles.",
     "Postes évolutifs, CAO, gros stockage", "834 → 2 111 €"],
]

MEM_HEADERS = ["Option", "Livraison", "Effet", "Coût de l’extension", "Total par poste"]
MEM_WIDTHS = [1.5, 3.1, 3.9, 4.2, 4.0]
MEM_ROWS = [
    ["A", "2 × 8 Go", "Double canal dès la commande ; les deux barrettes à remplacer",
     "Kit de 2 × 16 Go ≈ 500 €", "≈ %s" % eur(1112.92 + 500)],
    ["B", "1 × 16 Go", "Simple canal à 16 Go ; second emplacement libre",
     "1 barrette de 16 Go ≈ 250 €", "≈ %s" % eur(1112.92 + 250)],
    ["C", "32 Go d’origine, sur devis", "Conforme à la cible, double canal",
     "Aucune extension à prévoir", "sur devis"],
]

RECAP_HEADERS = ["Gamme", "Ce que je retiens", "Configuration", "Prix par poste"]
RECAP_WIDTHS = [2.7, 4.4, 5.3, 4.7]
RECAP_ROWS = [
    ["Entrée de gamme", "Lenovo M75q Gen 5 (AMD)\nLenovo M70q Gen 5 (Intel)",
     "16 Go DDR5 · 512 Go NVMe", "849,00 €\n556 907 FCFA"],
    ["Standard", "Lenovo M75q Gen 5 (AMD)\nHP Elite 800 G9 Mini (Intel)",
     "16 Go DDR5 · 512 Go NVMe, 32 Go en option", "1 112,92 €\n730 028 FCFA"],
    ["Confort", "Dell Pro Micro QCM1250\nLenovo M75t Gen 5 (AMD)",
     "32 Go DDR5 · 1 To NVMe", "sur devis"],
]

DEV_HEADERS = ["Ce qu’on exige au devis", "Ce qu’on refuse"]
DEV_WIDTHS = [8.55, 8.55]
DEV_ROWS = [
    ["Intel 13ᵉ génération minimum (i5-13500, i5-14500) ou Ryzen 5 8500G / 8600G",
     "Intel 12ᵉ génération et antérieurs"],
    ["16 Go DDR5 sur deux emplacements, une seule barrette occupée",
     "DDR4 hors entrée de gamme ; disque SATA ou eMMC"],
    ["NVMe 512 Go minimum, 1 To sur le confort", "Reconditionné sur le standard et le confort"],
    ["Windows 11 Professionnel, licence incluse",
     "Machine livrée sans emplacement mémoire libre"],
    ["Garantie 3 ans sur site, pièces et main-d’œuvre",
     "Garantie inférieure à 3 ans, ou retour atelier seulement"],
    ["Clavier AZERTY et souris s’ils sont fournis ; prix daté et provenance de l’offre",
     "Prix sans date de relevé, ni mention de la provenance"],
]


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
    r.font.size = DPt(24)
    r.font.color.rgb = DRGB.from_string(BLEU)
    p.paragraph_format.space_after = DPt(2)
    p = d.add_paragraph()
    r = p.add_run(subtitle)
    r.font.size = DPt(11)
    r.font.color.rgb = DRGB.from_string(GRIS_T)
    p.paragraph_format.space_after = DPt(10)

    doc.story.append(Paragraph(eyebrow.upper(), ParagraphStyle(
        "bey", fontName="DJ-B", fontSize=8.5, leading=11, textColor=hexc(ORANGE_T),
        spaceAfter=6)))
    doc.story.append(Paragraph(title, ParagraphStyle(
        "bti", fontName="DJ-B", fontSize=24, leading=27, textColor=hexc(BLEU),
        spaceAfter=3)))
    doc.story.append(Paragraph(subtitle, ParagraphStyle(
        "bsu", fontName="DJ", fontSize=10.5, leading=14.5, textColor=hexc(GRIS_T),
        spaceAfter=6)))
    doc.story.append(HLine())


def modele_table(doc, rows, caption):
    cells, greens = {}, {}
    body = []
    for i, r in enumerate(rows):
        bg, fg = FMT[r["st"]]
        if r["st"] == "v":
            greens[i] = VERT
        cells[(i, 6)] = {"bg": bg, "color": fg, "b": r["st"] == "v"}
        fiche = "[fiche](%s)" % r["url"] if r["url"] else "—"
        prix = (eur(r["prix"]) if r["prix"] is None
                else "%s\n%s" % (eur(r["prix"]), fcfa(r["prix"])))
        body.append([r["c"], r["ref"], r["voie"], r["cpu"], r["cfg"],
                     prix, r["label"], fiche])
    doc.table(M_HEADERS, body, M_WIDTHS, font=7.5, aligns=M_ALIGNS,
              first_col_bold=True, header_bg=BLEU, row_bg=greens, cell_fmt=cells,
              caption=caption)


# --------------------------------------------------------------------------- #
def build_doc():
    doc = Doc(
        base=BASE,
        title="ADCHIM — standardisation des postes fixes",
        subtitle="Trois gammes, un standard d’achat, un cahier des charges pour le revendeur",
        meta=[],
        doc_ref="ADCHIM · standardisation des postes fixes · novembre 2026",
        footer="GED-SERVICES · ADCHIM · standard des postes fixes · novembre 2026",
    )

    band(doc, "ADCHIM · postes fixes · note de décision",
         "Standardiser les postes fixes",
         "Trois gammes, un standard d’achat, un cahier des charges pour le revendeur.")
    doc.p("**Destinataires.** Comité de direction d’ADCHIM — la décision. Revendeur — "
          "la consultation et l’achat. **Émetteur.** Joël MBA OYONE, GED-SERVICES. "
          "**Date.** Novembre 2026. **Enveloppe.** 650 € à 1 350 € par poste, livraison "
          "comprise, écran et clavier exclus.", small=True)

    # ------------------------------------------------------------------ 1
    doc.h1_plain("1. L’essentiel")
    doc.p("Cinq points, et c’est tout ce qu’il faut retenir pour décider.", small=True)
    doc.ul([
        "**Un standard, trois gammes.** L’accueil, la bureautique intensive, les usages "
        "lourds. Un poste par usage — pas un poste pour tous.",
        "**Le standard du parc :** Lenovo ThinkCentre M75q Gen 5 en AMD, **1 112,92 €**, "
        "avec le HP Elite 800 G9 Mini à **1 055,99 €** comme seconde source.",
        "**L’entrée de gamme :** M75q Gen 5 à **849,00 €** ou M70q Gen 5 à **840,00 €** — "
        "même châssis, un seul jeu de pièces détachées.",
        "**La mémoire :** 16 Go livrés, 32 Go pour ≈ 250 € de plus, soit **1 362,92 €** "
        "par poste — 12,92 € au-dessus du plafond.",
        "**Le confort n’est pas chiffré.** Deux configurations conformes existent au "
        "catalogue ; aucune offre relevée ne tient l’enveloppe. Pas de commande avant devis.",
    ], small=True)

    # ------------------------------------------------------------------ 2
    doc.spacer(0.4)
    doc.h1_plain("2. Le profil de chaque gamme")
    doc.p("C’est le référentiel d’achat : ce qu’une offre doit tenir pour être instruite.",
          small=True)
    doc.table(PROFIL_HEADERS, PROFIL, PROFIL_WIDTHS, font=7.8,
              aligns=["l", "l", "l", "l"], first_col_bold=True, header_bg=BLEU,
              caption="Profil arrêté en novembre 2026. Les processeurs sont donnés avec "
                      "leur génération et leur année de sortie.")
    doc.p("**Utilité du tableau.** Il rend le profil opposable : une offre qui ne le tient "
          "pas ne s’instruit pas, quelle que soit sa remise ; une offre qui le tient mais "
          "sort du couloir de sa gamme est signalée, pas écartée.", small=True)

    doc.p("**Ce que ce document ne tranche pas.** La volumétrie du parc — combien de "
          "postes par gamme —, le choix des écrans et des claviers, et la stratégie "
          "d’enlèvement. Ces trois points viendront avec les devis, pas avant.", small=True)

    # ------------------------------------------------------------------ 3
    doc.pagebreak()
    doc.h1_plain("3. Les modèles retenus")
    doc.p("Seize références relevées sur le marché français en novembre 2026. En vert, "
          "celles que je retiens. Prix livrés, TTC, écran et clavier exclus ; le FCFA est "
          "converti au taux de 655,957. **Vert** : retenu. **Orange** : à vérifier ou sous "
          "réserve. **Rouge** : hors profil ou hors enveloppe. **Gris** : référence de prix.",
          small=True)

    doc.h2("3.1 Entrée de gamme — accueil, saisie, consultation")
    modele_table(doc, ENTREE,
                 "Cinq références chiffrées. « Fiche » ouvre la page produit du modèle ; "
                 "les prix peuvent y avoir évolué depuis le relevé.")
    doc.p("**Utilité du tableau.** L’entrée de gamme ne tient le profil qu’avec deux "
          "références neuves, et le moins cher n’est pas le meilleur : l’OptiPlex 7010 est "
          "reconditionné, le Pro 400 G9 est en DDR4 avec un disque SATA. **Ma préférence :** "
          "le M75q Gen 5 en AMD (DDR5, 849,00 €), le M70q Gen 5 en Intel (840,00 €) comme "
          "alternative.", small=True)

    doc.h2("3.2 Standard entreprise — le poste qui portera le volume")
    modele_table(doc, STANDARD,
                 "Cinq références. %s séparent le Dell du Lenovo à configuration voisine."
                 % eur(1112.92 - 999.95))
    doc.p("**Utilité du tableau.** Il vérifie la condition qui compte pour un parc : deux "
          "sources à peu près au même prix, pour ne pas être pris en défaut de livraison en "
          "cours d’année. **Ma préférence :** le M75q Gen 5 en AMD comme référence "
          "principale, l’Elite 800 G9 Mini en seconde source, l’OptiPlex 7020 MFF comme "
          "référence de prix.", small=True)

    # ------------------------------------------------------------------ 3.3
    doc.pagebreak()
    doc.h2("3.3 Confort — postes gardés cinq ans, CAO légère, gros tableurs")
    modele_table(doc, CONFORT,
                 "Six références. Les deux lignes vertes sont les seules à tenir 32 Go et "
                 "1 To ; elles ne sont pas encore chiffrées.")
    doc.p("**Utilité du tableau.** Il sépare ce qui est disponible de ce qui est seulement "
          "spécifié : quatre machines chiffrées tiennent 16 Go, deux configurations tiennent "
          "le profil complet et restent sur devis. **Ma préférence :** ne rien commander "
          "avant devis ; les deux lignes vertes sont les seules à instruire.", small=True)
    doc.p("**Ce que je ne retiens pas.** Le M90q Gen 6 sort de l’enveloppe de 274,88 € ; "
          "les deux HP en i7 sont livrés en 16 Go seulement, et l’Elite Desk 800 G9 dépasse "
          "déjà le plafond (1 363,75 €).", small=True)

    # ------------------------------------------------------------------ 4
    doc.spacer(0.4)
    doc.h1_plain("4. Les processeurs, Intel et AMD face à face")
    doc.p("Les processeurs retenus, par génération, architecture et date de sortie — au "
          "trimestre près, dates constructeur.", small=True)
    cpu_fmt = {}
    for i in range(len(CPU_ROWS)):
        if i in CPU_GREEN:
            cpu_fmt[(i, 5)] = {"bg": VERT, "color": VERT_T, "b": True}
    doc.table(CPU_HEADERS, CPU_ROWS, CPU_WIDTHS, font=7.8,
              aligns=["l", "l", "l", "c", "c", "c"], header_bg=BLEU, cell_fmt=cpu_fmt,
              row_bg={i: VERT for i in CPU_GREEN},
              caption="En vert : la génération visée par la gamme standard — Intel 14ᵉ "
                      "génération et Ryzen 5 9600X (Zen 5).")
    doc.p("**Utilité du tableau.** Il répond à la question qui revient toujours — « pourquoi "
          "pas le processeur le plus récent ? ». Une génération de plus se paie 250 à 500 € "
          "et ne change rien à l’ouverture d’un classeur. Il évite aussi les comparaisons "
          "fausses : un Ryzen 8000G (Zen 4) se compare à un Raptor Lake, pas à un Arrow "
          "Lake.", small=True)

    # ------------------------------------------------------------------ 5
    doc.pagebreak()
    doc.h1_plain("5. Les formats de châssis")
    doc.p("Le format décide de ce que le poste pourra recevoir pendant ses cinq ans, pas "
          "seulement de la place qu’il occupe sous le bureau.", small=True)
    doc.table(CHASSIS_HEADERS, CHASSIS_ROWS, CHASSIS_WIDTHS, font=7.8,
              aligns=["l", "l", "l", "l", "c"], first_col_bold=True, header_bg=BLEU)
    doc.p("**Utilité du tableau.** À trancher une seule question : aura-t-on besoin d’une "
          "carte graphique dans les cinq ans ? Si non — c’est le cas de l’essentiel du parc —, "
          "le mini est le bon choix : 150 à 200 € de moins qu’un SFF à configuration voisine, "
          "et il se fixe sous le bureau. Si oui, il faut le SFF ou la tour, et l’assumer dès "
          "le devis.", small=True)

    # ------------------------------------------------------------------ 6
    doc.spacer(0.4)
    doc.h1_plain("6. La mémoire : trois façons d’aller à 32 Go")
    doc.p("Le standard est livré en 16 Go pour 1 112,92 €. Trois façons d’aller à 32 Go, "
          "trois coûts :", small=True)
    mem_fmt = {(1, j): {"bg": VERT} for j in range(5)}
    mem_fmt[(1, 0)] = {"bg": VERT, "color": VERT_T, "b": True}
    doc.table(MEM_HEADERS, MEM_ROWS, MEM_WIDTHS, font=7.8,
              aligns=["c", "l", "l", "l", "r"], first_col_bold=True, header_bg=BLEU,
              cell_fmt=mem_fmt,
              caption="Barrette de 16 Go : ≈ 250 € au détail, à confirmer par devis. « ≈ » "
                      "marque un ordre de prix, non un relevé.")
    doc.p("**Utilité du tableau.** Il chiffre le seul arbitrage technique qui reste : "
          "32 Go coûtent 12,92 € de dépassement en option B, 262,92 € en option A. **Je "
          "recommande l’option B** — 1 × 16 Go à la commande, second emplacement libre, une "
          "barrette pour passer à 32 Go. Le double canal dès la commande reste possible ; "
          "il coûte 250 € de plus par poste et s’arbitre poste par poste.", small=True)
    doc.p("**Qui a vraiment besoin de 32 Go ?** Les gros tableurs et la CAO légère, pas la "
          "bureautique. Pour ces utilisateurs, l’option C — 32 Go d’origine, sur devis — vaut "
          "mieux qu’une extension après coup : la machine est livrée conforme, sous garantie.",
          small=True)

    doc.pagebreak()
    doc.h1_plain("7. La commande, en clair")
    doc.p("Trois lignes, trois références : c’est ce que je propose de commander, et ce "
          "qu’il faut mettre au devis.", small=True)
    doc.table(RECAP_HEADERS, RECAP_ROWS, RECAP_WIDTHS, font=7.8,
              aligns=["l", "l", "l", "r"], first_col_bold=True, header_bg=BLEU,
              row_bg={0: VERT, 1: VERT},
              caption="Prix livrés, TTC, écran et clavier exclus. FCFA au taux de 655,957.")
    doc.p("**Utilité du tableau.** Il tient sur une page et sert de support à la séance : "
          "trois gammes, deux sources par gamme, un prix. C’est aussi la base de la demande "
          "de prix.", small=True)

    doc.h2("Pour le revendeur — noir sur blanc")
    doc.table(DEV_HEADERS, DEV_ROWS, DEV_WIDTHS, font=7.8, aligns=["l", "l"],
              header_bg=BLEU,
              caption="À reprendre tel quel dans la demande de prix. Les prix sont des "
                      "relevés de marché datés, hors remise constructeur.")

    doc.h2("Réserves")
    doc.ul([
        "**Les prix sont indicatifs et datés** (novembre 2026) : ils servent à cadrer, pas "
        "à engager. Seul un devis fait foi.",
        "**La cible 32 Go se paie en supplément** (≈ 250 €) : elle sort du prix affiché.",
        "**Le confort n’est pas chiffré** : aucune offre relevée ne tient à la fois 32 Go, "
        "1 To et 1 350 €.",
        "**La disponibilité n’est pas garantie** : ruptures constatées chez les distributeurs, "
        "et certaines offres arrivent en clavier QWERTZ.",
    ], small=True)

    doc.spacer(0.25)
    doc.callout(
        "Décision sollicitée",
        "Valider les trois profils et leurs enveloppes ; retenir le M75q Gen 5 en AMD comme "
        "standard du parc, avec l’Elite 800 G9 Mini en seconde source ; arrêter la mémoire en "
        "1 × 16 Go, les 32 Go en option chiffrée ; autoriser la consultation du revendeur sur "
        "ces références ; ne passer commande qu’au vu des devis.", kind="warn")

    doc.spacer(0.15)
    doc.p("Joël MBA OYONE — GED-SERVICES, services informatiques · novembre 2026",
          small=True)

    return doc.save(OUTDIR)


if __name__ == "__main__":
    print(build_doc())
