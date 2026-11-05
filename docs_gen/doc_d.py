# -*- coding: utf-8 -*-
"""Document D — cinq tableaux comparatifs, un par constructeur."""
import os
from render import Doc
from charts import fig_d_prix

BASE = "D_Cinq_constructeurs_tableaux_comparatifs"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables")

doc = Doc(
    base=BASE,
    title="Cinq constructeurs, cinq lectures",
    subtitle="Configurations serveur comparées à l'existant",
    meta=[],
    doc_ref="GED-RAP-2026-04 · Confidentiel — usage interne",
    footer="Cinq constructeurs, cinq lectures",
)

# --------------------------------------------------------------------------- #
# Conventions de couleur
VERT_BG, VERT_TX = "E3F0DC", "1E6B2F"
JAUN_BG, JAUN_TX = "FBF3D0", "8A6D00"
ORAN_BG, ORAN_TX = "FBE0CE", "B4500F"


def F(bg=None, tx=None, b=False, i=False):
    return {"bg": bg, "color": tx, "b": b, "i": i}


FMT = {"g": F(VERT_BG, VERT_TX, True), "y": F(JAUN_BG, JAUN_TX, True),
       "o": F(ORAN_BG, ORAN_TX, True), "x": F()}

LIGNES = [
    ("Hébergement", "Type d'offre"),
    ("Matériel", "Modèle et format rackable"),
    ("", "Processeur et génération"),
    ("", "Cœurs / fréquence"),
    ("", "Mémoire vive livrée"),
    ("", "Disques / **capacité utile** en RAID1"),
    ("", "Baies et contrôleur RAID"),
    ("Réseau", "Ports intégrés"),
    ("Exploitation", "Hyperviseur / administration"),
    ("", "Garantie constructeur"),
    ("Conformité", "Verdict face aux exigences"),
    ("Commercial", "Product Number"),
    ("", "Fournisseur et canal"),
    ("", "Tarif HT équipé"),
    ("", "Fiche constructeur"),
    ("Perspective", "Équivalent reconditionné 128 Go"),
]

REF = [
    "Serveur dédié hébergé (Online / Scaleway)",
    "**Non communiqué** — format rack présumé",
    "**Non communiqué**",
    "**8 cœurs / 2,5 GHz**",
    "**64 Go** — 88,4 % occupés",
    "≈ 960 Go → **0,96 To** utiles",
    "Non communiqué",
    "Non communiqué",
    "Non communiqué — cible : Proxmox VE",
    "Incluse dans l'abonnement",
    "**Saturé** : mémoire et disque",
    "—",
    "Location (Online / Scaleway)",
    "Facture mensuelle — non communiquée",
    "—",
    "—",
]

REF_LVL = {4: "o", 5: "o", 10: "o"}

# --------------------------------------------------------------------------- #
# Données par constructeur
HPE = dict(
    nom="HPE ProLiant",
    intro="HPE est la référence du dossier : iLO 6 pour l'administration hors bande, 10 GbE "
          "natif, pièces disponibles. **Point de lecture :** le 1U AMD est deux fois moins cher "
          "que le 2U Intel (5 726 € en 64 Go contre 16 861 € en 128 Go) — l'écart ne mesure pas "
          "la qualité, mais le prix du double socket et d'un processeur à 2,0 GHz.",
    configs=[
        dict(model="**DL325 Gen11** — 1U", proto="1U / 1 socket",
             cpu="AMD EPYC **9124** — Zen 4 (EPYC 9004, 2023)",
             cores="**16** cœurs · 3,0 → 3,7 GHz", ram="**64 Go** DDR5 4800 · 12 slots, 3 To max",
             disks="2×480 Go SATA → **0,96 To utiles**", bays="8 SFF · MR408i-o",
             net="2×10 GbE + 4×1 GbE", hyp="Proxmox VE · iLO 6",
             war="3/3/3 — 3 ans sur site", verdict="**Limite** : mémoire juste",
             pn="P77252-425", sup="PC21.fr", price="**5 726 €** · relevé",
             link="[hpe.com — DL325 Gen11](https://www.hpe.com/us/en/compute/hpe-proliant-compute/dl325-gen11.html)",
             lvl={"cores": "g", "ram": "o", "utile": "y", "war": "g", "verdict": "y"}),
        dict(model="**DL325 Gen11** — 1U", proto="1U / 1 socket",
             cpu="AMD EPYC **9124** — Zen 4 (EPYC 9004, 2023)",
             cores="**16** cœurs · 3,0 → 3,7 GHz", ram="**128 Go** DDR5 4800 · 12 slots, 3 To max",
             disks="2×1,92 To NVMe → **1,92 To utiles**", bays="8 SFF · MR408i-o",
             net="2×10 GbE + 4×1 GbE", hyp="Proxmox VE · iLO 6",
             war="3/3/3 — 3 ans sur site", verdict="**Conforme** — cible recommandée",
             pn="P77252-425 + 2×32 Go", sup="PC21.fr + options", price="≈ **9 100 €** · estimé",
             link="[hpe.com — DL325 Gen11](https://www.hpe.com/us/en/compute/hpe-proliant-compute/dl325-gen11.html)",
             lvl={"cores": "g", "ram": "g", "utile": "g", "war": "g", "verdict": "g"}),
        dict(model="**DL380 Gen11** — 2U", proto="2U / 2 sockets (1 peuplé)",
             cpu="Intel Xeon **Silver 4514Y** — Emerald Rapids (2023)",
             cores="**16** cœurs · 2,0 → 3,5 GHz", ram="**128 Go** DDR5 5600 · 32 slots, 8 To max",
             disks="8 baies SFF — disques en option", bays="8 SFF · MR408i-o",
             net="OCP 3.0 + emplacements PCIe", hyp="Proxmox VE · iLO 6",
             war="3/3/3 — 3 ans sur site", verdict="**Conforme** — capacité et extension",
             pn="P77242-425", sup="PC21.fr", price="**16 861 €** · relevé",
             link="[hpe.com — DL380 Gen11](https://www.hpe.com/us/en/products/compute/proliant/dl380-gen11.html)",
             lvl={"cores": "y", "ram": "g", "utile": "y", "war": "g", "verdict": "g"}),
    ],
    recond="DL380 Gen10 — 2×Xeon Gold 6138 (40 cœurs) · 128 Go DDR4 · ≈ **1 700 €** · "
           "OPP! Shop — [voir la fiche](https://oppshop.fr/produit/hp/hpe-dl380-gen10)",
    note=("Note de lecture — HPE",
          "Le 1U AMD est **deux fois moins cher** que le 2U Intel pour des performances "
          "supérieures : 5 726 € en 64 Go contre 16 861 € en 128 Go. L'écart ne mesure pas la "
          "qualité du produit, mais le prix du passage à deux sockets et d'un processeur à 2,0 GHz."),
)

DELL = dict(
    nom="Dell PowerEdge",
    intro="Dell impose iDRAC 9 et un écosystème très large, mais son tarif constructeur est "
          "structurellement élevé. **Point de lecture :** les trois colonnes portent le même "
          "modèle — c'est le canal d'achat qui fait le prix. La colonne C est un relevé Dell.fr "
          "en direct ; à configuration voisine, un revendeur divise la facture par deux.",
    configs=[
        dict(model="**PowerEdge R6615** — 1U", proto="1U / 1 socket",
             cpu="AMD EPYC **9124** — Zen 4 (EPYC 9004, 2023)",
             cores="**16** cœurs · 3,0 → 3,7 GHz", ram="**64 Go** DDR5 · 12 slots, 3 To max",
             disks="2×960 Go SATA → **0,96 To utiles**", bays="10 SFF · PERC H755",
             net="2×1 GbE + OCP 3.0 (10 GbE option)", hyp="Proxmox VE · iDRAC 9",
             war="3 ans Basic NBD", verdict="**Limite** : mémoire juste",
             pn="PER661504A", sup="Revendeur (Senetic)", price="≈ **9 800 €** · estimé",
             link="[dell.com — PowerEdge R6615](https://www.dell.com/fr-fr/shop/ipovw/poweredge-r6615)",
             lvl={"cores": "g", "ram": "o", "utile": "y", "war": "g", "verdict": "y"}),
        dict(model="**PowerEdge R6615** — 1U", proto="1U / 1 socket",
             cpu="AMD EPYC **9124** — Zen 4 (EPYC 9004, 2023)",
             cores="**16** cœurs · 3,0 → 3,7 GHz", ram="**128 Go** DDR5 · 12 slots, 3 To max",
             disks="2×1,92 To → **1,92 To utiles**", bays="10 SFF · PERC H755",
             net="2×1 GbE + OCP 3.0 (10 GbE option)", hyp="Proxmox VE · iDRAC 9",
             war="3 ans Basic NBD", verdict="**Conforme** — mais 10 GbE en option",
             pn="PER661504A + extension", sup="Revendeur (Senetic)", price="≈ **11 900 €** · estimé",
             link="[dell.com — PowerEdge R6615](https://www.dell.com/fr-fr/shop/ipovw/poweredge-r6615)",
             lvl={"cores": "g", "ram": "g", "utile": "g", "war": "g", "verdict": "g"}),
        dict(model="**PowerEdge R6615** — 1U", proto="1U / 1 socket",
             cpu="AMD EPYC **9354P** — Zen 4, 32 cœurs",
             cores="**32** cœurs · 3,25 → 3,8 GHz", ram="**128 Go** DDR5",
             disks="2×1,92 To → **1,92 To utiles**", bays="10 SFF · PERC H755",
             net="2×1 GbE + OCP 3.0", hyp="Proxmox VE · iDRAC 9",
             war="3 ans Basic NBD", verdict="**Conforme** — surdimensionné en calcul",
             pn="PER661501A (Smart Selection)", sup="**Dell.fr — en direct**",
             price="**16 411 €** · relevé",
             link="[dell.com — PowerEdge R6615](https://www.dell.com/fr-fr/shop/ipovw/poweredge-r6615)",
             lvl={"cores": "g", "ram": "g", "utile": "g", "war": "g", "verdict": "g"}),
    ],
    recond="PowerEdge R7515 / R6515 — 128 Go DDR4 · ≈ **1 900 €** · DIB ou Cycle IT — "
           "[catalogue DIB](https://www.dib-reconditionne.fr/serveurs-hp/)",
    note=("Note de lecture — Dell",
          "Les trois colonnes portent le même modèle : c'est le **canal d'achat** qui fait le "
          "prix. La colonne 3 (16 411 € relevé chez Dell) correspond à du direct constructeur ; "
          "à configuration comparable, un revendeur divise la facture par deux."),
)

LENOVO = dict(
    nom="Lenovo ThinkSystem",
    intro="Lenovo est le plus agressif sur le prix d'entrée : 4 947 € HT relevés pour un "
          "SR645 V3 en EPYC 9124, avec 24 emplacements mémoire DDR5. **Point de lecture :** la "
          "configuration relevée n'a que 32 Go — le prix affiché n'est pas le prix du besoin. "
          "En 128 Go, Lenovo et HPE se tiennent à moins de 1 000 €.",
    configs=[
        dict(model="**ThinkSystem SR645 V3** — 1U", proto="1U / 1-2 sockets",
             cpu="AMD EPYC **9124** — Zen 4 (EPYC 9004, 2023)",
             cores="**16** cœurs · 3,0 → 3,7 GHz", ram="**64 Go** DDR5 4800 · 24 slots, 6 To max",
             disks="2×480 Go → **0,96 To utiles**", bays="8 × 2,5\" · 9350-8i",
             net="OCP 3.0 + emplacements PCIe", hyp="Proxmox VE · XClarity",
             war="3 ans 9×5 NBD", verdict="**Limite** : mémoire juste",
             pn="7D9CA014EA", sup="Revendeur (Redcorp)", price="**4 947 €** (32 Go) → ≈ 5 400 € (64 Go)",
             link="[lenovopress — SR645 V3](https://lenovopress.lenovo.com/ds0147.pdf)",
             lvl={"cores": "g", "ram": "o", "utile": "y", "war": "g", "verdict": "y"}),
        dict(model="**ThinkSystem SR645 V3** — 1U", proto="1U / 1-2 sockets",
             cpu="AMD EPYC **9124** — Zen 4 (EPYC 9004, 2023)",
             cores="**16** cœurs · 3,0 → 3,7 GHz", ram="**128 Go** DDR5 4800 · 24 slots, 6 To max",
             disks="2×1,92 To → **1,92 To utiles**", bays="8 × 2,5\" · 9350-8i",
             net="OCP 3.0 + emplacements PCIe", hyp="Proxmox VE · XClarity",
             war="3 ans 9×5 NBD", verdict="**Conforme** — le meilleur prix",
             pn="7D9CA014EA + extension", sup="Revendeur (Redcorp)", price="≈ **8 200 €** · estimé",
             link="[lenovopress — SR645 V3](https://lenovopress.lenovo.com/ds0147.pdf)",
             lvl={"cores": "g", "ram": "g", "utile": "g", "war": "g", "verdict": "g"}),
        dict(model="**ThinkSystem SR645 V3** — 1U", proto="1U / 1-2 sockets",
             cpu="AMD EPYC **9354P** — Zen 4, 32 cœurs",
             cores="**32** cœurs · 3,25 → 3,8 GHz", ram="**128 Go** DDR5 4800",
             disks="2×1,92 To → **1,92 To utiles**", bays="12 × 2,5\" · 9350-8i",
             net="OCP 3.0 + emplacements PCIe", hyp="Proxmox VE · XClarity",
             war="3 ans 9×5 NBD", verdict="**Conforme** — marge de calcul",
             pn="7D9C (CTO)", sup="Revendeur", price="≈ **12 300 €** · estimé",
             link="[lenovopress — SR645 V3](https://lenovopress.lenovo.com/ds0147.pdf)",
             lvl={"cores": "g", "ram": "g", "utile": "g", "war": "g", "verdict": "g"}),
    ],
    recond="ThinkSystem SR645 V2 — 128 Go DDR4 · ≈ **1 900 €** · marché reconditionné européen — "
           "[catalogue DIB](https://www.dib-reconditionne.fr/serveurs-hp/)",
    note=("Note de lecture — Lenovo",
          "Le ticket d'entrée le plus bas du panel (4 947 € relevé), mais la configuration relevée "
          "n'a que 32 Go : **le prix affiché n'est pas le prix du besoin**. En 128 Go, Lenovo et "
          "HPE se tiennent à moins de 1 000 €."),
)

SUPERMICRO = dict(
    nom="Supermicro",
    intro="Supermicro casse les prix : le 1U AS-1115CS-TNR est relevé à 2 040 € HT. **Point de "
          "lecture :** c'est un barebone, pas un serveur. CPU, mémoire et disques ajoutés, le prix "
          "rejoint HPE ou Lenovo — sans la couverture de garantie constructeur.",
    configs=[
        dict(model="**AS-1115CS-TNR** — 1U", proto="1U / 1 socket",
             cpu="AMD EPYC **9124** — Zen 4 (EPYC 9004, 2023)",
             cores="**16** cœurs · 3,0 → 3,7 GHz", ram="**64 Go** DDR5 4800 · 12 slots, 3 To max",
             disks="2×480 Go → **0,96 To utiles**", bays="10 × 2,5\" NVMe/SAS/SATA · RAID logiciel",
             net="2× AIOM (OCP 3.0) + 2× PCIe 5.0", hyp="Proxmox VE · IPMI dédié",
             war="1 à 3 ans — selon revendeur", verdict="**Limite** : mémoire juste",
             pn="AS-1115CS-TNR", sup="Senetic (barebone 2 040 €)", price="≈ **6 300 €** · configuré",
             link="[supermicro.com — AS-1115CS-TNR](https://www.supermicro.com/en/products/system/datasheet/AS-1115CS-TNR)",
             lvl={"cores": "g", "ram": "o", "utile": "y", "war": "y", "verdict": "y"}),
        dict(model="**AS-1115CS-TNR** — 1U", proto="1U / 1 socket",
             cpu="AMD EPYC **9124** — Zen 4 (EPYC 9004, 2023)",
             cores="**16** cœurs · 3,0 → 3,7 GHz", ram="**128 Go** DDR5 4800 · 12 slots, 3 To max",
             disks="2×1,92 To NVMe → **1,92 To utiles**", bays="10 × 2,5\" NVMe/SAS/SATA",
             net="2× AIOM (OCP 3.0) + 2× PCIe 5.0", hyp="Proxmox VE · IPMI dédié",
             war="1 à 3 ans — selon revendeur", verdict="**Conforme** — prix le plus bas",
             pn="AS-1115CS-TNR (config.)", sup="Senetic / intégrateur", price="≈ **8 400 €** · estimé",
             link="[supermicro.com — AS-1115CS-TNR](https://www.supermicro.com/en/products/system/datasheet/AS-1115CS-TNR)",
             lvl={"cores": "g", "ram": "g", "utile": "g", "war": "y", "verdict": "g"}),
        dict(model="**AS-2015CS-TNR** — 2U", proto="2U / 1 socket",
             cpu="AMD EPYC **9124** — Zen 4, 16 cœurs",
             cores="**16** cœurs · 3,0 → 3,7 GHz", ram="**128 Go** DDR5 4800",
             disks="4×1,92 To → 3,84 To possibles", bays="12 × 3,5\" NVMe/SAS/SATA",
             net="2× AIOM + 4× PCIe 5.0", hyp="Proxmox VE · IPMI dédié",
             war="1 à 3 ans — selon revendeur", verdict="**Conforme** — capacité disques",
             pn="AS-2015CS-TNR (config.)", sup="Senetic / intégrateur", price="≈ **9 100 €** · estimé",
             link="[supermicro.com — AS-2015CS-TNR](https://www.supermicro.com/en/products/system/datasheet/as-2015cs-tnr)",
             lvl={"cores": "g", "ram": "g", "utile": "g", "war": "y", "verdict": "g"}),
    ],
    recond="**Aucune offre structurée** : le reconditionné Supermicro se trouve au cas par cas, "
           "sans garantie homogène. À écarter comme source principale.",
    note=("Note de lecture — Supermicro",
          "Le barebone à 2 040 € HT n'est pas un serveur : c'est un châssis. Une fois le CPU, la "
          "mémoire et les disques ajoutés, le prix rejoint celui de HPE ou de Lenovo — sans la "
          "couverture de garantie constructeur."),
)

ASUS = dict(
    nom="ASUS",
    intro="ASUS complète le panel avec des plateformes AMD monocpu bien dotées en baies et en "
          "PCIe. **Point de lecture :** le 1U RS500A-E12 est annoncé **en fin de vie** sur le site "
          "du constructeur — un point de pérennité qui pèse lourd sur un achat à 5 ans.",
    configs=[
        dict(model="**RS500A-E12-RS12U** — 1U", proto="1U / 1 socket",
             cpu="AMD EPYC **9124** — Zen 4 (EPYC 9004, 2023)",
             cores="**16** cœurs · 3,0 → 3,7 GHz", ram="**64 Go** DDR5 4800 · 24 slots, 6 To max",
             disks="2×480 Go → **0,96 To utiles**", bays="12 × 2,5\" NVMe · RAID logiciel",
             net="2×1 GbE + OCP 3.0", hyp="Proxmox VE · ASMB11-iKVM",
             war="3 ans (revendeur)", verdict="**Limite** : mémoire + modèle EOL",
             pn="RS500A-E12-RS12U", sup="Intégrateur / import", price="≈ **6 400 €** · estimé",
             link="[servers.asus.com — RS500A-E12](https://servers.asus.com/products/servers/rack-servers/RS500A-E12-RS12U)",
             lvl={"cores": "g", "ram": "o", "utile": "y", "war": "y", "verdict": "o"}),
        dict(model="**RS500A-E12-RS12U** — 1U", proto="1U / 1 socket",
             cpu="AMD EPYC **9124** — Zen 4 (EPYC 9004, 2023)",
             cores="**16** cœurs · 3,0 → 3,7 GHz", ram="**128 Go** DDR5 4800 · 24 slots, 6 To max",
             disks="2×1,92 To NVMe → **1,92 To utiles**", bays="12 × 2,5\" NVMe",
             net="2×1 GbE + OCP 3.0", hyp="Proxmox VE · ASMB11-iKVM",
             war="3 ans (revendeur)", verdict="**Limite** : conforme techniquement, mais EOL",
             pn="RS500A-E12-RS12U", sup="Intégrateur / import", price="≈ **8 500 €** · estimé",
             link="[servers.asus.com — RS500A-E12](https://servers.asus.com/products/servers/rack-servers/RS500A-E12-RS12U)",
             lvl={"cores": "g", "ram": "g", "utile": "g", "war": "y", "verdict": "y"}),
        dict(model="**RS520A-E12-RS12U** — 2U", proto="2U / 1 socket",
             cpu="AMD EPYC **9124** — Zen 4, 16 cœurs",
             cores="**16** cœurs · 3,0 → 3,7 GHz", ram="**128 Go** DDR5 4800 · 24 slots",
             disks="4×1,92 To → 3,84 To possibles", bays="12 × 3,5\" NVMe/SATA/SAS",
             net="2×1 GbE + OCP 3.0 + PCIe 5.0", hyp="Proxmox VE · ASMB11-iKVM",
             war="3 ans (revendeur)", verdict="**Conforme** — modèle en cours",
             pn="RS520A-E12-RS12U", sup="Intégrateur / import", price="≈ **9 300 €** · estimé",
             link="[servers.asus.com — RS520A-E12](https://servers.asus.com/products/servers/rack-servers/RS520A-E12-RS12U)",
             lvl={"cores": "g", "ram": "g", "utile": "g", "war": "y", "verdict": "g"}),
    ],
    recond="**Aucune offre structurée** sur ce constructeur : le reconditionné ASUS serveur est "
           "marginal en Europe.",
    note=("Note de lecture — ASUS",
          "Le 1U est **annoncé EOL** par le constructeur : acheter neuf un produit en fin de vie "
          "n'a de sens que si la remise le compense. Le 2U RS520A, lui, est en cours de cycle — "
          "c'est la seule colonne ASUS défendable sur 5 ans."),
)

# --------------------------------------------------------------------------- #
doc.cover(
    eyebrow="Proposition D — comparative par constructeur",
    title="Cinq constructeurs,\ncinq lectures du même besoin",
    subtitle="Un tableau par constructeur, trois configurations par tableau, toutes confrontées "
             "ligne à ligne aux caractéristiques de l'hyperviseur actuel.",
    meta_rows=[
        ["Pour", "**Jad — Direction Générale**"],
        ["Objet", "Comparer les configurations serveur proposées par cinq constructeurs, "
                  "à exigences techniques identiques"],
        ["Référence de comparaison", "La fiche d'identité de l'hyperviseur actuel "
                                     "(64 Go, 8 cœurs, ≈ 960 Go, RAM à 88 %)"],
        ["Constructeurs", "HPE · Dell · Lenovo · Supermicro · ASUS"],
        ["Exigences minimales", "**128 Go de RAM** · **2 To utiles** · **12 cœurs minimum** · "
                                "rackable 1U à 3U · garantie 3 ans"],
        ["Statut des prix", "Mélange de prix **relevés** (sourcés) et d'**estimations** encadrées — "
                            "aucun prix ferme sans devis"],
        ["Date", "5 novembre 2026"],
    ],
    summary=("Comment lire ce document",
             "Chaque tableau reprend **les mêmes lignes** que la fiche de l'existant, puis les "
             "décline pour trois configurations. Les cellules sont colorées : **vert** = conforme "
             "aux exigences, **jaune** = à la limite, **orange** = en dessous. Les liens vers les "
             "fiches constructeur sont cliquables et ont été vérifiés.",
             "info"),
)

# --------------------------------------------------------------------------- #
doc.h1("1", "Méthode, exigences et conventions")

doc.p("Les cinq tableaux qui suivent sont construits sur une trame unique : **la même liste de "
      "lignes**, la même colonne de référence (l'existant), et trois colonnes de configuration. "
      "La comparaison est donc possible ligne à ligne, d'un constructeur à l'autre.", lead=True)

doc.h2("Exigences minimales retenues")
doc.table(
    ["Critère", "Seuil vert (conforme)", "Seuil jaune (limite)", "Orange (hors exigence)", "Origine de la contrainte"],
    [
        ["Mémoire vive", "**≥ 128 Go**", "96 Go", "**≤ 64 Go**", "88,4 % de RAM occupée sur 64 Go aujourd'hui"],
        ["Stockage utile", "**≥ 1,92 To**", "0,96 To", "< 0,96 To", "89,9 % de disque occupé sur ≈ 960 Go"],
        ["Processeur", "**≥ 16 cœurs à ≥ 3,0 GHz**", "12–16 cœurs ou 2,0–2,9 GHz", "**< 12 cœurs**", "Marge pour 5 ans, malgré 15 % de charge"],
        ["Génération CPU", "**EPYC 9004/9005, Xeon 4e/5e gén.**", "Génération précédente", "**Gen10 et antérieurs**", "Horizon de support et pièces"],
        ["Format", "**1U à 3U rackable**", "—", "Tour ou lame propriétaire", "Salle serveur existante"],
        ["Garantie", "**3 ans sur site**", "1 à 2 ans / revendeur", "Aucune", "Site isolé : l'intervention compte plus que la pièce"],
    ],
    widths=[2.5, 3.4, 3.4, 3.4, 4.4], font=7.9,
    caption="Tableau 1 — Seuils appliqués à chaque cellule des cinq tableaux comparatifs.",
    first_col_bold=True)

doc.h2("Conventions de couleur et de typographie")
doc.table(
    ["Code", "Signification", "Traitement appliqué à la cellule"],
    [
        ["**A**", "Conforme ou supérieur à l'exigence", "Fond vert clair · **texte vert foncé en gras**"],
        ["**B**", "À la limite : acceptable avec réserve", "Fond jaune clair · **texte ocre en gras**"],
        ["**C**", "En dessous de l'exigence : à écarter", "Fond orange clair · **texte orange foncé en gras**"],
        ["**—**", "Information non communiquée ou sans objet", "Fond neutre · texte gris ou italique"],
    ],
    widths=[1.4, 6.2, 9.5], font=8.2, aligns=["c", "l", "l"],
    caption="Tableau 2 — Légende. Les lignes sont également hiérarchisées : le libellé du critère est "
            "en gras, la valeur en caractères normaux, la mention de statut en gras.",
    cell_fmt={(0, 0): F(VERT_BG, VERT_TX, True), (1, 0): F(JAUN_BG, JAUN_TX, True),
              (2, 0): F(ORAN_BG, ORAN_TX, True)})

doc.h2("Trois règles de lecture")
doc.ul([
    "**Un prix bas n'est pas une configuration.** Le SR645 V3 relevé à 4 947 € HT est livré avec "
    "32 Go : la colonne indique systématiquement la configuration réellement comparée.",
    "**Le canal d'achat pèse autant que le constructeur.** Pour Dell, l'écart entre le direct et "
    "le revendeur atteint le double ; la ligne « fournisseur » est donc aussi importante que la "
    "ligne « tarif ».",
    "**Les estimations sont signalées.** Un prix marqué « estimé » est construit par analogie "
    "(socle relevé + options au prix du marché). Seuls les prix marqués « relevé » sont sourcés.",
])

# --------------------------------------------------------------------------- #
def table_constructeur(v, num, titre):
    doc.landscape(True)
    doc.h1(str(num), titre)
    doc.p(v["intro"], small=True)
    rows, cfmt = [], {}
    for i, (rub, elem) in enumerate(LIGNES):
        row = [f"**{rub}**" if rub else "", elem, REF[i]]
        for k, c in enumerate(v["configs"]):
            if i == 0:
                row.append(c["proto"])
            elif i == 1:
                row.append(c["model"])
            elif i == 2:
                row.append(c["cpu"])
            elif i == 3:
                row.append(c["cores"])
            elif i == 4:
                row.append(c["ram"])
            elif i == 5:
                row.append(c["disks"])
            elif i == 6:
                row.append(c["bays"])
            elif i == 7:
                row.append(c["net"])
            elif i == 8:
                row.append(c["hyp"])
            elif i == 9:
                row.append(c["war"])
            elif i == 10:
                row.append(c["verdict"])
            elif i == 11:
                row.append(c["pn"])
            elif i == 12:
                row.append(c["sup"])
            elif i == 13:
                row.append(c["price"])
            elif i == 14:
                row.append(c["link"])
            else:
                row.append(v["recond"] if k == 0 else "—")
        rows.append(row)

        # couleurs : niveau par config
        keymap = {3: "cores", 4: "ram", 5: "utile", 9: "war", 10: "verdict"}
        for k, c in enumerate(v["configs"]):
            lvl = c["lvl"].get(keymap.get(i)) if i in keymap else None
            if lvl:
                cfmt[(i, 3 + k)] = FMT[lvl]
        if i in REF_LVL:
            cfmt[(i, 2)] = FMT[REF_LVL[i]]
        if i == 15:
            cfmt[(i, 3)] = F(JAUN_BG, JAUN_TX, False, True)

    doc.table(
        ["Rubrique", "Élément", "**Existant — référence**",
         "**Config. A**", "**Config. B**", "**Config. C**"],
        rows,
        widths=[2.45, 3.0, 3.65, 5.6, 5.6, 5.6], font=7.1, zebra=False,
        caption=f"Tableau {num + 1} — {v['nom']} : trois configurations confrontées à l'existant "
                f"(prix HT, hors transport et douane ; « relevé » = prix public sourcé, "
                f"« estimé » = construit par analogie).",
        cell_fmt=cfmt)


table_constructeur(HPE, 2, "HPE ProLiant — trois configurations")
table_constructeur(DELL, 3, "Dell PowerEdge — trois configurations")
table_constructeur(LENOVO, 4, "Lenovo ThinkSystem — trois configurations")
table_constructeur(SUPERMICRO, 5, "Supermicro — trois configurations")
table_constructeur(ASUS, 6, "ASUS — trois configurations")

# --------------------------------------------------------------------------- #
doc.landscape(False)
doc.h1("7", "Synthèse : les quinze configurations en une page")

doc.p("Les quinze configurations des cinq tableaux, ramenées à trois indicateurs comparables : "
      "le prix d'acquisition, le prix au gigaoctet de mémoire et le respect des exigences.")

synth = []
for v in (HPE, DELL, LENOVO, SUPERMICRO, ASUS):
    for k, c in enumerate(v["configs"]):
        prix = {"HPE": [5726, 9100, 16861], "Dell": [9800, 11900, 16411],
                "Lenovo": [5400, 8200, 12300], "Supermicro": [6300, 8400, 9100],
                "ASUS": [6400, 8500, 9300]}[v["nom"].split()[0]][k]
        ram = [64, 128, 128][k]
        p = f"{prix:,}".replace(",", " ")
        synth.append([v["nom"].split()[0], c["model"].replace("**", ""),
                      f"{ram} Go", c["cores"].split("·")[0].replace("**", "").strip(),
                      c["verdict"].replace("**", ""), p + " €", f"{prix // ram} €",
                      c["lvl"]["verdict"].upper()])

lvl_txt = {"G": "Conforme", "Y": "Limite", "O": "Hors exigence"}
rows, cf = [], {}
for i, r in enumerate(synth):
    rows.append([r[0], r[1], r[2], r[3], r[4], r[5], r[6], lvl_txt.get(r[7], r[7])])
    cf[(i, 7)] = FMT[r[7].lower()]

doc.table(
    ["Constructeur", "Modèle", "RAM", "Cœurs", "Verdict", "Prix HT", "€/Go", "Statut"],
    rows,
    widths=[2.45, 3.35, 1.2, 1.9, 3.35, 1.7, 1.1, 2.3], font=7.6,
    aligns=["l", "l", "c", "c", "l", "r", "r", "c"],
    caption="Tableau 8 — Les quinze configurations classées par constructeur (prix HT équipés).",
    cell_fmt=cf, zebra=False)

doc.image("fig_d_prix.png", "Figure 1 — Le même besoin, trois niveaux de prix : l'écart entre le neuf en 64 Go, le neuf en 128 Go et le reconditionné est plus large que l'écart entre constructeurs.")

doc.h2("Ce que la comparaison établit")
doc.ul([
    "**Le reconditionné divise la facture par cinq** (1 700 à 1 900 € contre 8 200 à 11 900 € en "
    "neuf 128 Go), au prix d'un horizon de 2 à 3 ans et d'une garantie revendeur.",
    "**Le passage de 64 à 128 Go de RAM coûte 2 400 à 3 400 €** selon le constructeur — c'est le "
    "seul arbitrage qui compte, puisque c'est la ressource saturée.",
    "**HPE, Lenovo et Supermicro se tiennent dans un mouchoir** en 128 Go (8 200 à 8 500 €). "
    "Dell est 40 % plus cher, mais son relevé vient du canal direct, non du revendeur.",
    "**Le 2U ne se justifie pas** pour ce besoin : il coûte 1 000 à 8 000 € de plus pour des baies "
    "et une extensibilité dont l'existant n'a pas l'usage.",
    "**ASUS doit être écarté** sur le 1U : le modèle est annoncé en fin de vie par le constructeur.",
])

doc.callout("Recommandation finale",
            "**HPE DL325 Gen11 en 128 Go** (colonne B du tableau 2) : ≈ 9 100 € HT, 16 cœurs, "
            "2 To utiles, iLO 6, garantie 3/3/3. C'est la seule configuration qui coche toutes les "
            "exigences au meilleur niveau de prix **et** de pérennité. Alternative équivalente : "
            "Lenovo SR645 V3 en 128 Go (≈ 8 200 €), si le réseau de revendeurs le permet.",
            "ok")

# --------------------------------------------------------------------------- #
doc.h1("8", "Annexe — liens vérifiés et sources")

doc.table(
    ["Constructeur", "Fiche produit", "État du lien", "Prix relevés"],
    [
        ["HPE", "[DL325 Gen11](https://www.hpe.com/us/en/compute/hpe-proliant-compute/dl325-gen11.html)",
         "Vérifié le 5/11/2026", "PC21.fr — 5 726 € HT (P77252-425)"],
        ["HPE", "[DL380 Gen11](https://www.hpe.com/us/en/products/compute/proliant/dl380-gen11.html)",
         "Vérifié le 5/11/2026", "PC21.fr — 16 861 € HT (P77242-425)"],
        ["Dell", "[PowerEdge R6615](https://www.dell.com/fr-fr/shop/ipovw/poweredge-r6615)",
         "Vérifié le 5/11/2026", "Dell.fr direct — 16 411 € HT (config. 9354 / 64 Go)"],
        ["Lenovo", "[ThinkSystem SR645 V3](https://lenovopress.lenovo.com/ds0147.pdf)",
         "Vérifié le 5/11/2026", "Redcorp — 4 947 € HT (7D9CA014EA, 32 Go)"],
        ["Supermicro", "[AS-1115CS-TNR](https://www.supermicro.com/en/products/system/datasheet/AS-1115CS-TNR)",
         "Vérifié le 5/11/2026", "Senetic — 2 040 € HT (barebone)"],
        ["Supermicro", "[AS-2015CS-TNR](https://www.supermicro.com/en/products/system/datasheet/as-2015cs-tnr)",
         "Vérifié le 5/11/2026", "Estimation configurée"],
        ["ASUS", "[RS500A-E12-RS12U](https://servers.asus.com/products/servers/rack-servers/RS500A-E12-RS12U)",
         "Vérifié — **mention EOL** sur la fiche", "Estimation (barebone ≈ 2 150 €)"],
        ["ASUS", "[RS520A-E12-RS12U](https://servers.asus.com/products/servers/rack-servers/RS520A-E12-RS12U)",
         "Vérifié le 5/11/2026", "Estimation configurée"],
    ],
    widths=[2.4, 7.4, 3.6, 3.7], font=7.8,
    caption="Tableau 9 — Liens constructeur consultés le 5 novembre 2026 et source de chaque prix.")

doc.h2("Trois devis à demander, sur une nomenclature identique")
doc.table(
    ["À demander", "Pourquoi", "Effet attendu"],
    [
        ["Le même modèle en **64 Go et en 128 Go**", "Isoler le coût réel de la mémoire, seule ressource saturée",
         "Chiffrer l'arbitrage à 2 400–3 400 €"],
        ["La **référence exacte du processeur** et son TDP", "Un 12 cœurs à 2,0 GHz et un 16 cœurs à 3,0 GHz ne se comparent pas",
         "Éviter les offres « au choix »"],
        ["La **garantie 3 ans sur site** et son prix séparé", "C'est la ligne la plus souvent diluée dans le prix total",
         "Comparer à périmètre de couverture égal"],
        ["Un **disque de rechange** identique", "Le meilleur rapport sécurité/prix du projet",
         "500 à 700 € de plus, pas 5 000 €"],
        ["Le **fret et les droits de douane** rendus Libreville", "20 % du matériel, systématiquement absents des devis européens",
         "Éviter un dépassement budgétaire"],
    ],
    widths=[4.4, 6.6, 6.1], font=7.9,
    caption="Tableau 10 — Ce que chaque devis doit contenir pour être comparable.",
    first_col_bold=False)

doc.p("**Avertissement.** Les liens ont été ouverts et contrôlés à la date indiquée ; un "
      "constructeur peut modifier ou retirer une page produit à tout moment. Les prix marqués "
      "« relevé » proviennent de pages publiques de distributeurs français consultées le "
      "5 novembre 2026 et ne constituent pas des offres fermes. Les prix marqués « estimé » sont "
      "construits par analogie et doivent être remplacés par un devis avant tout engagement. "
      "Aucune commande ne devrait être passée sans une nomenclature détaillée, une garantie "
      "précisée et un chiffrage du transport et des droits de douane.", small=True)

doc.save(OUT)
print("saved", OUT)
