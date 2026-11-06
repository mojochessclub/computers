# -*- coding: utf-8 -*-
"""Étude GED-SERVICES — six processeurs relevés, face-à-face AMD / Intel,
caractéristiques complétées, quinze fournisseurs classés, prix par modèle.
Rédaction impersonnelle, sans référence à un document antérieur."""
import os
from urllib.parse import quote
from render import Doc

BASE = "G_Six_processeurs_face_a_face_AMD_Intel_et_prix_par_modele"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables")

doc = Doc(
    base=BASE,
    title="Six processeurs, huit machines",
    subtitle="Face-à-face AMD / Intel, caractéristiques complétées, quinze fournisseurs classés",
    meta=[],
    doc_ref="GED-RAP-2026-07 · Confidentiel — usage interne",
    footer="Étude GED-SERVICES · six processeurs, huit machines",
)

# --------------------------------------------------------------------------- #
VERT_BG, VERT_TX = "E3F0DC", "1E6B2F"
JAUN_BG, JAUN_TX = "FBF3D0", "8A6D00"
ORAN_BG, ORAN_TX = "FBE0CE", "B4500F"
BLEU_BG = "EAF0F7"
GRIS_BG = "F1F1F1"


def F(bg=None, tx=None, b=False, i=False):
    return {"bg": bg, "color": tx, "b": b, "i": i}


FMT = {"g": F(VERT_BG, VERT_TX, True), "y": F(JAUN_BG, JAUN_TX, True),
       "o": F(ORAN_BG, ORAN_TX, True), "x": F(), "n": F(GRIS_BG, "444444")}

_NT = [0]


def tab():
    _NT[0] += 1
    return f"Tableau {_NT[0]}"


def eur(n):
    return f"{round(n):,}".replace(",", " ") + " €"


def dec(x, n=1):
    return f"{x:.{n}f}".replace(".", ",")


# --------------------------------------------------------------------------- #
# 1. Les quinze fournisseurs, coefficient croissant
#    (nom, zone, coef, domaine, mode de lien, libellé du lien)
FOURN = [
    ("Alibaba.com", "Chine", 0.85, "alibaba.com", "search", "recherche"),
    ("Mindware", "Émirats / Dubaï", 1.00, "mindware.net", "google", "Google"),
    ("PC21.fr", "France", 1.00, "pc21.fr", "google", "Google"),
    ("Arena Bilgisayar", "Turquie", 1.02, "arena.com.tr", "google", "Google"),
    ("Senetic", "France / UE", 1.02, "senetic.fr", "search", "recherche"),
    ("Redcorp", "Belgique / UE", 1.04, "redcorp.com", "google", "Google"),
    ("MonParcInformatique", "France", 1.05, "monparcinformatique.fr", "google", "Google"),
    ("CDW", "États-Unis", 1.08, "cdw.com", "search", "recherche"),
    ("Mustek", "Afrique du Sud", 1.10, "mustek.co.za", "google", "Google"),
    ("Bechtle", "Allemagne / UE", 1.12, "bechtle.com", "google", "Google"),
    ("Insight", "UE / États-Unis", 1.15, "fr.insight.com", "search", "recherche"),
    ("LDLC Pro", "France", 1.18, "ldlc.pro", "search", "recherche"),
    ("Inmac wstore", "France", 1.22, "inmac-wstore.com", "search", "recherche"),
    ("GED-SERVICES", "Gabon / Libreville", 1.25, "gedservices.pro", "mail", "e-mail"),
    ("ServerMall", "France", 1.60, "servermall.com", "google", "Google"),
]

GABARIT = {
    "search": "https://{dom}/search/?text={q}",
    "google": "https://www.google.com/search?q=site%3A{dom}+{q}",
}
# endpoints de recherche natifs, ouverts et testés un par un
SPECIFIQUE = {
    "CDW": "https://www.cdw.com/search/?key={q}",
    "Insight": "https://fr.insight.com/fr_FR/search.html?q={q}",
    "LDLC Pro": "https://www.ldlc.pro/recherche/?q={q}",
    "Inmac wstore": "https://www.inmac-wstore.com/recherche/recherche.aspx?q={q}",
    "Alibaba.com": "https://www.alibaba.com/trade/search?SearchText={q}",
    "GED-SERVICES": "mailto:joel.mbaoyone@gedservices.pro?subject=Demande%20de%20prix%20{qs}",
}
FICHE_PRODUIT = {
    ("M1", "PC21.fr"): ("https://www.pc21.fr/fiche/p77252-425-hpe-proliant-dl325-gen11-9124-3-0ghz-"
                        "16c-64gb-r-8sff-mr408i-o-i5675189.html", "fiche P77252-425"),
    ("M1", "ServerMall"): ("https://servermall.com/sets/hpe-proliant-dl325-gen11-server/",
                           "configurateur DL325"),
}


def lien(nom, dom, mode, q):
    if nom == "GED-SERVICES":
        return SPECIFIQUE[nom].format(qs=quote(q))
    if nom in SPECIFIQUE:
        return SPECIFIQUE[nom].format(q=quote(q))
    return GABARIT[mode].format(dom=dom, q=quote(q))


# --------------------------------------------------------------------------- #
# 2. Les six processeurs du relevé, caractéristiques complétées
#    (code, modèle, architecture, socket, cœurs, threads, base, turbo, L3,
#     mémoire, pcie, tdp, sortie, fin, prix, statut)
CPU = [
    ("Intel", "Xeon Silver 4510", "Emerald Rapids", "LGA 4677", 12, 24, 2.40, 4.10, "30 Mo",
     "8 canaux · DDR5-4400 · 4 To", "80 voies · PCIe 5.0", 150, "2023", "≈ 2027", 1050, "g"),
    ("Intel", "Xeon Silver 4410Y", "Emerald Rapids", "LGA 4677", 12, 24, 2.00, 3.90, "30 Mo",
     "8 canaux · DDR5-4000 · 4 To", "80 voies · PCIe 5.0", 150, "2023", "≈ 2027", 900, "y"),
    ("Intel", "Xeon Gold 6426Y", "Sapphire Rapids", "LGA 4677", 16, 32, 2.50, 4.10, "37,5 Mo",
     "8 canaux · DDR5-4800 · 4 To", "80 voies · PCIe 5.0", 185, "2023", "≈ 2027", 2400, "g"),
    ("AMD", "EPYC 9124", "Zen 4 — 9004", "SP5", 16, 32, 3.00, 3.70, "64 Mo",
     "12 canaux · DDR5-4800 · 3 To", "128 voies · PCIe 5.0", 200, "2023", "≈ 2027", 1050, "g"),
    ("AMD", "EPYC 9125", "Zen 5 — 9005", "SP5", 16, 32, 2.60, 4.10, "64 Mo",
     "12 canaux · DDR5-6000 · 3 To", "128 voies · PCIe 5.0", 200, "2024", "≈ 2029", 1300, "g"),
    ("AMD", "EPYC 9224", "Zen 4 — 9004", "SP5", 24, 48, 2.50, 3.70, "64 Mo",
     "12 canaux · DDR5-4800 · 3 To", "128 voies · PCIe 5.0", 200, "2023", "≈ 2027", 2360, "g"),
]
EXISTANT = ("Existant", "8 vCPU partagés", "Hébergeur public", "—", 8, 8, None, None, "—",
            "64 Go · 88,4 % utilisés", "—", None, "2021", "en service", 0, "n")

# --------------------------------------------------------------------------- #
# 3. Modèles : huit machines, une configuration cible
MODELES = [
    ("M1", "HPE", "ProLiant DL325 Gen11", "EPYC 9124", "AMD", 3.00, 16, 8600,
     "https://www.hpe.com/fr/fr/products/compute/proliant/dl325-gen11.html",
     "1U · 8 SFF · 12 DIMM · 2×10 GbE OCP"),
    ("M2", "Lenovo", "ThinkSystem SR645 V3", "EPYC 9124", "AMD", 3.00, 16, 8500,
     "https://lenovopress.lenovo.com/ds0147",
     "1U · 10 SFF · 12 DIMM · 2×10 GbE"),
    ("M3", "Dell", "PowerEdge R6615", "EPYC 9124", "AMD", 3.00, 16, 11900,
     "https://www.dell.com/fr-fr/shop/ipovw/poweredge-r6615",
     "1U · 10 SFF · 12 DIMM · 2×10 GbE"),
    ("M4", "Supermicro", "AS-1115CS-TNR", "EPYC 9124", "AMD", 3.00, 16, 8400,
     "https://www.supermicro.com/en/products/system/clouddc/1u/as-1115cs-tnr",
     "1U · 10 baies 2,5 pouces · 12 DIMM · 2×10 GbE"),
    ("M5", "ASUS", "RS520A-E12-RS12U", "EPYC 9124", "AMD", 3.00, 16, 8500,
     "https://servers.asus.com/products/servers/rs520a-e12-rs12u",
     "2U · 12 baies 3,5 pouces · 24 DIMM · 2×10 GbE"),
    ("M6", "HPE", "ProLiant DL380 Gen11", "Xeon Silver 4510", "Intel", 2.40, 12, 14400,
     "https://www.hpe.com/fr/fr/products/compute/proliant/dl380-gen11.html",
     "2U · 8 SFF · 32 DIMM · 2×10 GbE"),
    ("M7", "Lenovo", "ThinkSystem SR650 V3", "Xeon Silver 4510", "Intel", 2.40, 12, 13200,
     "https://lenovopress.lenovo.com/lp1699",
     "2U · 8 SFF · 32 DIMM · 2×10 GbE"),
    ("M8", "Dell", "PowerEdge R660", "Xeon Silver 4510", "Intel", 2.40, 12, 15300,
     "https://www.dell.com/fr-fr/shop/ipovw/poweredge-r660",
     "1U · 10 SFF · 32 DIMM · 2×10 GbE"),
]
ADMISSIBLES = {"AMD": "9124 · 9125 · 9224 — même socket **SP5**, substitution sans changer de machine",
               "Intel": "4510 · 4410Y · 6426Y — même socket **LGA 4677**"}


def bande(p):
    if p <= 9500:
        return "g"
    if p <= 12500:
        return "y"
    return "o"


def bande_ghz(g):
    if g is None:
        return "n"
    if g >= 2.4:
        return "g"
    if g >= 2.0:
        return "y"
    return "o"


# --------------------------------------------------------------------------- #
doc.cover(
    eyebrow="Étude GED-SERVICES — processeurs",
    title="Six processeurs, huit machines :\nle face-à-face AMD / Intel",
    subtitle="Les six processeurs relevés, comparés sur leurs caractéristiques complètes — cœurs, "
             "socket, mémoire, PCIe, prix par cœur, indice — puis confrontés au prix réel des huit "
             "machines qui les reçoivent, chez les quinze fournisseurs consultés.",
    meta_rows=[
        ["Rédaction", "**GED-SERVICES** — étude interne, rédigée de façon impersonnelle : elle "
                      "instruit le dossier, elle ne le commente pas"],
        ["Objet", "Comparer les **six processeurs relevés** (trois Intel Xeon, trois AMD EPYC) sur "
                  "pièces, et établir le prix du serveur qui les reçoit chez chacun des quinze "
                  "fournisseurs"],
        ["Cible rappelée", "**128 Go DDR5** · **2×1,92 To utiles en RAID1** · **12 à 24 cœurs** · "
                           "**2×10 GbE** · rackable · Proxmox VE"],
        ["Seuil processeur", "**Conforme ≥ 2,4 GHz** · **Toléré 2,0 à 2,39 GHz** · **Exclu < 2,0 GHz**"],
        ["Périmètre", "Les **six processeurs du relevé**, et l'**existant** conservé comme référence "
                      "de coût et de charge"],
        ["Structure", "1) le dossier et la méthode · 2) les six processeurs, caractéristiques "
                      "complètes · 3) le seuil appliqué · 4) face-à-face AMD / Intel · 5) quinze "
                      "fournisseurs classés · 6) le serveur équipé, six processeurs × quinze "
                      "fournisseurs · 7) **prix par modèle, huit pages** · 8) synthèse · annexes"],
        ["Date", "6 novembre 2026"],
    ],
    summary=("Comment lire cette étude",
             "Chaque processeur est décrit deux fois : **sur pièces** (tableau 2, une colonne par "
             "processeur, comme sur le relevé d'origine) puis **en machine** (pages de prix du "
             "chapitre 7). Les couleurs suivent une règle unique : pour les fréquences, "
             "**vert ≥ 2,4 GHz, jaune 2,0–2,39 GHz (toléré), orange < 2,0 GHz (exclu)** ; pour les "
             "prix, **vert ≤ 9 500 €, jaune ≤ 12 500 €, orange au-delà**.", "info"),
)

# --------------------------------------------------------------------------- #
doc.h1("1", "Le dossier et la méthode")

doc.p("Le serveur en production sature sur deux ressources mesurées : la mémoire, à **88,4 % de "
      "64 Go**, et le stockage, à **89,9 % d'environ 960 Go utiles**. Le calcul, lui, tourne à "
      "**15 % de huit cœurs** — c'est la seule ressource que le remplacement ne doit pas "
      "sur-dimensionner. La cible est donc écrite depuis les mesures et non depuis un catalogue : "
      "**128 Go de DDR5**, **2×1,92 To utiles en RAID1**, **2×10 GbE**, rackable, virtualisée sous "
      "Proxmox VE.", lead=True)

doc.p("Six processeurs ont été relevés pour couvrir ce besoin : trois Intel Xeon (Silver 4510, "
      "Silver 4410Y, Gold 6426Y) et trois AMD EPYC (9124, 9125, 9224). Ce sont eux, et eux seuls, "
      "que cette étude instruit. Le relevé d'origine donnait pour chacun le nombre de cœurs, la "
      "fréquence de base, le turbo, l'année, l'architecture, l'enveloppe thermique et un tarif "
      "indicatif. Il manquait, pour décider, sept éléments que ce document complète : **le nombre "
      "de threads, le socket, les voies PCIe, la mémoire maximale et le nombre de canaux, le prix "
      "par cœur, l'indice de calcul et l'indice par millier d'euros, enfin la disponibilité et la "
      "fin de commercialisation**.")

doc.p("Trois règles de méthode valent pour tout le document. **Première** : un processeur ne "
      "coûte pas son tarif, il coûte le serveur qui le reçoit — d'où les prix par machine du "
      "chapitre 7. **Deuxième** : à configuration identique, sinon les écarts ne veulent rien dire "
      "— 128 Go DDR5, 2×1,92 To NVMe en RAID1, 2×10 GbE, garantie 3 ans. **Troisième** : toute "
      "ligne de prix porte un statut — *base relevée* quand elle vient d'une page publique "
      "consultée, *modélisée* quand elle applique le coefficient du fournisseur à cette base.")

doc.table(
    ["Ce que le relevé donnait", "Ce que cette étude ajoute", "Pourquoi cela change la lecture"],
    [
        ["Cœurs", "**Threads (SMT)**", "16 cœurs font 32 threads chez AMD comme chez Intel ; "
                                       "la finesse de découpage en machines virtuelles en dépend"],
        ["Fréquence de base, turbo", "**Indice = cœurs × fréquence de base**",
         "Un seul chiffre pour classer six processeurs, et le seul qui reste comparable d'une "
         "architecture à l'autre"],
        ["Tarif indicatif", "**Prix par cœur et indice par millier d'euros**",
         "Le tarif absolu avantage le petit processeur ; le prix par cœur révèle la vraie "
         "hiérarchie"],
        ["Architecture, année", "**Socket et fin de commercialisation**",
         "Un socket partagé entre deux générations, c'est une mise à jour possible sans changer "
         "de machine"],
        ["TDP", "**Voies PCIe et mémoire maximale**",
         "Ce sont les deux plafonds qui décident de la durée de vie de la machine, pas la "
         "fréquence"],
    ],
    widths=[4.6, 5.4, 7.0], font=8.2, aligns=["l", "l", "l"],
    caption=f"{tab()} — Les sept caractéristiques complétées, et ce qu'elles apportent à la "
            "décision.", zebra=True)

doc.callout("Ce que l'étude ne fait pas",
            "Elle ne mesure pas de performance applicative : aucun banc d'essai n'a été exécuté "
            "sur ces six processeurs. L'indice retenu — cœurs × fréquence de base — est un "
            "**indicateur de capacité**, pas une prévision de débit. Il sert à classer, pas à "
            "promettre. Les chiffres de performance réels dépendent de la charge, de la mémoire et "
            "du disque, qui sont traités séparément.", "info")

# --------------------------------------------------------------------------- #
doc.landscape(True)
doc.h1("2", "Les six processeurs, caractéristiques complètes")

doc.p("Le tableau reprend la disposition du relevé — les caractéristiques en lignes, un "
      "processeur par colonne — et la complète jusqu'à la décision : threads, socket, cache, "
      "mémoire, PCIe, prix par cœur, indice, indice par millier d'euros. La colonne de gauche "
      "rappelle l'existant, qui n'est pas un processeur mais un jeu de ressources louées.", small=True)

ROWS = [
    ("Modèle", lambda c: f"**{c[1]}**"),
    ("Famille et architecture", lambda c: c[2]),
    ("Socket", lambda c: c[3]),
    ("Cœurs / threads", lambda c: f"{c[4]} / {c[5]}"),
    ("Fréquence de base", lambda c: "non garantie" if c[6] is None else dec(c[6], 2) + " GHz"),
    ("Fréquence turbo", lambda c: "—" if c[7] is None else dec(c[7], 2) + " GHz"),
    ("Cache L3", lambda c: c[8]),
    ("Mémoire", lambda c: c[9]),
    ("PCIe", lambda c: c[10]),
    ("TDP", lambda c: "—" if c[11] is None else f"{c[11]} W"),
    ("Sortie / fin de com.", lambda c: f"{c[12]} · {c[13]}"),
    ("Prix indicatif", lambda c: "≈ 411 €/mois" if c[0] == "Existant" else eur(c[14])),
    ("Prix par cœur", lambda c: "—" if c[0] == "Existant" else eur(c[14] / c[4])),
    ("Indice (cœurs × GHz)", lambda c: "—" if c[6] is None else dec(c[4] * c[6])),
    ("Indice par millier d'euros",
     lambda c: "—" if c[6] is None else dec(c[4] * c[6] / (c[14] / 1000))),
    ("Statut au seuil de 2,4 GHz",
     lambda c: {"g": "**Conforme**", "y": "**Toléré**", "o": "**Exclu**",
                "n": "référence"}[c[15]]),
]

cols = [EXISTANT] + CPU
heads = ["**Caractéristique**", "**Existant**"] + [f"**{c[1]}**" for c in CPU]
rows, cf = [], {}
for i, (lab, fn) in enumerate(ROWS):
    rows.append([f"**{lab}**"] + [fn(c) for c in cols])
    for j, c in enumerate(cols):
        b = bande_ghz(c[6]) if i in (4, 15) else c[15] if i == 15 else None
        if i == 4:
            b = bande_ghz(c[6])
        if c[0] == "Existant":
            cf[(i, 1 + j)] = FMT["n"]
        elif b:
            cf[(i, 1 + j)] = FMT[b]
cf[(13, 0)] = FMT["g"]

doc.table(heads, rows,
          widths=[4.1] + [3.11] * 7, font=6.9,
          aligns=["l"] + ["c"] * 7,
          caption=f"{tab()} — Les six processeurs du relevé, caractéristiques complétées, "
                  "l'existant en référence. Indice = cœurs × fréquence de base ; indice au "
                  "millier d'euros calculé sur le prix du processeur seul, hors machine. "
                  "**Vert ≥ 2,4 GHz, jaune 2,0–2,39 GHz.**",
          cell_fmt=cf, zebra=False, first_col_bold=True)

doc.image("fig_g_cpu.png", caption="Figure 1 — Prix du processeur en abscisse, indice de calcul en "
                                   "ordonnée. Les deux droites en pointillé marquent 48 et 20 points "
                                   "d'indice par millier d'euros.", width_cm=22.0)

doc.p("**Note de lecture.** Le Xeon Gold 6426Y est donné pour 2,50 GHz de base sur la fiche "
      "constructeur ; le relevé d'origine portait 2,40 GHz. L'écart ne déplace aucun classement "
      "— l'indice passe de 38,4 à 40,0 — et la valeur de la fiche a été retenue. Les prix "
      "processeurs sont des tarifs indicatifs hors machine, relevés chez les revendeurs ; ils "
      "servent à comparer, pas à acheter.", small=True)

doc.callout("Le premier constat tombe sur l'axe vertical",
            "À 1 050 €, l'**EPYC 9124** place **48 points d'indice** là où le **Xeon Silver 4510** "
            "en place **28,8** — même prix, **67 % de calcul en plus**. Le **Gold 6426Y** ramène "
            "Intel à 40 points, mais à **2 400 €**, soit un indice par millier d'euros de 16,7 "
            "contre 45,7 pour l'EPYC. Sur les six processeurs, **le meilleur rendement du calcul "
            "acheté est AMD**, et ce n'est pas une nuance : c'est un facteur 2,7.", "warn")

# --------------------------------------------------------------------------- #
doc.landscape(False)
doc.h1("3", "Le seuil de 2,4 GHz appliqué aux six")

doc.p("Le seuil tient en trois bandes, et il se lit sur la fréquence de base — la seule "
      "fréquence tenue en charge continue. Le turbo est un régime de pointe, pas une promesse de "
      "production : il ne sert pas au classement.", lead=True)

doc.table(
    ["Bande", "Règle", "Processeurs du relevé", "Nombre", "Conséquence"],
    [
        ["**Conforme**", "≥ 2,40 GHz", "Xeon Silver 4510 (2,40) · **Xeon Gold 6426Y (2,50)** · "
                                       "EPYC 9124 (3,00) · EPYC 9125 (2,60) · EPYC 9224 (2,50)",
         "**5 sur 6**", "Achetable sans réserve"],
        ["**Toléré**", "2,00 à 2,39 GHz", "Xeon Silver 4410Y (2,00)", "**1 sur 6**",
         "Achetable si l'écart de prix le justifie"],
        ["**Exclu**", "< 2,00 GHz", "aucun processeur du relevé", "**0 sur 6**",
         "Aucune exclusion à arbitrer"],
    ],
    widths=[2.6, 2.9, 6.6, 2.0, 3.5], font=8.3, aligns=["l", "l", "l", "c", "l"],
    caption=f"{tab()} — La règle des trois bandes, appliquée aux six processeurs relevés.",
    cell_fmt={(0, 0): FMT["g"], (1, 0): FMT["y"], (2, 0): FMT["o"]}, zebra=False)

doc.p("**Le seuil ne tranche donc presque rien dans ce périmètre** : cinq processeurs sur six "
      "sont conformes, et la seule fréquence tolérée — le Silver 4410Y à 2,00 GHz — est aussi le "
      "processeur le moins cher du relevé (900 €). Le débat ne porte pas sur l'éligibilité mais "
      "sur ce que chaque euro achète, et c'est là que l'indice et le prix par cœur prennent le "
      "relais.", small=True)

doc.table(
    ["Rang", "Processeur", "Indice", "Prix", "Prix par cœur", "Indice / k€", "Statut"],
    [[f"**{i+1}**", f"**{c[1]}**", dec(c[4] * c[6]), eur(c[14]), eur(c[14] / c[4]),
      "**" + dec(c[4] * c[6] / (c[14] / 1000)) + "**", {"g": "Conforme", "y": "Toléré"}[c[15]]]
     for i, c in enumerate(sorted(CPU, key=lambda c: -(c[4] * c[6] / c[14])))],
    widths=[1.3, 4.6, 1.7, 2.0, 2.4, 2.3, 2.3], font=8.6,
    aligns=["c", "l", "c", "r", "r", "c", "c"],
    caption=f"{tab()} — Les six processeurs classés par rendement : indice de calcul obtenu par "
            "millier d'euros dépensé. Le classement par prix donnerait un ordre différent.",
    cell_fmt={(0, 5): FMT["g"], (1, 5): FMT["g"], (5, 5): FMT["o"]}, zebra=False)

doc.callout("Le classement par prix et le classement par rendement ne se ressemblent pas",
            "Par prix, l'ordre est : 4410Y (900 €), 4510 et 9124 (1 050 €), 9125 (1 300 €), "
            "9224 (2 360 €), 6426Y (2 400 €). Par rendement, il devient : **9124 (45,7)**, 9125 "
            "(32,0), 4510 (27,4), 4410Y (26,7), 9224 (25,4), 6426Y (16,7). Le processeur le moins "
            "cher n'est donc pas le moins cher à calculer : à 12 cœurs, le 4410Y rend 26,7 points "
            "par millier d'euros quand le 9124 en rend 45,7. **L'écart de 150 € à l'achat coûte "
            "19,0 points de rendement.**", "warn")

# --------------------------------------------------------------------------- #
doc.landscape(True)
doc.h1("4", "Face-à-face AMD / Intel")

doc.p("Le face-à-face se mène sur deux plans, et il faut les deux pour ne pas se tromper. Sur "
      "**pièces**, à nombre de cœurs comparable, la question est : qui donne le plus de calcul "
      "pour l'euro ? En **machine**, à configuration identique, la question devient : combien "
      "coûte le serveur qui reçoit ce processeur ? Les deux réponses ne pointent pas toujours du "
      "même côté.", lead=True)

doc.h2("4.1 — À nombre de cœurs comparable")
doc.table(
    ["Duel", "Processeur", "Indice", "Prix", "Prix par cœur", "Indice / k€", "Écart"],
    [
        ["**12 cœurs**", "Intel Xeon Silver 4510", "28,8", "1 050 €", "88 €", "27,4", "référence Intel"],
        ["", "Intel Xeon Silver 4410Y", "24,0", "900 €", "75 €", "26,7", "− 150 €, − 4,8 d'indice"],
        ["", "*AMD : aucun 12 cœurs dans le relevé*", "—", "—", "—", "—",
         "l'EPYC d'entrée est un 16 cœurs"],
        ["**16 cœurs**", "AMD EPYC 9124 (3,00 GHz)", "**48,0**", "1 050 €", "66 €", "**45,7**",
         "**+ 67 % d'indice à prix égal**"],
        ["", "AMD EPYC 9125 (2,60 GHz)", "41,6", "1 300 €", "81 €", "32,0",
         "Zen 5 : 3,70 → 4,10 GHz de turbo"],
        ["", "Intel Xeon Gold 6426Y (2,50 GHz)", "40,0", "2 400 €", "150 €", "16,7",
         "**2,3 × le prix du 9124**"],
        ["**24 cœurs**", "AMD EPYC 9224 (2,50 GHz)", "60,0", "2 360 €", "98 €", "25,4",
         "Intel : rien sous 2 700 € dans cette gamme"],
    ],
    widths=[2.6, 7.0, 1.9, 2.3, 2.6, 2.5, 6.9], font=8.8,
    aligns=["l", "l", "c", "r", "r", "c", "l"],
    caption=f"{tab()} — Le face-à-face sur pièces, à nombre de cœurs comparable. L'indice par "
            "millier d'euros ne tient compte que du processeur, pas du châssis.",
    cell_fmt={(3, 2): FMT["g"], (3, 5): FMT["g"], (5, 6): FMT["o"], (1, 6): FMT["y"]}, zebra=True)

doc.h2("4.2 — À configuration identique, en machine")
doc.p("Les trois constructeurs qui vendent les deux familles sur le même châssis permettent un "
      "duel honnête : même marque, même génération de plateforme, même garantie. La "
      "configuration est figée — 128 Go DDR5, 2×1,92 To NVMe en RAID1, 2×10 GbE — et le prix est "
      "celui du serveur complet.", small=True)

doc.table(
    ["Constructeur", "Version AMD", "Prix", "Indice", "Version Intel", "Prix", "Indice",
     "Écart de prix", "Écart d'indice"],
    [
        ["**HPE**", "DL325 Gen11 · EPYC 9124", "**8 600 €**", "48,0",
         "DL380 Gen11 · Silver 4510", "14 400 €", "28,8", "**+ 5 800 €**", "**− 40 %**"],
        ["**Lenovo**", "SR645 V3 · EPYC 9124", "**8 500 €**", "48,0",
         "SR650 V3 · Silver 4510", "13 200 €", "28,8", "**+ 4 700 €**", "− 40 %"],
        ["**Dell**", "R6615 · EPYC 9124", "**11 900 €**", "48,0",
         "R660 · Silver 4510", "15 300 €", "28,8", "**+ 3 400 €**", "− 40 %"],
    ],
    widths=[2.8, 5.2, 2.2, 1.5, 5.1, 2.1, 1.5, 2.4, 2.1], font=8.6,
    aligns=["l", "l", "r", "c", "l", "r", "c", "r", "c"],
    caption=f"{tab()} — Le face-à-face en machine, à configuration identique. L'écart d'indice est "
            "constant (− 40 %) ; l'écart de prix, lui, varie du simple au double selon le "
            "constructeur — c'est le châssis Intel 2U qui pèse, plus que le processeur.",
    cell_fmt={(0, 7): FMT["o"], (1, 7): FMT["o"], (2, 7): FMT["y"]}, zebra=True)

doc.image("fig_g_face.png", caption="Figure 2 — Les trois duels constructeur, à configuration "
                                    "identique : l'Intel est plus cher et calcule moins.",
          width_cm=16.5)

doc.p("**Trois enseignements, et un contre-argument honnête.** L'écart de calcul est stable : à "
      "12 cœurs Intel contre 16 cœurs AMD, l'AMD rend **67 % de calcul en plus**, quel que soit "
      "le constructeur. L'écart de prix, lui, varie du simple au triple — 3 400 € chez Dell, "
      "5 800 € chez HPE. Une partie vient du châssis, non du processeur : les Xeon Silver du "
      "relevé ne se montent que sur des 2U à 32 emplacements mémoire. **Le surcoût Intel est donc "
      "aussi un surcoût de plateforme.**")

doc.h2("4.3 — Trois nuances à connaître, et le point qui décide")
doc.ul([
    "**Les canaux mémoire.** L'EPYC a douze canaux, le Xeon Silver huit. Mais la cible ne "
    "remplit que quatre barrettes : quatre canaux sur douze chez AMD, soit un tiers de la "
    "largeur disponible, contre la moitié chez Intel. **À 128 Go seulement, l'écart de bande "
    "passante mémoire se resserre** ; l'avantage AMD ne s'exprime pleinement qu'à huit ou douze "
    "DIMM — donc à 256 Go et plus.",
    "**Les voies PCIe.** 128 voies chez AMD contre 80 chez Intel : cela ne change rien avec deux "
    "disques NVMe, mais décide de la marge si un jour il faut ajouter des disques, une carte "
    "réseau 25 GbE ou un GPU.",
    "**Le prix de la mémoire.** Peupler les douze emplacements AMD coûte plus cher que l'écart de "
    "prix entre les deux processeurs : les canaux ne servent que si l'on peut les garnir.",
    "**Le point qui décide.** Aucune combinaison Intel du relevé ne bat l'EPYC 9124 sur le "
    "couple performance / prix : le Gold 6426Y coûte 2,3 fois plus cher pour 40 points d'indice "
    "contre 48. L'EPYC 9224 (24 cœurs, 60 d'indice) est le seul à aller plus loin — pour "
    "+ 1 310 € sur la machine complète.",
])


doc.landscape(False)

# --------------------------------------------------------------------------- #
doc.h1("5", "Quinze fournisseurs, du coefficient le plus bas au plus haut")

doc.p("Les quinze fournisseurs sont classés par **coefficient** : le rapport constaté entre le "
      "prix qu'ils pratiquent et le prix de référence relevé sur les pages publiques de PC21. Un "
      "coefficient de 1,00 signifie « prix de référence » ; 1,25 signifie « 25 % plus cher à "
      "configuration identique ». Le classement est un ordre de grandeur de canal, pas un devis : "
      "chaque ligne du chapitre 7 porte son statut.", lead=True)

_CF_COEF = {}
for _i, (_n, _z, _c, _d, _m, _l) in enumerate(FOURN):
    _b = "g" if _c <= 1.02 else ("y" if _c <= 1.12 else "o")
    if _c == 0.85:
        _b = "y"
    _CF_COEF[(_i, 3)] = FMT[_b]

doc.table(
    ["#", "Fournisseur", "Zone", "Coefficient", "Lecture du coefficient", "Accès"],
    [[f"**{i+1}**", f"**{n}**", z, dec(c, 2),
      {"0.85": "Le moins cher, **hors garantie constructeur**",
       "1.00": "Prix de référence",
       "1.02": "+ 2 % : marge de canal faible",
       "1.04": "+ 4 %",
       "1.05": "+ 5 %",
       "1.08": "+ 8 %",
       "1.10": "+ 10 %",
       "1.12": "+ 12 %",
       "1.15": "+ 15 %",
       "1.18": "+ 18 % : distributeur français",
       "1.22": "+ 22 %",
       "1.25": "Notre propre canal, intégration et garantie comprises",
       "1.60": "**+ 60 % pour la même référence HPE**"}.get(f"{c:.2f}", ""),
      f"[{lib}]({lien(n, dom, mode, 'serveur 1U AMD EPYC')})"]
     for i, (n, z, c, dom, mode, lib) in enumerate(FOURN)],
    widths=[0.9, 4.2, 3.3, 2.2, 5.4, 2.8], font=8.2,
    aligns=["c", "l", "l", "c", "l", "l"],
    caption=f"{tab()} — Les quinze fournisseurs, coefficient croissant. Le lien ouvre la recherche "
            "du fournisseur ; le chapitre 7 donne, pour chaque machine, le lien vers son offre "
            "précise.",
    cell_fmt=_CF_COEF, zebra=False)

doc.ul([
    "**Cinq fournisseurs se tiennent entre 0,85 et 1,02** — soit 17 % d'amplitude à eux cinq. "
    "C'est là que se joue le prix d'achat, pas dans la négociation finale.",
    "**Deux seulement vendent en direct sur le web avec un prix affiché pour la configuration "
    "complète** : PC21 (fiche produit, référence P77252-425) et ServerMall (configurateur). Les "
    "autres passent par un devis.",
    "**ServerMall, à 1,60, est 60 % au-dessus de la référence** pour la même machine HPE : à "
    "8 600 € de base, cela fait 5 200 € d'écart. Ce n'est pas une option, c'est un point de "
    "comparaison.",
    "**Notre propre canal est à 1,25** — soit 1 075 € de plus que PC21 sur la machine cible. "
    "L'écart correspond à l'intégration, à la garantie sur site et au support ; il doit être "
    "annoncé comme tel dans toute offre.",
])

# --------------------------------------------------------------------------- #
doc.landscape(True)
doc.h1("6", "Le serveur équipé : six processeurs, quinze fournisseurs")

doc.p("Le tableau suivant croise les deux dimensions du dossier. Chaque ligne est un "
      "fournisseur ; chaque colonne, un des six processeurs monté dans le serveur qui le reçoit, "
      "à configuration identique (128 Go DDR5, 2×1,92 To NVMe en RAID1, 2×10 GbE). Les trois "
      "colonnes AMD reposent sur le **HPE DL325 Gen11** (1U, SP5) ; les trois colonnes Intel sur "
      "le **HPE DL380 Gen11** (2U, LGA 4677), seul châssis HPE qui reçoit ces Xeon — le surcoût "
      "Intel inclut donc un changement de châssis, pas seulement de processeur : c'est le prix "
      "d'une machine complète, pas d'une puce.", small=True)

PRIX_MACHINE = {  # base PC21, serveur nu + processeur + 128 Go + 2 × 1,92 To NVMe
    "EPYC 9124": 8600, "EPYC 9125": 8850, "EPYC 9224": 9900,
    "Xeon Silver 4510": 14400, "Xeon Silver 4410Y": 14250, "Xeon Gold 6426Y": 15750,
}
ORDRE_CPU = ["EPYC 9124", "EPYC 9125", "EPYC 9224",
             "Xeon Silver 4510", "Xeon Silver 4410Y", "Xeon Gold 6426Y"]

BYP = {c[1]: c for c in CPU}
heads = ["**Fournisseur**", "**Zone**"] + \
        [f"**{c}**\n{BYP[c][4]} cœurs · {dec(BYP[c][6], 2)} GHz" for c in ORDRE_CPU]
rows, cf = [], {}
for i, (nom, zone, coef, dom, mode, lib) in enumerate(FOURN):
    row = [f"**{nom}**", zone]
    for j, c in enumerate(ORDRE_CPU):
        p = round(PRIX_MACHINE[c] * coef / 100) * 100
        row.append(f"**{eur(p)}**")
        cf[(i, 2 + j)] = FMT[bande(p)]
    rows.append(row)

doc.table(heads, rows,
          widths=[3.8, 2.5] + [3.27] * 6, font=7.6,
          aligns=["l", "l"] + ["r"] * 6,
          caption=f"{tab()} — Le serveur équipé, six processeurs × quinze fournisseurs, prix HT, "
                  "coefficient croissant de haut en bas. Configuration identique partout : 128 Go "
                  "DDR5, 2×1,92 To NVMe RAID1, 2×10 GbE, garantie 3 ans. **Aucune colonne Intel "
                  "ne passe sous 12 500 €.**",
          cell_fmt=cf, zebra=False)

doc.ul([
    "**Le processeur ne déplace pas le classement des fournisseurs** : PC21 et Mindware restent "
    "en tête quelle que soit la colonne, ServerMall en queue. Choisir Intel ne rend pas un "
    "fournisseur compétitif.",
    "**À processeur égal, l'écart de canal atteint 6 500 €** : de 7 300 € (9124 chez Alibaba) à "
    "13 800 € (9124 chez ServerMall). C'est presque le prix d'un second serveur, pour une machine "
    "rigoureusement identique.",
    "**Entre 9124 et 9224, il n'y a que 1 300 €** sur la machine complète : passer de 16 à 24 "
    "cœurs coûte moins que le passage d'un fournisseur à l'autre dans le haut du tableau.",
    "**Entre 9124 et 9125, 250 € seulement** : la génération Zen 5 se paie au prix d'un module "
    "mémoire. Elle apporte la DDR5-6000 et une fin de commercialisation deux ans plus tardive.",
])

doc.landscape(False)

# --------------------------------------------------------------------------- #
doc.h1("7", "Le prix de chaque modèle, chez chacun des quinze")

doc.p("Huit pages suivent, une par machine. Chaque page donne, pour **une configuration figée** "
      "(128 Go DDR5, 2×1,92 To NVMe en RAID1, 2×10 GbE, garantie 3 ans), le prix chez les quinze "
      "fournisseurs **et le lien qui ouvre leur offre sur ce modèle précis**. Un clic, et le "
      "lecteur est sur le catalogue du fournisseur, à la bonne référence.", lead=True)

doc.table(
    ["Code", "Constructeur", "Modèle", "Processeur", "Cœurs / GHz", "Indice", "Prix PC21",
     "Fiche constructeur"],
    [[f"**{c}**", f, m, cpu, f"{co} c · {dec(g, 2)}", dec(co * g), f"**{eur(p)}**",
      f"[fiche]({url})"]
     for c, f, m, cpu, fam, g, co, p, url, ch in MODELES],
    widths=[1.0, 2.3, 3.4, 2.7, 2.2, 1.2, 1.9, 2.2], font=7.6,
    aligns=["c", "l", "l", "l", "c", "c", "r", "l"],
    caption=f"{tab()} — Les huit machines retenues, à configuration identique. Cinq en AMD "
            "(EPYC 9124), trois en Intel (Xeon Silver 4510).",
    cell_fmt={**{(i, 6): FMT[bande(MODELES[i][7])] for i in range(len(MODELES))},
              **{(i, 5): FMT[bande_ghz(MODELES[i][5])] for i in range(len(MODELES))}},
    zebra=False)

doc.h2("7.1 — Le même châssis, trois processeurs")
doc.p("Les six processeurs ne demandent pas six machines : le DL325 Gen11 reçoit les trois EPYC "
      "du relevé sans changement de plateforme, puisque le socket SP5 leur est commun. Voilà ce "
      "que cela change au prix et au rendement — mesuré cette fois sur la machine complète et non "
      "sur la seule pièce.", small=True)

doc.table(
    ["Processeur", "Cœurs", "Indice", "Prix machine", "Indice / k€ machine", "Surcoût vs 9124",
     "Quand le choisir"],
    [
        ["**EPYC 9124**", "16", "48,0", "**8 600 €**", "**5,6**", "référence",
         "**Le choix par défaut** : meilleur rendement, 16 cœurs suffisent à 15 % de charge"],
        ["**EPYC 9125**", "16", "41,6", "8 850 €", "4,7", "+ 250 €",
         "Si la longévité de plateforme prime : Zen 5, DDR5-6000, fin de com. ≈ 2029"],
        ["**EPYC 9224**", "24", "60,0", "9 900 €", "6,1", "+ 1 300 €",
         "Si la densité de machines virtuelles est le critère : **meilleur indice par euro de "
         "machine**"],
    ],
    widths=[2.6, 1.4, 1.4, 2.4, 2.6, 2.2, 4.4], font=8.2,
    aligns=["l", "c", "c", "r", "c", "r", "l"],
    caption=f"{tab()} — Trois processeurs, une seule machine. L'indice par millier d'euros "
            "rapporté à la machine complète change le vainqueur : le 9224, plus cher en pièce, "
            "devient le plus efficace en serveur.",
    cell_fmt={(0, 4): FMT["g"], (2, 4): FMT["g"], (2, 5): FMT["y"]}, zebra=True)

doc.callout("Un renversement qui mérite d'être dit",
            "Sur la pièce seule, l'EPYC 9124 écrase le 9224 en rendement (45,7 contre 25,4 points "
            "par millier d'euros). Sur la **machine complète**, l'ordre s'inverse : 5,6 points par "
            "millier d'euros pour le 9124, **6,1 pour le 9224**. La raison est simple — le "
            "châssis, la mémoire et les disques coûtent la même chose dans les deux cas, si bien "
            "que 1 300 € de processeur en plus achètent 12 cœurs de plus. **Le 9124 reste le choix "
            "par défaut ; le 9224 est le meilleur achat si l'on veut de la marge.**", "info")

# --------------------------------------------------------------------------- #
NOM = {m[0]: f"{m[1]} {m[2]}" for m in MODELES}
PRIX_AMD = {m[0]: m[7] for m in MODELES if m[4] == "AMD"}
PRIX_INTEL = {m[0]: m[7] for m in MODELES if m[4] == "Intel"}


def situer(code, fam, prix):
    if fam == "AMD":
        autre = min((v, k) for k, v in PRIX_AMD.items() if k != code)
        bas_i = min(PRIX_INTEL.values())
        return (f"**Pour situer** : la moins chère des cinq AMD est le **{NOM[autre[1]]}** à "
                f"{eur(autre[0])} ; cette machine est à **{round(prix/autre[0]*100-100)} %**. "
                f"Face à elle, l'Intel conforme la moins chère est à {eur(bas_i)} "
                f"(**+ {round(bas_i/prix*100-100)} %**).")
    bas_a = min(PRIX_AMD.values())
    return (f"**Pour situer** : le même besoin en AMD démarre à {eur(bas_a)} — soit "
            f"**{round(bas_a/prix*100-100)} %** par rapport à cette machine Intel. C'est le prix "
            f"de la plateforme Intel, autant que celui du processeur.")


for c, fab, mod, cpu, fam, ghz, cores, prix_ref, url_fab, chassis in MODELES:
    q = (f"{fab} {mod}".replace("ProLiant ", "").replace("ThinkSystem ", "")
         .replace("PowerEdge ", ""))
    doc.landscape(True)
    doc.h1(c, f"{fab} {mod} — {cpu} · {cores} cœurs à {dec(ghz, 1)} GHz")

    b = bande_ghz(ghz)
    statut_cpu = {"g": "conforme", "y": "toléré", "o": "exclu"}[b]
    doc.p(f"**{chassis}** · cible : **128 Go DDR5**, **2×1,92 To NVMe en RAID1**, **2×10 GbE**, "
          f"garantie 3 ans. Processeur **{cpu}** — indice **{dec(cores * ghz, 0)}** "
          f"({cores} cœurs × {dec(ghz, 2)} GHz), **{statut_cpu}** au seuil de 2,4 GHz. "
          f"Admissibles ici : {ADMISSIBLES[fam]}. Référence PC21 : **{eur(prix_ref)}** HT.",
          small=True)

    rows, cf = [], {}
    for i, (nom, zone, coef, dom, mode, lib) in enumerate(FOURN):
        p = round(prix_ref * coef / 100) * 100
        statut = ("**base relevée**" if nom == "PC21.fr"
                  else ("hors garantie" if nom == "Alibaba.com" else "modélisé"))
        fiche = FICHE_PRODUIT.get((c, nom))
        href = fiche[0] if fiche else lien(nom, dom, mode, q)
        libelle = fiche[1] if fiche else lib
        rows.append([f"**{i+1}**", f"**{nom}**", zone, dec(coef, 2), f"**{eur(p)}**", statut,
                     f"[{libelle}]({href})"])
        cf[(i, 4)] = FMT[bande(p)]
        if nom == "PC21.fr":
            cf[(i, 0)] = FMT["g"]

    doc.table(
        ["#", "Fournisseur", "Zone", "Coef.", "Prix HT", "Statut du prix", "Vérifier l'offre"],
        rows,
        widths=[0.9, 4.4, 3.3, 1.3, 2.5, 3.2, 10.2], font=9.2,
        aligns=["c", "l", "l", "c", "r", "l", "l"],
        caption=f"{tab()} — {fab} {mod} · configuration cible, prix HT chez les quinze "
                f"fournisseurs, du moins cher au plus cher. Le lien ouvre la recherche du site "
                f"pour « {q} ».",
        cell_fmt=cf, zebra=False)

    bas = sorted(round(prix_ref * f[2] / 100) * 100 for f in FOURN)
    median = bas[len(bas) // 2]
    doc.ul([
        f"**Prix médian des quinze** : {eur(median)} HT — c'est ce que paie un acheteur qui "
        f"consulte un seul revendeur. L'écart avec le meilleur prix ({eur(bas[0])}) est la marge "
        f"de négociation réelle.",
        f"**À demander dans le devis** : {fab} {mod} avec {cpu}, 128 Go (4 × 32 Go DDR5), "
        f"2 × 1,92 To NVMe U.3, RAID1, 2×10 GbE, **garantie 3 ans sur site**, rails et second "
        f"bloc d'alimentation.",
        f"**Coût complet** : {eur(prix_ref)} de serveur + 4 550 € de périphériques + 1 110 € de "
        f"licences ≈ **{eur(round((prix_ref + 5660)/100)*100)} HT** prêt à produire.",
        situer(c, fam, prix_ref),
    ])

# --------------------------------------------------------------------------- #
doc.landscape(False)
doc.h1("8", "Synthèse et recommandation")

doc.h2("8.1 — Ce que l'étude établit")
doc.ul([
    "**Cinq des six processeurs relevés sont conformes** au seuil de 2,4 GHz ; le sixième — "
    "Xeon Silver 4410Y, 2,00 GHz — est toléré et se trouve être le moins cher. Le seuil ne "
    "restreint donc pas le choix : il le hiérarchise.",
    "**L'AMD EPYC 9124 est le meilleur achat sur pièces** : 48 points d'indice pour 1 050 €, "
    "soit 45,7 points par millier d'euros, contre 27,4 pour le Xeon Silver 4510 au même prix et "
    "16,7 pour le Gold 6426Y, 2,3 fois plus cher.",
    "**Le surcoût Intel est un surcoût de plateforme** : + 3 400 à 5 800 € selon le "
    "constructeur, alors que le processeur lui-même n'explique qu'une partie de l'écart. Les Xeon "
    "Silver du relevé n'existent que sur des châssis 2U à 32 DIMM.",
    "**Le classement des fournisseurs ne bouge pas d'un processeur à l'autre** : cinq enseignes "
    "se tiennent entre 0,85 et 1,02, ServerMall reste à 1,60. C'est le premier levier d'économie, "
    "avant le choix du processeur.",
    "**Le socket SP5 est un actif** : 9124, 9125 et 9224 se remplacent sans changer de machine, "
    "et le 9224 apporte 24 cœurs pour 1 300 € de plus sur un serveur à 8 600 €.",
])

doc.table(
    ["Scénario", "Machine", "Prix HT", "Fournisseur", "Verdict"],
    [
        ["**Cible recommandée**", "HPE DL325 Gen11 · EPYC 9124 · 128 Go · NVMe",
         "**8 600 €**", "PC21", "**Retenir : suivi, garantie, prix**"],
        ["Meilleur prix", "Supermicro AS-1115CS-TNR · 128 Go · NVMe",
         "7 100 €", "Alibaba (hors garantie) · 8 400 € chez Mindware",
         "Si l'assemblage et la garantie sont maîtrisés"],
        ["Alternative marque", "Lenovo SR645 V3 · 128 Go · NVMe",
         "8 500 €", "PC21 · Senetic", "Si un contrat de service est exigé : 10 400 € chez Inmac"],
        ["Marge de calcul", "HPE DL325 Gen11 · **EPYC 9224** · 128 Go · NVMe",
         "9 900 €", "PC21", "**+ 1 300 € pour 24 cœurs** — le meilleur indice par euro de machine"],
        ["Conforme Intel la moins chère", "HPE DL380 Gen11 · Silver 4510 · 128 Go · NVMe",
         "14 400 €", "Mindware · PC21", "**Coût du choix Intel**"],
        ["Si Dell est imposé", "Dell R6615 · EPYC 9124 · 128 Go",
         "12 400 €", "Redcorp · 12 900 € chez CDW", "Le tarif public Dell est le plus élevé"],
    ],
    widths=[3.0, 4.9, 2.0, 3.9, 3.3], font=7.7, aligns=["l", "l", "r", "l", "l"],
    caption=f"{tab()} — Les six scénarios qui se dégagent de l'étude.",
    cell_fmt={(0, 0): FMT["g"], (0, 4): FMT["g"], (3, 4): FMT["g"], (4, 4): FMT["o"]},
    zebra=False)

doc.callout("Recommandation",
            "**HPE ProLiant DL325 Gen11 · EPYC 9124 (16 cœurs, 3,0 GHz, indice 48) · 128 Go DDR5 "
            "· 2×1,92 To NVMe en RAID1 · 2×10 GbE** — 8 600 € HT chez PC21, 8 800 € chez Senetic "
            "et chez Mindware. Un devis de contrôle chez **Redcorp** et **Inmac wstore** pour la "
            "garantie sur site. Si la densité de machines virtuelles devient le critère, la même "
            "machine en **EPYC 9224** coûte 9 900 € et rend 25 % de calcul de plus. Budget de "
            "projet complet : **21 000 à 22 000 € HT** année 1.", "ok")

# --------------------------------------------------------------------------- #
doc.landscape(True)
doc.h1_plain("Annexe A — autres points de comparaison")

doc.p("Les trois tableaux qui suivent ne traitent pas des processeurs, mais ils pèsent sur la "
      "même décision et changent le prix final dans des proportions comparables. Ils sont "
      "condensés ici pour que l'étude reste lisible d'un bout à l'autre : le détail figure dans "
      "les fiches techniques des constructeurs.", small=True)

doc.h2("A.1 — Mémoire")
doc.table(
    ["Type", "Vitesse", "Module", "Prix", "€ / Go", "Disponibilité", "Lecture"],
    [
        ["DDR4 RDIMM", "2 666 MT/s", "32 Go", "≈ 210 €", "6,6 €", "Marché secondaire",
         "**Fin de vie** — à éviter sur un achat neuf"],
        ["**DDR5 RDIMM**", "4 800 MT/s", "32 Go", "≈ 520 €", "**16,3 €**", "**Très tendu**",
         "**Standard des six plateformes du relevé**"],
        ["DDR5 RDIMM", "5 600 MT/s", "32 Go", "≈ 610 €", "19,1 €", "Tendu",
         "Gain réel faible en virtualisation"],
        ["DDR5 RDIMM", "4 800 MT/s", "64 Go", "≈ 1 150 €", "18,0 €", "Très tendu",
         "Si une seule barrette par canal"],
    ],
    widths=[3.3, 2.2, 1.6, 2.1, 1.5, 3.0, 12.2], font=8.0,
    aligns=["l", "c", "c", "r", "r", "l", "l"],
    caption=f"{tab()} — Matrice mémoire. Les six processeurs du relevé sont tous en DDR5 : aucun "
            "ne se monte en DDR4. L'existant est à 88,4 % de 64 Go — acheter 64 Go, c'est acheter "
            "la saturation constatée.",
    cell_fmt={(1, 4): FMT["o"], (0, 6): FMT["o"], (1, 6): FMT["g"]}, zebra=False)

doc.h2("A.2 — Disques")
doc.table(
    ["Support", "Interface", "IOPS 4K", "Latence", "Prix 1,92 To", "€ / To", "Deux disques RAID1",
     "Lecture"],
    [
        ["SATA SSD RI", "6 Gb/s", "≈ 95 000", "≈ 120 µs", "≈ 450 €", "234 €", "**900 €**",
         "Le moins cher, bridé par le contrôleur"],
        ["SAS SSD", "12 / 24 Gb/s", "≈ 210 000", "≈ 90 µs", "≈ 750 €", "391 €", "1 500 €",
         "Double port, endurance 3 DWPD"],
        ["**NVMe U.3**", "PCIe 5.0 x4", "**≈ 800 000**", "**≈ 20 µs**", "≈ 650 €", "**339 €**",
         "**1 300 €**", "**Meilleur rapport latence / prix**"],
        ["Disque constructeur", "—", "—", "—", "≈ 1 100 €", "573 €", "2 200 €",
         "**+ 70 %** : firmware validé, garantie intégrée"],
    ],
    widths=[3.6, 2.6, 2.6, 1.9, 2.6, 1.5, 3.0, 8.2], font=8.0,
    aligns=["l", "c", "c", "c", "r", "r", "r", "l"],
    caption=f"{tab()} — Matrice disques. Le NVMe ne coûte que 400 € de plus que le SATA pour un "
            "facteur six sur la latence : c'est le meilleur euro du dossier.",
    cell_fmt={(2, 7): FMT["g"], (0, 7): FMT["y"], (3, 5): FMT["o"]}, zebra=False)

doc.h2("A.3 — RAID, réseau et budget")
doc.table(
    ["Point", "Choix retenu", "Ce que cela engage", "Coût"],
    [
        ["RAID", "**RAID 1 (miroir) ou miroir ZFS**", "2 × 1,92 To pour 1,92 To utiles, "
                                                       "tolérance à la panne d'un disque, "
                                                       "reconstruction rapide", "inclus"],
        ["Réseau serveur", "**2 × 10 GbE BASE-T (OCP 3.0)**", "20 Gbit/s agrégés : sauvegarde et "
                                                               "migration à chaud des VM", "**inclus (DL325)**"],
        ["Switch 10 GbE", "8 ports BASE-T", "Sans lui, le 10 GbE du serveur ne sert à rien",
         "≈ 900 €"],
        ["Sauvegarde", "Proxmox Backup Server + stockage externe",
         "La règle 3-2-1 ne se négocie pas sur un serveur unique", "inclus dans les 4 550 €"],
        ["Licences", "Proxmox VE + PBS, an 1", "Support par abonnement, dépôts entreprise",
         "≈ 1 110 €"],
    ],
    widths=[2.7, 5.2, 12.3, 5.4], font=7.6, aligns=["l", "l", "l", "r"],
    caption=f"{tab()} — Les points qui entourent le serveur.",
    cell_fmt={(0, 1): FMT["g"], (1, 1): FMT["g"]}, zebra=False)

doc.table(
    ["Ligne budgétaire", "Montant HT", "Statut"],
    [
        ["Serveur cible — DL325 Gen11, EPYC 9124, 128 Go, 2×1,92 To NVMe RAID1", "**8 600 €**",
         "Base relevée"],
        ["Périphériques (onduleur, sauvegarde, switch, rechange, rack)", "4 550 €", "Indicatif"],
        ["**Sous-total matériel**", "**13 150 €**", "—"],
        ["Licences Proxmox VE + PBS, an 1", "≈ 1 110 €", "Indicatif"],
        ["**Total « prêt à produire »**", "**≈ 14 300 €**", "—"],
        ["Fret, douane, intégration, migration", "6 700 à 7 700 €", "Pour mémoire"],
        ["**Projet complet, année 1**", "**21 000 à 22 000 €**", "—"],
    ],
    widths=[13.4, 4.2, 8.3], font=8.2, aligns=["l", "r", "l"],
    caption=f"{tab()} — Du prix du serveur au budget de projet.",
    row_bg={2: BLEU_BG, 4: BLEU_BG, 6: BLEU_BG}, zebra=False)

doc.h2("A.4 — Ce que le TDP coûte réellement")
doc.table(
    ["Processeur", "TDP", "kWh / an (charge 60 %)", "Coût annuel à 0,20 €/kWh", "Écart vs 150 W",
     "Prix du processeur", "Délai de retour"],
    [
        ["Xeon Silver 4510 / 4410Y", "**150 W**", "788 kWh", "**158 €**", "référence", "900 à 1 050 €",
         "—"],
        ["Xeon Gold 6426Y", "185 W", "973 kWh", "195 €", "**+ 37 €/an**", "2 400 €",
         "**jamais** (35 € de TDP pour 1 350 € de prix)"],
        ["EPYC 9124 / 9125 / 9224", "**200 W**", "1 051 kWh", "210 €", "**+ 52 €/an**", "1 050 à 2 360 €",
         "**jamais** — et vainqueur au calcul"],
    ],
    widths=[5.0, 1.9, 3.2, 3.3, 2.4, 3.1, 6.9], font=7.9,
    aligns=["l", "c", "c", "c", "c", "c", "l"],
    caption=f"{tab()} — Le TDP ne décide de rien : 50 W d'écart valent 52 € par an, quand le même "
            "écart de choix vaut 2 000 € à l'achat. L'argument énergétique ne compense pas l'écart "
            "de prix.",
    cell_fmt={(0, 1): FMT["g"], (2, 1): FMT["o"], (1, 6): FMT["o"], (2, 6): FMT["y"]}, zebra=False)

doc.p("**Hypothèses de calcul** : 8 760 heures par an, charge moyenne à 60 % de la valeur du TDP, "
      "0,20 € le kWh. Un serveur ne consomme jamais son TDP nominal en permanence ; le chiffre est "
      "donné pour l'ordre de grandeur, pas pour la facture. À ce niveau, **le rendement du calcul "
      "par euro dépensé compte cent fois plus que le watt** : 50 W d'écart sur trois ans font "
      "156 €, quand le choix du processeur déplace la facture de 1 300 à 2 000 €.", small=True)

doc.p("**Trois arbitrages qui ne sont pas des arbitrages de processeur** — ils pèsent pourtant "
      "plus lourd que lui dans la facture :", small=True)
doc.ul([
    "**128 Go plutôt que 64 Go** (+ 1 600 €) : l'existant est à 88,4 % de 64 Go. Acheter 64 Go, "
    "c'est acheter la saturation constatée — la seule économie qui se paie deux fois.",
    "**NVMe plutôt que SATA** (+ 400 €) : six fois moins de latence pour 400 €, soit le meilleur "
    "euro du dossier, très loin devant l'arbitrage des fréquences processeur.",
    "**Le switch 10 GbE** (≈ 900 €) : les deux ports 10 GbE sont inclus dans le serveur, mais "
    "sans switch ils négocient à 1 Gbit/s. C'est la dépense la plus facile à oublier.",
])

# --------------------------------------------------------------------------- #
doc.landscape(False)
doc.h1_plain("Annexe B — méthode des prix et statut des liens")

doc.p("Aucun de ces prix n'est un devis ferme. Trois statuts coexistent et sont indiqués ligne "
      "par ligne : **base relevée** (page publique consultée le 5 novembre 2026 : fiche PC21 "
      "P77252-425 pour le DL325, P71675-425 pour le DL380), **modélisée** (coefficient du "
      "fournisseur appliqué à cette base, arrondi aux cent euros), **hors garantie** (Alibaba, "
      "marché gris).", lead=True)

doc.table(
    ["Fournisseur", "Coefficient", "Type de lien dans les tableaux", "Contrôle du 6 nov. 2026"],
    [
        ["PC21.fr", "1,00", "Fiche produit pour M1 · recherche Google pour les autres",
         "Fiche P77252-425 ouverte et lue"],
        ["Mindware", "1,00", "Recherche Google restreinte au site (`site:`)", "Moteur, pas de "
                                                                              "recherche native stable"],
        ["Alibaba.com", "0,85", "Recherche native (`SearchText`)", "Page atteinte, contrôle "
                                                                   "anti-robot à l'affichage"],
        ["Senetic", "1,02", "Recherche native (`/search/?text=`)", "Endpoint ouvert, aucun "
                                                                   "résultat sur le processeur seul"],
        ["CDW", "1,08", "Recherche native (`/search/?key=`)", "**17 résultats pour « DL325 "
                                                              "Gen11 »**"],
        ["Insight", "1,15", "Recherche native (`/search.html?q=`)", "Page chargée, résultats en "
                                                                    "JavaScript"],
        ["LDLC Pro", "1,18", "Recherche native (`/recherche/?q=`)", "Page chargée"],
        ["Inmac wstore", "1,22", "Recherche native (`recherche.aspx?q=`)", "Page chargée, "
                                                                          "0 résultat sur ce modèle"],
        ["ServerMall", "1,60", "Configurateur DL325 pour M1 · Google pour les autres",
         "Configurateur ouvert"],
        ["GED-SERVICES", "1,25", "Lien `mailto:` pré-rempli (objet + référence)", "Notre propre "
                                                                                 "canal"],
        ["Les six autres", "1,02 à 1,12", "Recherche Google restreinte au site (`site:`)",
         "Aucune recherche native exploitable"],
    ],
    widths=[3.0, 2.2, 6.3, 5.5], font=7.9, aligns=["l", "c", "l", "l"],
    caption=f"{tab()} — Ce que fait chaque lien, et ce qui a été constaté en l'ouvrant. Les liens "
            "ont été rouverts et revérifiés un par un le 6 novembre 2026.",
    cell_fmt={(4, 3): FMT["g"], (0, 0): FMT["g"]}, zebra=True)

doc.p("**Pourquoi certains liens passent par une recherche.** Six fournisseurs sur quinze "
      "exposent une adresse de recherche stable et directe ; les autres bloquent l'accès direct "
      "(JavaScript, contrôle anti-robot, session obligatoire). Dans ce cas, le lien ouvre le "
      "moteur de recherche restreint au site du fournisseur avec le nom exact du modèle — un clic "
      "mène à sa fiche, mais par un détour. C'est le compromis retenu plutôt qu'un lien mort.",
      small=True)

doc.p("**Avertissement.** Les tarifs processeurs sont des prix de revient indicatifs relevés chez "
      "les revendeurs, hors machine. Les prix de serveur sont ceux de la configuration décrite, "
      "HT, hors port et hors installation. Les liens peuvent changer sans préavis ; ils ont été "
      "revérifiés le 6 novembre 2026. Les prix de marché évoluent de 5 à 10 % par mois sur la "
      "mémoire et les disques : toute commande doit être revalidée sur la page du fournisseur au "
      "moment de l'engagement.", small=True)

doc.save(OUT)
print("saved", OUT)
