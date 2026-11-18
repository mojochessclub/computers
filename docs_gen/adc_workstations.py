# -*- coding: utf-8 -*-
"""ADCHIM — postes fixes : note d'arbitrage, benchmark Intel / AMD.

Trois gammes (entrée, standard, confort), deux plateformes (Intel depuis la
13e génération, AMD Ryzen), et pour chaque gamme deux références par
constructeur. Les prix sont des relevés du marché français ; là où rien n'a été
trouvé, la ligne le dit et reste « à chiffrer ».
"""
from __future__ import annotations

import os

from render import Doc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, os.environ.get("LIVRABLES_DIR", "estimations/ADC_Workstations 2026-11-18"))
BASE = "ADC_Workstations_2026-11-18_Note_arbitrage_postes_fixes"
TVA = 655.957
DUREE = 5  # durée de détention retenue pour l'obsolescence présumée

V, O, R, N = "v", "o", "r", "n"
FMT = {
    "v": {"bg": "D8EDCB", "color": "1E6B33"},
    "o": {"bg": "FAEBB8", "color": "7A5E12"},
    "r": {"bg": "F8CDB6", "color": "9B2C12"},
    "n": {"bg": "E9EBEF", "color": "4A5058"},
}


def eur(x):
    if x is None:
        return "—"
    ent, dec = ("%.2f" % x).split(".")
    out, i = "", 0
    for ch in reversed(ent):
        if i and i % 3 == 0:
            out = "\u00A0" + out
        out = ch + out
        i += 1
    return out + "," + dec + "\u00A0€"


def fcfa(x):
    if x is None:
        return "—"
    n = "%d" % int(round(x * TVA))
    out, i = "", 0
    for ch in reversed(n):
        if i and i % 3 == 0:
            out = "\u00A0" + out
        out = ch + out
        i += 1
    return out + "\u00A0FCFA"


def fcfa_num(x):
    """Le même nombre, sans l'unité : les colonnes FCFA la portent en en-tête. """
    return fcfa(x).replace("\u00A0FCFA", "")


def _r(constructeur, plateforme, modele, etat, cpu, annee, config, prix, conf,
       commentaire, lien):
    return {"constructeur": constructeur, "plateforme": plateforme, "modele": modele,
            "etat": etat, "cpu": cpu, "annee": annee, "obso": annee + DUREE,
            "config": config, "prix": prix, "conf": conf,
            "commentaire": commentaire, "lien": lien}


# --------------------------------------------------------------------------- #
# ENTRÉE DE GAMME — 16 Go (DDR4 ou DDR5, double canal), SSD 500-512 Go NVMe,
# équivalent Core i5 13e génération. Couloir indicatif 650-850 €.
# --------------------------------------------------------------------------- #
ENTREE = [
    _r("HP", "Intel", "Pro 400 G9 SFF", "Neuf", "Core i5-13500", 2023,
       "16 Go DDR4 · 512 Go SATA SSD + DVD", 1039.22, R,
       "DDR4 au lieu de DDR5, disque SATA au lieu de NVMe, et 189 € au-dessus du couloir.",
       "https://www.amazon.fr/dp/B0D4F6739P"),
    _r("HP", "Intel", "Pro Mini 400 G9 Tiny", "Neuf", "Core i5-13500T", 2023,
       "16 Go DDR4 · 512 Go NVMe", None, O,
       "Configuration valable sur le papier ; aucune offre chiffrée chez les cinq enseignes.",
       None),
    _r("Dell", "Intel", "OptiPlex 7010 Micro", "Reconditionné", "Core i5-13500T", 2023,
       "16 Go DDR4 · 512 Go NVMe", 689.83, O,
       "Prix le plus bas de la gamme, mais reconditionné et version 35 W.",
       "https://www.amazon.fr/dp/B0HKDSCK9X"),
    _r("Dell", "Intel", "OptiPlex 7010 SFF", "Neuf", "Core i5-13500", 2023,
       "16 Go DDR4 · 512 Go NVMe", None, O,
       "Châssis SFF neuf, plus évolutif que le Micro ; prix non publié sur le marché relevé.",
       None),
    _r("Lenovo", "Intel", "ThinkCentre M70q Gen 5 Tiny", "Neuf", "Core i5-13500T", 2023,
       "16 Go DDR4 · 512 Go NVMe", 840.00, V,
       "Seule ligne neuve de l'entrée dans le couloir, DDR4 admise par le profil.",
       "https://www.amazon.fr/dp/B0CR1YQ87P"),
    _r("Lenovo", "Intel", "ThinkCentre M70q Gen 5 (12TD009KFR)", "Neuf", "Core i5-13500T", 2023,
       "16 Go DDR4 · 512 Go NVMe", None, O,
       "Variante allemande repérée à 773,88 € chez un revendeur hors liste : à reconfirmer.",
       None),
    _r("HP", "AMD", "ProDesk 2 G1a Tower", "Neuf", "Ryzen 5 8500G", 2024,
       "16 Go DDR5 · 512 Go SSD", 827.52, O,
       "DDR5 et prix juste dans le couloir ; vendeur tiers, garantie et clavier à vérifier.",
       "https://www.amazon.fr/dp/B0FR3R6P42"),
    _r("HP", "AMD", "Pro 405 G9 SFF", "Neuf", "Ryzen 5 PRO 8600G", 2024,
       "16 Go DDR5 · 512 Go NVMe", None, O,
       "Référence au catalogue HP, absente des cinq enseignes au moment du relevé.",
       None),
    _r("Lenovo", "AMD", "ThinkCentre M75q Gen 5 Tiny", "Neuf", "Ryzen 5 PRO 8500GE", 2024,
       "16 Go DDR5 · 512 Go NVMe", 763.67, V,
       "Le meilleur rapport conformité / prix de l'entrée : DDR5, neuf, dans le couloir.",
       "https://www.cdiscount.com/Informatique/achat-pc-ordinateur/lenovo-thinkcentre-m75q-gen-5/f-1070853-aabod39488.html"),
    _r("Lenovo", "AMD", "ThinkCentre M75q Gen 5 (8600GE)", "Neuf", "Ryzen 5 PRO 8600GE", 2024,
       "16 Go DDR5 · 512 Go NVMe", None, O,
       "Montée en puce du même châssis ; tarif non publié en ligne.",
       None),
]

# --------------------------------------------------------------------------- #
# STANDARD — 16 ou 32 Go DDR5 double canal, SSD 500 Go NVMe, équivalent
# Core i5 14e génération. Couloir indicatif 850-1 200 €.
# --------------------------------------------------------------------------- #
STANDARD = [
    _r("HP", "Intel", "Elite 800 G9 Mini", "Neuf", "Core i5-14500", 2024,
       "16 Go DDR5 SO-DIMM · 512 Go NVMe", 1140.18, V,
       "Référence de la gamme : DDR5, neuf, 16 Go livrés — 32 Go restent à ajouter.",
       "https://www.amazon.fr/dp/B0D76M6T6R"),
    _r("HP", "Intel", "Elite 800 G9 SFF", "Neuf", "Core i5-14500", 2024,
       "16 Go DDR5 · 512 Go NVMe", None, O,
       "Même puce en châssis SFF, donc extensible en PCIe ; prix non stabilisé.",
       None),
    _r("Dell", "Intel", "OptiPlex 7020 SFF", "Neuf", "Core i5-14500", 2024,
       "16 Go DDR5 (2 emplacements) · 512 Go NVMe", 857.99, V,
       "Le moins cher des 14e génération en DDR5, chez un distributeur informatique français.",
       "https://store.actualsystemes.com/p7506414/dell-optiplex-7020-sff-pra%C2%AAt-pour-l-ia-core-i5-i5-14500-2-6-ghz-16-go-ssd-512-go-francais.aspx"),
    _r("Dell", "Intel", "OptiPlex 7020 Tower", "Neuf", "Core i5-14500", 2024,
       "16 Go DDR5 · 512 Go NVMe", None, O,
       "Format tour, deux baies, carte graphique possible ; prix à demander.",
       None),
    _r("Lenovo", "Intel", "ThinkCentre M90q Gen 5 Tiny", "Neuf", "Core i5-14500T", 2024,
       "16 Go DDR5 · 512 Go NVMe", 1532.86, R,
       "Hors enveloppe de 182 € et en rupture chez le distributeur : écarté en l'état.",
       "https://www.senetic.fr/product/12TH001FPB"),
    _r("Lenovo", "Intel", "ThinkCentre M90t Gen 5 Tower", "Neuf", "Core i5-14500", 2024,
       "32 Go DDR5 · 1 To NVMe", None, O,
       "La configuration 32 Go / 1 To existe au catalogue Lenovo ; prix à obtenir en devis.",
       None),
    _r("HP", "AMD", "Elite 805 G9 SFF", "Neuf", "Ryzen 7 8700G", 2024,
       "16 Go DDR5 5600 · 512 Go NVMe", 1528.34, R,
       "Hors enveloppe et livré en clavier QWERTZ : bon poste, mauvaise offre.",
       "https://www.amazon.fr/dp/B0DHLD7ZWM"),
    _r("HP", "AMD", "Elite Mini 805 G9", "Neuf", "Ryzen 7 8700GE", 2024,
       "16 Go DDR5 · 512 Go NVMe", None, O,
       "Le format mini existe en AMD chez HP ; aucune offre chiffrée relevée.",
       None),
    _r("Lenovo", "AMD", "ThinkCentre M75q Gen 5 Tiny", "Neuf", "Ryzen 7 PRO 8700GE", 2024,
       "16 Go DDR5 · 512 Go NVMe", 1139.49, V,
       "Meilleur prix de la gamme en DDR5 ; 16 Go conformes au plancher, pas à la cible 32 Go.",
       "https://www.cdiscount.com/informatique/achat-pc-ordinateur/mini-pc-lenovo/f-1070853-aabtn40622.html"),
    _r("Lenovo", "AMD", "ThinkCentre M75t Gen 5 Tower", "Neuf", "Ryzen 7 PRO 8700G", 2024,
       "32 Go DDR5 · 1 To NVMe", None, O,
       "Format tour AMD, seul à pouvoir recevoir une carte graphique ; prix à demander.",
       None),
]

# --------------------------------------------------------------------------- #
# CONFORT — 16 Go DDR5 double canal minimum, SSD 500 Go à 1 To NVMe, équivalent
# Core i7 14e génération et plus récent. Couloir indicatif 1 200-1 350 €.
# --------------------------------------------------------------------------- #
CONFORT = [
    _r("HP", "Intel", "Pro Mini 400 G9 — i7-14700T", "Neuf", "Core i7-14700T", 2024,
       "16 Go DDR · 512 Go NVMe", 1286.14, O,
       "28 threads en 35 W ; 16 Go seulement, la cible 32 Go reste à financer.",
       "https://www.amazon.fr/dp/B0D7424V46"),
    _r("HP", "Intel", "Elite Mini 800 G9 — i7-14700", "Neuf", "Core i7-14700", 2024,
       "16 Go DDR5 · 512 Go NVMe", 1331.80, O,
       "Version 65 W, plus puissante que la T ; à 18 € du plafond de l'enveloppe.",
       "https://www.cdiscount.com/search/10/hp+elite+mini+800+g9+i7-14700.html"),
    _r("Dell", "Intel", "Dell Pro Micro QCM1250", "Neuf", "Core i7-14700T", 2024,
       "32 Go DDR5 · 1 To NVMe", None, O,
       "La seule configuration Dell conforme au profil complet ; prix uniquement sur devis.",
       "https://www.dell.com/fr-fr/search/dell%20pro%20micro%20qcm1250"),
    _r("Dell", "Intel", "OptiPlex 7020 Tower — i7-14700", "Neuf", "Core i7-14700", 2024,
       "32 Go DDR5 · 1 To NVMe", None, O,
       "Format tour, carte graphique possible si la CAO 3D reste au périmètre.",
       None),
    _r("Lenovo", "Intel", "ThinkCentre M90q Gen 6 Tiny", "Neuf", "Core Ultra 7 265", 2025,
       "Configuration non publiée", 1624.88, R,
       "274,88 € au-dessus du plafond : la génération 2025 sort de l'enveloppe.",
       "https://www.cdiscount.com/search/10/thinkcentre+m90q+gen+6.html"),
    _r("Lenovo", "Intel", "ThinkCentre M90t Gen 5 — i7-14700", "Neuf", "Core i7-14700", 2024,
       "32 Go DDR5 · 1 To NVMe", None, O,
       "La tour 20 cœurs / 28 threads est le seul Lenovo conforme sur le papier ; à chiffrer.",
       None),
    _r("HP", "AMD", "Elite 805 G9 SFF — Ryzen 7 8700G", "Neuf", "Ryzen 7 8700G", 2024,
       "16 Go DDR5 5600 · 512 Go NVMe", 1528.34, R,
       "178,34 € au-dessus du plafond, et 16 Go / 512 Go au lieu de 32 Go / 1 To.",
       "https://www.amazon.fr/dp/B0DHLD7ZWM"),
    _r("HP", "AMD", "Pro 405 G9 Tower — Ryzen 7 8700G", "Neuf", "Ryzen 7 8700G", 2024,
       "32 Go DDR5 · 1 To NVMe", None, O,
       "Configuration tour 8 cœurs, la plus évolutive de la voie AMD ; prix à demander.",
       None),
    _r("Lenovo", "AMD", "ThinkCentre M75q Gen 5 — 32 Go / 1 To", "Neuf", "Ryzen 7 PRO 8700GE", 2024,
       "32 Go DDR5 · 1 To NVMe", None, O,
       "La référence existe au catalogue mais n'est pas distribuée en ligne.",
       None),
    _r("Lenovo", "AMD", "ThinkCentre M75t Gen 5 — 32 Go / 1 To", "Neuf", "Ryzen 7 PRO 8700G", 2024,
       "32 Go DDR5 · 1 To NVMe", None, O,
       "Tour AMD 8 cœurs, Radeon intégrée : la voie la plus pertinente si la CAO arrive.",
       None),
]

VIGILANCE = {
    "Entrée de gamme": [
        ["À écarter",
         "Le DDR4 en simple canal et les configurations SATA présentées comme NVMe : le "
         "HP Pro 400 G9 SFF et le Dell OptiPlex 7010 Micro reconditionné sont dans ce cas."],
        ["Point de vigilance",
         "Les six références sans prix ne sont pas des offres : ce sont des machines du "
         "catalogue constructeur qu'aucun distributeur ne tarifie au moment du relevé. Un "
         "devis suffit à les faire entrer dans la comparaison."],
        ["Décision proposée",
         "Retenir le Lenovo M70q Gen 5 (840 €) en Intel et le Lenovo M75q Gen 5 (763,67 €) "
         "en AMD ; demander le prix du Pro Mini 400 G9 Tiny avant de fermer la liste HP."],
    ],
    "Standard entreprise": [
        ["À écarter",
         "L'Elite 805 G9 SFF en AMD, à 1 528,34 €, livré en QWERTZ et hors enveloppe ; le "
         "M90q Gen 5 en Intel, à 1 532,86 € et en rupture, pour 16 Go seulement."],
        ["Point de vigilance",
         "16 Go livrés en 1 × 16 Go : l'extension à 32 Go coûte une barrette, environ 250 €, "
         "et non une paire. Deux barrettes de 8 Go obligeraient au contraire à tout remplacer. "
         "C'est le premier point à faire écrire au devis."],
        ["Décision proposée",
         "Retenir le Lenovo M75q Gen 5 (1 139,49 €) et garder le HP Elite 800 G9 Mini "
         "(1 140,18 €) comme seconde source. Le Dell OptiPlex 7020 SFF (857,99 €) reste la "
         "référence prix, à 16 Go."],
    ],
    "Confort": [
        ["À écarter",
         "Le Lenovo M90q Gen 6, à 1 624,88 € : 274,88 € au-dessus du plafond, pour une "
         "génération Core Ultra dont le gain ne se voit pas sur ce profil. Le HP Elite 805 G9 "
         "AMD, à 1 528,34 €, à 16 Go et en QWERTZ."],
        ["Point de vigilance",
         "Aucune des dix références ne réunit 32 Go, 1 To et un i7 sous 1 350 €. Les deux "
         "configurations qui tiennent le profil complet — Dell Pro Micro QCM1250, OptiPlex "
         "7020 Tower i7 — ne sont pas tarifées."],
        ["Décision proposée",
         "Traiter le confort en devis, sur la base d'un 32 Go et d'un 1 To négociés au volume, "
         "ou relever le plafond à environ 1 550 €. En l'état, le HP Pro Mini 400 G9 "
         "(1 286,14 €) est la seule base chiffrée."],
    ],
}

GAMMES = [
    ("Entrée de gamme", "accueil, saisie, consultation", "650–850 €", ENTREE,
     "Profil : 16 Go DDR4 ou DDR5 en double canal, SSD 500 Go NVMe, équivalent Core i5 13ᵉ génération."),
    ("Standard entreprise", "bureautique intensive : Sage, Teams, multi-applications", "850–1 200 €",
     STANDARD,
     "Profil : 16 Go DDR5 plancher, 32 Go en cible, SSD 500 Go NVMe, équivalent Core i5 14ᵉ génération."),
    ("Confort", "postes gardés cinq ans, CAO légère, gros tableurs", "1 200–1 350 €", CONFORT,
     "Profil : 16 Go DDR5 minimum, 32 Go conseillés, SSD 500 Go à 1 To NVMe, équivalent Core i7 14ᵉ génération."),
]

# --------------------------------------------------------------------------- #
HEADERS = ["Constructeur", "Modèle", "Voie", "État", "Processeur", "Sortie",
           "Obsol.\nprésumée", "Mémoire · stockage", "Prix livré", "Prix FCFA",
           "Conformité", "Commentaire", "Fiche"]
# Somme = 39,2 cm : la largeur utile exacte d'une page A3 paysage. Au-delà, Word comprime.
WIDTHS = [2.7, 5.4, 1.5, 2.9, 3.5, 1.4, 2.3, 5.2, 2.5, 2.9, 2.4, 5.0, 1.5]
ALIGNS = ["l", "l", "c", "c", "l", "c", "c", "l", "r", "r", "c", "l", "c"]

SEUILS_HEADERS = ["Critère", "Entrée de gamme", "Standard entreprise", "Confort"]
SEUILS_WIDTHS = [3.0, 4.7, 4.7, 4.7]
SEUILS = [
    ["Mémoire", "16 Go — DDR4 ou DDR5, double canal", "16 Go DDR5 plancher, 32 Go cible",
     "16 Go DDR5 minimum, 32 Go conseillés"],
    ["Stockage", "SSD 500 Go NVMe", "SSD 500 Go NVMe", "SSD 500 Go à 1 To NVMe"],
    ["Intel", "i5-13400 (10C) ou i5-13500 (14C) — 2023", "i5-14400 (10C) ou i5-14500 (14C) — 2024",
     "i7-14700 (20C) — 2024, ou plus récent"],
    ["Intel — cœurs / threads", "10C/16T · 14C/20T", "10C/16T · 14C/20T", "20C/28T"],
    ["AMD", "Ryzen 5 8500G / 8600G (6C) — 2024", "Ryzen 5 8600G / 9600X (6C) — 2024",
     "Ryzen 7 8700G / 9700X (8C) — 2024"],
    ["AMD — cœurs / threads", "6C/12T", "6C/12T", "8C/16T"],
    ["Graphique", "iGPU suffisant", "indifférent", "iGPU ; GPU dédié 6 Go si CAO 3D"],
    ["Système", "Windows 11 Professionnel", "Windows 11 Professionnel", "Windows 11 Professionnel"],
    ["Garantie", "3 ans sur site", "3 ans sur site", "3 ans sur site"],
]

CPU_HEADERS = ["Année", "Intel", "Cœurs Intel", "AMD", "Cœurs AMD", "Gamme visée"]
CPU_WIDTHS = [1.5, 4.0, 2.1, 4.6, 2.0, 2.9]
CPU_ROWS = [
    ["2023", "Core i5-13400 · i5-13500 · i5-13500T", "10C/16T · 14C/20T",
     "— (la voie AMD 7000 reste en DDR5 AM5, non retenue)", "—", "Entrée de gamme"],
    ["2024", "Core i5-14400 · i5-14500 · i5-14500T", "10C/16T · 14C/20T",
     "Ryzen 5 8500G / 8500GE · 8600G · 9600X", "6C/12T", "Entrée et standard"],
    ["2024", "Core i7-14700 · i7-14700T", "20C/28T",
     "Ryzen 7 8700G / 8700GE · 9700X", "8C/16T", "Confort"],
    ["2025", "Core Ultra 7 265 (Arrow Lake)", "20C/20T",
     "Ryzen 7 9700X (Zen 5)", "8C/16T", "Confort — hors enveloppe chez Lenovo"],
]

EQUIV_HEADERS = ["Famille AMD", "Architecture", "Contemporain Intel", "Année", "Lecture"]
EQUIV_WIDTHS = [2.7, 2.4, 3.4, 1.5, 7.1]
EQUIV_ROWS = [
    ["Ryzen 8000G / 8000GE", "Zen 4", "Core 13ᵉ et 14ᵉ gen. (Raptor Lake)", "2024",
     "Même époque, même DDR5 : les deux voies sont comparables poste à poste."],
    ["Ryzen 7000 / PRO 7000", "Zen 4", "Core 13ᵉ gen. (Raptor Lake)", "2023",
     "Ancienne génération AMD, encore en DDR5 : à réserver aux fins de série."],
    ["Ryzen 9000", "Zen 5", "Core Ultra 200S (Arrow Lake)", "2024-2025",
     "Génération suivante : aucun poste de ce type sous 1 350 € au relevé."],
]

BUDGET_HEADERS = ["Gamme", "Couloir", "Intel — €", "AMD — €", "Intel — FCFA", "AMD — FCFA"]
BUDGET_WIDTHS = [2.6, 2.2, 2.95, 2.95, 3.2, 3.2]

F2F_HEADERS = ["Gamme", "Constructeur", "Voie Intel — modèle et prix", "Voie AMD — modèle et prix",
               "Écart AMD − Intel", "Lecture"]
F2F_WIDTHS = [2.5, 2.5, 6.5, 6.5, 2.5, 5.4]


def eur_num(x):
    """Le même nombre, sans l'unité : les colonnes de prix la portent en en-tête. """
    return eur(x).replace("\u00A0€", "")


def _fourchette(fn, mini, maxi):
    """ « 689,83 → 1 039,22 € » ; une seule valeur quand les bornes coïncident. """
    if mini is None:
        return "—"
    if mini == maxi:
        return fn(mini)
    return "%s → %s" % (fn(mini), fn(maxi))


def _min_max(rows, voie):
    px = [r["prix"] for r in rows if r["prix"] and r["plateforme"] == voie]
    return (min(px), max(px)) if px else (None, None)


def _catalogue(doc, rows):
    body, cf = [], {}
    for i, r in enumerate(rows):
        lien = "[fiche](%s)" % r["lien"] if r["lien"] else "—"
        body.append([r["constructeur"], r["modele"], r["plateforme"], r["etat"], r["cpu"],
                     str(r["annee"]), "%d\n%d ans" % (r["obso"], DUREE), r["config"],
                     eur(r["prix"]), fcfa(r["prix"]), _conformite(r), r["commentaire"], lien])
        cf[(i, 10)] = FMT[r["conf"]]
        cf[(i, 0)] = {"b": True}
        cf[(i, 2)] = {"bg": "EDE3F2" if r["plateforme"] == "AMD" else "E3ECF7", "b": True}
        if r["conf"] == "r":
            cf[(i, 8)] = FMT[R]
    doc.table(HEADERS, body, WIDTHS, font=9.4, header_bg="1F3B63", aligns=ALIGNS,
              cell_fmt=cf)


def _conformite(r):
    return {"v": "Conforme", "o": "À chiffrer" if r["prix"] is None else "Partielle",
            "r": "Non conforme", "n": "Sans objet"}[r["conf"]]


def build_doc():
    doc = Doc(
        base=BASE,
        title="Postes fixes ADCHIM — benchmark Intel / AMD",
        subtitle="Note d'arbitrage — trois gammes, deux plateformes, le prix et la conformité",
        meta=[],
        doc_ref="GED-SERVICES · note d'arbitrage ADCHIM · 18 novembre 2026",
        footer="GED-SERVICES · postes fixes ADCHIM · benchmark Intel / AMD",
    )

    doc.cover(
        eyebrow="Note d'arbitrage · postes fixes professionnels · ADCHIM",
        title="Postes fixes,\nbenchmark\nIntel / AMD",
        subtitle="Trois gammes de postes — entrée, standard, confort —, deux plateformes "
                 "conduites en parallèle, et pour chacune deux références par constructeur. "
                 "Le prix, l'année de sortie, l'obsolescence présumée et la conformité au "
                 "profil, ligne à ligne.",
        meta_rows=[
            ["Date", "**18 novembre 2026**"],
            ["Émetteur", "**Joël MBA OYONE**, prestataire informatique — GED-SERVICES"],
            ["Destinataire", "**Jad SAID**, directeur général — ADCHIM"],
            ["Objet", "Spécifier les postes fixes à approvisionner, puis les chiffrer sur le "
                      "marché français en Intel et en AMD"],
            ["Enveloppe", "**650 € à 1 350 €** par poste, écran, clavier et livraison non compris"],
            ["Gammes", "**Entrée de gamme · Standard entreprise · Confort**"],
            ["Périmètre", "HP, Dell, Lenovo — deux références par constructeur et par voie"],
            ["Prix", "Relevés du marché français, TTC ; **1 € = 655,957 FCFA**, parité fixe"],
            ["Réserve", "Prix **illustratifs** : de quoi arbitrer, pas de quoi contractualiser"],
        ],
        pagebreak=True,
    )

    # ------------------------------------------------------------------ 1 objet
    doc.h1_plain("1. Objet et ce que cette note tranche")
    doc.p("Vous m'avez demandé de spécifier le poste fixe qui servira de standard chez ADCHIM, "
          "puis de le chiffrer sur le marché français. Cette note fait les deux, et ajoute ce "
          "qui manquait pour décider : **la même recherche conduite en Intel et en AMD**, sur "
          "des configurations équivalentes, avec le prix en euros et en francs CFA.", lead=True)
    doc.p("Trois gammes structurent la commande : **l'entrée de gamme** pour l'accueil et la "
          "saisie, **le standard** pour la bureautique intensive — Sage, Teams, plusieurs "
          "applications ouvertes à la fois —, et **le confort** pour les postes que vous "
          "garderez cinq ans, y compris la CAO légère. Chaque gamme est déclinée sur "
          "**deux plateformes** et **deux références par constructeur**, pour que le choix ne "
          "dépende pas d'une seule machine disponible un jour donné.", small=True)
    doc.spacer(0.2)
    doc.h2("Ce que vous trouverez, section par section")
    doc.table(["Section", "Ce qu'elle apporte à la décision"], [
        ["2. Seuils matériels", "Le profil opposable, gamme par gamme, en Intel et en AMD. "
                                "Une machine qui ne le tient pas est écartée, quel que soit son prix."],
        ["3. Processeurs par année", "Les puces retenues, leur année de sortie et leur équivalent "
                                     "dans l'autre voie. C'est ce tableau qui rend le face-à-face honnête."],
        ["4. Enveloppe budgétaire", "Le couloir de prix de chaque gamme, en euros et en francs CFA, "
                                    "confronté à ce que le marché donne réellement."],
        ["5 à 7. Benchmark", "Les références retenues, gamme par gamme : prix livré, conformité au "
                             "profil, commentaire, et le lien vers la fiche produit."],
        ["8. Face-à-face", "Intel contre AMD, à configuration équivalente, avec l'écart de prix signé."],
        ["9. Recommandation", "Ce que je recommande de retenir, et ce que je ne recommande pas."],
    ], [3.6, 13.5], font=8.0, aligns=["l", "l"], first_col_bold=True,
        caption="Le plan de la note. Les sections 5 à 7 sont en paysage : treize colonnes ne "
                "tiennent pas sur une page portrait.")

    doc.spacer(0.25)
    doc.h2("Code couleur — trois états, jamais confondus")
    doc.table([], [["Vert — conforme au profil", "Orange — partielle, ou prix non relevé",
                    "Rouge — hors enveloppe, ou non conforme"]], [1, 1, 1], font=7.4,
              header=False, zebra=False,
              cell_fmt={(0, 0): FMT[V], (0, 1): FMT[O], (0, 2): FMT[R]})
    doc.p("Le fond **bleu clair** désigne la voie Intel, le fond **violet clair** la voie AMD. "
          "Une ligne orange dont le prix est vide porte la mention « à chiffrer » : elle décrit "
          "une référence réelle, pas une offre relevée.", small=True)

    # ------------------------------------------------------------------ 2 seuils
    doc.pagebreak()
    doc.h1_plain("2. Seuils matériels retenus")
    doc.p("Ces seuils sont ceux que j'oppose à chaque offre. Ils reprennent votre cadrage, en "
          "ajoutant la double canal mémoire, qui conditionne la performance réelle bien plus que "
          "la fréquence affichée.", small=True)
    doc.table(SEUILS_HEADERS, SEUILS, SEUILS_WIDTHS, font=7.8,
              aligns=["l", "l", "l", "l"], first_col_bold=True,
              caption="Le profil par gamme. La colonne « Conformité » des tableaux 5 à 7 répond "
                      "point par point à ces lignes ; la colonne « Commentaire » dit ce qui manque.")
    doc.spacer(0.2)
    doc.p("**Trois précisions qui évitent les mauvaises surprises.**", small=True)
    doc.ul([
        "**La double canal n'est pas un détail.** Un poste livré en une seule barrette de 16 Go perd "
        "de l'ordre de 15 à 20 % en usage bureautique lourd. Il faut donc deux barrettes, ou une "
        "extension à prévoir au devis.",
        "**La DDR4 est tolérée en entrée seulement.** Au-delà, elle signale une plateforme antérieure "
        "à 2024 : c'est un critère d'écart, pas un détail de fiche technique.",
        "**Le format décide de l'évolutivité.** Un Tiny n'a pas de logement PCIe exploitable : la "
        "clause « carte graphique si CAO 3D » du confort impose un SFF ou une tour.",
    ], small=True)
    doc.h2("Pourquoi trois gammes, et pas cinq")
    doc.p("Parce que le prix d'un poste ne dit rien de son coût sur cinq ans. Un poste d'accueil qui "
          "ouvre Sage et un poste de comptabilité qui recalcule un classeur de quatre-vingt mille "
          "lignes n'ont pas les mêmes besoins ; les aligner sur le même modèle revient soit à payer "
          "du confort inutile à l'accueil, soit à faire attendre la comptabilité. Trois gammes, "
          "c'est le plus petit nombre qui permette de trancher poste par poste sans arbitrage au "
          "cas par cas.", small=True)
    doc.p("Ce que ces seuils ne disent pas, c'est le nombre de postes par gamme : il n'est pas dans "
          "la commande, et il change tout, parce que quarante postes et quatre cents ne se "
          "négocient pas au même prix. C'est le premier élément qu'il me faut pour transformer "
          "cette note en commande — je le reprends en section 11.", small=True)

    # ------------------------------------------------------------------ 3 CPU
    doc.pagebreak()
    doc.h1_plain("3. Processeurs par année de sortie, et équivalences")
    doc.p("Une comparaison Intel / AMD n'a de sens qu'à époque comparable. Ce tableau fixe l'année "
          "de sortie de chaque puce retenue, et l'équivalent d'en face.", small=True)
    doc.table(CPU_HEADERS, CPU_ROWS, CPU_WIDTHS, font=8.2,
              aligns=["c", "l", "c", "l", "c", "l"], first_col_bold=True,
              caption="Les puces retenues, par année. Les dates sont celles des lancements "
                      "constructeur ; la génération commerciale du châssis peut différer d'un an.")
    doc.spacer(0.2)
    doc.table(EQUIV_HEADERS, EQUIV_ROWS, EQUIV_WIDTHS, font=8.2,
              aligns=["l", "l", "l", "c", "l"], first_col_bold=True,
              caption="Correspondance des architectures. C'est sur cette base que les tableaux 5 à 7 "
                      "mettent les deux voies côte à côte.")
    doc.spacer(0.2)
    doc.p("**Une règle simple pour la suite :** l'année de sortie du processeur sert aussi à dater "
          "l'obsolescence présumée du poste. Je retiens **cinq ans de détention**, ce qui place la "
          "sortie de service d'un i5-13500 en 2028 et celle d'un i7-14700 en 2029. C'est le chiffre "
          "qui figure dans les tableaux, et il vaut pour un poste bureautique, pas pour une machine "
          "de calcul.", small=True)
    doc.h2("Ce que ces deux tableaux disent du marché")
    doc.p("Sous 1 350 €, le neuf est presque exclusivement Intel : Raptor Lake 13ᵉ et 14ᵉ "
          "générations, en DDR5 chez tous les constructeurs sauf HP sur l'entrée de gamme. AMD "
          "apparaît sur des plateformes plus récentes — AM5, DDR5, Zen 4 — mais sur un nombre de "
          "références distribué beaucoup plus étroit : deux châssis HP, deux Lenovo, aucun Dell.",
          small=True)
    doc.p("Conséquence pratique : la voie Intel apporte le prix et la disponibilité, la voie AMD "
          "apporte la DDR5 et un iGPU sérieux dès l'entrée de gamme. Ni l'une ni l'autre ne donne "
          "32 Go et 1 To dans l'enveloppe : c'est un arbitrage de mémoire, pas de marque.",
          small=True)

    # ------------------------------------------------------------------ 4 budget
    doc.pagebreak()
    doc.h1_plain("4. Enveloppe budgétaire, confrontée au marché")
    doc.p("L'enveloppe de travail est de **650 € à 1 350 € par poste**. À l'intérieur, chaque gamme "
          "a son couloir : c'est une indication de pilotage, pas une barrière — une offre hors "
          "couloir mais dans l'enveloppe reste recevable, signalée en orange.", small=True)
    lignes = []
    for nom, _usage, couloir, rows, _p in GAMMES:
        i_min, i_max = _min_max(rows, "Intel")
        a_min, a_max = _min_max(rows, "AMD")
        lignes.append([nom, couloir,
                       _fourchette(eur_num, i_min, i_max), _fourchette(eur_num, a_min, a_max),
                       _fourchette(fcfa_num, i_min, i_max),
                       _fourchette(fcfa_num, a_min, a_max)])
    doc.kpi([("650–1 350 €", "par poste, hors écran et clavier"),
             ("16 Go", "DDR5, double canal exigée"),
             ("512 Go", "NVMe, cinq ans de détention"),
             ("3 ans", "garantie sur site attendue")])
    doc.table(BUDGET_HEADERS, lignes, BUDGET_WIDTHS, font=7.4,
              aligns=["l", "l", "r", "r", "r", "r"], first_col_bold=True,
              caption="Les prix réellement relevés, par gamme et par voie. L'étalement vient moins "
                      "de la puce que de l'état de la machine et du format.")
    doc.spacer(0.2)
    doc.p("**Ce que l'enveloppe achète, et ce qu'elle n'achète pas.**", small=True)
    doc.ul([
        "**En entrée de gamme, l'enveloppe suffit** : deux offres neuves tiennent sous 850 €, l'une "
        "en Intel chez Lenovo (840 €), l'autre en AMD chez Lenovo également (763,67 €).",
        "**En standard, elle suffit aussi, mais pas avec 32 Go.** Le Dell OptiPlex 7020 en DDR5 à "
        "857,99 € et le HP Elite 800 G9 Mini à 1 140,18 € sont à 16 Go : l'extension mémoire est un "
        "coût séparé, à chiffrer.",
        "**En confort, elle ne suffit plus.** Les deux seules configurations réellement conformes "
        "(32 Go, 1 To, i7) sont sans prix publié ; les machines chiffrées sont soit à 16 Go, soit "
        "au-delà de 1 500 €.",
    ], small=True)
    doc.p("**Le coût sur cinq ans, qui est le vrai chiffre.** Un poste à 840 € détenu cinq ans coûte "
          "168 € par an ; un poste à 1 140 €, 228 €. L'écart de 300 € à l'achat vaut donc 60 € par "
          "an et par poste — moins qu'une intervention sur site. Ce qui coûte cher, ce n'est pas la "
          "gamme haute du devis, c'est le poste qu'on remplace au bout de trois ans parce qu'il "
          "n'ouvre plus les fichiers du métier.", small=True)
    doc.p("**Tendance à retenir :** entre 650 € et 1 350 €, on achète aujourd'hui une puce de "
          "13ᵉ ou 14ᵉ génération, 16 Go de DDR5 et 512 Go de NVMe. Les 32 Go et le téraoctet "
          "demandés au confort font sortir de l'enveloppe sur toutes les marques, sauf à les "
          "obtenir en devis avec une remise de volume.", small=True)

    # ------------------------------------------------------------------ 5-7 bench
    for n, (nom, usage, couloir, rows, profil) in enumerate(GAMMES, start=5):
        doc.landscape3(True)
        if n > 5:
            doc.pagebreak()
        doc.h1_plain("Tableau %d — %s : %s" % (n - 3, nom, usage))
        doc.p("**%s** Couloir indicatif : %s. Deux références par constructeur et par voie ; "
              "l'absence d'offre AMD chez Dell est un fait de catalogue, pas un oubli."
              % (profil, couloir), small=True)
        _catalogue(doc, rows)
        doc.spacer(0.15)
        doc.p("**Lecture de la gamme.** " + _lecture(nom), small=True)
        doc.spacer(0.2)
        doc.table([], VIGILANCE[nom], [5.4, 33.8], font=8.8, header=False, zebra=False,
                  first_col_bold=True, aligns=["l", "l"])

    # ------------------------------------------------------------------ 8 face à face
    doc.landscape(True)
    doc.h1_plain("8. Face-à-face Intel / AMD à configuration équivalente")
    doc.p("Le face-à-face ne compare que ce qui est comparable : 16 Go de DDR5 de part et d'autre, "
          "512 Go de NVMe, même millésime. Quand une des deux voies n'a pas de prix, je l'écris "
          "plutôt que de comparer deux choses différentes.", small=True)
    cf, body = {}, []
    paires = [
        ("Entrée", "Lenovo", "M70q Gen 5 — i5-13500T", 840.00, "M75q Gen 5 — R5 PRO 8500GE", 763.67,
         "AMD 76,33 € moins cher, en DDR5, avec six cœurs contre quatorze."),
        ("Entrée", "HP", "Pro 400 G9 SFF — i5-13500", 1039.22, "ProDesk 2 G1a — R5 8500G", 827.52,
         "AMD 211,70 € moins cher, mais châssis tour et vendeur tiers."),
        ("Standard", "HP", "Elite 800 G9 Mini — i5-14500", 1140.18, "Elite 805 G9 SFF — R7 8700G",
         1528.34, "AMD 388,16 € plus cher : l'écart paie le SFF et la Radeon 780M."),
        ("Standard", "Lenovo", "M90q Gen 5 — i5-14500T", 1532.86, "M75q Gen 5 — R7 PRO 8700GE",
         1139.49, "AMD 393,37 € moins cher, à 16 Go des deux côtés."),
        ("Confort", "HP", "Pro Mini 400 G9 — i7-14700T", 1286.14, "Elite 805 G9 SFF — R7 8700G",
         1528.34, "AMD 242,20 € plus cher, et seulement 16 Go / 512 Go."),
    ]
    for i, (g, c, mi, pi, ma, pa, lect) in enumerate(paires):
        ecart = pa - pi
        body.append([g, c, "%s — %s" % (mi, eur(pi)), "%s — %s" % (ma, eur(pa)),
                     ("+" if ecart > 0 else "−") + eur(abs(ecart)), lect])
        cf[(i, 4)] = FMT[R] if ecart > 0 else FMT[V]
        cf[(i, 1)] = {"b": True}
        cf[(i, 2)] = {"bg": "E3ECF7"}
        cf[(i, 3)] = {"bg": "EDE3F2"}
    doc.table(F2F_HEADERS, body, F2F_WIDTHS, font=8.6,
              aligns=["l", "l", "l", "l", "c", "l"], cell_fmt=cf,
              caption="Cinq paires comparables, sur les six constructeurs-gammes possibles. "
                      "L'écart est calculé AMD moins Intel ; il est vert quand l'AMD est moins cher.")
    doc.spacer(0.2)
    doc.p("**Ce que le face-à-face montre.** L'AMD n'est pas systématiquement moins cher, ni "
          "systématiquement plus performant : il gagne en entrée de gamme, où ses six cœurs "
          "suffisent et où sa plateforme est plus récente ; il perd en standard et en confort "
          "dès qu'on lui demande un châssis extensible, parce que les seules machines AMD "
          "distribuées sont des SFF haut de gamme. **La voie se choisit par gamme, pas par "
          "doctrine.**", small=True)
    doc.p("**Ce que l'écart achète, concrètement.** Chez HP, l'AMD coûte 388 € de plus en standard : "
          "c'est le passage d'un mini 1 litre à un SFF avec deux emplacements mémoire et un "
          "logement PCIe. Chez Lenovo, l'AMD coûte 393 € de moins en standard : c'est le même "
          "format Tiny, mais une puce de génération antérieure. Le même écart de prix recouvre "
          "donc deux réalités opposées.", small=True)

    # ------------------------------------------------------------------ 9 reco
    doc.landscape(False)
    doc.h1_plain("9. Ma recommandation")
    doc.p("**Je recommande le Lenovo ThinkCentre M75q Gen 5 en AMD comme standard d'achat, et le "
          "HP Elite 800 G9 Mini en Intel comme référence de repli.** Le Lenovo est neuf, en DDR5, "
          "livré à **1 139,49 €** — sous le plafond de 1 350 € avec 210 € de marge pour passer à "
          "32 Go. Le HP, à 1 140,18 €, tient la même position en Intel et laisse le choix d'une "
          "seconde source en cas de rupture.", lead=True)
    doc.p("Cette recommandation est **conditionnelle** sur trois points, que je ne peux pas lever "
          "seul :", small=True)
    doc.ul([
        "**Le montage mémoire.** Les 16 Go doivent être livrés en 1 × 16 Go, sinon l'extension "
        "impose de remplacer les deux barrettes et coûte plus cher que le chiffrage ci-dessous.",
        "**Le prix de l'extension.** Une barrette SO-DIMM DDR5 de 16 Go se situe autour de 250 € "
        "au détail : c'est ce qui décide si le poste reste dans l'enveloppe.",
        "**La garantie.** Trois ans sur site, pièces et main-d'œuvre, à faire figurer au devis. "
        "C'est ce qui distingue une offre constructeur d'une offre de place de marché.",
    ], small=True)
    doc.spacer(0.2)
    doc.table(["Poste de coût", "Prix €", "Prix FCFA", "Nature du prix"], [
        ["Lenovo M75q Gen 5 — Ryzen 7 PRO 8700GE, 16 Go DDR5, 512 Go NVMe",
         eur(1139.49), fcfa(1139.49), "Relevé Cdiscount, neuf, livré"],
        ["Extension 1 × 16 Go DDR5 SO-DIMM", "≈ 250 €", "≈ 163 989",
         "Ordre de prix du marché, à confirmer par devis"],
        ["**Total cible 32 Go / 512 Go**", "**≈ 1 389,49 €**", "**≈ 911 283**",
         "**Dépassement d'environ 39 €** — à arbitrer"],
    ], [8.2, 2.7, 2.8, 3.4], font=8.2, aligns=["l", "r", "r", "l"],
        caption="Le chiffrage de la cible. L'extension fait sortir le poste de l'enveloppe de "
                "39 € : c'est le seul point qui demande votre arbitrage. « ≈ » marque un ordre de "
                "prix, non un relevé.")
    doc.spacer(0.2)
    doc.p("**Ce que je ne recommande pas.** Le confort en l'état : aucune offre chiffrée ne "
          "descend sous 1 286 € avec 32 Go et 1 To, et les deux configurations qui tiennent le "
          "profil complet ne sont pas tarifées. Si le confort doit être commandé maintenant, il "
          "faut soit relever le plafond à 1 550 €, soit accepter 16 Go et 512 Go en le documentant.",
          small=True)

    # ------------------------------------------------------------------ 10 sécuriser
    doc.h1_plain("10. Points à sécuriser avant décision")
    doc.ul([
        "**Référence commerciale exacte** de chaque machine retenue, avec son code constructeur : "
        "les mêmes noms de gamme recouvrent des configurations très différentes.",
        "**Montage mémoire** : deux barrettes de 8 Go ou une de 16 Go — la réponse change le coût "
        "de l'extension.",
        "**Interface du disque** : NVMe exigé ; plusieurs offres d'entrée de gamme sont encore en "
        "SATA sans que l'annonce le dise clairement.",
        "**Garantie 3 ans sur site**, pièces et main-d'œuvre, inscrite au devis — et non une "
        "garantie vendeur d'un an.",
        "**Prix livré**, port compris : les écarts de port atteignent 15 € par poste, soit "
        "9 838 FCFA.",
        "**Clavier AZERTY** : deux offres relevées sont en QWERTZ, l'une chez HP en AMD, l'autre "
        "chez Lenovo. À exclure ou à remplacer.",
        "**Écran, clavier, souris** : hors périmètre de cette note, à approvisionner séparément.",
    ], small=True)

    # ------------------------------------------------------------------ 11 méthode
    doc.pagebreak()
    doc.h1_plain("11. Méthode et limites")
    doc.p("Je préfère dire ce que valent ces chiffres plutôt que de les présenter comme des prix "
          "fermes.", small=True)
    doc.ul([
        "**Sources** : relevés du marché français — Amazon.fr en référence principale, puis "
        "Cdiscount, Fnac, LDLC, Materiel.net, les sites constructeur HP, Dell et Lenovo, et deux "
        "distributeurs informatiques français.",
        "**Date** : 18 novembre 2026. Un prix d'enseigne bouge en quelques jours, surtout en "
        "reconditionné et sur les fins de série.",
        "**Nature des prix** : TTC, port compris quand il est connu. Ils sont **illustratifs** : "
        "ils servent à arbitrer entre deux voies et deux formats, pas à engager une commande. "
        "Un devis constructeur ou grossiste les décalera de 15 à 25 % à la baisse sur volume.",
        "**Conversion** : 1 € = 655,957 FCFA, parité fixe. Les francs sont exacts, les euros ne "
        "le sont pas — ils changent chaque semaine.",
        "**Année de sortie** : celle du lancement constructeur de la puce. **Obsolescence "
        "présumée** : sortie + cinq ans, durée de détention retenue ; c'est une hypothèse de "
        "travail, pas une date de fin de support.",
        "**Conformité** : jugée sur la mémoire, le stockage, la puce et l'enveloppe. Une case "
        "orange n'est pas un avis, c'est un fait : un point manque, ou le prix n'est pas connu.",
        "**Ce que la note ne fait pas** : aucun benchmark mesuré — les repères sont "
        "architecturaux ; aucune volumétrie de parc ; aucun devis ferme.",
    ], small=True)
    doc.spacer(0.2)
    doc.p("**Décision proposée :** autoriser la consultation sur la base du **Lenovo M75q Gen 5 "
          "en AMD** et du **HP Elite 800 G9 Mini en Intel**, avec obligation de chiffrer la "
          "configuration 32 Go complète et de produire les justificatifs de conformité — garantie "
          "trois ans, montage mémoire, interface NVMe — avant toute validation de commande.",
          small=True)

    doc.spacer(0.8)
    doc.p("Je reste à disposition pour présenter cette note en comité, ouvrir les demandes de "
          "devis dès votre accord, et revenir avec des prix fermes sous huit jours.", small=True)
    doc.spacer(0.5)
    doc.p("**Joël MBA OYONE** — GED-SERVICES, prestataire informatique", small=True)

    dpath, ppath = doc.save(OUT)

    import docx as _docx

    d = _docx.Document(dpath)
    cp = d.core_properties
    cp.author = "GED-SERVICES"
    cp.last_modified_by = "GED-SERVICES"
    cp.comments = ""
    cp.category = "Note d'arbitrage — postes fixes"
    cp.title = "Postes fixes ADCHIM — benchmark Intel / AMD"
    d.save(dpath)
    return dpath, ppath


def _lecture(nom):
    return {
        "Entrée de gamme": "deux offres neuves tiennent le couloir, l'une en Intel (M70q Gen 5, "
                           "840 €), l'autre en AMD (M75q Gen 5, 763,67 €). Le HP Pro 400 G9 est "
                           "au-dessus du couloir et en SATA ; le Dell OptiPlex 7010 chiffré est "
                           "reconditionné. **La voie AMD est ici la plus cohérente** : DDR5, neuf, "
                           "prix le plus bas.",
        "Standard entreprise": "trois offres neuves en DDR5 : Dell OptiPlex 7020 à 857,99 €, HP "
                               "Elite 800 G9 Mini à 1 140,18 €, Lenovo M75q Gen 5 à 1 139,49 €. "
                               "Toutes livrent 16 Go : **le 32 Go de la cible est un coût séparé "
                               "sur les trois**. Le M90q Gen 5 en Intel sort de l'enveloppe à "
                               "1 532,86 €.",
        "Confort": "aucune offre chiffrée ne réunit 32 Go, 1 To et un i7 sous 1 350 €. Le HP Pro "
                   "Mini 400 G9 tient la puce et le prix mais pas la mémoire ; le Lenovo M90q "
                   "Gen 6 dépasse de 274,88 €. **Le confort reste une spécification sans offre "
                   "chiffrée** : il se jouera en devis.",
    }[nom]


if __name__ == "__main__":
    print(build_doc())
