# -*- coding: utf-8 -*-
"""Profil ciblé, catalogue et face-à-face Intel / AMD — version alpha.

Trois temps : le profil technique opposable (trois gammes), le catalogue des
postes qui y répondent (trois constructeurs, deux plateformes), puis
l'arbitrage — tarifs Intel et AMD face à face, configuration par configuration.

Les prix sont des relevés du 5 novembre 2026, portés ici à titre illustratif.
Aucun montant n'est estimé : là où rien n'a été trouvé, la case le dit.
"""
from __future__ import annotations

import os

from render import Doc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "livrables")
BASE = "Postes_fixes_profil_cible_et_catalogue_Intel_AMD_alpha"
TVA = 655.957

G, Y, O, N = "g", "y", "o", "n"
FMT = {
    "g": {"bg": "D8EDCB", "color": "1E6B33"},
    "y": {"bg": "FAEBB8", "color": "7A5E12"},
    "o": {"bg": "F8CDB6", "color": "A23B1A"},
    "n": {"bg": "E6E8EC", "color": "555B66"},
}
TINT_PAIR = ["EDF2F7", "FFFFFF", "EFF4EE"]      # trois paires de lignes


# --------------------------------------------------------------------------- #
def _eur(x):
    ent, dec = ("%.2f" % x).split(".")
    out, i = "", 0
    for ch in reversed(ent):
        if i and i % 3 == 0:
            out = "\u00A0" + out
        out = ch + out
        i += 1
    return out + "," + dec + "\u00A0€"


def _fcfa(x):
    n = "%d" % int(round(x))
    out, i = "", 0
    for ch in reversed(n):
        if i and i % 3 == 0:
            out = "\u00A0" + out
        out = ch + out
        i += 1
    return out + "\u00A0FCFA"


def _pct(a, b):
    return ("%.1f" % ((a - b) / b * 100.0)).replace(".", ",")


def _r(constructeur, voie, modele, etat, cpu, coeurs, fbase, fturbo, ram, disque,
       revendeur, prix, conformite, lien, code):
    return {
        "constructeur": constructeur, "voie": voie, "modele": modele, "etat": etat,
        "cpu": cpu, "coeurs": coeurs, "fbase": fbase, "fturbo": fturbo, "ram": ram,
        "disque": disque, "revendeur": revendeur, "prix": prix,
        "fcfa": int(round(prix * TVA)) if prix else None,
        "conformite": conformite, "lien": lien, "code": code,
    }


# --------------------------------------------------------------------------- #
# Catalogue : six voies par gamme — HP, Dell, Lenovo × Intel / AMD.
# --------------------------------------------------------------------------- #
ENTREE = [
    _r("HP", "Intel", "Pro 400 G9 SFF", "Neuf", "Core i5-13500", "14C / 20T",
       "2,5 GHz", "4,8 GHz", "16 Go · DDR4 · fréq. n. c.",
       "512 Go · SATA · SSD + lecteur DVD", "Amazon", 1039.22,
       "Partielle — DDR4 au lieu de DDR5, et SATA au lieu de NVMe",
       "[ouvrir](https://www.amazon.fr/dp/B0D4F6739P)", Y),
    _r("HP", "AMD", "ProDesk 2 G1a — Ryzen 5 8500G", "Neuf", "Ryzen 5 8500G",
       "6C / 12T", "3,5 GHz", "5,0 GHz", "16 Go · DDR5 (plateforme AM5)",
       "512 Go · SSD (interface n. c.)", "Amazon (vendeur tiers)", 827.52,
       "Partielle — 8500G au lieu du 8600G cité ; vendeur tiers, clavier et garantie à vérifier",
       "[ouvrir](https://www.amazon.fr/dp/B0FR3R6P42)", Y),
    _r("Dell", "Intel", "OptiPlex 7010 Micro", "Reconditionné", "Core i5-13500T",
       "14C / 20T", "1,6 GHz", "4,6 GHz", "16 Go · DDR4 3200 MHz",
       "512 Go · NVMe · SSD", "Amazon", 689.83,
       "Partielle — version T 35 W, DDR4, et reconditionné",
       "[ouvrir](https://www.amazon.fr/dp/B0HKDSCK9X)", Y),
    _r("Dell", "AMD", "—", "—", "—", "—", "—", "—", "—", "—", "—", None,
       "Pas d'offre AMD sur OptiPlex : fait de catalogue, pas un oubli", "—", N),
    _r("Lenovo", "Intel", "ThinkCentre M70q Gen 5 Tiny", "Neuf", "Core i5-13500T",
       "14C / 20T", "1,6 GHz", "4,6 GHz", "16 Go · DDR4 3200 MHz",
       "512 Go · NVMe · SSD", "Materiel.net", None,
       "À chiffrer — aucun prix relevé chez les cinq enseignes",
       "[fiche](https://www.materiel.net/recherche/thinkcentre%20m70q%20gen%205/)", O),
    _r("Lenovo", "AMD", "ThinkCentre M75q Gen 5 Tiny", "Neuf", "Ryzen 5 PRO 8500GE",
       "6C / 12T", "3,4 GHz", "5,0 GHz", "16 Go · DDR5 · fréq. n. c.",
       "512 Go · NVMe · SSD", "Cdiscount", 763.67,
       "Conforme — DDR5 tenue ; 8500GE au lieu du 8600G cité",
       "[ouvrir](https://www.cdiscount.com/informatique/achat-pc-ordinateur/lenovo-thinkcentre-m75q-gen-5/f-1070853-aabod39488.html)", G),
]

STANDARD = [
    _r("HP", "Intel", "Elite 800 G9 Mini", "Neuf", "Core i5-14500", "14C / 20T",
       "2,6 GHz", "5,0 GHz", "16 Go · DDR5 SO-DIMM · fréq. n. c.",
       "512 Go · NVMe · SSD", "Amazon", 1140.18,
       "Conforme sur 16 Go — les 32 Go de la cible restent à ajouter",
       "[ouvrir](https://www.amazon.fr/dp/B0D76M6T6R)", G),
    _r("HP", "AMD", "Elite 805 G9 SFF — Ryzen 7 8700G", "Neuf", "Ryzen 7 8700G",
       "8C / 16T", "4,2 GHz", "5,1 GHz", "16 Go · DDR5 5600 MHz",
       "512 Go · NVMe · SSD", "Amazon", 1528.34,
       "Partielle — hors plafond (1 528,34 €), clavier QWERTZ",
       "[ouvrir](https://www.amazon.fr/dp/B0DHLD7ZWM)", O),
    _r("Dell", "Intel", "OptiPlex 7070 Micro + écran 27\"", "Reconditionné",
       "Core i9 9ᵉ gén.", "8C / 16T", "n. c.", "5,0 GHz",
       "16 Go · DDR4 · fréq. n. c.", "512 Go · NVMe · SSD + écran 27\" inclus",
       "Amazon", 790.91,
       "Hors millésime — plateforme 2019, 16 Go seulement",
       "[ouvrir](https://www.amazon.fr/dp/B0H415LBD6)", O),
    _r("Dell", "AMD", "—", "—", "—", "—", "—", "—", "—", "—", "—", None,
       "Pas d'offre AMD sur OptiPlex : fait de catalogue, pas un oubli", "—", N),
    _r("Lenovo", "Intel", "ThinkCentre M90q Gen 5 Tiny", "Neuf", "Core i5-14500T",
       "14C / 20T", "1,8 GHz", "4,8 GHz", "32 Go · DDR5 · fréq. n. c.",
       "1 To · NVMe · SSD", "Fnac", None,
       "À chiffrer — configuration retenue, aucune offre chiffrée",
       "[fiche](https://www.fnac.com/SearchResult/ResultList.aspx?Search=thinkcentre%20m90q%20gen%205)", O),
    _r("Lenovo", "AMD", "ThinkCentre M75q Gen 5 Tiny — Ryzen 7 PRO 8700GE", "Neuf",
       "Ryzen 7 PRO 8700GE", "8C / 16T", "3,6 GHz", "5,1 GHz",
       "16 Go · DDR5 · fréq. n. c.", "512 Go · NVMe · SSD", "Cdiscount", 1139.49,
       "Conforme sur 16 Go — le 32 Go de la cible reste à ajouter",
       "[ouvrir](https://www.cdiscount.com/informatique/achat-pc-ordinateur/mini-pc-lenovo/f-1070853-aabtn40622.html)", G),
]

CONFORT = [
    _r("HP", "Intel", "Pro Mini 400 G9 — i7-14700T", "Neuf", "Core i7-14700T",
       "20C / 28T", "1,3 GHz", "5,2 GHz", "16 Go · DDR (type n. c.)",
       "512 Go · NVMe · SSD", "Amazon", 1286.14,
       "Partielle — version T 35 W ; 16 Go et 512 Go à porter à 32 Go / 1 To",
       "[ouvrir](https://www.amazon.fr/dp/B0D7424V46)", Y),
    _r("HP", "AMD", "Elite 805 G9 SFF — Ryzen 7 8700G", "Neuf", "Ryzen 7 8700G",
       "8C / 16T", "4,2 GHz", "5,1 GHz", "16 Go · DDR5 5600 MHz",
       "512 Go · NVMe · SSD", "Amazon", 1528.34,
       "Partielle — 16 Go / 512 Go au lieu de 32 Go / 1 To, et hors plafond",
       "[ouvrir](https://www.amazon.fr/dp/B0DHLD7ZWM)", O),
    _r("Dell", "Intel", "Dell Pro Micro QCM1250 — i7-14700T", "Neuf", "Core i7-14700T",
       "20C / 28T", "1,8 GHz", "4,8 GHz", "32 Go · DDR5 (configuration visée)",
       "1 To · NVMe · SSD", "Dell (site constructeur)", None,
       "À devis — la fiche affiche « voir les options », sans prix",
       "[ouvrir](https://www.dell.com/fr-fr/search/dell%20pro%20micro%20qcm1250)", O),
    _r("Dell", "AMD", "—", "—", "—", "—", "—", "—", "—", "—", "—", None,
       "Pas d'offre AMD sur OptiPlex : fait de catalogue, pas un oubli", "—", N),
    _r("Lenovo", "Intel", "ThinkCentre M90q Gen 6 Tiny", "Neuf", "Core Ultra 7 265",
       "20C / 20T", "2,4 GHz", "5,3 GHz", "n. c. — configuration non publiée",
       "n. c. — configuration non publiée", "Cdiscount", 1624.88,
       "Hors enveloppe — 1 624,88 € pour un plafond de 1 300 €",
       "[fiche](https://www.cdiscount.com/search/10/thinkcentre+m90q+gen+6.html)", O),
    _r("Lenovo", "AMD", "ThinkCentre M75q Gen 5 — 32 Go / 1 To", "Neuf",
       "Ryzen 7 PRO 8700GE", "8C / 16T", "3,6 GHz", "5,1 GHz",
       "32 Go · DDR5 (configuration visée)", "1 To · NVMe · SSD", "Cdiscount", None,
       "À chiffrer — la version 32 Go / 1 To n'est pas distribuée en ligne",
       "[fiche](https://www.cdiscount.com/search/10/thinkcentre+m75q+gen+5.html)", O),
]

# --------------------------------------------------------------------------- #
HEADERS = ["Constructeur", "Voie", "Modèle", "État", "CPU", "Cœurs /\nthreads",
           "Fréq.\nbase", "Fréq.\nturbo", "RAM — capacité · type · fréquence",
           "Disque — capacité · interface · type", "Revendeur", "Prix livré €",
           "Prix FCFA", "Conformité au profil", "Lien"]
WIDTHS = [3.4, 1.8, 4.6, 3.4, 4.0, 2.3, 2.0, 2.2, 5.5, 5.5, 3.0, 2.9, 3.4, 5.7, 1.9]
ALIGNS = ["l", "c", "l", "c", "l", "c", "c", "c", "l", "l", "l", "r", "r", "l", "c"]

F2F_HEADERS = ["Constructeur", "Voie Intel — modèle et prix livré",
               "Voie AMD — modèle et prix livré", "Écart AMD − Intel", "Ce que l'écart achète"]
F2F_WIDTHS = [3.4, 10.6, 10.6, 6.4, 8.8]

REP_HEADERS = ["Processeur", "Cœurs", "Threads", "Turbo", "Carte graphique intégrée",
               "Ce que la puce sait faire de mieux"]
REP_WIDTHS = [6.4, 3.0, 3.0, 3.4, 6.6, 16.6]

PROFIL_HEADERS = ["Gamme", "Usage", "Millésime", "Intel", "AMD", "Mémoire",
                  "Stockage", "GPU", "Garantie"]
PROFIL_WIDTHS = [2.2, 3.2, 2.6, 3.0, 3.0, 2.3, 2.2, 1.3, 2.2]
PROFIL_ROWS = [
    ["Entrée de gamme", "Accueil, saisie, consultation",
     "≥ 2023", "i5-13400 (10C) ou i5-13500 (14C)", "Ryzen 5 8600G / 9600X (6C)",
     "16 Go DDR5", "512 Go NVMe", "iGPU", "3 ans"],
    ["Standard — référence", "Bureautique intensive : Sage, Teams, multi-applications",
     "≥ 2024", "« Core i5 14ᵉ » : i5-14400 (10C) ou i5-14500 (14C)",
     "Ryzen 5 8600G / 9600X (6C)", "16 Go DDR5 plancher, 32 Go cible",
     "512 Go NVMe", "Indifférent", "3 ans"],
    ["Confort / longue durée", "Postes gardés cinq ans, CAO légère, gros tableurs",
     "≥ 2025", "i7-14700 (20C)", "Ryzen 7 8700G / 9700X (8C)",
     "32 Go DDR5", "1 To NVMe", "iGPU ; GPU 6 Go si CAO 3D", "3 ans"],
]

# Repères de calcul, par gamme : aucune note chiffrée n'est affichée, faute de mesure.
REPERES = {
    "entree": [
        ["Core i5-13500 / 13500T", "6 P + 8 E", "20", "4,8 / 4,6 GHz", "UHD 770",
         "Le multi-thread le plus large de la gamme, sans coût supplémentaire."],
        ["Ryzen 5 PRO 8500GE", "6", "12", "5,0 GHz", "Radeon 740M",
         "Six cœurs rapides, un graphique supérieur à l'UHD 770, un tiers de threads en moins."],
        ["Ryzen 5 8500G", "2 + 4 c", "12", "5,0 GHz", "Radeon 740M",
         "Deux cœurs rapides et quatre d'appoint : en dessous du 8600G, suffisant pour l'accueil."],
        ["Ryzen 5 PRO 8600G", "6", "12", "5,0 GHz", "Radeon 760M",
         "Même dessin que le 8500GE, avec un graphique encore au-dessus : le meilleur iGPU de la gamme."],
    ],
    "standard": [
        ["Core i5-14500 / 14500T", "6 P + 8 E", "20", "5,0 / 4,8 GHz", "UHD 770",
         "Vingt threads : la référence de la gamme, et le meilleur rendement en bureautique lourde."],
        ["Ryzen 7 PRO 8700GE", "8", "16", "5,1 GHz", "Radeon 780M",
         "Huit cœurs homogènes et le graphique le plus solide : à préférer si l'affichage compte."],
        ["Ryzen 7 8700G", "8", "16", "5,1 GHz", "Radeon 780M",
         "Le même, en 65 W : plus libre de monter en fréquence que la version GE bridée."],
    ],
    "confort": [
        ["Core i7-14700T", "8 P + 12 E", "28", "5,2 GHz", "UHD 770",
         "Vingt-huit threads en 35 W : le plus large de tout le document."],
        ["Core Ultra 7 265", "8 P + 12 E", "20", "5,3 GHz", "Graphics intégrée",
         "Sans hyper-threading : moins de threads, mais une architecture plus récente et plus sobre."],
        ["Ryzen 7 8700G / 8700GE", "8", "16", "5,1 GHz", "Radeon 780M",
         "Le meilleur graphique intégré du document — l'argument décisif si la CAO 3D reste au périmètre."],
    ],
}

# Face-à-face : lignes par gamme, calculées à partir des prix du catalogue.
F2F = {
    "entree": [
        ["HP", "Pro 400 G9 SFF — i5-13500", 1039.22,
         "ProDesk 2 G1a — Ryzen 5 8500G", 827.52,
         "211 € de moins, et la DDR5 que le HP Intel n'a pas — au prix d'une puce plus faible."],
        ["Dell", "OptiPlex 7010 Micro — i5-13500T, reconditionné", 689.83,
         "—", None,
         "Pas de comparaison possible : Dell n'a pas d'OptiPlex AMD. Le prix Intel est celui d'un reconditionné."],
        ["Lenovo", "M70q Gen 5 — i5-13500T", None,
         "M75q Gen 5 — Ryzen 5 PRO 8500GE", 763.67,
         "Le seul Lenovo chiffré de la gamme, et le moins cher des deux AMD en DDR5."],
    ],
    "standard": [
        ["HP", "Elite 800 G9 Mini — i5-14500", 1140.18,
         "Elite 805 G9 SFF — Ryzen 7 8700G", 1528.34,
         "Un châssis SFF extensible et un graphique Radeon 780M, payés 388 € de plus."],
        ["Dell", "OptiPlex 7070 Micro — i9 9ᵉ gén., reconditionné", 790.91,
         "—", None,
         "Pas de comparaison : Dell ne propose pas d'AMD sur cette famille."],
        ["Lenovo", "M90q Gen 5 — i5-14500T, 32 Go / 1 To", None,
         "M75q Gen 5 — Ryzen 7 PRO 8700GE, 16 Go / 512 Go", 1139.49,
         "L'AMD chiffré tient l'enveloppe sur 16 Go ; l'Intel n'a pas de prix."],
    ],
    "confort": [
        ["HP", "Pro Mini 400 G9 — i7-14700T", 1286.14,
         "Elite 805 G9 SFF — Ryzen 7 8700G", 1528.34,
         "28 threads contre 16, mais 512 Go et un format mini sans PCIe : l'AMD n'apporte pas la mémoire."],
        ["Dell", "Dell Pro Micro QCM1250 — i7-14700T, 32 Go / 1 To", None,
         "—", None,
         "Seule voie Dell conforme sur le papier, et sans prix publié."],
        ["Lenovo", "M90q Gen 6 — Core Ultra 7 265", 1624.88,
         "M75q Gen 5 — Ryzen 7 PRO 8700GE, 32 Go / 1 To", None,
         "Ni l'une ni l'autre ne tient le plafond : 1 624,88 € pour l'Intel, rien de chiffré pour l'AMD."],
    ],
}

GAMMES = [
    ("entree", "Tableau 1 — Entrée de gamme : accueil, saisie, consultation", ENTREE,
     "16 Go DDR5 · 512 Go NVMe · millésime 2023 ou plus récent · 650 à 850 €"),
    ("standard", "Tableau 2 — Standard de référence : bureautique intensive", STANDARD,
     "16 Go DDR5 en plancher, 32 Go en cible · 512 Go NVMe · millésime 2024 ou plus récent"),
    ("confort", "Tableau 3 — Confort : postes gardés cinq ans", CONFORT,
     "32 Go DDR5 · 1 To NVMe · millésime 2025 ou plus récent · plafond 1 300 €"),
]

LECTURE = {
    "entree": "**Ce que la gamme montre.** Les deux voies AMD tiennent la DDR5 — **827,52 € chez HP, "
              "763,67 € chez Lenovo** — et les deux voies Intel chiffrées sont en DDR4, dont un "
              "disque SATA chez HP. La voie AMD est donc la seule qui réponde au profil dans cette "
              "gamme, et elle est aussi la moins chère. La réserve ne porte pas sur la mémoire mais "
              "sur la puce : un 8500G et un 8500GE sont en dessous du 8600G cité par la spécification.",
    "standard": "**Ce que la gamme montre.** La paire HP est la seule comparable à configuration "
                "voisine : même 16 Go DDR5, même 512 Go, **1 140,18 € en Intel, 1 528,34 € en AMD**, "
                "soit **+388,16 € (+34,0 %)**. L'écart n'achète pas la mémoire — les deux sont à 16 Go — "
                "mais un châssis SFF extensible et une Radeon 780M.",
    "confort": "**Ce que la gamme montre.** Aucune des six voies ne livre 32 Go et 1 To sous "
               "1 300 €. Le moins cher des conformes sur la puce est le HP Intel à 1 286,14 €, "
               "mais en 16 Go / 512 Go : la mise à niveau le portera au-delà du plafond. Le confort "
               "reste une spécification sans budget.",
}


# --------------------------------------------------------------------------- #
def _catalogue(doc, rows):
    body, cf = [], {}
    for i, r in enumerate(rows):
        body.append([r["constructeur"], r["voie"], r["modele"], r["etat"], r["cpu"],
                     r["coeurs"], r["fbase"], r["fturbo"], r["ram"], r["disque"],
                     r["revendeur"],
                     _eur(r["prix"]) if r["prix"] else "—",
                     _fcfa(r["fcfa"]) if r["fcfa"] else "—",
                     r["conformite"].replace(" €", "\u00A0€"),
                     r["lien"] if r["lien"] else "—"])
        tint = TINT_PAIR[i // 2 % 3]
        for c in range(len(HEADERS)):
            cf[(i, c)] = {"bg": tint}
        cf[(i, 0)] = {"bg": tint, "b": True}
        cf[(i, 1)] = {"bg": "EDE3F2" if r["voie"] == "AMD" else "E3ECF7", "b": True}
        cf[(i, 13)] = FMT[r["code"]]
    doc.table(HEADERS, body, WIDTHS, font=8.2, header_bg="1F3B63", aligns=ALIGNS,
              header=True, cell_fmt=cf)


def _f2f(doc, rows, caption):
    body, cf = [], {}
    for i, (cons, mi, pi, ma, pa, verdict) in enumerate(rows):
        cel_i = (mi + " — " + (_eur(pi) if pi else "prix non relevé"))
        cel_a = ("—" if ma == "—" else ma + " — " + (_eur(pa) if pa else "prix non relevé"))
        if pi and pa:
            signe = "+" if pa >= pi else "−"
            pv = ("%.1f" % (abs(pa - pi) / pi * 100.0)).replace(".", ",")
            ecart = "%s  (%s%s %%)" % (signe + _eur(abs(pa - pi)), signe, pv)
            cf[(i, 3)] = FMT[G] if pa < pi else FMT[O]
        else:
            ecart = "n. c."
            cf[(i, 3)] = FMT[N]
        body.append([cons, cel_i, cel_a, ecart, verdict])
        cf[(i, 0)] = {"b": True}
        cf[(i, 1)] = {"bg": "E3ECF7"}
        cf[(i, 2)] = {"bg": "EDE3F2"}
    doc.table(F2F_HEADERS, body, F2F_WIDTHS, font=8.4, header_bg="1F3B63",
              aligns=["l", "l", "l", "c", "l"], cell_fmt=cf, caption=caption)


def build_doc():
    doc = Doc(
        base=BASE,
        title="Profil ciblé, catalogue, face-à-face Intel / AMD",
        subtitle="Spécifier, chiffrer, arbitrer — version alpha",
        meta=[],
        doc_ref="GED-POSTES-2026-11-C · version alpha · Confidentiel — usage interne",
        footer="GED-SERVICES · profil ciblé, catalogue, face-à-face Intel / AMD",
    )

    doc.cover(
        eyebrow="Postes fixes — spécification et arbitrage · version alpha",
        title="Le profil,\nle catalogue,\nle face-à-face",
        subtitle="Spécifier le poste fixe à approvisionner, descendre cette spécification sur six "
                 "voies réelles — trois constructeurs, deux plateformes — puis mettre les tarifs "
                 "Intel et AMD face à face pour que l'arbitrage se fasse sur des chiffres.",
        meta_rows=[
            ["Destinataire", "**M. Jad, directeur général — ADCHIM**"],
            ["Émetteur", "**Joël MBA OYONE — GED-SERVICES**"],
            ["Objet", "Spécifier le profil technique des postes fixes, puis l'illustrer par un "
                      "catalogue chiffré et un face-à-face Intel / AMD"],
            ["Profil", "Trois gammes : **entrée de gamme, standard de référence, confort**"],
            ["Catalogue", "**Six voies par gamme** : HP, Dell, Lenovo × Intel, AMD"],
            ["Prix", "Relevés le **5 novembre 2026**, TTC, port compris ; valeur **illustrative** — "
                     "de quoi arbitrer, pas de quoi contractualiser"],
            ["Conversion", "**1 € = 655,957 FCFA**, parité fixe"],
            ["État", "Chaque ligne porte **Neuf** ou **Reconditionné**"],
            ["Lecture", "**n. c.** = non communiqué par l'annonce, jamais déduit"],
            ["Statut", "**Version alpha** — la structure est arrêtée, les relevés sont à compléter"],
        ],
        pagebreak=True,
    )

    # ------------------------------------------------------------------ objet
    doc.h1_plain("Objet du livrable")
    doc.p("Ce document a un objet unique : **spécifier le profil technique des postes fixes à "
          "approvisionner**, puis **le confronter au marché** pour que la décision se prenne sur "
          "des machines et des prix, non sur des intentions.", lead=True)
    doc.p("Il se lit en trois temps, et chaque temps a ses tableaux.", small=True)
    doc.ul([
        "**Le profil** — page suivante. Les trois seuils opposables : entrée de gamme, standard de "
        "référence, confort. Un poste qui ne les tient pas n'entre pas dans la commande, quel que "
        "soit son prix.",
        "**Le catalogue** — **tableaux 1, 2 et 3**, un par gamme. Chaque gamme est descendue sur "
        "**six voies** : trois constructeurs imposés — HP, Dell, Lenovo — croisés avec deux "
        "plateformes, Intel et AMD. Le modèle, l'état, le processeur, la mémoire, le disque, le "
        "revendeur, le prix en euros et en francs CFA, la conformité et le lien y figurent ligne à ligne.",
        "**L'arbitrage** — sous chaque catalogue, **un face-à-face des tarifs Intel et AMD** "
        "configuration par configuration, puis une lecture par gamme. La synthèse de la page 8 "
        "tranche entre les deux voies et dit ce que chaque écart achète.",
    ], small=True)

    doc.spacer(0.15)
    doc.p("**Ce que valent les prix.** Ils sont **réellement relevés** chez les enseignes citées, mais "
          "ils n'ont ici qu'une **valeur illustrative** : ils servent à arbitrer entre deux voies "
          "techniques, pas à engager une commande. Un devis constructeur ou grossiste décalera ces "
          "montants de 15 à 25 % à la baisse sur volume, et davantage à la hausse sur délai tendu. "
          "Chaque prix porte sa date de relevé, et chaque case vide est une case où rien n'a été "
          "trouvé : **aucun montant n'est estimé**.", small=True)

    doc.spacer(0.15)
    doc.p("**Comment se lisent les couleurs.** Trois états, jamais confondus, et deux teintes de voie.",
          small=True)
    doc.table([], [["Vert — conforme au profil", "Jaune — partielle : un point manque, chiffrable",
                    "Orange — hors seuil ou non chiffrée", "Gris — la voie n'existe pas"]],
              [1, 1, 1, 1], font=7.2, header=False, zebra=False,
              cell_fmt={(0, 0): FMT[G], (0, 1): FMT[Y], (0, 2): FMT[O], (0, 3): FMT[N]})
    doc.table([], [["Fond bleu clair — voie Intel", "Fond violet clair — voie AMD"]],
              [1, 1], font=7.2, header=False, zebra=False,
              cell_fmt={(0, 0): {"bg": "E3ECF7", "color": "1F3B63"},
                        (0, 1): {"bg": "EDE3F2", "color": "5B3B6E"}})

    doc.spacer(0.3)
    doc.h2("Ce que cette version alpha ne fait pas encore")
    doc.ul([
        "**Trois prix manquent** : M70q Gen 5, M90q Gen 5, et le M75q Gen 5 en 32 Go / 1 To. "
        "Ils sont signalés « à chiffrer », jamais estimés.",
        "**Aucun devis ferme.** Un prix d'enseigne n'engage personne ; le devis Dell du confort, "
        "comme les remises volume, restent à demander.",
        "**Aucune mesure de performance.** Les repères des planches décrivent l'architecture — "
        "cœurs, threads, fréquence, classe de graphique — et ne prétendent pas à un score.",
        "**Aucune volumétrie.** Le document chiffre un poste, pas un parc : sans le nombre de "
        "postes par gamme, l'arbitrage budgétaire reste ouvert.",
    ], small=True)

    # ------------------------------------------------------------------ profil
    doc.pagebreak()
    doc.h1_plain("Le profil technique ciblé")
    doc.p("L'enveloppe est fixée **entre 650 € et 1 300 € par poste**, écran non compris, pour des "
          "postes fixes de marque HP, Dell ou Lenovo, sous Windows 11 Professionnel, clavier AZERTY, "
          "avec une garantie de trois ans. Les trois gammes se distinguent par la charge, pas par le "
          "confort d'usage.", small=True)
    doc.table(PROFIL_HEADERS, PROFIL_ROWS, PROFIL_WIDTHS, font=7.2,
              aligns=["l", "l", "c", "l", "l", "l", "l", "l", "c"], first_col_bold=True,
              caption="Le seuil par gamme, tel que la spécification le fixe. C'est lui qui sert de "
                      "juge aux tableaux 1 à 3 : la colonne « Conformité » y répond point par point.")
    doc.p("**Deux réserves de méthode, à trancher avant la commande.**", small=True)
    doc.ul([
        "**Le millésime « ≥ 2025 » du confort exclut la puce qu'il cite.** L'i7-14700 et le Core "
        "Ultra 7 série 2 sont des plateformes 2023-2024 ; exiger 2025 revient à sortir de la liste "
        "le processeur inscrit dans la même ligne. Il faut choisir : le millésime du châssis, ou "
        "celui de la puce.",
        "**Deux dates de la spécification sont fausses** et sont reprises telles quelles dans ce "
        "document, sans correction d'autorité : le i5-13400/13500 est de **janvier 2023** et non "
        "d'octobre 2022 (octobre 2022 = les versions K) ; l'i7-14700 non-K est de **janvier 2024** "
        "et non d'octobre 2023.",
        "**Le format Tiny n'a pas de logement PCIe exploitable.** La clause « GPU dédié 6 Go si CAO "
        "3D » devient donc inapplicable sur M75q ou M90q, comme sur un OptiPlex Micro : si la CAO "
        "est réelle, le confort doit s'imposer en SFF ou en tour.",
    ], small=True)

    # ------------------------------------------------------------------ marché
    doc.pagebreak()
    doc.h1_plain("Le marché, tel qu'il a été relevé")
    doc.p("Cinq enseignes classiques — Amazon, Fnac, Cdiscount, LDLC, Materiel.net — plus les sites "
          "constructeur. Le relevé porte sur les six voies de chaque gamme, sans exception : quand "
          "une voie n'existe pas chez une enseigne, c'est écrit, ce n'est pas comblé.", small=True)
    doc.table(["Enseigne", "Ce qu'elle donne sur ces références", "Voies servies"], [
        ["Amazon.fr", "Les seules offres Dell chiffrées, dont les deux reconditionnées. Attention : "
                      "le HP Elite 805 G9 y est vendu en **clavier QWERTZ**, et certaines annonces "
                      "sont expédiées par des tiers en import.", "HP, Dell"],
        ["Cdiscount", "La voie AMD de Lenovo, seule plateforme AMD réellement distribuée sur les "
                      "trois gammes, et le M90q Gen 6 hors enveloppe.", "Lenovo"],
        ["Materiel.net", "Les ThinkCentre Intel figurent au catalogue sans prix affiché pour la "
                         "configuration visée ; la recherche ProDesk 405 G9 ne rend rien.", "Lenovo, HP"],
        ["Fnac", "Le M90q Gen 5 en 32 Go / 1 To est annoncé, aucune offre chiffrée ne correspond.",
         "Lenovo"],
        ["LDLC", "Aucune offre sur les châssis G9 et G10 au moment du relevé.", "—"],
        ["Site Dell", "Les configurations existent, le prix passe par un devis.", "Dell"],
    ], [2.8, 11.0, 3.3], font=7.6, aligns=["l", "l", "c"], first_col_bold=True,
        caption="L'état du relevé, enseigne par enseigne. Trois constats en sortent, et ils pèsent "
                "plus lourd que les prix.")
    doc.ul([
        "**La voie AMD n'est pas distribuée de la même façon chez les trois constructeurs.** Lenovo "
        "la vend en ligne (M75q Gen 5, trois gammes) ; HP en propose deux — une tour d'entrée en "
        "8500G à 827,52 € et une SFF en 8700G qui dépasse le plafond ; **Dell n'a pas "
        "d'offre AMD sur OptiPlex** — ce n'est pas un manque de relevé, c'est un fait de catalogue.",
        "**Le neuf domine, et c'est vérifié ligne à ligne.** Sur les quinze lignes où une machine "
        "existe, **treize sont neuves (87 %)** et deux seulement sont reconditionnées : les deux Dell. "
        "Aucun reconditionné confort "
        "n'existe chez les cinq enseignes. Le seuil de 60 % de neuf est tenu.",
        "**Le reconditionné casse la garantie du profil.** Pas de trois ans sur site J+1 : garantie "
        "légale de conformité côté vendeur, au mieux douze mois d'extension en atelier. Sur un poste "
        "gardé cinq ans, c'est disqualifiant — d'où sa place marginale, et son absence au confort.",
    ], small=True)

    doc.spacer(0.3)
    doc.h2("Les prix relevés, en un coup d'œil")
    lignes = []
    for nom, jeu in (("Entrée de gamme", ENTREE), ("Standard", STANDARD), ("Confort", CONFORT)):
        prix = sorted(r["prix"] for r in jeu if r["prix"])
        lignes.append([nom, "%d sur 5" % len(prix), _eur(prix[0]), _eur(prix[-1]),
                       _eur(prix[-1] - prix[0])])
    doc.table(["Gamme", "Lignes chiffrées", "Prix le plus bas", "Prix le plus haut", "Étalement"],
              lignes, [3.4, 3.0, 3.6, 3.6, 3.5], font=8.0,
              aligns=["l", "c", "r", "r", "r"], first_col_bold=True,
              caption="Cinq voies possibles par gamme, trois à quatre chiffrées. L'étalement se lit "
                      "comme un avertissement : sur une même gamme, le prix varie de 349 € à 737 € "
                      "sans que la conformité suive.")
    doc.p("**Le prix ne mesure pas la conformité.** En standard, la ligne la moins chère "
          "(790,91 €) est un reconditionné de 2019, hors millésime ; la plus chère (1 528,34 €) "
          "est un AMD neuf qui ne livre que 16 Go. Entre les deux, le HP à 1 140,18 € est le seul "
          "qui tienne le profil — sans être le moins cher ni le plus puissant.", small=True)

    # ------------------------------------------------------------------ planches
    for n, (key, titre, rows, seuil) in enumerate(GAMMES):
        doc.landscape3(True)
        if n:
            doc.pagebreak()
        doc.h1_plain(titre)
        doc.p("**Le seuil à tenir** — " + seuil + ". Les six lignes ci-dessous s'y confrontent "
              "une à une : deux par constructeur, la voie Intel puis la voie AMD.", small=True)
        _catalogue(doc, rows)
        doc.spacer(0.2)
        _f2f(doc, F2F[key],
             "Le face-à-face des tarifs, ligne à ligne. L'écart est calculé **AMD moins Intel**, "
             "à configuration voisine ; « n. c. » signifie qu'une des deux voies n'a pas de prix.")
        doc.spacer(0.15)
        doc.p(LECTURE[key], small=True)
        doc.spacer(0.15)
        doc.table(REP_HEADERS, REPERES[key], REP_WIDTHS, font=7.6, header_bg="1F3B63",
                  aligns=["l", "c", "c", "c", "l", "l"], first_col_bold=True,
                  caption="Repères de calcul de la gamme — cœurs, threads, fréquence, classe de "
                          "graphique. **Aucune note chiffrée n'est affichée** : ces machines n'ont "
                          "pas été mesurées, et un score repris de tiers serait invérifiable ici. "
                          "Les repères sont structurels ; une campagne de mesure reste à faire.")

    # ------------------------------------------------------------------ synthèse
    doc.landscape3(False)
    doc.h1_plain("Ce que les trois planches disent")
    doc.table(["Gamme", "Voie la moins chère", "Voie la plus chère", "Ce qui tient l'enveloppe"],
              [["Entrée de gamme", "**Dell Intel, reconditionné — 689,83 €**",
                "HP Intel — 1 039,22 €",
                "Les deux voies AMD tiennent la DDR5, à **763,67 € et 827,52 €** ; les deux Intel sont en DDR4."],
               ["Standard", "**Dell Intel, reconditionné — 790,91 €**",
                "HP AMD — 1 528,34 €",
                "Le HP Intel à **1 140,18 €** tient le profil sur 16 Go ; le 32 Go reste à ajouter."],
               ["Confort", "**HP Intel — 1 286,14 €**", "Lenovo Intel — 1 624,88 €",
                "Rien : aucune voie ne livre 32 Go et 1 To sous 1 300 €."]],
              [3.0, 5.4, 4.4, 8.0], font=8.0, aligns=["l", "l", "l", "l"],
              first_col_bold=True,
              caption="Le classement par prix, toutes voies confondues. Deux des trois lignes les "
                      "moins chères sont des reconditionnés — ce n'est pas un choix, c'est ce que "
                      "le marché propose.")
    doc.spacer(0.2)
    doc.h2("L'arbitrage Intel / AMD")
    doc.p("**Trois paires sont comparables à configuration voisine**, et toutes chez HP : en entrée "
          "l'AMD coûte **211,70 € de moins (−20,4 %)**, en standard **388,16 € de plus (+34,0 %)**, "
          "en confort **242,20 € de plus (+18,8 %)**. Partout ailleurs, une des deux voies n'a pas de "
          "prix. L'arbitrage n'est donc pas une doctrine de marque : il dépend de la gamme.", small=True)
    doc.ul([
        "**Ce que l'AMD achète chez HP n'est pas la mémoire.** Les deux configurations comparées "
        "sont à 16 Go et 512 Go. L'écart paie un châssis SFF extensible et une **Radeon 780M** — "
        "utile si la CAO 3D arrive, inutile pour Sage et Teams.",
        "**Là où l'AMD gagne, c'est en entrée de gamme — sur deux critères à la fois.** Le M75q Gen 5 "
        "à 763,67 € et le ProDesk 2 G1a à 827,52 € sont **les deux seules lignes neuves qui tiennent "
        "la DDR5 sous 1 000 €**, et l'AMD y est moins cher que le HP Intel de 211,70 €. Intel n'a rien "
        "à opposer dans cette gamme : ses deux offres sont en DDR4.",
        "**Le confort reste sans budget, dans les deux voies.** 28 threads Intel ou 16 threads AMD, "
        "32 Go et 1 To ne descendent pas sous 1 300 €. Tant que la direction ne tranche pas — relever "
        "le plafond, ou redescendre la puce — le confort est une spécification, pas une commande.",
        "**La garantie 3 ans sur site reste le critère qui départage.** Elle est incluse chez les "
        "constructeurs, absente en reconditionné : c'est elle, plus que le prix, qui limite la place "
        "du reconditionné dans un parc gardé cinq ans.",
    ], small=True)

    # ------------------------------------------------------------------ méthode
    doc.pagebreak()
    doc.h1_plain("Méthode et réserves")
    doc.ul([
        "**Source** : relevés du 5 novembre 2026 sur Amazon.fr, Fnac, Cdiscount, LDLC et "
        "Materiel.net, rapprochés des fiches constructeur HP, Dell et Lenovo.",
        "**Prix** : TTC, port compris dans la colonne « Prix livré ». La conversion applique "
        "1 € = 655,957 FCFA, parité fixe : les francs sont exacts, les euros ne le sont pas — ils "
        "changent chaque semaine. Valeur **illustrative**, à recaler par devis avant tout engagement.",
        "**Liens** : fiches produit `/dp/` chez Amazon, pages produit chez Cdiscount, liens de "
        "recherche par référence chez les enseignes qui n'exposent pas d'URL stable par modèle. "
        "Un lien peut mener à une autre configuration que celle décrite : c'est le prix relevé, "
        "pas l'annonce entière, qui fait foi ici.",
        "**n. c.** : information absente de l'annonce, jamais déduite d'une autre source. « — » "
        "signifie que le produit n'existe pas au catalogue du constructeur.",
        "**Conformité** : jugée sur le millésime, la mémoire, le stockage et l'enveloppe, sans note "
        "d'appréciation. Une case orange n'est pas un avis, c'est un fait : le point n'est pas tenu, "
        "ou le prix n'est pas connu.",
        "**Repères de calcul** : ils portent sur l'architecture — cœurs, threads, fréquence, classe "
        "de graphique — et non sur des scores mesurés. Aucun chiffre de benchmark n'est avancé : "
        "il serait invérifiable en l'état. Une campagne de mesure sur les six voies est la suite "
        "logique de ce document.",
        "**Précaution d'achat** : sur Amazon et Fnac, vérifier la mention « vendu et expédié par » "
        "avant de commander. Les mêmes machines y circulent en import, en clavier QWERTZ, avec une "
        "garantie constructeur parfois inapplicable en France — le HP Elite 805 G9 relevé en est "
        "un exemple.",
        "**Version alpha** : la structure et l'arbitrage sont arrêtés ; il manque trois prix "
        "(M70q Gen 5, M90q Gen 5, M75q Gen 5 en 32 Go / 1 To) et un devis Dell. "
        "Les relevés seront à refaire à la commande, pas avant.",
    ], small=True)

    dpath, ppath = doc.save(OUT)

    import docx as _docx

    d = _docx.Document(dpath)
    cp = d.core_properties
    cp.author = "GED-SERVICES"
    cp.last_modified_by = "GED-SERVICES"
    cp.comments = ""
    cp.category = "Postes fixes — spécification et arbitrage"
    cp.title = "Postes fixes — profil ciblé, catalogue et face-à-face Intel / AMD (version alpha)"
    d.save(dpath)
    return dpath, ppath


if __name__ == "__main__":
    print(build_doc())
