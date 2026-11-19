# -*- coding: utf-8 -*-
"""Version Comité de direction — postes fixes ADCHIM.

Document court (10 pages) construit pour une réunion : la philosophie, les cibles
techniques, les cibles retenues gamme par gamme (surlignées), le face-à-face des
processeurs et les formats de châssis, chaque tableau suivi de son mode d'emploi.

Tous les montants sont recalculés depuis les prix des tableaux de gamme ; la
conversion FCFA et les écarts sont calculés ici, jamais saisis à la main.
"""
from __future__ import annotations

import os

from render import Doc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, os.environ.get(
    "LIVRABLES_DIR", "estimations/ADC_Workstations 2026-11-18"))
BASE = "ADC_Workstations_2026-11-18_Note_comite_direction"
TVA = 655.957
DUREE = 5

VERT = "D8EDCB"
VERT_T = "1E6B33"
ORANGE = "FAEBB8"
ROUGE = "F8CDB6"
GRIS = "E9EBEF"
BLEU = "1F3B63"
FMT = {
    "v": {"bg": VERT, "color": VERT_T},
    "o": {"bg": ORANGE, "color": "7A5E12"},
    "r": {"bg": ROUGE, "color": "9B2C12"},
    "n": {"bg": GRIS, "color": "4A5058"},
}
RETENU = {"bg": VERT, "b": True}


# --------------------------------------------------------------------------- #
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


def _grp(n):
    """Nombre entier, séparateur de milliers insécable."""
    out, i = "", 0
    for ch in reversed("%d" % n):
        if i and i % 3 == 0:
            out = "\u00A0" + out
        out = ch + out
        i += 1
    return out


def eur_num(x):
    return eur(x).replace("\u00A0€", "")


def fcfa_num(x):
    return fcfa(x).replace("\u00A0FCFA", "")


def r(constructeur, modele, voie, cpu, annee, prix, conf, statut, retenu=False, excl=False):
    """excl=True : machine chiffrée mais exclue des fourchettes (reconditionné)."""
    return dict(constructeur=constructeur, modele=modele, voie=voie, cpu=cpu, annee=annee,
                obso=annee + DUREE, prix=prix, conf=conf, statut=statut, retenu=retenu,
                excl=excl)


# Prix : relevés du 19 novembre 2026, ceux des tableaux de la note.
ENTREE = [
    r("HP", "Pro 400 G9 SFF", "Intel", "Core i5-13500", 2023, 943.61, "r",
      "DDR4 et SATA, +93,61 € hors couloir"),
    r("HP", "Pro Mini 400 G9 Tiny", "Intel", "Core i5-13500T", 2023, None, "o", "à chiffrer"),
    r("Dell", "OptiPlex 7010 Micro", "Intel", "Core i5-13500T", 2023, 759.05, "r",
      "reconditionné", excl=True),
    r("Dell", "OptiPlex 7010 SFF", "Intel", "Core i5-13500", 2023, None, "o", "à chiffrer"),
    r("Lenovo", "ThinkCentre M70q Gen 5", "Intel", "Core i5-13500T", 2023, 840.00, "v",
      "cible retenue en Intel", retenu=True),
    r("Lenovo", "ThinkCentre M70q Gen 5 (12TD009KFR)", "Intel", "Core i5-13500T", 2023, None,
      "o", "variante DE repérée à 773,88 €"),
    r("HP", "ProDesk 2 G1a (Tour)", "AMD", "Ryzen 5 8500G", 2024, 834.19, "v",
      "le moins cher des conformes"),
    r("HP", "Pro 405 G9 SFF", "AMD", "Ryzen 5 PRO 8600G", 2024, None, "o", "à chiffrer"),
    r("Lenovo", "ThinkCentre M75q Gen 5", "AMD", "Ryzen 5 PRO 8500GE", 2024, 849.00, "v",
      "cible retenue en AMD", retenu=True),
    r("Lenovo", "ThinkCentre M75q Gen 5 (8600GE)", "AMD", "Ryzen 5 PRO 8600GE", 2024, None,
      "o", "à chiffrer"),
]

STANDARD = [
    r("HP", "Elite 800 G9 Mini", "Intel", "Core i5-14500", 2024, 1055.99, "v",
      "cible retenue en Intel — seconde source", retenu=True),
    r("HP", "Elite 800 G9 SFF", "Intel", "Core i5-14500", 2024, None, "o", "à chiffrer"),
    r("Dell", "OptiPlex 7020 MFF", "Intel", "Core i5-14500T", 2024, 999.95, "v",
      "référence prix, non retenue"),
    r("Dell", "OptiPlex 7020 Tower", "Intel", "Core i5-14500", 2024, None, "o", "à chiffrer"),
    r("Lenovo", "ThinkCentre M90q Gen 5", "Intel", "Core i5-14500T", 2024, 1470.45, "r",
      "hors enveloppe de 120,45 €"),
    r("Lenovo", "ThinkCentre M90t Gen 5 Tower", "Intel", "Core i5-14500", 2024, None, "o",
      "32 Go / 1 To, à chiffrer"),
    r("HP", "Elite 805 G9 SFF", "AMD", "Ryzen 7 8700G", 2024, 1251.58, "o",
      "hors couloir de 51,58 €, clavier QWERTZ"),
    r("HP", "Elite 805 G9 Mini", "AMD", "Ryzen 7 8700GE", 2024, None, "o", "à chiffrer"),
    r("Lenovo", "ThinkCentre M75q Gen 5", "AMD", "Ryzen 7 PRO 8700GE", 2024, 1112.92, "v",
      "cible retenue en AMD — standard d'achat", retenu=True),
    r("Lenovo", "ThinkCentre M75t Gen 5 Tower", "AMD", "Ryzen 7 PRO 8700G", 2024, None, "o",
      "32 Go / 1 To, à chiffrer"),
]

CONFORT = [
    r("HP", "Pro Mini 400 G9 (i7)", "Intel", "Core i7-14700T", 2024, 1109.30, "o",
      "16 Go seulement, sous le couloir"),
    r("HP", "Elite Desk 800 G9 Tour", "Intel", "Core i7-14700", 2024, 1363.75, "o",
      "16 Go, +13,75 € hors plafond"),
    r("HP", "Elite Mini 800 G9", "Intel", "Core i7-14700", 2024, 2111.27, "r",
      "hors enveloppe de 761,27 €"),
    r("Dell", "Pro Micro QCM1250", "Intel", "Core i7-14700T", 2024, None, "v",
      "32 Go / 1 To, cible à chiffrer", retenu=True),
    r("Dell", "OptiPlex 7020 Tower (i7)", "Intel", "Core i7-14700", 2024, None, "o",
      "32 Go / 1 To, à chiffrer"),
    r("Lenovo", "ThinkCentre M90q Gen 6", "Intel", "Core Ultra 7 265", 2025, 1624.88, "r",
      "hors enveloppe de 274,88 €"),
    r("Lenovo", "ThinkCentre M90t Gen 5 Tower", "Intel", "Core i7-14700", 2024, None, "o",
      "32 Go / 1 To, à chiffrer"),
    r("HP", "Elite 805 G9 SFF", "AMD", "Ryzen 7 8700G", 2024, 1528.34, "r",
      "16 Go / 512 Go, hors enveloppe"),
    r("HP", "Pro 405 G9 Tower", "AMD", "Ryzen 7 8700G", 2024, None, "o",
      "32 Go / 1 To, à chiffrer"),
    r("Lenovo", "ThinkCentre M75q Gen 5 (32/1 To)", "AMD", "Ryzen 7 PRO 8700GE", 2024, None,
      "o", "à chiffrer"),
    r("Lenovo", "ThinkCentre M75t Gen 5 Tower", "AMD", "Ryzen 7 PRO 8700G", 2024, None, "v",
      "32 Go / 1 To, cible à chiffrer", retenu=True),
]

GAMMES = [
    ("Entrée de gamme", "accueil, saisie, consultation", "650–850 €", ENTREE,
     "16 Go DDR4 ou DDR5 en double canal, SSD 500 Go NVMe, équivalent Core i5 13ᵉ génération."),
    ("Standard entreprise", "bureautique intensive — Sage, Teams, multi-applications",
     "850–1 200 €", STANDARD,
     "16 Go DDR5 en double canal (32 Go en cible), SSD 500 Go NVMe, équivalent Core i5 14ᵉ "
     "génération."),
    ("Confort", "postes gardés cinq ans — CAO légère, gros tableurs", "1 200–1 350 €", CONFORT,
     "16 Go DDR5 minimum, 32 Go conseillés, SSD 500 Go à 1 To NVMe, équivalent Core i7 "
     "14ᵉ génération ou plus récent."),
]

CAT_HEADERS = ["Constructeur", "Modèle", "Voie", "Processeur", "Sortie", "Obsol.", "Prix livré",
               "Prix FCFA", "Conformité et commentaire"]
CAT_WIDTHS = [2.5, 5.3, 1.5, 3.3, 1.4, 1.4, 2.5, 2.9, 5.1]
CAT_ALIGNS = ["l", "l", "c", "l", "c", "c", "r", "r", "l"]

SEUILS = [
    ["Mémoire", "16 Go DDR4 ou DDR5 (DDR5 préférée), double canal",
     "16 Go DDR5 double canal (plancher) — 32 Go en cible",
     "16 Go DDR5 double canal minimum — 32 Go conseillés"],
    ["Stockage", "SSD 500 Go NVMe", "SSD 500 Go NVMe", "SSD 500 Go à 1 To NVMe"],
    ["Intel — génération", "13ᵉ gén. : i5-13400 (10C) ou i5-13500 (14C), 2023",
     "14ᵉ gén. : i5-14400 (10C) ou i5-14500 (14C), 2024",
     "14ᵉ gén. : i7-14700 (20C), 2024, ou plus récent"],
    ["Intel — cœurs / threads", "10C/16T · 14C/20T", "10C/16T · 14C/20T", "20C/28T"],
    ["AMD — plateforme", "Ryzen 5 8500G · 8600G (6C), AM5, 2024",
     "Ryzen 5 8600G · 9600X (6C), AM5, 2024", "Ryzen 7 8700G · 9700X (8C), AM5, 2024"],
    ["AMD — cœurs / threads", "6C/12T", "6C/12T", "8C/16T"],
    ["Graphique", "iGPU suffisant", "indifférent", "iGPU ; GPU dédié 6 Go si CAO 3D"],
    ["Système", "Windows 11 Professionnel", "Windows 11 Professionnel",
     "Windows 11 Professionnel"],
    ["Garantie", "3 ans sur site", "3 ans sur site", "3 ans sur site"],
]
SEUILS_WIDTHS = [3.3, 4.6, 4.6, 4.6]

CPU_HEADERS = ["Année", "Intel — puces, génération et sortie", "Cœurs",
               "AMD — puces, génération et sortie", "Cœurs", "Gamme visée"]
CPU_WIDTHS = [1.4, 5.3, 1.6, 5.2, 1.6, 2.4]
CPU_ROWS = [
    ["2023",
     "**i5-13400 · i5-13500 · i5-13500T**\n13ᵉ gén. (Raptor Lake) — T1 2023",
     "10C/16T\n14C/20T",
     "**Aucune puce retenue**\nZen 4 (AM5), T3 2022 : hors des offres relevées",
     "—", "Entrée de gamme"],
    ["2024",
     "**i5-14400 · i5-14500 · i5-14500T**\n14ᵉ gén. (Raptor Lake Refresh) — T1 2024",
     "10C/16T\n14C/20T",
     "**Ryzen 5 8500G · 8500GE · 8600G**\nZen 4 (AM5) — T1 2024",
     "6C/12T", "Entrée et standard"],
    ["2024",
     "**i7-14700 · i7-14700T**\n14ᵉ gén. (Raptor Lake Refresh) — T1 2024",
     "20C/28T",
     "**Ryzen 7 8700G · 8700GE**\nZen 4 (AM5) — T1 2024",
     "8C/16T", "Confort"],
    ["2025",
     "**Core Ultra 7 265**\nCore Ultra série 2 (Arrow Lake) — T1 2025",
     "20C/20T",
     "**Ryzen 7 9700X**\nZen 5 (AM5) — T3 2024",
     "8C/16T", "Confort, hors enveloppe"],
]
EQUIV_HEADERS = ["Famille AMD", "Architecture", "Contemporain Intel", "Année", "Ce que ça change"]
EQUIV_WIDTHS = [3.0, 2.4, 3.5, 1.4, 6.8]
EQUIV_ROWS = [
    ["Ryzen 8000G / 8000GE", "Zen 4", "Core 13ᵉ et 14ᵉ gén. (Raptor Lake)", "2024",
     "Même époque, même DDR5 : les deux voies se comparent poste à poste."],
    ["Ryzen 7000 / PRO 7000", "Zen 4", "Core 13ᵉ gén. (Raptor Lake)", "2023",
     "Génération antérieure, encore en DDR5 : réservée aux fins de série."],
    ["Ryzen 9000", "Zen 5", "Core Ultra 200S (Arrow Lake)", "2024-2025",
     "Génération suivante : aucun poste de ce type sous 1 350 € au relevé."],
]

CHASSIS_HEADERS = ["Format", "Encombrement", "Extension possible", "Mémoire · stockage",
                   "Gammes où on le trouve", "Prix constatés"]
CHASSIS_WIDTHS = [2.4, 2.7, 3.5, 3.3, 2.5, 2.4]
CHASSIS_ROWS = [
    ["Mini / Tiny / Micro", "1 litre environ, alimentation externe",
     "Aucun logement PCIe exploitable ; carte graphique impossible",
     "1 baie M.2 · 2 emplacements SO-DIMM", "Entrée et standard", "759 → 1 625 €"],
    ["SFF (petit format)", "7 à 9 litres, alimentation interne",
     "1 logement PCIe bas profil ; carte graphique basse consommation",
     "1 à 2 baies · 2 à 4 emplacements DIMM", "Standard", "944 → 1 528 €"],
    ["Tour", "15 litres et plus", "PCIe pleine hauteur : carte graphique 6 Go possible",
     "2 baies 3,5\" · 4 emplacements DIMM", "Confort (CAO 3D)", "834 → 2 111 €"],
]


# --------------------------------------------------------------------------- #
def _budget_rows():
    out = []
    for nom, _, couloir, rows, _ in GAMMES:
        cells = [nom, couloir]
        for voie in ("Intel", "AMD"):
            px = sorted(x["prix"] for x in rows
                        if x["prix"] and x["voie"] == voie and not x["excl"])
            if not px:
                cells += ["—", "—"]
            elif round(px[0]) == round(px[-1]):
                cells += ["%s €" % _grp(round(px[0])), _grp(round(px[0] * TVA))]
            else:
                cells += ["%s → %s €" % (_grp(round(px[0])), _grp(round(px[-1]))),
                          "%s → %s" % (_grp(round(px[0] * TVA)), _grp(round(px[-1] * TVA)))]
        out.append(cells)
    return out


def _catalogue(doc, rows):
    body, cf = [], {}
    for i, x in enumerate(rows):
        body.append([x["constructeur"], x["modele"], x["voie"], x["cpu"], str(x["annee"]),
                     "%d\n%d ans" % (x["obso"], DUREE), eur(x["prix"]), fcfa(x["prix"]),
                     x["statut"]])
        cf[(i, 2)] = {"bg": "EDE3F2" if x["voie"] == "AMD" else "E3ECF7", "b": True}
        cf[(i, 8)] = FMT[x["conf"]]
        if x["prix"] is None:
            cf[(i, 6)] = {"color": "7A5E12", "i": True}
            cf[(i, 7)] = {"color": "7A5E12", "i": True}
        if x["retenu"]:
            for j in range(len(CAT_HEADERS) - 1):
                cf[(i, j)] = dict(RETENU, color=VERT_T)
            cf[(i, 2)] = {"bg": "C9E3B7", "b": True, "color": VERT_T}
    doc.table(CAT_HEADERS, body, CAT_WIDTHS, font=8.1, aligns=CAT_ALIGNS, cell_fmt=cf,
              header_bg=BLEU,
              caption="Les lignes surlignées en vert sont les cibles retenues pour la gamme. "
                      "« À chiffrer » signale une machine réelle dont aucun distributeur ne "
                      "publie le prix : aucune estimation n'a été substituée au prix manquant.")


def build_doc():
    doc = Doc(
        base=BASE,
        title="Postes fixes ADCHIM — note de comité de direction",
        subtitle="Trois gammes, deux voies, une décision : le format et la mémoire",
        meta=[],
        doc_ref="GED-SERVICES · note de comité ADCHIM · 19 novembre 2026",
        footer="GED-SERVICES · postes fixes ADCHIM · note de comité de direction",
    )

    doc.cover(
        eyebrow="Comité de direction · postes fixes professionnels · ADCHIM",
        title="Postes fixes,\nla décision\nen dix pages",
        subtitle="Ce que le comité doit retenir : trois gammes de postes, deux voies "
                 "techniques conduites en parallèle, un prix par gamme, et une seule décision "
                 "qui reste ouverte — le passage à 32 Go de mémoire.",
        meta_rows=[
            ["Date", "**19 novembre 2026**"],
            ["Émetteur", "**Joël MBA OYONE**, prestataire informatique — GED-SERVICES"],
            ["Destinataire", "**Comité de direction d'ADCHIM** — Jad SAID, directeur général"],
            ["Objet", "Décider de la spécification des postes fixes et du modèle à "
                      "approvisionner, gamme par gamme"],
            ["Enveloppe", "**650 € à 1 350 €** par poste, écran, clavier et livraison non "
                          "compris"],
            ["À décider", "Les trois gammes et leurs couloirs ; les modèles retenus en entrée "
                          "et en standard ; le sort du confort (relever le plafond ou "
                          "commander 16 Go)"],
        ],
    )

    # ------------------------------------------------------------------ 1 essentiel
    doc.h1_plain("1. L'essentiel, en une page")
    doc.kpi([("650–1 350 €", "enveloppe par poste, hors écran"),
             ("3", "gammes, un couloir de prix par gamme"),
             ("31", "références relevées, dont 15 chiffrées"),
             ("5 ans", "durée de détention retenue")])
    doc.p("**Deux machines seulement réunissent les trois conditions — neuve, conforme au "
          "profil, dans l'enveloppe — et ce sont deux Lenovo d'entrée de gamme** : le "
          "ThinkCentre M70q Gen 5 en Intel à **840,00 €** et le M75q Gen 5 en AMD à "
          "**849,00 €**. Le standard tient aussi, mais juste au-dessus du couloir de gamme : "
          "HP Elite 800 G9 Mini à **1 055,99 €** et Lenovo M75q Gen 5 en Ryzen 7 à "
          "**1 112,92 €**.", lead=True)
    doc.p("**Le confort n'a pas d'offre chiffrée conforme.** Aucune des onze références "
          "relevées ne réunit 32 Go, 1 To et un i7 dans l'enveloppe : les deux configurations "
          "qui tiennent le profil complet — Dell Pro Micro QCM1250 et Lenovo M75t Gen 5 — "
          "n'existent qu'en devis. C'est la deuxième décision à prendre, et elle est budgétaire, "
          "pas technique.", small=True)
    doc.p("**La décision qui reste ouverte porte sur 250 € et 12,92 €.** Le poste standard "
          "d'achat coûte 1 112,92 € en 16 Go ; la barrette de 16 Go qui le porte à 32 Go vaut "
          "environ 250 € au détail, soit une cible à **%s** — %s au-dessus du plafond de "
          "1 350 €. C'est le seul arbitrage qui demande votre signature."
          % (eur(1112.92 + 250), eur(1112.92 + 250 - 1350)), small=True)
    doc.p("**Ce que la note ne demande pas.** Aucune volumétrie de parc ne figure dans la "
          "commande : le nombre de postes par gamme reste à communiquer, et il pèse plus lourd "
          "sur le prix final que le choix de la marque.", small=True)
    doc.spacer(0.15)
    doc.callout(
        "Comment lire cette note",
        "Chaque section se termine par un encadré « à quoi ça sert ». Si vous ne lisez qu'une "
        "chose : la section 5 (les cibles retenues, surlignées en vert) et la section 8 (la "
        "décision demandée). Les deux tableaux techniques — processeurs et châssis — servent à "
        "répondre aux deux questions qui reviennent toujours en comité : « pourquoi cette puce "
        "et pas la plus récente ? » et « pourquoi pas un mini, moins cher ? ».",
        kind="info")

    doc.pagebreak()
    # ------------------------------------------------------------------ 2 philosophie
    doc.h1_plain("2. La philosophie : trois principes, une seule grille")
    doc.p("La note ne cherche pas le meilleur poste, elle cherche le poste juste — celui qu'on "
          "peut acheter en série, à un prix tenu, et dont on sait quand il faudra le remplacer. "
          "Trois principes en découlent, plus une précaution de lecture.", small=True)
    doc.table(
        ["Principe", "Ce qu'il décide", "Pourquoi ce choix"],
        [["**Trois gammes, pas une**", "Le couloir de prix de chaque poste : 650–850 €, "
          "850–1 200 €, 1 200–1 350 €",
          "Un poste d'accueil et un poste de comptabilité n'ont pas les mêmes besoins. Les "
          "aligner revient soit à payer du confort inutile à l'accueil, soit à faire attendre "
          "la comptabilité."],
         ["**Deux voies, Intel et AMD**", "La source d'approvisionnement : deux références par "
          "constructeur et par voie",
          "Ne pas dépendre d'une seule machine disponible un jour donné, et faire jouer la "
          "concurrence sur le prix comme sur les délais."],
         ["**Cinq ans de détention**", "L'année d'obsolescence présumée, et donc le coût annuel "
          "réel du poste",
          "Un poste à 840 € sur cinq ans coûte 168 € par an ; à 1 113 €, 222 €. L'écart de "
          "300 € à l'achat vaut 60 € par an — moins qu'une intervention sur site."],
         ["**Des prix illustratifs**", "La marge de négociation, et rien d'autre",
          "Les montants relevés sont des prix d'enseigne, pas des devis. Un devis constructeur "
          "ou grossiste les décale de 15 à 25 % à la baisse sur volume."]],
        [4.0, 5.2, 7.9], font=8.6, aligns=["l", "l", "l"], first_col_bold=False,
        caption="Les trois premiers principes structurent la dépense ; le quatrième protège la "
                "décision.")
    doc.spacer(0.2)
    doc.callout(
        "À quoi ça sert",
        "C'est le cadre d'acceptation : une offre qui ne respecte pas ces principes ne "
        "s'instruit pas, quelle que soit sa remise. À l'inverse, une offre qui les respecte "
        "mais sort du couloir de sa gamme reste recevable — elle est signalée, pas rejetée. "
        "C'est ce qui évite de renégocier le principe à chaque commande.")
    doc.p("**Ce que la grille garantit, concrètement.** Deux barrettes de mémoire et non une "
          "seule (15 à 20 % de performance en usage bureautique lourd), un disque NVMe et non "
          "un SATA, un processeur d'une génération datée et comparable en face, et une garantie "
          "de trois ans sur site. Quatre critères, tous vérifiables sur une fiche produit.",
          small=True)

    doc.pagebreak()
    # ------------------------------------------------------------------ 3 cibles techniques
    doc.h1_plain("3. Les cibles techniques, gamme par gamme")
    doc.p("C'est la grille que j'oppose à chaque offre. Elle reprend le cadrage validé, en "
          "insistant sur le double canal mémoire, qui conditionne la performance réelle bien "
          "plus que la fréquence affichée.", small=True)
    doc.table(["Critère", "Entrée de gamme", "Standard entreprise", "Confort"], SEUILS,
              SEUILS_WIDTHS, font=8.4, aligns=["l", "l", "l", "l"], first_col_bold=True,
              caption="Le profil opposable. La conformité de chaque machine, dans la section 5, "
                      "répond point par point à ces lignes.")
    doc.spacer(0.2)
    doc.callout(
        "À quoi ça sert",
        "Ce tableau transforme une préférence en critère. En réunion, il permet de dire « cette "
        "offre est conforme » ou « il lui manque le NVMe », sans discussion d'opinion. Il sert "
        "aussi à écarter sans état d'âme les machines hors sujet : un i5 de 12ᵉ génération ou "
        "un disque SATA ne s'instruisent pas, quel que soit le prix.")
    doc.p("**Trois précisions qui évitent les mauvaises surprises.** Le double canal n'est pas "
          "un détail : un poste livré en une seule barrette perd de l'ordre de 15 à 20 % en "
          "usage lourd. La DDR4 n'est tolérée qu'en entrée de gamme : au-delà, elle date la "
          "plateforme. Le format décide de l'évolutivité : un mini n'a pas de logement PCIe "
          "exploitable, donc pas de carte graphique — c'est ce qui rend la section 7 utile.",
          small=True)

    doc.pagebreak()
    # ------------------------------------------------------------------ 4 budget
    doc.h1_plain("4. Ce que le marché donne, gamme par gamme")
    doc.p("Les fourchettes ci-dessous sont celles des machines réellement chiffrées dans la "
          "note — ni des estimations, ni des prix de devis. Une gamme sans offre conforme se "
          "voit tout de suite : c'est le cas du confort.", small=True)
    doc.table(["Gamme", "Couloir", "Intel — €", "Intel — FCFA", "AMD — €",
               "AMD — FCFA"], _budget_rows(), [2.9, 2.1, 2.7, 3.1, 2.7, 3.1], font=7.6,
              aligns=["l", "l", "r", "r", "r", "r"], first_col_bold=True,
              caption="Relevés du 19 novembre 2026, TTC, port compris quand il est connu. "
                      "Conversion à 1 € = 655,957 FCFA, parité fixe. Montants arrondis à l'euro. Le reconditionné "
                      "(759,05 €) est exclu des fourchettes : il ne répond pas à la cible "
                      "« neuf ».")
    doc.spacer(0.2)
    doc.callout(
        "À quoi ça sert",
        "À situer une offre en dix secondes : en dessous de la fourchette, il manque quelque "
        "chose (mémoire, disque, garantie) ; au-dessus, on paie du format ou de la génération. "
        "Le confort est le seul couloir que le marché ne remplit pas — c'est une information "
        "de décision, pas un défaut de la note.")
    doc.p("**Deux constats.** En entrée de gamme, l'enveloppe suffit : deux offres neuves "
          "tiennent sous 850 €. En standard, elle suffit à 16 Go, pas à 32 Go — l'extension est "
          "un coût séparé sur toutes les marques. En confort, elle ne suffit plus : les seules "
          "configurations réellement conformes ne sont pas tarifées, et les machines chiffrées "
          "sont soit à 16 Go, soit au-delà de 1 500 €.", small=True)
    doc.p("**Le coût sur cinq ans, qui est le vrai chiffre.** Un poste à 840 € détenu cinq ans "
          "coûte 168 € par an ; un poste à 1 113 €, 222 €. L'écart de 273 € à l'achat vaut donc "
          "55 € par an et par poste — moins qu'une intervention sur site. Ce qui coûte cher, ce "
          "n'est pas la gamme haute du devis : c'est le poste qu'on remplace au bout de trois ans "
          "parce qu'il n'ouvre plus les fichiers du métier.", small=True)
    doc.p("**Et la marge de négociation.** Ces prix sont des prix d'enseigne. Sur un parc "
          "significatif, un devis constructeur ou grossiste les décale de 15 à 25 % à la baisse, "
          "soit 170 à 280 € par poste standard. C'est plus que l'écart entre les trois gammes : "
          "la négociation pèse plus lourd que le choix du modèle.", small=True)

    # ------------------------------------------------------------------ 5 cibles retenues
    for n, (nom, usage, couloir, rows, profil) in enumerate(GAMMES):
        doc.landscape(True) if n == 0 else doc.pagebreak()
        doc.h1_plain("5.%d  %s — %s" % (n + 1, nom, usage))
        doc.p("**%s** Couloir : %s. Les lignes surlignées en vert sont les cibles retenues pour "
              "cette gamme." % (profil, couloir), small=True)
        _catalogue(doc, rows)
        doc.spacer(0.08)
        doc.p(_lecture(nom), small=True)
        doc.p("**Comment s'en servir.** La ligne verte est le modèle à mettre au devis ; les "
              "lignes « à chiffrer » se demandent en devis, avec la référence constructeur ; la "
              "dernière colonne dit, en clair, ce qui manque à l'offre ou ce qui la disqualifie.",
              small=True)

    doc.landscape(False)

    # ------------------------------------------------------------------ 6 processeurs
    doc.h1_plain("6. Les processeurs, face à face par année et par génération")
    doc.p("Une comparaison Intel / AMD n'a de sens qu'à époque comparable. Ce tableau aligne "
          "les puces retenues par année de lancement et par génération, avec leur équivalent "
          "dans l'autre voie. Les dates sont celles des lancements constructeur, au trimestre "
          "près.", small=True)
    doc.table(CPU_HEADERS, CPU_ROWS, CPU_WIDTHS, font=7.9,
              aligns=["c", "l", "c", "l", "c", "l"],
              cell_fmt={(1, j): {"bg": VERT} for j in range(6)},
              caption="La ligne 2024 (14ᵉ génération / Ryzen 8000G) est la génération standard "
                      "retenue : c'est le meilleur rapport prix / durée de vie du relevé. La "
                      "ligne 2025 est conforme mais hors enveloppe.")
    doc.spacer(0.15)
    doc.table(EQUIV_HEADERS, EQUIV_ROWS, EQUIV_WIDTHS, font=7.9,
              aligns=["l", "l", "l", "c", "l"], first_col_bold=True,
              cell_fmt={(0, j): {"bg": VERT} for j in range(5)},
              caption="Correspondance des architectures : c'est sur cette base que les deux "
                      "voies sont comparées poste à poste.")
    doc.spacer(0.15)
    doc.callout(
        "À quoi ça sert",
        "À répondre, chiffres en main, à la question « pourquoi ne pas prendre le processeur le "
        "plus récent ? ». Parce qu'une génération de plus se paie 250 à 500 € et ne change rien "
        "à l'ouverture d'un classeur : sur ce profil, un i5 de 14ᵉ génération et un Ryzen 5 "
        "8000G se valent. Ce tableau sert aussi à dater l'obsolescence : sortie + 5 ans, soit "
        "2028 pour l'entrée de gamme et 2029 pour le confort.")
    doc.p("**Ce que ces puces disent du marché.** Sous 1 350 €, le neuf est presque "
          "exclusivement Intel : Raptor Lake 13ᵉ et 14ᵉ générations, en DDR5 partout sauf chez "
          "HP en entrée de gamme. AMD apparaît sur des plateformes plus récentes — AM5, DDR5, "
          "Zen 4 — mais sur un nombre de références distribué beaucoup plus étroit : deux "
          "châssis HP, deux Lenovo, aucun Dell. La voie se choisit donc par gamme, pas par "
          "doctrine.", small=True)

    doc.pagebreak()
    # ------------------------------------------------------------------ 7 chassis
    doc.h1_plain("7. Les formats de châssis, et ce qu'ils permettent")
    doc.p("Le format n'est pas un détail d'encombrement : c'est ce qui décide si le poste peut "
          "recevoir une carte graphique, un second disque, ou deux barrettes de plus. C'est le "
          "critère qui distingue vraiment les trois gammes.", small=True)
    doc.table(CHASSIS_HEADERS, CHASSIS_ROWS, CHASSIS_WIDTHS, font=8.2,
              aligns=["l", "l", "l", "l", "l", "c"], first_col_bold=True)
    doc.spacer(0.15)
    doc.callout(
        "À quoi ça sert",
        "À trancher la seule vraie question de format : a-t-on besoin d'une carte graphique "
        "dans les cinq ans ? Si non — c'est le cas de 90 % du parc bureautique — le mini est le "
        "bon choix : il coûte de l'ordre de 150 à 200 € de moins qu'un SFF à configuration "
        "voisine (HP standard : 1 055,99 € en mini, 1 251,58 € en SFF), il se fixe sous le "
        "bureau et il ne chauffe pas. Si oui, le confort impose le SFF ou la tour, et il faut "
        "l'assumer budgétairement dès le départ.")
    doc.p("**La règle que j'applique.** Entrée de gamme et standard : mini, sans état d'âme. "
          "Confort : SFF ou tour, parce que la clause « carte graphique si CAO 3D » ne peut pas "
          "être tenue autrement. Et dans tous les cas, deux barrettes de mémoire plutôt qu'une : "
          "c'est le seul « plus » technique qui se voit à l'usage et qui ne coûte rien au "
          "moment de la commande.", small=True)

    doc.pagebreak()
    # ------------------------------------------------------------------ 8 décision
    doc.h1_plain("8. Ce que je demande au comité")
    doc.p("**Trois décisions, dont une seule engage un budget nouveau.** Les deux premières "
          "entérinent ce qui est déjà instruit ; la troisième fixe le coût du confort.", lead=True)
    doc.table(
        ["Décision", "Ce que je propose", "Ce que cela engage"],
        [["**1. Valider les gammes**", "Entrée 650–850 €, standard 850–1 200 €, confort "
          "1 200–1 350 €, avec la grille de la section 3",
          "Aucun engagement financier : c'est le cadre qui permettra d'instruire les devis."],
         ["**2. Retenir les modèles**", "Entrée : Lenovo M70q Gen 5 (840,00 €) et M75q Gen 5 "
          "(849,00 €). Standard : Lenovo M75q Gen 5 Ryzen 7 (1 112,92 €), avec le HP Elite 800 "
          "G9 Mini (1 055,99 €) comme seconde source",
          "Le prix du poste standard, et la fin de la dépendance à une seule référence."],
         ["**3. Trancher le confort**", "Soit relever le plafond à 1 500 € pour obtenir un "
          "devis 32 Go / 1 To, soit commander 16 Go / 512 Go en le documentant",
          "La seule ligne budgétaire qui varie : de 0 € (renoncement) à environ 1 500 € par "
          "poste."]],
        [3.4, 8.2, 5.5], font=8.6, aligns=["l", "l", "l"],
        caption="Les montants sont ceux des tableaux de la section 5, tous frais de port "
                "compris quand ils sont connus.")
    doc.spacer(0.2)
    doc.p("**Le chiffrage de la cible 32 Go**, qui est l'arbitrage financier de ce comité :",
          small=True)
    doc.table(["Poste de coût", "Prix", "Prix FCFA", "Nature du prix"], [
        ["Lenovo M75q Gen 5 — Ryzen 7 PRO 8700GE, 16 Go DDR5, 512 Go NVMe",
         eur(1112.92), fcfa(1112.92), "Relevé du 19 novembre, neuf, livré"],
        ["Extension 1 × 16 Go DDR5 SO-DIMM", "≈ 250 €", fcfa(250),
         "Ordre de prix du marché, à confirmer par devis"],
        ["**Total cible 32 Go / 512 Go**", "**≈ %s**" % eur(1112.92 + 250),
         "**≈ %s**" % fcfa(1112.92 + 250),
         "**Dépassement de %s** — à arbitrer" % eur(1112.92 + 250 - 1350)],
    ], [7.4, 2.6, 3.1, 4.0], font=8.2, aligns=["l", "r", "r", "l"],
        caption="« ≈ » marque un ordre de prix, non un relevé.")
    doc.spacer(0.2)
    doc.p("**Trois conditions, à faire figurer au devis.** Le montage mémoire : les 16 Go "
          "doivent être livrés en une barrette de 16 Go, sinon l'extension impose de remplacer "
          "les deux. Le prix de l'extension : une barrette SO-DIMM DDR5 de 16 Go se situe "
          "autour de 250 € au détail. La garantie : trois ans sur site, pièces et main-d'œuvre, "
          "exigés — c'est ce qui distingue une offre constructeur d'une offre de place de "
          "marché.", small=True)
    doc.spacer(0.3)
    doc.p("**Ce que le comité ne tranche pas aujourd'hui.** Le nombre de postes par gamme, le "
          "choix de l'écran et du clavier (hors périmètre), et la stratégie d'enlèvement. Ces "
          "trois points pèsent sur le prix final plus que la marque retenue.", small=True)
    doc.spacer(0.4)
    doc.p("Joël MBA OYONE — GED-SERVICES, services informatiques · 19 novembre 2026", small=True)

    dpath, ppath = doc.save(OUTDIR)
    return dpath, ppath


def _lecture(nom):
    return {
        "Entrée de gamme":
            "**Lecture de la gamme.** Cinq machines sont chiffrées. Deux sont neuves, conformes "
            "et dans le couloir : le M70q Gen 5 en Intel (840,00 €) et le M75q Gen 5 en AMD "
            "(849,00 €), tous deux en DDR5 côté AMD. Le HP Pro 400 G9 sort à 943,61 € pour du "
            "DDR4 et du SATA ; le seul Dell chiffré est reconditionné à 759,05 €. "
            "**La décision proposée est de rester chez Lenovo** : même châssis, deux "
            "plateformes, un seul jeu de pièces détachées.",
        "Standard entreprise":
            "**Lecture de la gamme.** Trois offres neuves en DDR5 tiennent le profil, toutes à "
            "16 Go : Dell OptiPlex 7020 MFF à 999,95 €, HP Elite 800 G9 Mini à 1 055,99 €, "
            "Lenovo M75q Gen 5 Ryzen 7 à 1 112,92 €. Le 32 Go de la cible est un coût séparé "
            "sur les trois. Deux machines sortent du jeu : le M90q Gen 5 Intel à 1 470,45 € "
            "(hors enveloppe de 120,45 €) et l'Elite 805 G9 AMD à 1 251,58 €, hors couloir et "
            "livré en QWERTZ.",
        "Confort":
            "**Lecture de la gamme.** Aucune offre chiffrée ne réunit 32 Go, 1 To et un i7 sous "
            "1 350 €. Le HP Pro Mini 400 G9 (1 109,30 €) tient la puce et le prix mais seulement "
            "16 Go ; l'Elite Mini 800 G9 à 2 111,27 € et le M90q Gen 6 à 1 624,88 € sont hors "
            "enveloppe. **Les cibles retenues sont donc à chiffrer en devis** : Dell Pro Micro "
            "QCM1250 en Intel et Lenovo M75t Gen 5 en AMD, toutes deux en 32 Go / 1 To.",
    }[nom]


if __name__ == "__main__":
    print(build_doc())
