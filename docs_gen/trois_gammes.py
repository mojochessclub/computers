# -*- coding: utf-8 -*-
"""Trois gammes, trois propositions par gamme — HP, Dell et Lenovo.

Un tableau par gamme (entrée, standard, confort) : modèle, état neuf ou
reconditionné, processeur, fréquences, cœurs et threads, mémoire détaillée,
disque détaillé, revendeur, prix en euros et en francs CFA, conformité à la
spécification et lien vers l'offre.

Les prix viennent des relevés du 5 novembre 2026 ; aucun montant n'est estimé.
Là où aucun prix n'a été trouvé, la case le dit.
"""
from __future__ import annotations

import os

from render import Doc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "livrables")
BASE = "Trois_gammes_trois_propositions_HP_Dell_Lenovo"
TVA = 655.957

HEADERS = ["Constructeur", "Modèle", "État", "CPU", "Fréq. base", "Fréq. turbo",
           "Cœurs / threads", "RAM — capacité · type · fréquence",
           "Disque — capacité · interface · type", "Revendeur", "Prix livré €",
           "Prix FCFA", "Conformité à la spécification", "Lien"]
WIDTHS = [3.6, 5.4, 3.6, 4.0, 2.3, 2.3, 2.5, 5.8, 6.1, 3.4, 3.0, 3.0, 5.9, 1.5]
ALIGNS = ["l", "l", "c", "l", "c", "c", "c", "l", "l", "l", "r", "r", "l", "c"]

G, Y, O = "g", "y", "o"
FMT = {
    "g": {"bg": "D8EDCB", "color": "1E6B33"},
    "y": {"bg": "FAEBB8", "color": "7A5E12"},
    "o": {"bg": "F8CDB6", "color": "A23B1A"},
}


def _r(constructeur, modele, etat, cpu, fbase, fturbo, coeurs, ram, disque,
       revendeur, prix, conformite, lien, code):
    return {
        "constructeur": constructeur, "modele": modele, "etat": etat, "cpu": cpu,
        "fbase": fbase, "fturbo": fturbo, "coeurs": coeurs, "ram": ram,
        "disque": disque, "revendeur": revendeur, "prix": prix,
        "fcfa": int(round(prix * TVA)) if prix else None,
        "conformite": conformite, "lien": lien, "code": code,
    }


# --------------------------------------------------------------------------- #
ENTREE = [
    _r("HP", "Pro 400 G9 SFF", "Neuf", "Core i5-13500", "2,5 GHz", "4,8 GHz", "14C / 20T",
       "16 Go · DDR4 · fréquence n. c.", "512 Go · SATA · SSD + lecteur DVD",
       "Amazon", 1039.22,
       "Partielle — mémoire DDR4 au lieu de DDR5", "[ouvrir](https://www.amazon.fr/dp/B0D4F6739P)", Y),
    _r("Dell", "OptiPlex 7010 Micro", "Reconditionné", "Core i5-13500T", "1,6 GHz", "4,6 GHz",
       "14C / 20T", "16 Go · DDR4 3200 MHz", "512 Go · NVMe · SSD",
       "Amazon", 689.83,
       "Partielle — version T 35 W, DDR4, reconditionné",
       "[ouvrir](https://www.amazon.fr/dp/B0HKDSCK9X)", Y),
    _r("Lenovo", "ThinkCentre M70q Gen 5 Tiny", "Neuf", "Core i5-13500T", "1,6 GHz", "4,6 GHz",
       "14C / 20T", "16 Go · DDR4 3200 MHz", "512 Go · NVMe · SSD",
       "Materiel.net", None,
       "À chiffrer — aucun prix relevé chez les cinq enseignes",
       "[fiche](https://www.materiel.net/recherche/thinkcentre%20m70q%20gen%205/)", O),
]

STANDARD = [
    _r("HP", "Elite 800 G9 Mini", "Neuf", "Core i5-14500", "2,6 GHz", "5,0 GHz", "14C / 20T",
       "16 Go · DDR5 SO-DIMM · fréquence n. c.", "512 Go · NVMe · SSD",
       "Amazon", 1140.18,
       "Conforme sur 16 Go — les 32 Go de la cible restent à ajouter",
       "[ouvrir](https://www.amazon.fr/dp/B0D76M6T6R)", G),
    _r("Dell", "OptiPlex 7070 Micro + écran 27\"", "Reconditionné", "Core i9 9ᵉ gén.", "n. c.",
       "5,0 GHz", "8C / 16T", "16 Go · DDR4 · fréquence n. c.",
       "512 Go · NVMe · SSD + écran 27\" inclus", "Amazon", 790.91,
       "Hors millésime — plateforme 2019, 16 Go seulement",
       "[ouvrir](https://www.amazon.fr/dp/B0H415LBD6)", O),
    _r("Lenovo", "ThinkCentre M90q Gen 5 Tiny", "Neuf", "Core i5-14500T", "1,8 GHz", "4,8 GHz",
       "14C / 20T", "32 Go · DDR5 · fréquence n. c.", "1 To · NVMe · SSD",
       "Fnac", None,
       "À chiffrer — configuration retenue, aucune offre chiffrée",
       "[fiche](https://www.fnac.com/SearchResult/ResultList.aspx?Search=thinkcentre%20m90q%20gen%205)", O),
]

CONFORT = [
    _r("HP", "Pro Mini 400 G9 — i7-14700T", "Neuf", "Core i7-14700T", "1,3 GHz", "5,2 GHz",
       "20C / 28T", "16 Go · DDR (type n. c.)", "512 Go · NVMe · SSD",
       "Amazon", 1286.14,
       "Partielle — version T 35 W, 16 Go et 512 Go à porter à 32 Go / 1 To",
       "[ouvrir](https://www.amazon.fr/dp/B0D7424V46)", Y),
    _r("Dell", "Dell Pro Micro QCM1250 — i7-14700T", "Neuf", "Core i7-14700T", "1,8 GHz",
       "4,8 GHz", "20C / 28T", "32 Go · DDR5 (configuration visée)",
       "1 To · NVMe · SSD", "Dell (site constructeur)", None,
       "À devis — la fiche affiche « voir les options », sans prix",
       "[ouvrir](https://www.dell.com/fr-fr/search/dell%20pro%20micro%20qcm1250)", O),
    _r("Lenovo", "ThinkCentre M90q Gen 6 Tiny", "Neuf", "Core Ultra 7 265", "2,4 GHz",
       "5,3 GHz", "20C / 20T", "n. c. — configuration non publiée",
       "n. c. — configuration non publiée", "Cdiscount", 1624.88,
       "Hors enveloppe — 1 624,88 € pour un plafond de 1 300 €",
       "[fiche](https://www.cdiscount.com/search/10/thinkcentre+m90q+gen+6.html)", O),
]

SPEC_HEADERS = ["Gamme", "Millésime", "CPU plancher", "Mémoire", "Stockage", "Réseau", "Garantie"]
SPEC_WIDTHS = [2.2, 2.0, 4.8, 2.5, 2.2, 2.4, 1.6]
SPEC_ROWS = [
    ["Entrée de gamme", "≥ 2023", "Intel i5-13400 / i5-13500 · AMD Ryzen 5 8600G / 9600X",
     "16 Go DDR5", "512 Go NVMe", "1 GbE, Wi-Fi 6 en option", "3 ans"],
    ["Standard (référence)", "≥ 2024", "Intel i5 14ᵉ gén. · Core Ultra 5 · AMD Ryzen 5 8600G / 9600X",
     "16 Go plancher, 32 Go cible, DDR5", "512 Go NVMe", "1 GbE, Wi-Fi 6 en option", "3 ans"],
    ["Confort", "≥ 2025", "Intel i7 14ᵉ gén. · Core Ultra 7 série 2 · AMD Ryzen 7 8700G / 9700X",
     "32 Go DDR5", "1 To NVMe", "1 GbE, Wi-Fi 6 en option", "3 ans"],
]


def _table(doc, rows, caption, lecture=None, demander=None, profil=None):
    cf = {}
    body = []
    for i, r in enumerate(rows):
        body.append([r["constructeur"], r["modele"], r["etat"], r["cpu"], r["fbase"],
                     r["fturbo"], r["coeurs"], r["ram"], r["disque"], r["revendeur"],
                     _eur(r["prix"]) if r["prix"] else "—",
                     _fcfa(r["fcfa"]) if r["fcfa"] else "—",
                     r["conformite"].replace(" €", "\u00A0€"),
                     r["lien"] if r["lien"] else "—"])
        cf[(i, 12)] = FMT[r["code"]]
        cf[(i, 0)] = {"b": True}
        cf[(i, 1)] = {"b": True}
    if profil:
        doc.p(profil, small=True)
    doc.table(HEADERS, body, WIDTHS, font=8.4, header_bg="1F3B63", aligns=ALIGNS,
              zebra=True, cell_fmt=cf, caption=caption)
    if lecture:
        doc.p(lecture, small=True)
    if demander:
        doc.p(demander, small=True)
    doc.p("**Légende de la colonne Conformité** — vert : conforme ; jaune : partielle, un point "
          "manque et il est chiffrable ; orange : hors seuil, ou prix non relevé. "
          "Les prix sont des totaux livrés, TTC.", small=True)


def _eur(x):
    return ("%.2f" % x).replace(",", "X").replace(".", ",").replace("X", " ") + " €"


def _fcfa(x):
    n = "%d" % int(round(x))
    out, i = "", 0
    for ch in reversed(n):
        if i and i % 3 == 0:
            out = " " + out
        out = ch + out
        i += 1
    return out + " FCFA"


def build_doc():
    doc = Doc(
        base=BASE,
        title="Trois gammes, trois propositions — HP, Dell, Lenovo",
        subtitle="Entrée de gamme, standard, confort : le modèle, le prix, la conformité",
        meta=[],
        doc_ref="GED-POSTES-2026-11-B · Confidentiel — usage interne",
        footer="GED-SERVICES · trois gammes, trois propositions",
    )

    doc.cover(
        eyebrow="Postes fixes — sélection d'offres · trois gammes",
        title="Trois gammes,\ntrois propositions",
        subtitle="Un tableau par gamme, une proposition par constructeur : HP, Dell et Lenovo, "
                 "avec le prix en euros et en francs CFA, le détail des composants, l'état de "
                 "l'offre et le lien vers le revendeur.",
        meta_rows=[
            ["Destinataire", "**M. Jad, directeur général — ADCHIM**"],
            ["Émetteur", "**Joël MBA OYONE — GED-SERVICES**"],
            ["Objet", "Sélectionner trois modèles par gamme, un par constructeur, chiffrés et "
                      "confrontés à la spécification"],
            ["Tableau 1", "**Entrée de gamme** — accueil, saisie, consultation"],
            ["Tableau 2", "**Standard entreprise** — bureautique intensive, Sage, Teams"],
            ["Tableau 3", "**Confort** — postes gardés cinq ans, CAO légère, gros tableurs"],
            ["Prix", "TTC, **frais de port compris**, relevés le **5 novembre 2026** ; "
                     "1 € = 655,957 FCFA, parité fixe"],
            ["État", "Chaque ligne indique **Neuf** ou **Reconditionné**"],
            ["Lecture", "**n. c.** = non communiqué par l'annonce, jamais déduit. La couleur de "
                        "la colonne Conformité donne le verdict"],
            ["Livrables", "Word (.docx) et PDF identiques"],
        ],
        pagebreak=False,
    )
    doc.pagebreak()

    # ------------------------------------------------------------ spécification
    doc.h1_plain("Ce que la spécification impose")
    doc.p("L'enveloppe est fixée **entre 650 € et 1 300 € par poste**, écran non compris. Les "
          "constructeurs sont imposés — HP, Dell, Lenovo — sur des familles de postes fixes : "
          "ProDesk et Elite chez HP, OptiPlex chez Dell, ThinkCentre chez Lenovo. Le clavier est "
          "AZERTY, le système Windows 11 Professionnel, la garantie de trois ans.", small=True)
    doc.table(SPEC_HEADERS, SPEC_ROWS, SPEC_WIDTHS, font=7.4,
              aligns=["l", "c", "l", "l", "l", "l", "c"], first_col_bold=True,
              caption="Le seuil par gamme. Tout ce qui suit s'y confronte ligne par ligne : "
                      "la colonne « Conformité » dit ce qui est tenu, ce qui manque et ce qui "
                      "dépasse.")

    doc.p("**Comment se lit un tableau.** Le prix est le **total livré**, frais de port "
          "compris ; la conversion en francs CFA applique la parité fixe. La mémoire et le "
          "disque sont détaillés en trois éléments — capacité, type, fréquence ou interface. "
          "La conformité se juge sur quatre points : millésime du processeur, mémoire, stockage, "
          "et enveloppe de prix. Une ligne sans prix décrit la configuration retenue, pas une "
          "offre relevée : c'est écrit ainsi dans la colonne Conformité.", small=True)

    doc.table([], [["Vert — conforme ou conforme sur le point principal",
                    "Jaune — partielle : un point manque, chiffrable",
                    "Orange — hors seuil ou non chiffrée"]], [1, 1, 1], font=7.4,
              header=False, zebra=False,
              cell_fmt={(0, 0): FMT[G], (0, 1): FMT[Y], (0, 2): FMT[O]})

    doc.spacer(0.4)
    doc.h2("Où la recherche a porté")
    doc.table(["Enseigne", "Ce qu'elle donne sur ces références", "Lignes servies"], [
        ["Amazon.fr", "Cinq des six offres chiffrées du document, et les deux seules "
                      "reconditionnées : c'est la source la plus fournie sur ces millésimes.",
         "Tableaux 1, 2 et 3"],
        ["Materiel.net", "Le ThinkCentre M70q Gen 5 est au catalogue, mais la configuration "
                         "visée n'affiche aucun prix.", "Tableau 1"],
        ["Fnac", "Le ThinkCentre M90q Gen 5 est annoncé ; aucune offre chiffrée ne "
                 "correspond au 32 Go / 1 To.", "Tableau 2"],
        ["Cdiscount", "Un M90q Gen 6 chiffré à 1 624,88 € : seule offre confort chiffrée, "
                      "et elle dépasse le plafond de 324,88 €.", "Tableau 3"],
        ["Dell (site constructeur)", "Configurations publiées, prix uniquement sur devis.",
         "Tableau 3"],
        ["LDLC", "Aucune offre sur les générations G9 et G10 au moment du relevé.", "—"],
    ], [3.0, 10.6, 3.5], font=7.6, aligns=["l", "l", "c"], first_col_bold=True,
        caption="Les cinq enseignes demandées, plus le site constructeur Dell. Deux d'entre "
                "elles seulement publient un prix ferme sur ces références ; les autres "
                "renvoient au devis ou n'ont pas la configuration.")

    # ------------------------------------------------------------ tableau 1
    doc.landscape3(True)
    doc.spacer(5.5)
    doc.h1_plain("Tableau 1 — Entrée de gamme : accueil, saisie, consultation")
    _table(doc, ENTREE,
           "Tableau 1 — Entrée de gamme. Deux offres chiffrées sur trois. Aucune ne tient le "
           "DDR5 demandé : à ce niveau de prix, la mémoire DDR4 reste la règle. Le Lenovo n'a "
           "pas d'offre chiffrée chez les cinq enseignes ; la ligne décrit la configuration "
           "retenue.",
           lecture="**Ce que la gamme coûte.** Deux offres chiffrées : **1 039,22 €** chez HP, "
                   "neuf et en 65 W, contre **689,83 €** chez Dell, reconditionné et en 35 W. "
                   "L'écart de 349 € ne vient pas de la puce : il vient de l'état de la machine, "
                   "de la version thermique et d'un lecteur optique que le Dell n'a pas.",
           demander="**À demander** : le prix ferme du ThinkCentre M70q Gen 5 chez Materiel.net, "
                    "et la fréquence de la mémoire du HP, que l'annonce ne donne pas.",
           profil="**Le profil demandé** — millésime 2023 ou plus récent, i5-13400 ou i5-13500, "
                  "16 Go DDR5, 512 Go NVMe, 1 GbE, garantie 3 ans sur site, Wi-Fi 6 en option. "
                  "Les trois lignes qui suivent s'y confrontent une à une.")

    # ------------------------------------------------------------ tableau 2
    doc.pagebreak()
    doc.spacer(5.5)
    doc.h1_plain("Tableau 2 — Standard entreprise : bureautique intensive")
    _table(doc, STANDARD,
           "Tableau 2 — Standard entreprise. Le HP Elite 800 G9 Mini est la seule proposition "
           "conforme sur 16 Go, à 1 140,18 € livré. Le Dell est reconditionné et de 2019 ; le "
           "Lenovo n'est pas chiffré. Passer de 16 à 32 Go reste à faire sur les trois lignes.",
           lecture="**Ce que la gamme coûte.** **1 140,18 €** pour le HP, seule offre conforme sur "
                   "16 Go ; **790,91 €** pour le Dell reconditionné, écran 27 pouces compris, mais "
                   "sur une plateforme de 2019 — donc hors millésime malgré son prix.",
           demander="**À demander** : le prix du passage à 32 Go chez HP (deux barrettes "
                    "SO-DIMM), et une offre chiffrée du M90q Gen 5 en 32 Go / 1 To.",
           profil="**Le profil demandé** — millésime 2024 ou plus récent, i5 de 14ᵉ génération "
                  "ou Core Ultra 5, 16 Go DDR5 en plancher et 32 Go en cible, 512 Go NVMe, "
                  "garantie 3 ans sur site.")

    # ------------------------------------------------------------ tableau 3
    doc.pagebreak()
    doc.spacer(5.5)
    doc.h1_plain("Tableau 3 — Confort : postes gardés cinq ans")
    _table(doc, CONFORT,
           "Tableau 3 — Confort. Aucune proposition ne tient les 32 Go et le 1 To dans "
           "l'enveloppe : la seule offre chiffrée chez HP est une version 35 W à compléter, "
           "Dell ne publie pas de prix, et le Lenovo dépasse le plafond de 324,88 €.",
           lecture="**Ce que la gamme coûte.** Aucune offre ne tient le seuil. **1 286,14 €** pour "
                   "le HP en version 35 W, avec 16 Go et 512 Go : la mise à 32 Go et 1 To portera "
                   "le poste au-delà de 1 500 €, donc hors enveloppe. Dell n'affiche aucun prix, "
                   "le Lenovo dépasse le plafond de 324,88 €.",
           demander="**À demander** : un devis Dell Pro Micro QCM1250 en 32 Go / 1 To, et le prix "
                    "de la carte T400 si la CAO 3D reste au périmètre du profil.",
           profil="**Le profil demandé** — millésime 2025 ou plus récent, i7 de 14ᵉ génération, "
                  "Core Ultra 7 série 2 ou Ryzen 7 8700G / 9700X, 32 Go DDR5, 1 To NVMe, "
                  "garantie 3 ans sur site, dans un plafond de 1 300 €.")

    # ------------------------------------------------------------ lecture
    doc.landscape3(False)
    doc.h1_plain("Ce que les trois tableaux disent")
    doc.p("**Six propositions sur neuf sont chiffrées**, et deux seulement tiennent la "
          "spécification sans réserve : le HP Elite 800 G9 Mini en standard, et — sous réserve "
          "de la mémoire DDR4 — le HP Pro 400 G9 SFF en entrée de gamme. Le reste s'écarte pour "
          "trois raisons, toujours les mêmes.", small=True)
    doc.ul([
        "**La mémoire DDR5 demandée n'existe pas au prix de l'entrée de gamme** : les machines "
        "sous 1 000 € sont livrées en DDR4. Exiger la DDR5 partout, c'est relever le plancher "
        "de prix d'environ 150 €, ou accepter la DDR4 en entrée.",
        "**Les versions 35 W tirent le prix vers le bas sans le dire** : un i5-13500T ou un "
        "i7-14700T porte le même nom que la version 65 W et coûte 15 à 20 % moins cher, pour "
        "30 % de performance en moins. C'est le cas de quatre lignes sur six.",
        "**Le plafond de 1 300 € ne couvre pas le confort** : 32 Go, 1 To et un i7 65 W "
        "dépassent l'enveloppe. Le Lenovo M90q Gen 6 à 1 624,88 € en donne la mesure.",
    ], small=True)

    doc.spacer(0.5)
    doc.h1_plain("Le reconditionné : deux propositions sur neuf")
    doc.p("La spécification ne l'interdit pas, et le marché en propose beaucoup. Sur les neuf "
          "lignes, **deux portent sur du reconditionné** — les deux Dell, l'OptiPlex 7010 Micro "
          "en entrée de gamme (689,83 €) et l'OptiPlex 7070 Micro en standard (790,91 €, écran "
          "27 pouces compris). Aucune offre reconditionnée de gamme confort n'a été trouvée.", small=True)
    doc.p("**L'objectif de 70 % de reconditionné n'est pas atteignable avec ces relevés** : les "
          "enseignes interrogées ne publient presque pas de reconditionné récent (2024-2025). "
          "Y parvenir suppose un balayage dédié du reconditionné — Cdiscount, Materiel.net, Back "
          "Market — sur les trois gammes, référence par référence. La mécanique est en place : "
          "il suffit d'alimenter les lignes.", small=True)

    doc.spacer(0.5)
    doc.h1_plain("Méthode et réserves")
    doc.ul([
        "**Source** : relevés du 5 novembre 2026 sur Amazon.fr, Fnac, Cdiscount, LDLC et "
        "Materiel.net, rapprochés des fiches constructeur HP, Dell et Lenovo.",
        "**Prix** : TTC, port compris dans la colonne « Prix livré ». La conversion en francs "
        "CFA applique 1 € = 655,957 FCFA, parité fixe : les francs sont exacts, les euros ne le "
        "sont pas — ils changent chaque semaine.",
        "**Liens** : fiches produit `/dp/` pour Amazon ; liens de recherche par référence "
        "exacte pour les autres enseignes, qui ne publient pas d'URL stable par modèle.",
        "**n. c.** : information absente de l'annonce, jamais déduite d'une autre source.",
        "**Conformité** : jugée sur le millésime du processeur, la mémoire, le stockage et "
        "l'enveloppe, sans note d'appréciation. Une case orange n'est pas un avis, c'est un "
        "fait : le point n'est pas tenu ou le prix n'est pas connu.",
        "**Deux dates à corriger dans la spécification** : le i5-13400/13500 est de **janvier "
        "2023** et non d'octobre 2022 (octobre 2022 = les versions K) ; l'i7-14700 non-K est de "
        "**janvier 2024** et non d'octobre 2023. Enfin, un millésime « ≥ 2025 » au confort "
        "exclut la 14ᵉ génération qui y est citée : il faut choisir entre les deux.",
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
    cp.title = "Trois gammes, trois propositions — HP, Dell, Lenovo"
    cp.subject = "Entrée de gamme, standard, confort : modèles, prix, conformité"
    d.save(dpath)
    return dpath, ppath


if __name__ == "__main__":
    print(build_doc())
