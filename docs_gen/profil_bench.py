# -*- coding: utf-8 -*-
"""Profil matériel des postes fixes — deux bases mémoire, trois gammes.

    1. Base 16 Go      ┐ mêmes lignes, mêmes colonnes, seule la base change :
    2. Base 32 Go      ┘ les deux tableaux se lisent face à face
    3. Les processeurs retenus (référence et alternative, Intel et AMD)
    4. Trois constructeurs par gamme : une référence HP, Dell et Lenovo
    5. Les pièges qui comptent
    6. Les postes nomades, puis méthode et recommandation
"""
from __future__ import annotations

import os

from render import Doc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "livrables")
BASE = "Profil_postes_fixes_base_16_Go_et_base_32_Go"

BLEU = "1F3B63"
GRIS = "EDEDED"

# --------------------------------------------------------------------------- #
# Tableaux 1 et 2 — six colonnes identiques
BASE_HEADERS = ["Gamme", "CPU Intel — référence et alternative",
                "CPU AMD — référence et alternative", "Mémoire",
                "Stockage", "Système · réseau · garantie"]
BASE_WIDTHS = [2.4, 6.6, 5.6, 3.6, 2.6, 5.1]

CPU_I_ENTREE = ("**Core i5-13400** · 10C/16T (6P+4E) · 2,5/4,6 GHz · 65 W · LGA1700 · janv. 2023. "
                "Alt. **i5-13500** · 14C/20T · 2,5/4,8 GHz · 65 W.")
CPU_A_ENTREE = ("**Ryzen 5 PRO 7645** · 6C/12T · 3,8/5,1 GHz · 65 W · AM5 · 2023. "
                "Alt. **Ryzen 5 8500G** · 6C/12T (2 Zen 4 + 4 Zen 4c) · 3,5/5,0 GHz.")
CPU_I_STD = ("**Core i5-14500** · 14C/20T (6P+8E) · 2,6/5,0 GHz · 65 W · LGA1700 · janv. 2024. "
             "Alt. **Core Ultra 5 235** · 14C/14T · 3,4/5,0 GHz · LGA1851 · 2025.")
CPU_A_STD = ("**Ryzen 7 PRO 7745** · 8C/16T · 3,8/5,3 GHz · 65 W · AM5 · 2023. "
             "Alt. **Ryzen 5 PRO 8600G** · 6C/12T · 4,3/5,0 GHz.")
CPU_I_CONF = ("**Core i7-14700** · 20C/28T (8P+12E) · 2,1/5,3 GHz · 65 W · LGA1700 · janv. 2024. "
              "Alt. **Core Ultra 7 265** · 20C/20T · 2,4/5,3 GHz · LGA1851 · 2025.")
CPU_A_CONF = ("**Ryzen 9 PRO 7945** · 12C/24T · 3,7/5,4 GHz · 65 W · AM5 · 2023. "
              "Alt. **Ryzen 7 9700X** · 8C/16T · 3,8/5,5 GHz · août 2024.")

T1 = [
    ["**Entrée de gamme**", CPU_I_ENTREE, CPU_A_ENTREE,
     "16 Go DDR4 ou DDR5, 2 emplacements",
     "SSD 512 Go — SATA toléré",
     "Windows 11 Pro · 1 GbE + Wi-Fi 6 · **1 an** (3 ans en option)"],
    ["**Standard entreprise**", CPU_I_STD, CPU_A_STD,
     "16 Go DDR5 — minimum de la base ; la cible reste 32 Go",
     "SSD NVMe 512 Go à 1 To",
     "Windows 11 Pro · 1 GbE + Wi-Fi 6/6E · **3 ans sur site**"],
    ["**Confort / longue durée**", "Non ouvert sur cette base", "Non ouvert sur cette base",
     "—", "—", "Voir tableau 2"],
]

T2 = [
    ["**Entrée de gamme**", CPU_I_ENTREE, CPU_A_ENTREE,
     "32 Go DDR5 (2 × 16), 2 emplacements",
     "SSD NVMe 512 Go",
     "Windows 11 Pro · 1 GbE + Wi-Fi 6 · **3 ans sur site**"],
    ["**Standard entreprise**", CPU_I_STD, CPU_A_STD,
     "32 Go DDR5 (2 × 16), extensible à 64 Go",
     "SSD NVMe 512 Go à 1 To",
     "Windows 11 Pro · 1 GbE + Wi-Fi 6/6E · **3 ans sur site**"],
    ["**Confort / longue durée**", CPU_I_CONF, CPU_A_CONF,
     "32 Go DDR5 (2 × 16), extensible à 64 Go",
     "SSD NVMe 1 To + emplacement libre",
     "Windows 11 Pro · 1 GbE + Wi-Fi 6E · **3 ans sur site**"],
]

# Sommaire des trois gammes
SOMMAIRE = [
    ["**Entrée de gamme**", "Accueil, saisie, consultation, poste nomade occasionnel",
     "i5-13400 ou Ryzen 5 PRO 7645 · 16 Go · SSD 512 Go · Windows 11 Pro · "
     "1 GbE + Wi-Fi 6 · 1 an"],
    ["**Standard entreprise**", "Bureautique intensive, Sage, Teams, applications multiples",
     "i5-14500 ou Ryzen 7 PRO 7745 · 32 Go DDR5 · NVMe 512 Go à 1 To · Windows 11 Pro · "
     "3 ans sur site"],
    ["**Confort / longue durée**", "Postes gardés cinq ans, CAO légère, gros tableurs",
     "i7-14700 ou Ryzen 9 PRO 7945 · 32 Go extensible à 64 Go · NVMe 1 To · Windows 11 Pro · "
     "3 ans sur site"],
]

# Tableau des deux bases en perspective
PERSP_HEADERS = ["Critère", "Base 16 Go", "Base 32 Go"]
PERSP = [
    ["Gammes ouvertes", "Entrée de gamme et standard", "Les trois, confort compris"],
    ["Usage couvert", "Accueil, saisie, consultation, Sage mono-société, Teams",
     "Bureautique intensive, Sage multi-sociétés, gros tableurs, CAO légère, cinq ans"],
    ["Mémoire", "16 Go (1 × 16 ou 2 × 8), DDR4 ou DDR5", "32 Go (2 × 16), DDR5"],
    ["Extension", "Jusqu'à 32 Go sur la plupart des châssis", "Jusqu'à 64 Go"],
    ["Marge sur cinq ans", "Saturée en deux à trois ans selon l'usage",
     "Confortable jusqu'au retrait du poste"],
    ["Décision", "Plancher budgétaire, à assumer comme tel",
     "Base d'achat recommandée pour tout le parc"],
]

# --------------------------------------------------------------------------- #
# Tableau 3 — les processeurs retenus
CPU_HEADERS = ["Gamme", "Marque", "Modèle", "Cœurs / threads", "Base / boost", "TDP",
               "Socket", "Mémoire", "Sortie", "Commentaire"]
CPU_WIDTHS = [2.6, 1.9, 3.4, 3.2, 2.6, 1.7, 2.2, 2.4, 2.1, 3.8]
CPU_ROWS = [
    ["Entrée", "Intel", "Core i5-13400", "10C/16T (6P+4E)", "2,5 / 4,6 GHz", "65 W",
     "LGA1700", "DDR4 ou DDR5", "janv. 2023", "Plancher de l'entrée de gamme"],
    ["Entrée", "Intel", "Core i5-13500", "14C/20T (6P+8E)", "2,5 / 4,8 GHz", "65 W",
     "LGA1700", "DDR4 ou DDR5", "janv. 2023", "14 cœurs pour le prix d'un 10 cœurs"],
    ["Entrée", "AMD", "Ryzen 5 PRO 7645", "6C/12T", "3,8 / 5,1 GHz", "65 W",
     "AM5", "DDR5", "2023", "PRO : DASH, chipset PRO requis"],
    ["Entrée", "AMD", "Ryzen 5 8500G", "6C/12T (2 Zen 4 + 4 Zen 4c)", "3,5 / 5,0 GHz", "65 W",
     "AM5", "DDR5", "janv. 2024", "iGPU correct, pas de PRO"],
    ["Standard", "Intel", "Core i5-14500", "14C/20T (6P+8E)", "2,6 / 5,0 GHz", "65 W",
     "LGA1700", "DDR4 ou DDR5", "janv. 2024", "Référence du standard"],
    ["Standard", "Intel", "Core Ultra 5 235", "14C/14T (6P+8E)", "3,4 / 5,0 GHz", "65 W",
     "LGA1851", "DDR5", "janv. 2025", "Pas d'hyperthreading : 14 cœurs = 14 threads"],
    ["Standard", "AMD", "Ryzen 7 PRO 7745", "8C/16T", "3,8 / 5,3 GHz", "65 W",
     "AM5", "DDR5", "2023", "Le plus proche du 14500, 6 cœurs de moins"],
    ["Standard", "AMD", "Ryzen 5 PRO 8600G", "6C/12T", "4,3 / 5,0 GHz", "65 W",
     "AM5", "DDR5", "2024", "iGPU Radeon 760M"],
    ["Confort", "Intel", "Core i7-14700", "20C/28T (8P+12E)", "2,1 / 5,3 GHz", "65 W",
     "LGA1700", "DDR4 ou DDR5", "janv. 2024", "Jamais en version T : 65 W exigés"],
    ["Confort", "Intel", "Core Ultra 7 265", "20C/20T (8P+12E)", "2,4 / 5,3 GHz", "65 W",
     "LGA1851", "DDR5", "janv. 2025", "20 cœurs / 20 threads"],
    ["Confort", "AMD", "Ryzen 9 PRO 7945", "12C/24T", "3,7 / 5,4 GHz", "65 W",
     "AM5", "DDR5", "2023", "Seule réponse AMD au 14700"],
    ["Confort", "AMD", "Ryzen 7 9700X", "8C/16T", "3,8 / 5,5 GHz", "65 W",
     "AM5", "DDR5", "août 2024", "Zen 5, 8 cœurs seulement"],
]

# --------------------------------------------------------------------------- #
# Tableau 4 — trois constructeurs par gamme
FAB_HEADERS = ["Gamme", "Constructeur", "Référence de châssis", "CPU retenu",
               "Mémoire", "Garantie", "Voie AMD"]
FAB_WIDTHS = [1.7, 2.5, 4.0, 2.8, 2.4, 1.7, 2.0]
FAB_ROWS = [
    ["Entrée", "HP", "ProDesk 400 G9 SFF", "i5-13500 — 65 W", "16 Go DDR4", "1 an",
     "ProDesk 405 G9"],
    ["Entrée", "Dell", "OptiPlex 7010 SFF", "i5-13500 — 65 W", "16 Go DDR4", "1 an",
     "—"],
    ["Entrée", "Lenovo", "ThinkCentre M70t Gen 4", "i5-13500 — 65 W", "16 Go DDR4", "1 an",
     "M75t Gen 2"],
    ["Standard", "HP", "Elite 800 G9 Mini", "i5-14500 — 65 W", "32 Go DDR5", "3 ans",
     "EliteDesk 805 G9"],
    ["Standard", "Dell", "OptiPlex 7020 MFF", "i5-14500 — 65 W", "32 Go DDR5", "3 ans",
     "—"],
    ["Standard", "Lenovo", "ThinkCentre M90q Gen 5", "i5-14500 — 65 W", "32 Go DDR5", "3 ans",
     "M75q Gen 5"],
    ["Confort", "HP", "Elite 800 G9 SFF", "i7-14700 — 65 W", "32 → 64 Go DDR5", "3 ans",
     "EliteDesk 805 G9"],
    ["Confort", "Dell", "OptiPlex 7020 SFF", "i7-14700 — 65 W", "32 → 64 Go DDR5", "3 ans",
     "—"],
    ["Confort", "Lenovo", "ThinkCentre M90t Gen 5", "i7-14700 — 65 W", "32 → 64 Go DDR5", "3 ans",
     "M75t Gen 2"],
]

# --------------------------------------------------------------------------- #
CHASSIS_HEADERS = ["Format", "Ce qu'il apporte", "Ce qu'il impose", "Gamme"]
CHASSIS_WIDTHS = [2.4, 6.2, 5.6, 2.9]
CHASSIS_ROWS = [
    ["Mini 1 litre", "Encombrement minimal, fixation VESA derrière l'écran",
     "Version T (35 W) le plus souvent, deux SO-DIMM seulement, pas de carte graphique",
     "Entrée, standard"],
    ["SFF", "Processeur 65 W, deux barrettes DIMM, un emplacement demi-hauteur",
     "Volume au sol, ventilation un peu plus audible", "Standard, confort"],
    ["Tour", "65 W, extension maximale : barrettes, disques, carte graphique",
     "Le plus encombrant, le plus lourd", "Confort"],
]

# Tableau 5 — les pièges
PIE_HEADERS = ["Piège", "Ce qui se passe", "Ce qu'il faut exiger"]
PIE_WIDTHS = [3.3, 7.2, 6.6]
PIE_ROWS = [
    ["Dégradation Raptor Lake (13ᵉ et 14ᵉ générations)",
     "Instabilité par dérive de tension, surtout sur i7 et i9. Correctifs microcode 0x12B "
     "puis 0x12F, distribués par BIOS.",
     "BIOS à jour à la livraison, version relevée sur chaque poste et consignée ; contrôle "
     "annuel de la flotte."],
    ["vPro (AMT) sans équivalent AMD",
     "AMD propose DASH, qui fonctionne, mais l'outillage de gestion de parc est plus mince. "
     "Les CPU PRO exigent en plus un chipset PRO.",
     "vPro exigé au-delà de 50 postes ; en deçà, DASH documenté noir sur blanc dans la "
     "commande."],
    ["AM5 est DDR5 exclusif",
     "LGA1700 accepte DDR4 et DDR5 selon la carte mère ; AM5 non.",
     "Budget contraint sur l'entrée de gamme : rester en LGA1700 pour garder la DDR4."],
    ["Ryzen non-G et SKU « F » sans iGPU",
     "Les Ryzen non-G ont un iGPU minimal (2 CU), suffisant en bureautique ; les « F » "
     "n'affichent rien sans carte dédiée.",
     "Proscrire tout SKU F dans la commande ; vérifier la présence d'un iGPU sur chaque ligne."],
    ["Wi-Fi 6E sur plateforme AMD",
     "Passe le plus souvent par un module Intel AX211 en CNVio2, qui suppose une carte mère "
     "compatible.",
     "Exiger le Wi-Fi 6E au devis, sinon le poste retombe en Wi-Fi 6 sans que le prix baisse."],
    ["SKU à écarter pour un parc tenu cinq ans",
     "Core i5-12400 (2022), Ryzen 5 5600G (AM4, DDR4, 2021) et tout « T » à 35 W sur le "
     "profil confort.",
     "Millésime 2023 ou plus récent ; version T tolérée en entrée de gamme et en mini-PC, "
     "interdite en confort."],
    ["Postes nomades",
     "Le 1 GbE passe presque toujours par la station d'accueil en USB-C ; le Thunderbolt "
     "reste Intel.",
     "Dock imposé dans la commande ; Thunderbolt seulement si la plateforme est Intel."],
]

# --------------------------------------------------------------------------- #
# Tableau 6 — les nomades
NOM_HEADERS = ["Gamme", "Intel", "Cœurs / threads", "Base / boost", "TDP", "Sortie", "AMD"]
NOM_WIDTHS = [2.1, 3.3, 3.0, 2.5, 1.6, 1.9, 2.7]
NOM_ROWS = [
    ["Entrée", "Core i5-1345U", "10C/12T (2P+8E)", "1,2 / 4,7 GHz", "15 W", "janv. 2023",
     "Ryzen 5 PRO 7540U · 6C/12T · 3,2/4,9 GHz"],
    ["Standard", "Core Ultra 5 135U", "12C/14T (2P+8E+2LP)", "1,3 / 4,4 GHz", "15 W", "déc. 2023",
     "Ryzen 5 8640U · 6C/12T · 3,5/4,9 GHz"],
    ["Confort", "Core Ultra 7 165U", "12C/14T (2P+8E+2LP)", "1,7 / 4,9 GHz", "15 W", "2024",
     "Ryzen 7 PRO 8840U · 8C/16T · 3,3/5,1 GHz"],
]


# --------------------------------------------------------------------------- #
def build_doc():
    doc = Doc(
        base=BASE,
        title="Profil matériel des postes fixes — base 16 Go et base 32 Go",
        subtitle="Trois gammes, deux bases mémoire, trois constructeurs",
        meta=[],
        doc_ref="GED-PROFIL-2026-11-A · Confidentiel — usage interne",
        footer="GED-SERVICES · profil matériel des postes fixes",
    )

    doc.cover(
        eyebrow="Profil matériel — postes fixes · trois gammes",
        title="Postes fixes\nbase 16 Go · base 32 Go",
        subtitle="Le profil technique des trois gammes — entrée de gamme, standard, confort — "
                 "présenté sur deux bases mémoire, puis décliné chez HP, Dell et Lenovo.",
        meta_rows=[
            ["Destinataire", "**M. Jad, directeur général — ADCHIM**"],
            ["Émetteur", "**Joël MBA OYONE — GED-SERVICES**"],
            ["Objet", "Fixer le profil matériel des postes fixes : trois gammes, deux bases "
                      "mémoire, une référence par constructeur"],
            ["Tableau 1", "**Base 16 Go** — entrée de gamme et standard"],
            ["Tableau 2", "**Base 32 Go** — les trois gammes ; se lit face au tableau 1"],
            ["Tableau 3", "**Les processeurs retenus** — référence et alternative, Intel et AMD, "
                          "cœurs, fréquences, TDP, socket, sortie"],
            ["Tableau 4", "**Trois constructeurs par gamme** — une référence HP, Dell et Lenovo"],
            ["Tableau 5", "**Les pièges** — Raptor Lake, vPro et DASH, AM5, iGPU, Wi-Fi 6E, "
                          "SKU à écarter"],
            ["Tableau 6", "**Les postes nomades** — équivalents mobiles par gamme"],
            ["Lecture", "Fréquences **base / boost**, TDP de base constructeur, socket, "
                        "**année de lancement du processeur** — jamais celle du châssis"],
            ["Sources", "Fiches Intel et AMD ; gammes HP, Dell et Lenovo ; relevés Amazon.fr "
                        "du **5 novembre 2026** pour les prix, qui ne figurent pas ici"],
        ],
        pagebreak=False,
    )
    doc.pagebreak()

    # ------------------------------------------------------- deux bases en regard
    doc.h1_plain("Deux bases, une seule grille de lecture")
    doc.p("Le profil se présente sur **deux bases mémoire distinctes**, 16 Go et 32 Go. Les deux "
          "tableaux qui suivent ont les mêmes lignes et les mêmes colonnes : ils se lisent l'un "
          "sous l'autre, et l'écart entre deux lignes est exactement ce que la base mémoire "
          "change. Le processeur ne change pas d'une base à l'autre — la mémoire, le stockage, "
          "la garantie et les gammes ouvertes, si.", small=True)
    doc.table(["Gamme", "Usage visé", "Plancher technique retenu"], SOMMAIRE,
              [2.6, 5.4, 9.1], font=7.8, aligns=["l", "l", "l"], first_col_bold=True,
              cell_fmt={(i, 0): {"bg": "EDF1F7"} for i in range(len(SOMMAIRE))},
              caption="Les trois gammes en une ligne. Le détail suit : bases mémoire aux "
                      "tableaux 1 et 2, processeurs au tableau 3, constructeurs au tableau 4.")

    doc.spacer(0.2)
    doc.table(PERSP_HEADERS, PERSP, [3.4, 6.6, 7.1], font=8.2,
              aligns=["l", "l", "l"], first_col_bold=True,
              cell_fmt={(i, 0): {"bg": "EDF1F7"} for i in range(len(PERSP))},
              caption="Les deux bases en perspective. La base 16 Go n'ouvre pas le profil "
                      "confort : ce n'est pas une opinion, c'est une conséquence de la mémoire "
                      "demandée par les applicatifs du profil.")
    doc.p("**Trois gammes, une référence par constructeur.** Chaque gamme existe sur les deux "
          "bases et se décline chez HP, Dell et Lenovo (tableau 4) : une référence retenue par "
          "gamme et par constructeur, les autres configurations restant au devis. La voie AMD "
          "n'est ouverte que chez HP et Lenovo.", small=True)

    doc.p("**Comment lire les tableaux qui suivent.**", small=True)
    doc.ul([
        "**Fréquences** : la base est le régime garanti, le boost une pointe sur un ou deux "
        "cœurs. Un poste se juge sur la base ; le boost fait la ligne de la plaquette.",
        "**TDP** : 65 W pour les châssis SFF et les tours, 35 W pour les versions T des mini-PC. "
        "Le même nom de processeur ne donne pas le même poste dans les deux châssis.",
        "**Socket et mémoire** : LGA1700 accepte DDR4 et DDR5 selon la carte mère ; AM5 et "
        "LGA1851 sont DDR5 exclusivement.",
        "**Cœurs** : un plancher, pas une promesse — cœurs performance et cœurs efficaces n'ont "
        "pas le même rendement.",
        "**Année** : celle du lancement du processeur, jamais celle du châssis.",
    ], small=True)

    # ------------------------------------------------------------- tableaux 1 et 2
    doc.landscape(True)
    doc.h1_plain("Tableau 1 — Base 16 Go")
    doc.table(BASE_HEADERS, T1, BASE_WIDTHS, font=7.4, header_bg=BLEU,
              aligns=["l", "l", "l", "l", "l", "l"], first_col_bold=True,
              cell_fmt={(2, j): {"bg": GRIS, "color": "6E6E6E"} for j in range(6)},
              caption="Tableau 1 — Base 16 Go : DDR4 ou DDR5 selon la carte mère. Le confort "
                      "n'est pas ouvert sur cette base.")

    doc.spacer(0.2)
    doc.h1_plain("Tableau 2 — Base 32 Go")
    doc.table(BASE_HEADERS, T2, BASE_WIDTHS, font=7.4, header_bg=BLEU,
              aligns=["l", "l", "l", "l", "l", "l"], first_col_bold=True,
              caption="Tableau 2 — Base 32 Go : DDR5 exclusivement, deux barrettes de 16 Go, "
                      "extension à 64 Go. Mêmes lignes, mêmes colonnes que le tableau 1 : la "
                      "comparaison se fait ligne à ligne.")

    # ---------------------------------------------------------------- tableau 3
    doc.pagebreak()
    doc.h1_plain("Tableau 3 — Les processeurs retenus, gamme par gamme")
    doc.p("Douze processeurs, six Intel et six AMD : pour chaque gamme, une référence et une "
          "alternative par constructeur de puce. Les fréquences sont données en base et en "
          "boost, les TDP sont les enveloppes de base annoncées par Intel et AMD.", small=True)
    doc.table(CPU_HEADERS, CPU_ROWS, CPU_WIDTHS, font=7.4,
              aligns=["l", "c", "l", "l", "c", "c", "c", "c", "c", "l"],
              first_col_bold=True,
              cell_fmt={(i, 9): {"b": False} for i in range(len(CPU_ROWS))},
              caption="Tableau 3 — Le catalogue de référence. LGA1700 accepte DDR4 et DDR5 "
                      "selon la carte mère ; LGA1851 et AM5 sont DDR5 exclusivement.")

    # ---------------------------------------------------------------- tableau 4
    doc.landscape(False)
    doc.h1_plain("Tableau 4 — Trois constructeurs, une référence par gamme")
    doc.p("Neuf lignes, trois gammes et trois constructeurs. Pour chacune, le châssis retenu, le "
          "processeur qu'il accepte en version 65 W, la dotation mémoire de la base 32 Go et la "
          "garantie. La dernière colonne indique la voie AMD du constructeur, quand elle existe.",
          small=True)
    doc.table(FAB_HEADERS, FAB_ROWS, FAB_WIDTHS, font=7.6,
              aligns=["l", "c", "l", "l", "l", "c", "l"], first_col_bold=True,
              caption="Tableau 4 — Références de châssis indicatives : le SKU exact, la "
                      "configuration mémoire et la durée de garantie se confirment à la "
                      "commande. Dell ne propose pas d'OptiPlex AMD : le tiret signale une "
                      "gamme fermée à AMD chez ce constructeur. Les mini-PC n'acceptent que "
                      "des versions T à 35 W, réservées à l'entrée de gamme et au standard ; "
                      "le confort exige un SFF ou une tour.")

    doc.spacer(0.2)
    doc.table(CHASSIS_HEADERS, CHASSIS_ROWS, CHASSIS_WIDTHS, font=7.6,
              aligns=["l", "l", "l", "c"], first_col_bold=True,
              caption="Le format décide du processeur avant la marque : un mini impose souvent "
                      "la version T, une tour l'accepte en 65 W. À trancher avec la gamme, pas "
                      "après la commande.")

    # ---------------------------------------------------------------- tableau 5
    doc.pagebreak()
    doc.h1_plain("Tableau 5 — Les pièges qui comptent")
    doc.p("Sept points qui coûtent plus cher que la fréquence : ce sont eux qui décident du "
          "vieillissement d'un parc sur cinq ans.", small=True)
    doc.table(PIE_HEADERS, PIE_ROWS, PIE_WIDTHS, font=7.6, aligns=["l", "l", "l"],
              first_col_bold=True,
              caption="Tableau 5 — À vérifier avant la commande, pas après la livraison.")

    # ---------------------------------------------------------------- tableau 6
    doc.pagebreak()
    doc.h1_plain("Tableau 6 — Les postes nomades")
    doc.p("Mêmes trois gammes, mêmes exigences, transposées au portable : les processeurs "
          "mobiles n'ont pas les fréquences des fixes, et le réseau passe par la station "
          "d'accueil.", small=True)
    doc.table(NOM_HEADERS, NOM_ROWS, NOM_WIDTHS, font=7.6,
              aligns=["l", "l", "l", "c", "c", "c", "l"], first_col_bold=True,
              caption="Tableau 6 — Équivalents mobiles. Le 1 GbE passe presque toujours par le "
                      "dock en USB-C ; le Thunderbolt reste réservé aux plateformes Intel.")

    # ---------------------------------------------------------------- méthode
    doc.h1_plain("Méthode et réserves")
    doc.ul([
        "**Périmètre** : postes fixes de bureautique, trois gammes, deux bases mémoire, trois "
        "constructeurs. Les stations de travail graphiques et les serveurs sont hors sujet.",
        "**Spécifications** : fréquences base et boost, TDP de base, socket et année de "
        "lancement du processeur, tels qu'annoncés par Intel et AMD. Aucune valeur déduite, "
        "aucune estimation.",
        "**Deux bases** : 16 Go DDR4 ou DDR5, 32 Go DDR5. La base 16 Go n'ouvre pas le profil "
        "confort ; le tableau 2 le montre ligne à ligne.",
        "**Garanties** : 1 an constructeur en entrée de gamme — 3 ans en option ; 3 ans sur site, "
        "pièces et main-d'œuvre, à partir du standard.",
        "**Processeurs** : un i5-1334U (15 W, 10 cœurs, version AiO ou portable) porte le même "
        "nom qu'un i5-13500 (65 W, 14 cœurs) et vaut environ la moitié en multi-cœur. D'où le "
        "plancher de cœurs et les deux fréquences, qui valent mieux que le nom de la gamme.",
        "**Stockage** : SATA toléré en entrée de gamme seulement ; NVMe obligatoire à partir du "
        "standard, pour 10 € d'écart sur 512 Go et un facteur quatre en débit.",
        "**Version T (35 W)** : imposée par les châssis d'un litre, tolérée en entrée de gamme et "
        "en standard, **interdite en confort** — le profil perd alors 30 % de performance.",
        "**AMD** : aucune offre OptiPlex chez Dell ; la voie AMD se joue chez HP (ProDesk, "
        "EliteDesk) et Lenovo (ThinkCentre M75). Les configurations exactes se confirment au "
        "devis, les châssis PRO AMD n'étant pas toujours ouverts sur les mêmes SKU que les "
        "châssis Intel.",
        "**Prix** : aucun prix dans ce document. Les tarifs relevés le 5 novembre 2026 figurent "
        "dans les benchmarks HP et Dell du même dossier.",
    ], small=True)

    doc.h1_plain("Recommandation")
    doc.p("Retenir la **base 32 Go** comme standard d'achat : c'est la seule qui couvre les trois "
          "gammes et tienne cinq ans. La base 16 Go reste le plancher budgétaire de l'accueil et "
          "de la saisie, à condition d'assumer un remplacement à trois ans.", small=True)
    doc.p("Côté puce, un **Core i5-14500** en 65 W avec 32 Go DDR5 et trois ans sur site couvre le "
          "standard sans discussion ; un **i7-14700** en SFF ou en tour couvre le confort — jamais "
          "en version T. AMD se justifie sur une contrainte thermique ou électrique, ou sur une "
          "politique de socket durable (AM5 est annoncé jusqu'en 2027, LGA1700 est en fin de vie, "
          "LGA1851 sera remplacé vite) : pas sur le prix.", small=True)
    doc.p("Une réserve à garder en tête : le profil confort parle de CAO légère avec un GPU "
          "intégré. C'est optimiste. Toute CAO un peu sérieuse réclame une carte graphique "
          "dédiée, quelle que soit la puce retenue.", small=True)

    dpath, ppath = doc.save(OUT)

    import docx as _docx

    d = _docx.Document(dpath)
    cp = d.core_properties
    cp.author = "GED-SERVICES"
    cp.last_modified_by = "GED-SERVICES"
    cp.comments = ""
    cp.keywords = ""
    cp.category = ""
    cp.title = "Profil matériel des postes fixes — base 16 Go et base 32 Go"
    cp.subject = "Trois gammes, deux bases mémoire, trois constructeurs"
    d.save(dpath)
    return dpath, ppath


if __name__ == "__main__":
    print(build_doc())
