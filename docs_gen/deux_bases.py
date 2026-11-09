# -*- coding: utf-8 -*-
"""Postes fixes — deux bases face à face, avec colonnes de chiffrage.

    Base A (16 Go)   : le seuil, puis les trois constructeurs, puis les cinq enseignes
    Base B (32 Go)   : les seuils B1 et B2, puis les trois constructeurs, puis les cinq enseignes
    Puis les CPU, les raisons de la présentation, l'état du chiffrage et le point de blocage.

Règle des cellules de prix : un montant quand il existe, « 0 résultat » quand l'enseigne a
été interrogée sans succès, « non relevé » quand la recherche n'a pas abouti, « — » quand
le constructeur ne propose pas de produit. Aucune case n'est remplie par estimation.
"""
from __future__ import annotations

import os

from render import Doc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "livrables")
BASE = "Postes_fixes_deux_bases_base_A_16_Go_et_base_B_32_Go"

GRIS = "8A8A8A"
BLEU = "1F3B63"

# --------------------------------------------------------------------------- #
A_SEUIL = [
    ["Usage", "Accueil, saisie, consultation, poste nomade occasionnel"],
    ["CPU plancher", "Core i5-13400 · Ryzen 5 PRO 7645"],
    ["RAM", "16 Go DDR4 ou DDR5, 2 emplacements"],
    ["Stockage", "SSD 512 Go (SATA toléré)"],
    ["Réseau", "1 GbE + Wi-Fi 6"],
    ["Millésime", "2023 minimum"],
    ["Garantie", "3 ans sur site"],
]

B_SEUIL = [
    ["Usage", "Bureautique intensive, Sage, Teams, applications multiples",
     "Utilisateurs exigeants, postes gardés cinq ans, CAO légère"],
    ["CPU plancher", "Core i5-14500 · Ryzen 7 PRO 7745", "Core i7-14700 · Ryzen 7 PRO 8700G"],
    ["RAM", "32 Go DDR5, extensible à 64 Go", "32 Go DDR5, extensible à 64 Go"],
    ["Stockage", "NVMe 512 Go à 1 To (SATA refusé)", "NVMe 1 To + emplacement libre"],
    ["Graphique", "Carte intégrée (iGPU)", "Carte dédiée imposée (T400 / T600, 4 à 8 Go)"],
    ["Réseau", "1 GbE + Wi-Fi 6/6E", "1 GbE + Wi-Fi 6E"],
    ["Millésime", "2024 minimum", "2024-2025"],
    ["Garantie", "3 ans sur site", "3 ans sur site"],
]

# --------------------------------------------------------------------------- #
MARCHE_HEADERS = ["Constructeur", "Référence de châssis", "CPU Intel", "Variante AMD", "RAM",
                  "Stockage", "Réseau", "Amazon", "Fnac", "Cdiscount", "LDLC", "Materiel.net",
                  "Fiche"]
MARCHE_WIDTHS = [3.4, 4.2, 2.8, 3.8, 2.4, 2.6, 3.0, 2.4, 2.0, 2.7, 2.0, 3.2, 1.6]
MARCHE_ALIGNS = ["l", "l", "l", "l", "l", "l", "l", "r", "c", "r", "c", "r", "c"]

A_MARCHE = [
    ["HP", "ProDesk 400 G10 SFF", "Core i5-13400", "ProDesk 405 G9 · Ryzen 5 PRO 7645",
     "16 Go DDR4", "512 Go NVMe", "1 GbE + Wi-Fi 6 (option)",
     "—", "non relevé", "—", "0 résultat", "—",
     "[ouvrir](https://www.hp.com/fr-fr/shop/search?q=ProDesk%20400%20G10)"],
    ["Dell", "OptiPlex 7010 MFF", "Core i5-13400T", "—",
     "16 Go DDR4", "512 Go NVMe", "1 GbE + Wi-Fi 6 (option)",
     "—", "non relevé", "—", "—", "—",
     "[ouvrir](https://www.dell.com/fr-fr/search/optiplex-7010)"],
    ["Lenovo", "ThinkCentre M70q Gen 5 Tiny", "Core i5-13400T",
     "M75q Gen 5 · Ryzen 5 PRO 7645",
     "16 Go DDR4", "512 Go NVMe", "1 GbE + Wi-Fi 6 (option)",
     "—", "non relevé", "—", "—", "—",
     "[ouvrir](https://www.lenovo.com/fr/fr/search?text=ThinkCentre%20M70q%20Gen%205)"],
]

B1_MARCHE = [
    ["HP", "Elite 800 G9 Mini", "Core i5-14500T", "Elite Mini 805 G9 · Ryzen 7 PRO 8700G",
     "32 Go DDR5", "1 To NVMe", "1 GbE + Wi-Fi 6E",
     "—", "non relevé", "975 € (i5)", "0 résultat", "1 199,95 € °",
     "[ouvrir](https://www.hp.com/fr-fr/shop/search?q=Elite%20800%20G9%20Mini)"],
    ["Dell", "OptiPlex 7020 MFF", "Core i5-14500T", "—",
     "32 Go DDR5", "1 To NVMe", "1 GbE + Wi-Fi 6E",
     "—", "non relevé", "—", "—", "—",
     "[ouvrir](https://www.dell.com/fr-fr/search/optiplex-7020)"],
    ["Lenovo", "ThinkCentre M90q Gen 5 Tiny", "Core i5-14500T",
     "M75q Gen 5 · Ryzen 7 PRO 8700GE",
     "32 Go DDR5", "1 To NVMe", "1 GbE + Wi-Fi 6E",
     "—", "non relevé", "1 624,88 € °", "—", "—",
     "[ouvrir](https://www.lenovo.com/fr/fr/search?text=ThinkCentre%20M90q%20Gen%205)"],
]

B2_MARCHE = [
    ["HP", "Elite SFF 800 G9", "Core i7-14700", "Elite SFF 805 G9 · Ryzen 7 PRO 8700G",
     "32 Go DDR5 → 64 Go", "1 To NVMe", "1 GbE + Wi-Fi 6E",
     "—", "non relevé", "—", "0 résultat", "1 699,95 € °",
     "[ouvrir](https://www.hp.com/fr-fr/shop/search?q=Elite%20800%20G9%20SFF)"],
    ["Dell", "OptiPlex 7020 SFF", "Core i7-14700", "—",
     "32 Go DDR5 → 64 Go", "1 To NVMe", "1 GbE + Wi-Fi 6E",
     "—", "non relevé", "—", "—", "—",
     "[ouvrir](https://www.dell.com/fr-fr/search/optiplex-7020)"],
    ["Lenovo", "ThinkCentre M90s Gen 5 SFF", "Core i7-14700", "M75s Gen 5 · Ryzen 7 PRO 8700G",
     "32 Go DDR5 → 64 Go", "1 To NVMe", "1 GbE + Wi-Fi 6E",
     "2 393,57 € °", "non relevé", "—", "—", "—",
     "[ouvrir](https://www.lenovo.com/fr/fr/search?text=ThinkCentre%20M90s%20Gen%205)"],
]

# --------------------------------------------------------------------------- #
CPU_HEADERS = ["Base", "Modèle", "Cœurs / threads", "Base → Turbo", "TDP", "Sortie", "Socket"]
CPU_WIDTHS = [1.5, 3.6, 3.4, 3.0, 1.6, 2.0, 2.0]
CPU_ROWS = [
    ["A", "Core i5-13400", "10C/16T (6P+4E)", "2,5 → 4,6 GHz", "65 W", "janv. 2023", "LGA1700"],
    ["A", "Core i5-13400T", "10C/16T (6P+4E)", "1,5 → 4,4 GHz", "35 W", "janv. 2023", "LGA1700"],
    ["A", "Ryzen 5 PRO 7645", "6C/12T", "3,8 → 5,1 GHz", "65 W", "2023", "AM5"],
    ["B1", "Core i5-14500", "14C/20T (6P+8E)", "2,6 → 5,0 GHz", "65 W", "janv. 2024", "LGA1700"],
    ["B1", "Core i5-14500T", "14C/20T (6P+8E)", "1,8 → 4,8 GHz", "35 W", "janv. 2024", "LGA1700"],
    ["B1", "Ryzen 7 PRO 7745", "8C/16T", "3,8 → 5,3 GHz", "65 W", "2023", "AM5"],
    ["B2", "Core i7-14700", "20C/28T (8P+12E)", "2,1 → 5,3 GHz", "65 W", "janv. 2024", "LGA1700"],
    ["B2", "Ryzen 7 PRO 8700G", "8C/16T", "4,2 → 5,1 GHz", "65 W", "févr. 2024", "AM5"],
]

# --------------------------------------------------------------------------- #
CHIFFRAGE_HEADERS = ["Enseigne", "Ce qui a été trouvé", "Ce que ça vaut pour la grille"]
CHIFFRAGE_WIDTHS = [2.6, 8.2, 6.3]
CHIFFRAGE_ROWS = [
    ["Materiel.net", "ProDesk 2 et 4 G1i, de 919,95 à 1 399,95 €",
     "Le successeur du ProDesk 400 G10 : référence à réactualiser, prix utilisable"],
    ["Materiel.net", "EliteDesk 8 Mini G1i — Ultra 5 235T à 1 199,95 €, Ultra 7 265T à 1 699,95 €",
     "Le successeur de l'Elite 800 G9 Mini ; seuls prix neufs complets trouvés à ce jour"],
    ["Cdiscount", "Elite Mini 800 G9, i5 et i7, de 975 à 2 123 €",
     "La référence exacte de la base B1, en mini ; reconditionné fréquent, à vérifier ligne à ligne"],
    ["Cdiscount", "ThinkCentre M90q Gen 6, Ultra 7 265, 1 624,88 €",
     "La génération suivante du M90q Gen 5 : prix de la relève, pas de la référence écrite"],
    ["Amazon", "ThinkCentre M90q Gen 5, i7-14700, 64 Go / 2 To, 2 393,57 €",
     "Configuration très au-delà du seuil : elle situe le haut du marché, pas le prix d'achat"],
    ["Amazon", "Variantes ThinkCentre M75q Gen 5",
     "La voie AMD existe chez Lenovo, mais les prix ne sont pas consolidés par référence"],
    ["LDLC", "Aucun résultat sur ProDesk 400 G10 et Elite 800 G9",
     "Ces deux générations n'y sont pas cataloguées : élargir aux G1i avant de conclure"],
    ["Fnac", "Recherche en échec (erreur technique du moteur, pas absence d'offre)",
     "Rien d'exploitable : à reprendre par référence exacte ou par une autre entrée"],
]

BLOCAGE_HEADERS = ["Référence écrite", "Statut au catalogue 2026", "Successeur", "Conséquence"]
BLOCAGE_WIDTHS = [4.0, 4.4, 4.4, 4.3]
BLOCAGE_ROWS = [
    ["HP ProDesk 400 G10 SFF", "En fin de commercialisation",
     "HP ProDesk 4 G1i — 919,95 à 1 399,95 €", "Prix disponible, référence à réécrire"],
    ["HP Elite 800 G9 Mini", "Encore vendu, souvent en reconditionné",
     "HP EliteDesk 8 Mini G1i — 1 199,95 à 1 699,95 €", "Deux prix, deux générations"],
    ["HP Elite SFF 800 G9", "Fin de commercialisation",
     "HP EliteDesk 8 SFF G1i", "Prix non relevé à ce jour"],
    ["Dell OptiPlex 7010 MFF", "Remplacé",
     "Dell OptiPlex 7020, puis Dell Pro Micro QCM1250", "Aucun prix relevé sur les cinq enseignes"],
    ["Dell OptiPlex 7020 MFF / SFF", "Courant en 2025-2026",
     "Dell Pro Micro QCM1250 · Pro Slim QCS1250", "Aucun prix relevé sur les cinq enseignes"],
    ["Lenovo M70q Gen 5", "Remplacé",
     "ThinkCentre M70q Gen 6", "Aucun prix relevé pour cette référence"],
    ["Lenovo M90q Gen 5", "Remplacé",
     "ThinkCentre M90q Gen 6 — 1 624,88 €", "Le prix trouvé est celui de la relève"],
    ["Lenovo M90s Gen 5", "Remplacé",
     "ThinkCentre M90s Gen 6", "Prix non relevé à ce jour"],
]

OPTIONS_HEADERS = ["Option", "Ce qu'elle donne", "Ce qu'elle coûte"]
OPTIONS_WIDTHS = [3.4, 7.0, 6.7]
OPTIONS_ROWS = [
    ["Garder les références écrites",
     "La grille reste celle qui a été validée ; les seuils techniques ne bougent pas. "
     "Les cases vides restent vides, et l'écart avec le catalogue se voit.",
     "Le chiffrage restera partiel : ces châssis quittent les catalogues, les prix neufs "
     "se raréfient et le risque de payer du stock au prix du neuf augmente."],
    ["Réactualiser sur G1i et Gen 6",
     "Chaque ligne reçoit son successeur, avec un prix neuf réellement pratiqué. La grille "
     "devient chiffrable de bout en bout.",
     "Il faut réécrire huit références et refaire valider les équivalences — une demi-journée "
     "de travail, aucune remise en cause des seuils."],
]


# --------------------------------------------------------------------------- #
def _marche(doc, rows, caption, note=None):
    cf = {}
    for i, row in enumerate(rows):
        for j in range(7, 12):
            v = row[j]
            if v == "—":
                cf[(i, j)] = {"color": GRIS}
            elif v == "non relevé" or v == "0 résultat":
                cf[(i, j)] = {"color": GRIS, "b": False}
    doc.table(MARCHE_HEADERS, rows, MARCHE_WIDTHS, font=8.2, header_bg=BLEU,
              aligns=MARCHE_ALIGNS, first_col_bold=True, cell_fmt=cf,
              caption=caption + (" ° prix relevé sur un châssis ou une génération voisine : "
                                 "il éclaire le niveau de prix, il ne vaut pas offre." if note else ""))


def build_doc():
    doc = Doc(
        base=BASE,
        title="Postes fixes — deux bases, une décision",
        subtitle="Base A 16 Go et base B 32 Go, face à face, avec le chiffrage des cinq enseignes",
        meta=[],
        doc_ref="GED-POSTES-2026-11-A · Confidentiel — usage interne",
        footer="GED-SERVICES · postes fixes, deux bases",
    )

    doc.cover(
        eyebrow="Postes fixes — grille d'achat · base A et base B",
        title="Deux bases,\nune décision",
        subtitle="La base A (16 Go) et la base B (32 Go) présentées côte à côte, jamais l'une "
                 "sans l'autre : c'est la comparaison qui porte la décision, pas le tableau isolé.",
        meta_rows=[
            ["Destinataire", "**M. Jad, directeur général — ADCHIM**"],
            ["Émetteur", "**Joël MBA OYONE — GED-SERVICES**"],
            ["Objet", "Choisir entre deux bases mémoire et trois gammes, avec les prix des cinq "
                      "enseignes quand ils existent"],
            ["Base A", "16 Go DDR4 ou DDR5 — **entrée de gamme**, chemin de repli budgétaire"],
            ["Base B", "32 Go DDR5 — **référence d'achat** : B1 standard, B2 confort"],
            ["Constructeurs", "HP, Dell et Lenovo : un modèle par constructeur et par gamme, "
                              "variante AMD accolée quand elle existe"],
            ["Chiffrage", "Amazon · Fnac · Cdiscount · LDLC · Materiel.net, relevé du "
                          "**5 novembre 2026**. Une case vide reste vide"],
            ["Lecture", "Un montant = un prix relevé. **0 résultat** = enseigne interrogée, "
                        "aucun produit. **non relevé** = recherche non aboutie. **—** = le "
                        "constructeur ne propose pas ce produit"],
            ["Livrables", "Word (.docx) et PDF identiques, plus le classeur `.xlsx` à cinq "
                          "feuilles filtrables"],
        ],
        pagebreak=False,
    )
    doc.pagebreak()

    # ------------------------------------------------------------ règles de lecture
    doc.h1_plain("Deux règles de lecture, avant tout")
    doc.ul([
        "**La base B est la référence d'achat.** La base A n'existe que comme chemin de repli "
        "budgétaire, et elle se justifie poste par poste, jamais par lot.",
        "**Dell n'a pas d'offre AMD sur OptiPlex.** La cellule est marquée « — » : c'est un fait "
        "de catalogue, pas un oubli. Le croisement AMD se fait chez HP (séries 405 et 805) et "
        "Lenovo (séries M75).",
        "**Une case vide reste vide.** Aucun prix n'est estimé, aucune moyenne n'est calculée "
        "pour combler un trou : le chiffrage partiel se voit, il ne se masque pas.",
    ], small=True)

    doc.table(["Ce que dit la cellule", "Ce qu'elle signifie"], [
        ["**975 €**", "Un prix relevé sur l'enseigne indiquée, à la date du document"],
        ["**0 résultat**", "L'enseigne a été interrogée : elle ne propose pas ce produit"],
        ["**non relevé**", "La recherche n'a pas abouti : la case ne dit rien du marché"],
        ["**—**", "Le constructeur ne propose pas ce produit (cas AMD chez Dell)"],
        ["**°**", "Prix d'un châssis ou d'une génération voisine, utile pour situer le niveau"],
    ], [4.6, 12.5], font=8.4, aligns=["l", "l"],
              cell_fmt={(i, 0): {"bg": "EDF1F7"} for i in range(5)},
              caption="Quatre états, jamais confondus. C'est la différence entre « il n'y a rien » "
                      "et « on n'a pas cherché ».")

    # ------------------------------------------------------------ base A
    doc.h1_plain("Tableau 1 — Base A, entrée de gamme : le seuil opposable")
    doc.table(["Seuil opposable", "Valeur"], A_SEUIL, [4.6, 12.5], font=8.4,
              aligns=["l", "l"], first_col_bold=True,
              cell_fmt={(i, 0): {"bg": "EDF1F7"} for i in range(len(A_SEUIL))},
              caption="Tableau 1 — Ce qui est exigé, quel que soit le constructeur. Le seuil "
                      "s'oppose au vendeur ; il ne se négocie pas au cas par cas.")

    # ------------------------------------------------------------ marché base A
    doc.landscape(True)
    doc.h1_plain("Tableau 2 — Base A : les trois constructeurs et les cinq enseignes")
    _marche(doc, A_MARCHE,
            "Tableau 2 — Base A, entrée de gamme. Aucune des trois références n'a de prix "
            "complet sur les cinq enseignes : LDLC ne catalogue pas ces générations, la Fnac "
            "n'a pas répondu, Amazon et Cdiscount ne les ont pas en neuf à la référence exacte. "
            "Le détail est page « état du chiffrage ».", note=False)
    doc.p("**Ce que le tableau dit.** Aucune des trois références n'a de prix neuf chez les cinq "
          "enseignes. LDLC ne catalogue ni le ProDesk 400 G10 ni les G9 ; la Fnac n'a pas "
          "répondu ; Amazon et Cdiscount ne proposent pas ces générations en neuf à la référence "
          "exacte. Le chiffrage de la base A est donc ouvert : il ne pourra se fermer qu'en "
          "élargissant aux G1i et Gen 6.", small=True)
    doc.table([], [["0 prix sur 3 références", "5 enseignes muettes sur 5", "1 génération non cataloguée chez LDLC"]], [1, 1, 1], font=7.8, header=False,
              zebra=False, cell_fmt={(0, j): {"bg": "EDF1F7", "b": True}
                                    for j in range(3)})


    # ------------------------------------------------------------ base B seuils
    doc.landscape(False)
    doc.h1_plain("Tableau 3 — Base B, référence d'achat : les deux seuils")
    doc.p("La base B se scinde en deux : **B1** pour la bureautique intensive, **B2** pour les "
          "postes gardés cinq ans et la CAO légère. La différence tient en deux lignes — le "
          "processeur et la carte graphique. Le reste est identique, et c'est volontaire : une "
          "seule base mémoire, deux niveaux de puissance.", small=True)
    doc.table(["Seuil opposable", "B1 — Standard entreprise", "B2 — Confort / longue durée"],
              B_SEUIL, [3.4, 6.8, 6.9], font=8.2, aligns=["l", "l", "l"],
              first_col_bold=True,
              cell_fmt={(i, 0): {"bg": "EDF1F7"} for i in range(len(B_SEUIL))},
              caption="Tableau 3 — B1 et B2 partagent la même mémoire, le même réseau et la même "
                      "garantie. Elles divergent sur le processeur, le stockage et la carte "
                      "graphique.")
    doc.p("**Trois conséquences directes.**", small=True)
    doc.ul([
        "**La carte graphique sépare B1 de B2, pas le processeur** : un i7 sans carte dédiée ne "
        "fait pas un poste confort, il fait un poste standard plus cher.",
        "**Le suffixe T passe en B1 et disparaît en B2** : un châssis d'un litre n'a pas la place "
        "d'une carte graphique, et le confort en exige une.",
        "**La mémoire ne change pas entre B1 et B2** : 32 Go extensibles à 64 Go dans les deux "
        "cas. Seule la vitesse d'extension distingue les châssis.",
    ], small=True)
    doc.table([], [["2 seuils", "1 seule base mémoire", "1 garantie de 3 ans"]], [1, 1, 1],
              font=7.8, header=False, zebra=False,
              cell_fmt={(0, j): {"bg": "EDF1F7", "b": True} for j in range(3)})

    # ------------------------------------------------------------ marché B1
    doc.landscape(True)
    doc.h1_plain("Tableau 4 — Base B1, standard entreprise : les trois constructeurs")
    _marche(doc, B1_MARCHE,
            "Tableau 4 — Base B1. Deux prix utilisables : l'Elite Mini 800 G9 à 975 € chez "
            "Cdiscount et l'EliteDesk 8 Mini G1i à 1 199,95 € chez Materiel.net. Les deux "
            "autres constructeurs restent sans prix neuf à la référence exacte.", note=True)
    doc.p("**Ce que le tableau dit.** B1 est la seule base aujourd'hui partiellement chiffrable : "
          "975 € pour l'Elite Mini 800 G9 chez Cdiscount, 1 199,95 € pour l'EliteDesk 8 Mini G1i "
          "chez Materiel.net. Dell est absent des cinq enseignes sur l'OptiPlex 7020, et la Fnac "
          "n'a rien rendu. L'ordre de grandeur de la base B se situe donc autour de 1 000 à "
          "1 200 € pour un mini correctement doté.", small=True)
    doc.table([], [["2 prix sur 3 références", "975 € à 1 199,95 €", "Dell absent des cinq enseignes"]], [1, 1, 1], font=7.8, header=False,
              zebra=False, cell_fmt={(0, j): {"bg": "EDF1F7", "b": True}
                                    for j in range(3)})


    # ------------------------------------------------------------ marché B2
    doc.pagebreak()
    doc.h1_plain("Tableau 5 — Base B2, confort : les trois constructeurs")
    _marche(doc, B2_MARCHE,
            "Tableau 5 — Base B2. Aucune des trois références n'a de prix correspondant : les "
            "montants trouvés portent sur des châssis plus petits, sans carte graphique, donc "
            "hors du profil confort. Le chiffrage de B2 est ouvert.", note=True)
    doc.p("**Ce que le tableau dit.** Les montants trouvés portent sur des châssis plus petits, "
          "sans carte graphique : ils situent le haut du marché, ils ne chiffrent pas le profil "
          "confort. Il manque deux choses pour fermer B2 : le prix d'un SFF correctement doté, et "
          "celui de la carte T400 ou T600 qui va avec.", small=True)
    doc.table([], [["0 prix correspondant sur 3", "2 prix hors châssis", "carte graphique non chiffrée"]], [1, 1, 1], font=7.8, header=False,
              zebra=False, cell_fmt={(0, j): {"bg": "EDF1F7", "b": True}
                                    for j in range(3)})


    # ------------------------------------------------------------ CPU
    doc.landscape(False)
    doc.h1_plain("Tableau 6 — Les processeurs : planchers et plafonds")
    doc.p("Huit processeurs suffisent à couvrir les trois gammes, quatre Intel et quatre AMD. "
          "Les fréquences sont données en base et en turbo, les TDP sont ceux annoncés par les "
          "constructeurs, le socket fixe la plateforme et la mémoire.", small=True)
    doc.table(CPU_HEADERS, CPU_ROWS, CPU_WIDTHS, font=8.0,
              aligns=["c", "l", "l", "c", "c", "c", "c"], first_col_bold=True,
              caption="Tableau 6 — Le « T » désigne la version 35 W livrée dans les châssis "
                      "d'un litre : environ 30 % de performance en moins, à dénomination "
                      "identique. Il est assumé en A et en B1, exclu en B2.")
    doc.p("**À écarter, quelle que soit la base** : Core i5-12400 (12ᵉ génération), Ryzen 5 "
          "5600G (plateforme AM4 de 2021), tout processeur suffixé « T » en B2, et toute "
          "déclinaison « F » — ces dernières n'ont pas de circuit graphique et n'affichent rien "
          "sans carte dédiée.", small=True)

    # ------------------------------------------------------------ pourquoi
    doc.h1_plain("Pourquoi cette présentation et pas une autre")
    doc.p("**Le face-à-face est forcé, pas décoratif.** Un tableau unique avec trois gammes "
          "laisse toujours filer une caractéristique d'une colonne à l'autre — c'est exactement "
          "ce qui s'est produit au départ, avec les 32 Go redescendus à 16. Deux bases séparées "
          "rendent la bascule visible : on ne passe plus de l'une à l'autre sans le dire.", small=True)
    doc.p("**Le suffixe T est enfin au bon endroit.** Les mini-PC d'un litre sont livrés en 35 W, "
          "soit environ 30 % de performance en moins à dénomination identique. En base A et en "
          "B1, il est assumé et adossé au châssis. En B2, il est exclu : un châssis mini ne "
          "reçoit pas de carte graphique, et le profil confort en exige une.", small=True)
    doc.p("**La carte graphique remplace la mention « CAO ».** « CAO légère » avec un circuit "
          "intégré, c'était le point faible du tableau d'origine. Une T400 de 4 Go tient dans un "
          "SFF et suffit à SolidWorks ou AutoCAD en deux dimensions : c'est ce qui rend le profil "
          "confort tenable.", small=True)
    doc.p("**La garantie trois ans sur site remonte en base A.** Elle n'apparaissait qu'en "
          "confort, ce qui n'avait pas de sens : le poste d'accueil tombe aussi.", small=True)
    doc.p("**Le millésime est opposable.** 2023 pour A, 2024 minimum pour B. Attention : les "
          "ProDesk 400 G9 et ThinkCentre M70q Gen 4 sont des châssis de 2022 — en 2026, exiger "
          "les G10 et Gen 5, sinon c'est du stock de déstockage vendu au prix du neuf.", small=True)
    doc.p("**Le Wi-Fi est marqué en option.** Les châssis d'un litre n'en ont presque jamais de "
          "série. Sur une flotte, cela se commande en configuration, pas en reprise après "
          "livraison.", small=True)

    # ------------------------------------------------------------ chiffrage
    doc.pagebreak()
    doc.h1_plain("Où en est le chiffrage : partiel, et il se voit")
    doc.p("Les cinq enseignes ont été interrogées le 5 novembre 2026. Le résultat est mince, et "
          "il vaut mieux le montrer tel quel : sur neuf références, deux seulement ont un prix "
          "neuf correspondant. Tout le reste est vide, et chaque case vide dit pourquoi.", small=True)
    doc.table(CHIFFRAGE_HEADERS, CHIFFRAGE_ROWS, CHIFFRAGE_WIDTHS, font=7.8,
              aligns=["l", "l", "l"], first_col_bold=True,
              caption="Ce qui a été trouvé, enseigne par enseigne, et ce que chaque trouvaille "
                      "vaut pour la grille. Aucun de ces montants ne comble une case du tableau "
                      "de la base correspondante s'il ne porte pas sur la même référence.")
    doc.p("**Ce qui reste à faire**, dans cet ordre :", small=True)
    doc.ul([
        "reprendre la Fnac par référence exacte, l'échec venant du moteur de recherche et non de "
        "l'absence d'offre ;",
        "élargir LDLC aux G1i, les G9 et G10 n'y étant pas catalogués ;",
        "trancher entre garder les références écrites et les réactualiser sur G1i et Gen 6 ;",
        "ouvrir une fiche constructeur par référence, une seule fois la référence arrêtée ;",
        "étendre la même logique à deux bases aux postes nomades, non entamés à ce jour.",
    ], small=True)

    # ------------------------------------------------------------ blocage
    doc.pagebreak()
    doc.h1_plain("Le point de blocage n'est pas technique, il est de catalogue")
    doc.p("Les châssis de la spécification datent de 2023-2024. En 2026, ils quittent les "
          "catalogues : les offres neuves basculent sur les générations G1i chez HP et Gen 6 chez "
          "Lenovo. Garder les références écrites, c'est accepter de chiffrer des machines qu'on "
          "ne trouve plus neuves ; les réactualiser, c'est réécrire huit lignes sans toucher aux "
          "seuils.", small=True)
    doc.table(BLOCAGE_HEADERS, BLOCAGE_ROWS, BLOCAGE_WIDTHS, font=7.8,
              aligns=["l", "l", "l", "l"], first_col_bold=True,
              caption="Référence par référence : ce qu'elle est devenue, par quoi elle est "
                      "remplacée, et ce que cela change pour le chiffrage.")

    doc.p("Deux options, une seule recommandation :", small=True)
    doc.table(OPTIONS_HEADERS, OPTIONS_ROWS, OPTIONS_WIDTHS, font=7.8,
              aligns=["l", "l", "l"], first_col_bold=True,
              caption="Les deux chemins possibles. Le second ne change aucun seuil technique : "
                      "il change les références et rend la grille chiffrable.")
    doc.p("**Recommandation.** Réactualiser les références sur G1i et Gen 6, en conservant la "
          "spécification comme exigence : ce sont les seuils qui protègent l'achat, pas les "
          "numéros de génération. Les prix relevés chez Materiel.net et Cdiscount donnent déjà "
          "un ordre de grandeur crédible pour la base B.", small=True)

    # ------------------------------------------------------------ trancher
    doc.pagebreak()
    doc.h1_plain("Ce qui reste à trancher")
    doc.p("La base B1 — i5-14500, 32 Go, garantie trois ans — couvre environ 80 % du besoin réel "
          "pour un coût maîtrisé. Le choix qui pèse vraiment n'est donc pas Intel contre AMD : "
          "c'est base A ou base B, poste par poste, et carte graphique ou non sur les profils "
          "confort.", small=True)
    doc.p("**Deux réserves à garder en tête.** Les processeurs Raptor Lake, 13ᵉ et 14ᵉ "
          "générations, imposent un BIOS en microcode 0x12F minimum à la livraison : c'est le "
          "premier contrôle à faire, avant la fréquence. Et l'AMD coûte le vPro : DASH fonctionne, "
          "mais l'outillage de gestion de parc est nettement plus mince au-delà de cinquante "
          "postes.", small=True)

    doc.h1_plain("Méthode")
    doc.ul([
        "**Source** : relevés du 5 novembre 2026 sur Amazon.fr, Fnac, Cdiscount, LDLC et "
        "Materiel.net, plus les fiches constructeur HP, Dell et Lenovo.",
        "**Cellules de prix** : quatre états distincts — montant, « 0 résultat », « non relevé », "
        "« — ». Aucune estimation, aucune moyenne, aucun report d'une enseigne à l'autre.",
        "**Prix** : TTC, hors frais de port sauf mention contraire. Ils changent chaque semaine ; "
        "le document fixe la méthode et les seuils, pas les montants.",
        "**Liens constructeur** : liens d'entrée de catalogue, par référence, sur le site du "
        "constructeur. La fiche exacte dépend du catalogue local et s'ouvre avant commande.",
        "**Spécifications** : cœurs, fréquences et TDP tels qu'annoncés par Intel et AMD ; "
        "millésime = année de lancement du processeur, non du châssis.",
        "**Périmètre** : postes fixes de bureautique. Les postes nomades suivront la même logique "
        "à deux bases ; ils ne sont pas traités ici.",
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
    cp.title = "Postes fixes — deux bases, une décision"
    cp.subject = "Base A 16 Go et base B 32 Go, trois constructeurs, chiffrage des cinq enseignes"
    d.save(dpath)
    return dpath, ppath


# --------------------------------------------------------------------------- #
def _sheet(ws, headers, widths):
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
    from openpyxl.utils import get_column_letter

    head = PatternFill("solid", fgColor=BLEU)
    for c, (h, w) in enumerate(zip(headers, widths), 1):
        cell = ws.cell(row=1, column=c, value=h)
        cell.fill = head
        cell.font = Font(color="FFFFFF", bold=True, size=9, name="Calibri")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = Border(bottom=Side(style="thin", color="D0D7E2"))
        ws.column_dimensions[get_column_letter(c)].width = w
    ws.row_dimensions[1].height = 32


def build_xlsx(path):
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

    wb = Workbook()
    thin = Side(style="thin", color="D0D7E2")

    # ---- 1 machines
    ws = wb.active
    ws.title = "1 Machines"
    heads = ["Base", "Gamme", "Constructeur", "Référence de châssis", "CPU Intel", "Variante AMD",
             "RAM", "Stockage", "Réseau", "Amazon", "Fnac", "Cdiscount", "LDLC", "Materiel.net",
             "Fiche constructeur", "Réserves"]
    widths = [7, 16, 12, 30, 16, 42, 20, 14, 26, 12, 12, 16, 12, 16, 34, 40]
    _sheet(ws, heads, widths)
    gammes = [("A", "Entrée de gamme")] * 3 + [("B1", "Standard entreprise")] * 3 + \
             [("B2", "Confort / longue durée")] * 3
    notes = [
        "Aucun prix neuf à la référence exacte sur les cinq enseignes",
        "Aucun prix neuf à la référence exacte sur les cinq enseignes",
        "Aucun prix neuf à la référence exacte sur les cinq enseignes",
        "Prix Cdiscount sur la référence exacte ; Materiel.net sur la génération G1i (°)",
        "Aucun prix relevé sur les cinq enseignes",
        "Prix Cdiscount sur la génération Gen 6 (°)",
        "Prix Materiel.net sur la génération G1i, châssis mini (°)",
        "Aucun prix relevé sur les cinq enseignes",
        "Prix Amazon sur un châssis mini, 64 Go / 2 To (°)",
    ]
    rows = A_MARCHE + B1_MARCHE + B2_MARCHE
    for i, (row, (b, g), note) in enumerate(zip(rows, gammes, notes), start=2):
        vals = [b, g, row[0], row[1], row[2], row[3], row[4], row[5], row[6]] + row[7:12] + \
               [row[12].replace("[ouvrir](", "").rstrip(")"), note]
        for j, v in enumerate(vals, 1):
            cell = ws.cell(row=i, column=j, value=v)
            cell.font = Font(size=9, name="Calibri")
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.border = Border(bottom=thin)
            if j == 15:
                cell.hyperlink = v
                cell.font = Font(size=9, name="Calibri", color="1155CC", underline="single")
            if 10 <= j <= 14 and isinstance(v, str) and not v[0].isdigit():
                cell.font = Font(size=9, name="Calibri", color=GRIS)
    ws.auto_filter.ref = "A1:P%d" % (len(rows) + 1)
    ws.freeze_panes = "D2"
    ws.sheet_properties.tabColor = BLEU

    # ---- 2 seuils
    ws2 = wb.create_sheet("2 Seuils")
    _sheet(ws2, ["Base", "Seuil opposable", "Valeur"], [8, 26, 90])
    r = 2
    for k, v in A_SEUIL:
        for j, val in enumerate(("A", k, v), 1):
            c = ws2.cell(row=r, column=j, value=val)
            c.font = Font(size=9, bold=(j == 1), name="Calibri")
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = Border(bottom=thin)
        r += 1
    for row in B_SEUIL:
        for j, val in enumerate(("B", row[0], "%s / %s" % (row[1], row[2])), 1):
            c = ws2.cell(row=r, column=j, value=val)
            c.font = Font(size=9, bold=(j == 1), name="Calibri")
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = Border(bottom=thin)
        r += 1
    ws2.auto_filter.ref = "A1:C%d" % (r - 1)
    ws2.freeze_panes = "A2"
    ws2.sheet_properties.tabColor = "1E6B33"

    # ---- 3 cpu
    ws3 = wb.create_sheet("3 CPU")
    _sheet(ws3, CPU_HEADERS, [8, 24, 22, 18, 10, 14, 14])
    for i, row in enumerate(CPU_ROWS, start=2):
        for j, v in enumerate(row, 1):
            c = ws3.cell(row=i, column=j, value=v)
            c.font = Font(size=9, bold=(j == 1), name="Calibri")
            c.border = Border(bottom=thin)
    ws3.auto_filter.ref = "A1:G%d" % (len(CPU_ROWS) + 1)
    ws3.freeze_panes = "B2"
    ws3.sheet_properties.tabColor = "7A5E12"

    # ---- 4 chiffrage
    ws4 = wb.create_sheet("4 Chiffrage")
    _sheet(ws4, CHIFFRAGE_HEADERS, [16, 60, 60])
    for i, row in enumerate(CHIFFRAGE_ROWS, start=2):
        for j, v in enumerate(row, 1):
            c = ws4.cell(row=i, column=j, value=v)
            c.font = Font(size=9, bold=(j == 1), name="Calibri")
            c.alignment = Alignment(wrap_text=True, vertical="top")
            c.border = Border(bottom=thin)
    ws4.auto_filter.ref = "A1:C%d" % (len(CHIFFRAGE_ROWS) + 1)
    ws4.freeze_panes = "B2"
    ws4.sheet_properties.tabColor = "A23B1A"

    # ---- 5 méthode
    ws5 = wb.create_sheet("5 Méthode")
    ws5.column_dimensions["A"].width = 20
    ws5.column_dimensions["B"].width = 110
    notes5 = [
        ("Deux règles", "La base B (32 Go) est la référence d'achat ; la base A (16 Go) est un "
                        "chemin de repli budgétaire, justifié poste par poste."),
        ("Dell et AMD", "Aucune offre AMD sur OptiPlex : la cellule vaut « — », fait de "
                        "catalogue. AMD chez HP (405, 805) et Lenovo (M75)."),
        ("Cellules de prix", "Quatre états : montant relevé, « 0 résultat » (enseigne "
                             "interrogée, rien), « non relevé » (recherche en échec), « — » "
                             "(produit inexistant chez ce constructeur). Aucune estimation."),
        ("°", "Prix d'un châssis ou d'une génération voisine : il situe le niveau, il ne vaut "
              "pas offre."),
        ("Source", "Amazon.fr, Fnac, Cdiscount, LDLC, Materiel.net — relevés du 5 novembre 2026."),
        ("Prix", "TTC, hors frais de port sauf mention contraire ; ils changent chaque semaine."),
        ("Filtres", "Filtre automatique sur chaque feuille ; il fonctionne à l'identique dans "
                    "Excel, LibreOffice Calc et Google Sheets."),
    ]
    for r, (k, v) in enumerate(notes5, start=1):
        a = ws5.cell(row=r, column=1, value=k)
        a.font = Font(bold=True, size=9)
        b = ws5.cell(row=r, column=2, value=v)
        b.font = Font(size=9)
        b.alignment = Alignment(wrap_text=True, vertical="top")

    wb.properties.creator = "GED-SERVICES"
    wb.properties.title = "Postes fixes — deux bases, une décision"
    wb.properties.subject = "Base A 16 Go, base B 32 Go, trois constructeurs, cinq enseignes"
    wb.save(path)
    return path


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print("xlsx :", build_xlsx(os.path.join(OUT, BASE + ".xlsx")))
    print("docx+pdf :", build_doc())
