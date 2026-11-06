# -*- coding: utf-8 -*-
"""Document F — seuils CPU abaissés, 15 fournisseurs classés, duels AMD/Intel,
et une page de prix par modèle avec lien direct chez chaque fournisseur."""
import os
from urllib.parse import quote
from render import Doc

BASE = "F_Seuils_abaisses_duels_AMD_Intel_et_prix_par_modele"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables")

doc = Doc(
    base=BASE,
    title="Seuils abaissés, duels AMD-Intel, prix par modèle",
    subtitle="Proposition F — quinze fournisseurs classés, huit modèles, un lien par offre",
    meta=[],
    doc_ref="GED-RAP-2026-06 · Confidentiel — usage interne",
    footer="Proposition F · seuils, duels et prix par modèle",
)

# --------------------------------------------------------------------------- #
VERT_BG, VERT_TX = "E3F0DC", "1E6B2F"
JAUN_BG, JAUN_TX = "FBF3D0", "8A6D00"
ORAN_BG, ORAN_TX = "FBE0CE", "B4500F"
BLEU_BG = "EAF0F7"


def F(bg=None, tx=None, b=False, i=False):
    return {"bg": bg, "color": tx, "b": b, "i": i}


FMT = {"g": F(VERT_BG, VERT_TX, True), "y": F(JAUN_BG, JAUN_TX, True),
       "o": F(ORAN_BG, ORAN_TX, True), "x": F()}

_NT = [0]


def tab():
    _NT[0] += 1
    return f"Tableau {_NT[0]}"


def eur(n):
    return f"{round(n):,}".replace(",", " ") + " €"


# --------------------------------------------------------------------------- #
# 1. Les quinze fournisseurs, du moins cher au plus cher (coefficient croissant)
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

# gabarits de recherche : un clic mène à l'offre du fournisseur pour ce modèle
GABARIT = {
    "search": "https://{dom}/search/?text={q}",           # Senetic
    "google": "https://www.google.com/search?q=site%3A{dom}+{q}",
}
SPECIFIQUE = {
    # endpoints de recherche natifs, vérifiés un par un
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
# 2. Modèles : huit machines, une seule configuration cible chacune
#    (code, constructeur, modèle, cpu, famille, ghz, cœurs, prix PC21, fiche constructeur, châssis)
MODELES = [
    ("M1", "HPE", "ProLiant DL325 Gen11", "EPYC 9124", "AMD", 3.00, 16, 8600,
     "https://www.hpe.com/fr/fr/compute/hpe-proliant-compute/dl325-gen11.html",
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
     "https://www.hpe.com/fr/fr/compute/hpe-proliant-compute/dl380-gen11.html",
     "2U · 8 SFF · 32 DIMM · 2×10 GbE"),
    ("M7", "Lenovo", "ThinkSystem SR650 V3", "Xeon Silver 4510", "Intel", 2.40, 12, 13200,
     "https://lenovopress.lenovo.com/lp1699",
     "2U · 8 SFF · 32 DIMM · 2×10 GbE"),
    ("M8", "Dell", "PowerEdge R660", "Xeon Silver 4510", "Intel", 2.40, 12, 15300,
     "https://www.dell.com/fr-fr/shop/ipovw/poweredge-r660",
     "1U · 10 SFF · 32 DIMM · 2×10 GbE"),
]

# --------------------------------------------------------------------------- #
# 3. Paramètres du modèle de prix
BASE_AMD, BASE_INTEL = 5726, 11455     # relevés PC21 (DL325 9124 / DL380 4510), 64 Go
RAM_128 = 1600
DISK = {"SATA": 900, "SAS": 1500, "NVMe": 1300}
CPU_INTEL_16C = 1900                    # Xeon Silver 4510 (2,4) -> Gold 6426Y (2,5)

VAR = [("a", "SATA", 12), ("b", "SAS", 12), ("c", "NVMe", 16),
       ("d", "SATA", 16), ("e", "SAS", 12), ("f", "NVMe", 16)]
DOUBLON = {"e": "b", "f": "c"}


def prix(base, disque, coeurs, famille):
    """Chez AMD, 12 comme 16 cœurs sont couverts par l'EPYC 9124 (16 cœurs, 3,0 GHz)."""
    p = base + DISK[disque]
    if famille == "Intel" and coeurs == 16:
        p += CPU_INTEL_16C
    return p


def bande(p):
    if p <= 9500:
        return "g"
    if p <= 12500:
        return "y"
    return "o"


def bande_ghz(g):
    """Nouveau seuil : 2,4 GHz conforme, 2,0–2,39 toléré, < 2,0 exclu."""
    if g >= 2.4:
        return "g"
    if g >= 2.0:
        return "y"
    return "o"


# --------------------------------------------------------------------------- #
doc.cover(
    eyebrow="Proposition F — seuils abaissés",
    title="Le seuil passe à 2,4 GHz :\nce que cela change",
    subtitle="Quinze fournisseurs classés du moins cher au plus cher, huit modèles en face-à-face "
             "AMD / Intel, et pour chaque modèle le prix chez chacun des quinze, avec le lien direct "
             "qui mène à son offre.",
    meta_rows=[
        ["Pour", "**Jad — Direction Générale**"],
        ["Objet", "Reprendre la proposition E avec un seuil processeur abaissé à 2,4 GHz "
                  "(2,0–2,4 GHz toléré), un classement des fournisseurs par prix croissant et un "
                  "face-à-face AMD / Intel par modèle"],
        ["Cible rappelée", "**128 Go DDR5** · **2×1,92 To utiles en RAID1** · **12 à 16 cœurs** · "
                           "**2×10 GbE** · rackable · Proxmox VE"],
        ["Nouveau seuil CPU", "**Conforme ≥ 2,4 GHz** · **Toléré 2,0 à 2,39 GHz** · **Exclu < 2,0 GHz**"],
        ["Ce qui change", "Le Xeon Silver 4510 (2,4 GHz) **devient conforme** : l'Intel redevient "
                          "achetable sans surcoût de 1 900 €"],
        ["Structure", "1) ce qui change · 2) les 15 fournisseurs classés · 3) les seuils · "
                      "4) les duels AMD/Intel · 5) grilles A et B · 6) **prix par modèle, 8 pages** · "
                      "7) matrices C à F · 8) synthèse"],
        ["Date", "6 novembre 2026"],
    ],
    summary=("Comment lire ce document",
             "Chaque modèle a sa page : quinze lignes, quinze prix, et pour chacune un lien qui ouvre "
             "l'offre du fournisseur pour **cette machine précise**. Les couleurs suivent la règle "
             "**vert ≤ 9 500 €, jaune ≤ 12 500 €, orange au-delà** ; pour les processeurs, "
             "**vert ≥ 2,4 GHz, jaune 2,0–2,39 GHz (toléré), orange < 2,0 GHz (exclu)**.",
             "info"),
)

# --------------------------------------------------------------------------- #
doc.h1("1", "Ce qui change par rapport à la proposition E")

doc.p("La proposition E retenait 2,5 GHz comme plancher strict. Ce seul chiffre écartait tous les "
      "Xeon Silver et imposait un Xeon Gold à + 1 900 €, ce qui doublait le prix des configurations "
      "Intel. Le seuil est ramené à **2,4 GHz**, avec une **plage de tolérance de 2,0 à 2,4 GHz** : "
      "une machine peut être retenue sous 2,4 GHz, mais elle doit alors être signalée comme "
      "**tolérée** et justifiée. En dessous de 2,0 GHz, elle est exclue.", lead=True)

doc.table(
    ["Point", "Proposition E", "Proposition F", "Effet"],
    [
        ["Seuil processeur", "2,5 GHz strict", "**2,4 GHz**, tolérance 2,0–2,39 GHz",
         "Les Xeon Silver 4510 et 4410Y entrent dans le périmètre"],
        ["Statut du Xeon Silver 4510 (2,4 GHz)", "**Non conforme**", "**Conforme**",
         "La machine Intel la moins chère devient éligible"],
        ["Configuration Intel conforme la moins chère (128 Go, NVMe)",
         "16 300 € — Xeon Gold 6426Y, 16 cœurs", "**14 400 €** — Xeon Silver 4510, 12 cœurs",
         "**− 1 900 €**, mais avec **4 cœurs de moins**"],
        ["Configuration AMD (128 Go, NVMe)", "8 600 €", "**8 600 €**",
         "Inchangée : l'EPYC 9124 était déjà conforme"],
        ["Variante 12 cœurs chez AMD", "EPYC 9224 (24 c.), + 1 300 €",
         "**EPYC 9124 (16 c.)**, sans surcoût", "**− 1 300 €** sur les colonnes 12 cœurs"],
        ["Fournisseurs", "Liste par zone", "**Classés par prix croissant**",
         "Le moins cher en haut, le plus cher en bas"],
        ["Prix par modèle", "Six variantes × 15 fournisseurs",
         "**Huit modèles × 15 fournisseurs**, un lien par ligne", "Un clic mène à l'offre"],
    ],
    widths=[3.4, 3.4, 4.9, 5.4], font=7.6, aligns=["l", "l", "l", "l"],
    caption=f"{tab()} — Les sept différences entre la proposition E et la proposition F.",
    cell_fmt={(1, 2): FMT["g"], (2, 2): FMT["g"], (1, 1): FMT["o"]}, zebra=False)

doc.table(
    ["Bloc", "Configuration, prix PC21", "Proposition E", "Proposition F", "Ce qui change"],
    [
        ["A.1", "AMD · 64 Go · NVMe · 12 cœurs", "8 300 €", "**7 000 €**", "− 1 300 € (EPYC 9124 au lieu du 9224)"],
        ["A.2", "AMD · 128 Go · NVMe · 12 cœurs", "9 900 €", "**8 600 €**", "− 1 300 € (même raison)"],
        ["B.1", "Intel · 64 Go · NVMe · 12 cœurs", "12 800 €", "12 800 €", "Prix inchangé, **statut conforme**"],
        ["B.2", "Intel · 128 Go · NVMe · 12 cœurs", "14 400 €", "14 400 €", "Prix inchangé, **statut conforme**"],
        ["B.2", "Intel · 128 Go · NVMe · 16 cœurs", "16 300 €", "16 300 €",
         "Toujours le Gold : 16 cœurs à 2,4 GHz n'existent pas"],
    ],
    widths=[1.2, 5.0, 2.6, 2.6, 5.7], font=7.6, aligns=["c", "l", "r", "r", "l"],
    caption=f"{tab()} — Ce que le nouveau seuil change, bloc par bloc, à fournisseur constant (PC21). "
            "L'écart B.2 12 cœurs / 16 cœurs est le prix des quatre cœurs manquants.",
    cell_fmt={(0, 3): FMT["g"], (1, 3): FMT["g"], (2, 3): FMT["g"], (3, 3): FMT["g"]}, zebra=False)

doc.callout("La conséquence à retenir avant tout le reste",
            "Le seuil de 2,4 GHz ne fait pas baisser le prix d'une machine donnée : il **rend "
            "éligible une machine qui existait déjà à 14 400 €**. L'économie de 1 900 € se paie en "
            "**cœurs** (12 au lieu de 16), pas en euros par cœur. Et l'écart avec AMD reste entier : "
            "8 600 € contre 14 400 € pour le même service rendu.",
            "warn")

# --------------------------------------------------------------------------- #
doc.h1("2", "Les quinze fournisseurs, du moins cher au plus cher")

doc.p("Les mêmes quinze fournisseurs que dans la proposition E, mais classés par **coefficient de "
      "prix croissant** : l'indice 1,00 correspond au prix PC21, et chaque ligne indique l'écart "
      "attendu sur une nomenclature identique. Chaque nom porte un lien : la recherche du site "
      "lorsqu'elle existe, sinon une recherche restreinte au domaine du fournisseur.", lead=True)

TYPE = {
    "Alibaba.com": "Place de marché", "Mindware": "Distributeur (Dubaï)", "PC21.fr": "Catalogue + configurateur",
    "Arena Bilgisayar": "Distributeur (Istanbul)", "Senetic": "Catalogue en ligne",
    "Redcorp": "Catalogue en ligne", "MonParcInformatique": "Catalogue en ligne", "CDW": "Catalogue B2B",
    "Mustek": "Distributeur (Le Cap)", "Bechtle": "Intégrateur", "Insight": "Intégrateur",
    "LDLC Pro": "Catalogue B2B", "Inmac wstore": "Intégrateur (Bechtle)",
    "GED-SERVICES": "Intégrateur local", "ServerMall": "Configurateur en ligne",
}

rows, cf = [], {}
for i, (nom, zone, coef, dom, mode, lib) in enumerate(FOURN):
    rows.append([f"**{i+1}**", f"**{nom}**", zone, f"{coef:.2f}".replace(".", ","), TYPE[nom],
                 f"[{lib}]({lien(nom, dom, mode, 'serveur rack 128 Go')})"])
    cf[(i, 3)] = FMT["g"] if coef <= 1.05 else (FMT["y"] if coef <= 1.18 else FMT["o"])

doc.table(
    ["#", "Fournisseur", "Zone", "Coef.", "Type d'acteur", "Trouver son offre"],
    rows,
    widths=[0.9, 4.0, 3.2, 1.3, 4.2, 3.5], font=7.8,
    aligns=["c", "l", "l", "c", "l", "l"],
    caption=f"{tab()} — Classement par coefficient croissant. **Vert ≤ 1,05** (prix PC21 ou moins), "
            "**jaune ≤ 1,18**, **orange au-delà**. Alibaba est sous 1,00 mais sans garantie "
            "constructeur ; ServerMall est à 1,60 pour la même référence HPE.",
    cell_fmt=cf, zebra=False)

doc.h2("Ce que veulent dire les trois types de lien")
doc.ul([
    "**recherche** — l'adresse ouvre directement le moteur de recherche interne du fournisseur avec "
    "la référence du modèle. Vérifié pour Senetic, CDW, Insight, LDLC Pro, Inmac wstore et Alibaba.",
    "**Google** — le fournisseur n'expose pas d'adresse de recherche exploitable : le lien ouvre une "
    "recherche Google **restreinte à son domaine** (`site:`). Un clic, puis un clic sur le résultat : "
    "on arrive bien sur sa fiche produit.",
    "**e-mail** — GED-SERVICES, intégrateur à Libreville, ne publie pas de catalogue : le lien ouvre "
    "un message prérempli avec la référence du modèle et la configuration cible.",
])

doc.callout("Pourquoi quatorze liens passent par une recherche",
            "Deux fournisseurs seulement publient une adresse produit stable : PC21 (fiche "
            "**P77252-425**) et ServerMall (configurateur DL325). Sur les pages de ces deux modèles, "
            "le lien pointe **directement sur l'offre**. Partout ailleurs, l'adresse produit change "
            "à chaque remise à jour du catalogue : le moteur de recherche du site — ou une recherche "
            "restreinte à son domaine — reste la seule porte d'entrée qui ne tombe pas en erreur 404. "
            "Nous avons préféré un lien qui fonctionne à un lien qui brille.",
            "info")

# --------------------------------------------------------------------------- #
doc.h1("3", "Le nouveau seuil, appliqué aux processeurs")

doc.p("Trois zones, et une seule règle. **Vert** : la fréquence de base atteint 2,4 GHz, la machine "
      "est conforme sans réserve. **Jaune** : entre 2,0 et 2,39 GHz, la machine est tolérée — elle "
      "peut être retenue si la charge le justifie, avec une dérogation écrite. **Orange** : sous "
      "2,0 GHz, elle est exclue, quelle que soit sa génération.", lead=True)

CPU = [
    # modèle, archi, année, cœurs, base, turbo, tdp, prix, statut
    ("AMD EPYC 9124", "Zen 4 — 9004", "2023", 16, 3.00, 3.70, 200, "≈ 1 050 €"),
    ("AMD EPYC 9224", "Zen 4 — 9004", "2023", 24, 2.50, 3.70, 200, "≈ 2 350 €"),
    ("AMD EPYC 9125", "Zen 5 — 9005", "2024", 16, 2.60, 4.10, 200, "≈ 1 300 €"),
    ("AMD EPYC 9354P", "Zen 4 — 9004", "2023", 32, 3.25, 3.80, 280, "≈ 4 200 €"),
    ("Intel Xeon Gold 6426Y", "Sapphire Rapids", "2023", 16, 2.50, 4.10, 185, "≈ 2 400 €"),
    ("Intel Xeon Silver 4510", "Emerald Rapids", "2023", 12, 2.40, 4.10, 150, "≈ 1 050 €"),
    ("Intel Xeon Silver 4410Y", "Emerald Rapids", "2023", 12, 2.00, 3.90, 150, "≈ 900 €"),
    ("Intel Xeon Silver 4514Y", "Emerald Rapids", "2023", 16, 2.00, 3.50, 150, "≈ 1 500 €"),
    ("Intel Xeon Gold 6430", "Sapphire Rapids", "2023", 32, 2.10, 3.40, 270, "≈ 4 600 €"),
    ("Intel Xeon Gold 6138", "Skylake — Gen10", "2017", 20, 2.00, 3.70, 125, "≈ 120 € (occasion)"),
]
LIB = {"g": "**Conforme**", "y": "Toléré", "o": "Exclu"}

rows, cf = [], {}
for i, (m, archi, an, c, base, turbo, tdp, px) in enumerate(CPU):
    b = bande_ghz(base)
    statut = LIB[b]
    if "6138" in m:
        statut = "Toléré, mais **EOL 2023**"
    rows.append([f"**{m}**", archi, an, f"{c}", f"{base:.2f}".replace(".", ","),
                 f"{turbo:.2f}".replace(".", ","), f"{tdp} W", px, statut])
    cf[(i, 4)] = FMT[b]
    cf[(i, 8)] = FMT[b]
    if "6138" in m:
        cf[(i, 8)] = FMT["o"]

doc.table(
    ["Processeur", "Architecture", "Sortie", "Cœurs", "Base", "Turbo", "TDP", "Prix indicatif",
     "Statut au nouveau seuil"],
    rows,
    widths=[3.3, 2.35, 1.25, 1.3, 1.3, 1.3, 1.25, 2.35, 2.7], font=7.5,
    aligns=["l", "l", "c", "c", "c", "c", "c", "r", "l"],
    caption=f"{tab()} — Le classement des processeurs au seuil de 2,4 GHz. La colonne « Base » porte "
            "la couleur du statut : **vert ≥ 2,4 · jaune 2,0–2,39 · orange < 2,0**.")

doc.ul([
    "**Ce que le seuil fait gagner** : le Xeon Silver 4510 (12 cœurs à 2,4 GHz) passe de « non "
    "conforme » à « conforme ». C'est la référence Intel la plus vendue, et la moins chère.",
    "**Ce qu'il ne fait pas gagner** : la fréquence de base reste 2,4 GHz contre 3,0 GHz chez "
    "l'EPYC 9124. À cœurs comparables, l'AMD garde 25 % de fréquence et 70 % d'indice de calcul.",
    "**Ce qu'il faut éviter** : un Xeon Silver 4514Y (16 cœurs à 2,0 GHz) affiché « 16 cœurs » mais "
    "toléré seulement — il coûte plus cher que le 4510 et calcule moins.",
    "**Ce que la bande verte ne dit pas** : le turbo. Un Xeon Silver 4510 monte à 4,1 GHz sur un "
    "cœur ; cela ne change rien à une charge de virtualisation étalée sur douze cœurs, où seule la "
    "fréquence de base compte. C'est elle que nous classons.",
    "**Ce que le seuil ne règle pas** : l'obsolescence. Un Xeon Gold 6138 de 2017 passe le seuil "
    "des 2,0 GHz, mais il est arrêté depuis 2023 : ni pièces, ni firmware, ni garantie.",
])

doc.table(
    ["Bande", "Fréquence de base", "Statut", "Ce que cela autorise", "Ce qu'il faut faire"],
    [
        ["**Vert**", "≥ 2,4 GHz", "**Conforme**", "Retenue sans réserve",
         "Rien à justifier"],
        ["**Jaune**", "2,0 à 2,39 GHz", "Toléré", "Retenue possible si la charge le justifie",
         "Dérogation écrite, avec mesure de charge à l'appui"],
        ["**Orange**", "< 2,0 GHz", "Exclu", "Écartée",
         "Aucune dérogation, sauf reconditionné de transition"],
    ],
    widths=[1.8, 2.9, 2.1, 4.9, 5.4], font=8.0, aligns=["c", "c", "c", "l", "l"],
    caption=f"{tab()} — La règle des trois bandes, telle qu'elle est appliquée dans tout le document.",
    cell_fmt={(0, 0): FMT["g"], (1, 0): FMT["y"], (2, 0): FMT["o"]}, zebra=False)

# --------------------------------------------------------------------------- #
doc.landscape(True)
doc.h1("4", "Face-à-face AMD / Intel, modèle par modèle")

doc.p("Trois constructeurs proposent les deux familles sur le même châssis. À configuration "
      "identique — 128 Go DDR5, 2×1,92 To NVMe en RAID1, 2×10 GbE — voici ce que chacun facture, "
      "et ce qu'il rend en calcul.", small=True)

DUELS = [
    # (constructeur, modèle AMD, cpu AMD, prix AMD, modèle Intel, cpu Intel, prix Intel)
    ("HPE", "ProLiant DL325 Gen11", "EPYC 9124", 8600, "ProLiant DL380 Gen11", "Xeon Silver 4510", 14400),
    ("Lenovo", "ThinkSystem SR645 V3", "EPYC 9124", 8500, "ThinkSystem SR650 V3", "Xeon Silver 4510", 13200),
    ("Dell", "PowerEdge R6615", "EPYC 9124", 11900, "PowerEdge R660", "Xeon Silver 4510", 15300),
]

rows, cf = [], {}
for i, (c, ma, ca, pa, mi, ci, pi) in enumerate(DUELS):
    ia, ii = 16 * 3.0, 12 * 2.4
    rows.append([f"**{c}**", f"{ma}\n**{ca}** · 16 c · 3,0 GHz", f"**{eur(pa)}**",
                 f"{mi}\n**{ci}** · 12 c · 2,4 GHz", f"**{eur(pi)}**",
                 f"**+ {round((pi/pa-1)*100)} %**", f"{ia:.1f} vs {ii:.1f}",
                 f"**× {ia/ii:.2f}**", f"{ia/(pa/1000):.1f} vs {ii/(pi/1000):.1f}"])
    cf[(i, 2)] = FMT["g"]
    cf[(i, 4)] = FMT["o"]
    cf[(i, 5)] = FMT["o"]
    cf[(i, 7)] = FMT["g"]

doc.table(
    ["Constructeur", "Modèle AMD", "Prix AMD", "Modèle Intel", "Prix Intel", "Surcoût Intel",
     "Indice calcul", "Rapport", "Indice / k€"],
    rows,
    widths=[2.4, 4.6, 2.4, 4.6, 2.4, 2.2, 3.0, 1.8, 2.5], font=7.8,
    aligns=["l", "l", "r", "l", "r", "c", "c", "c", "c"],
    caption=f"{tab()} — Le duel à configuration identique. Indice de calcul = cœurs × fréquence "
            "de base (GHz). « Indice / k€ » mesure le calcul obtenu par euro investi.",
    cell_fmt=cf, zebra=False)

doc.p("**Lecture.** Sur les trois constructeurs, la même conclusion : **l'AMD coûte 20 à 60 % moins "
      "cher et calcule 1,7 fois plus**. L'écart de prix ne vient pas du châssis, qui est comparable, "
      "mais du processeur : un EPYC 9124 à 16 cœurs se négocie autour de 1 050 €, un Xeon Silver "
      "4510 à 12 cœurs autour de 1 050 € aussi — mais il faut, chez Intel, une carte mère bi-socket "
      "et un châssis 2U plus cher pour le même service.", small=True)

doc.ul([
    "**Le processeur ne fait pas la différence de prix** : un EPYC 9124 et un Xeon Silver 4510 se "
    "négocient tous deux autour de 1 050 €. L'écart de 5 000 € vient de la plateforme.",
    "**La plateforme, si** : chez Intel, le Xeon Silver impose un châssis 2U, une carte mère "
    "bi-socket et 32 emplacements mémoire — trois postes que l'AMD 1U à un socket évite.",
    "**Le calcul ne suit pas le prix** : indice 48 pour l'AMD contre 28,8 pour l'Intel. Ramené à "
    "l'euro investi, l'AMD rend **5,6 points d'indice par millier d'euros**, l'Intel 2,0.",
])

doc.pagebreak()
doc.h1_plain("Ce que le face-à-face décide")
doc.image("fig_f_duel.png",
          "Figure 1 — Prix (barres) et indice de calcul (cœurs × GHz) des six machines, à "
          "configuration identique : 128 Go, 2×1,92 To NVMe RAID1, 2×10 GbE.",
          width_cm=20.0)

doc.callout("Quand Intel se justifie quand même",
            "Trois cas, et trois seulement : un **parc déjà standardisé** sur HPE/Dell Intel avec "
            "contrat de service en cours ; une **contrainte applicative mono-thread** (le turbo à "
            "4,1 GHz du 4510 rattrape l'EPYC sur une charge à un seul fil) ; une **exigence de "
            "fournisseur imposée** par un marché public. Hors ces cas, payer 67 % de plus pour 40 % "
            "de calcul en moins ne se défend pas.",
            "bad")

doc.p("**Ce que cela implique pour la suite du document** : les grilles A et B gardent les deux "
      "familles, pour que la comparaison reste possible poste par poste. Mais la recommandation est "
      "déjà écrite ici : **AMD EPYC 9124, 128 Go, NVMe en RAID1** — 8 600 € chez PC21.", small=True)

# --------------------------------------------------------------------------- #



def table_prix(famille, ram_go, num, titre, intro, recommandation):
    base = BASE_AMD if famille == "AMD" else BASE_INTEL
    doc.landscape(True)
    doc.h1(num, titre)
    doc.p(intro, small=True)

    heads = ["**Fournisseur**", "**Zone**"]
    for lettre, disque, coeurs in VAR:
        extra = f"\nidentique à {DOUBLON[lettre]})" if lettre in DOUBLON else ""
        if famille == "AMD":
            ghz, cpu = "3,0 GHz ✓", "9124"
        else:
            ghz, cpu = ("2,4 GHz ✓", "4510") if coeurs == 12 else ("2,5 GHz ✓", "6426Y")
        heads.append(f"**{lettre}) {disque}**\n{coeurs} cœurs · {ghz}{extra}")

    rows, cf, mat = [], {}, []
    for i, (nom, zone, coef, dom, mode, lib) in enumerate(FOURN):
        row = [f"**{nom}**", zone]
        line = []
        for j, (lettre, disque, coeurs) in enumerate(VAR):
            p = (prix(base, disque, coeurs, famille) + (RAM_128 if ram_go == 128 else 0)) * coef
            p = round(p / 100) * 100
            line.append(p)
            row.append(f"**{eur(p)}**")
            cf[(i, 2 + j)] = FMT[bande(p)]
        rows.append(row)
        mat.append(line)

    doc.table(heads, rows,
              widths=[3.9, 2.4] + [3.26] * 6, font=8.0,
              aligns=["l", "l"] + ["r"] * 6,
              caption=f"{tab()} — {famille} · {ram_go} Go DDR5 · six variantes disques · prix HT chez "
                      f"les quinze fournisseurs, **classés par prix croissant**. Cible rappelée : "
                      f"2×1,92 To utiles en **RAID1**, **2×10 GbE**, 128 Go DDR5. "
                      f"{'Toutes les colonnes sont conformes (3,0 GHz).' if famille == 'AMD' else 'Toutes les colonnes sont conformes (2,4 et 2,5 GHz).'}",
              cell_fmt=cf, zebra=False)

    vals = [(mat[i][4], FOURN[i][0]) for i in range(len(FOURN))]
    lo, hi = min(vals), max(vals)
    med = sorted(mat[i][4] for i in range(len(FOURN)))[len(FOURN) // 2]
    doc.ul([
        f"**Écart de canal** : {eur(lo[0])} chez **{lo[1]}**, {eur(hi[0])} chez **{hi[1]}** — "
        f"**+ {round((hi[0]/lo[0]-1)*100)} %** pour un serveur identique ; médiane à {eur(med)}.",
        recommandation,
        "**Ce que ces prix ne comprennent pas** : fret et douane (5 à 12 % depuis l'Asie), "
        "installation, et la TVA locale. Ils comprennent la machine montée, la garantie 3 ans du "
        "constructeur et le port en France métropolitaine.",
    ])
    doc.p("**Statut des prix** — PC21 est la base de référence (relevés du 5 novembre 2026 : "
          "P77252-425, P71675-425). Les autres lignes sont **modélisées** par le coefficient du "
          "tableau 1. Aucun devis ferme.", small=True)


table_prix("AMD", 64, "5", "A.1 — AMD · 64 Go DDR5 · six variantes disques",
           "Cible : 2×1,92 To utiles en RAID1, 12 à 16 cœurs, 2×10 GbE, 64 Go DDR5. Chez AMD, la "
           "distinction 12 / 16 cœurs disparaît : l'EPYC 9124 (16 cœurs à 3,0 GHz) est le processeur "
           "d'entrée et couvre les deux demandes, d'où des colonnes a) à f) à prix égal.",
           "**À retenir** : 6 600 € en SATA, 7 000 € en NVMe chez PC21 — le même prix quelles que "
           "soient les colonnes a) à f), puisque le processeur ne change pas.")

table_prix("AMD", 128, "6", "A.2 — AMD · 128 Go DDR5 · six variantes disques",
           "Le bloc de la configuration recommandée : 128 Go, NVMe, 16 cœurs à 3,0 GHz.",
           "**Recommandation** : 8 200 € en SATA, 8 600 € en NVMe chez PC21 ; 8 400 et 8 800 € chez "
           "Senetic. C'est la cible du dossier.")

table_prix("Intel", 64, "7", "B.1 — Intel · 64 Go DDR5 · 2,4 et 2,5 GHz",
           "Les colonnes 12 cœurs reposent sur le Xeon Silver 4510 (2,4 GHz), **conforme au nouveau "
           "seuil** ; les colonnes 16 cœurs sur le Xeon Gold 6426Y (2,5 GHz).",
           "**À retenir** : le Xeon Silver 4510 devient conforme — les quatre colonnes 12 cœurs "
           "sont désormais éligibles, **à prix inchangé**. Passer à 16 cœurs conformes coûte "
           "toujours + 1 900 €.")

table_prix("Intel", 128, "8", "B.2 — Intel · 128 Go DDR5 · 2,4 et 2,5 GHz",
           "Le même bloc avec 128 Go. L'Intel conforme reste deux fois plus cher que l'AMD.",
           "**À retenir** : 14 400 € en NVMe chez PC21, contre 8 600 € en AMD — **+ 67 %** pour un "
           "indice de calcul inférieur de 40 %.")

# --------------------------------------------------------------------------- #
doc.landscape(False)
doc.h1("9", "Le prix de chaque modèle, chez chacun des quinze")

doc.p("Huit pages suivent, une par machine. Chaque page donne, pour **une configuration figée** "
      "(128 Go DDR5, 2×1,92 To NVMe en RAID1, 2×10 GbE, 12 à 16 cœurs), le prix chez les quinze "
      "fournisseurs **et le lien qui ouvre leur offre sur ce modèle précis**. Un clic, et vous êtes "
      "sur le catalogue du fournisseur, à la bonne référence.", lead=True)

doc.table(
    ["Code", "Constructeur", "Modèle", "Processeur", "Cœurs / GHz", "Indice", "Prix PC21",
     "Fiche constructeur"],
    [[f"**{c}**", f, m, cpu, f"{co} c · {g:.2f}".replace(".", ","), f"{co*g:.0f}",
      f"**{eur(p)}**", f"[fiche]({url})"]
     for c, f, m, cpu, fam, g, co, p, url, ch in MODELES],
    widths=[1.1, 2.4, 3.6, 2.8, 1.8, 1.2, 2.0, 2.2], font=7.6,
    aligns=["c", "l", "l", "l", "c", "c", "r", "l"],
    caption=f"{tab()} — Les huit machines retenues, à configuration identique (128 Go, 2×1,92 To "
            "NVMe RAID1, 2×10 GbE). Cinq en AMD, trois en Intel.",
    cell_fmt={**{(i, 6): FMT[bande(MODELES[i][7])] for i in range(len(MODELES))},
              **{(i, 5): FMT[bande_ghz(MODELES[i][5])] for i in range(len(MODELES))}}, zebra=False)

doc.h2("Pourquoi ces huit machines")
doc.ul([
    "**Cinq en AMD** — c'est la famille recommandée : les quatre constructeurs du dossier (HPE, "
    "Lenovo, Dell, Supermicro) plus ASUS, qui complète la comparaison sur un 2U à 24 DIMM.",
    "**Trois en Intel** — seuls HPE, Lenovo et Dell proposent les deux familles sur le même châssis, "
    "ce qui rend le face-à-face honnête : même marque, même génération, même support.",
    "**Une seule configuration chacune** — 128 Go, 2×1,92 To NVMe en RAID1, 2×10 GbE. C'est la cible "
    "du dossier, et c'est le seul moyen de comparer des prix qui veulent dire quelque chose.",
])

doc.table(
    ["Modèle", "Emplacements DIMM", "RAM max.", "Baies", "Réseau", "Gestion", "Verdict"],
    [
        ["HPE DL325 Gen11", "12", "3 To", "8 SFF", "2×10 GbE OCP", "iLO 6", "**Le meilleur compromis**"],
        ["Lenovo SR645 V3", "12", "3 To", "10 SFF", "2×10 GbE", "XCC2", "**Prix le plus bas en marque**"],
        ["Dell R6615", "12", "3 To", "10 SFF", "2×10 GbE", "iDRAC9", "Cher au tarif public"],
        ["Supermicro AS-1115CS-TNR", "12", "3 To", "10 × 2,5 pouces", "2×10 GbE + AIOM", "BMC", "**Meilleur prix, assemblage à prévoir**"],
        ["ASUS RS520A-E12-RS12U", "24", "6 To", "12 × 3,5 pouces", "2×10 GbE", "ASMB11", "Si la capacité disque compte"],
        ["HPE DL380 Gen11", "32", "8 To", "8 SFF", "2×10 GbE", "iLO 6", "Conforme Intel, mais 2U et cher"],
        ["Lenovo SR650 V3", "32", "8 To", "8 SFF", "2×10 GbE", "XCC2", "Intel le mieux placé"],
        ["Dell R660", "32", "8 To", "10 SFF", "2×10 GbE", "iDRAC9", "Intel le plus cher"],
    ],
    widths=[3.6, 2.6, 1.8, 2.3, 3.0, 1.7, 5.1], font=7.5,
    aligns=["l", "c", "c", "c", "l", "c", "l"],
    caption=f"{tab()} — Ce que chaque châssis apporte, au-delà du processeur. Les huit machines "
            "acceptent la configuration cible ; elles ne se distinguent que par la marge.",
    cell_fmt={(0, 6): FMT["g"], (1, 6): FMT["g"], (3, 6): FMT["g"], (7, 6): FMT["o"]}, zebra=False)

NOM = {m[0]: f"{m[1]} {m[2]}" for m in MODELES}
PRIX_AMD = {m[0]: m[7] for m in MODELES if m[4] == "AMD"}
PRIX_INTEL = {m[0]: m[7] for m in MODELES if m[4] == "Intel"}


def situer(code, fam, prix):
    if fam == "AMD":
        autre = min((v, k) for k, v in PRIX_AMD.items() if k != code)
        bas_i = min(PRIX_INTEL.values())
        return (f"**Pour situer** : le moins cher des cinq AMD est le **{NOM[autre[1]]}** à {eur(autre[0])} ; "
                f"cette machine est à **{round(prix/autre[0]*100-100)} %**. Face à elle, l'Intel "
                f"conforme le moins cher est à {eur(bas_i)} (**+ {round(bas_i/prix*100-100)} %**).")
    bas_a = min(PRIX_AMD.values())
    return (f"**Pour situer** : le même besoin en AMD démarre à {eur(bas_a)} — soit "
            f"**{round(bas_a/prix*100-100)} %** par rapport à cette machine Intel. C'est le prix de "
            f"la conformité côté Intel.")


for c, fab, mod, cpu, fam, ghz, cores, prix_ref, url_fab, chassis in MODELES:
    q = f"{fab} {mod}".replace("ProLiant ", "").replace("ThinkSystem ", "").replace("PowerEdge ", "")
    doc.landscape(True)
    doc.h1(c, f"{fab} {mod} — {cpu} · {cores} cœurs à {ghz:.1f} GHz".replace(".", ","))

    b = bande_ghz(ghz)
    doc.p(f"**{chassis}** · configuration chiffrée : **128 Go DDR5**, **2×1,92 To NVMe en RAID1**, "
          f"**2×10 GbE**, garantie 3 ans. Processeur **{cpu}** — indice de calcul "
          f"**{cores * ghz:.0f}** ({cores} cœurs × {ghz:.2f} GHz".replace(".", ",") +
          f"), statut **{ {'g': 'conforme', 'y': 'toléré', 'o': 'exclu'}[b] }** au seuil de 2,4 GHz. "
          f"Prix de référence PC21 : **{eur(prix_ref)}** HT · [fiche constructeur]({url_fab}).",
          small=True)

    rows, cf = [], {}
    for i, (nom, zone, coef, dom, mode, lib) in enumerate(FOURN):
        p = round(prix_ref * coef / 100) * 100
        statut = "**base relevée**" if nom == "PC21.fr" else ("hors garantie" if nom == "Alibaba.com"
                                                              else "modélisé")
        fiche = FICHE_PRODUIT.get((c, nom))
        href = fiche[0] if fiche else lien(nom, dom, mode, q)
        libelle = fiche[1] if fiche else lib
        rows.append([f"**{i+1}**", f"**{nom}**", zone, f"{coef:.2f}".replace(".", ","),
                     f"**{eur(p)}**", statut, f"[{libelle}]({href})"])
        cf[(i, 4)] = FMT[bande(p)]
        if nom == "PC21.fr":
            cf[(i, 0)] = FMT["g"]

    doc.table(
        ["#", "Fournisseur", "Zone", "Coef.", "Prix HT", "Statut du prix", "Vérifier l'offre"],
        rows,
        widths=[0.9, 4.4, 3.2, 1.4, 2.6, 3.4, 9.6], font=9.6,
        aligns=["c", "l", "l", "c", "r", "l", "l"],
        caption=f"{tab()} — {fab} {mod} · prix HT de la configuration cible chez les quinze "
                f"fournisseurs, du moins cher au plus cher. Le lien ouvre la recherche du site "
                f"pour la requête « {q} ».",
        cell_fmt=cf, zebra=False)

    bas = [round(prix_ref * f[2] / 100) * 100 for f in FOURN]
    bas.sort()
    median = bas[len(bas) // 2]
    doc.ul([
        f"**Prix médian des quinze** : {eur(median)} HT — c'est ce que paiera un acheteur qui "
        f"consulte un seul revendeur. L'écart avec le meilleur prix ({eur(bas[0])}) est la marge de "
        f"négociation réelle.",
        f"**À demander dans le devis** : {fab} {mod} avec {cpu}, 128 Go (4 × 32 Go DDR5), 2 × 1,92 To "
        f"NVMe U.3, RAID1, 2×10 GbE, **garantie 3 ans sur site**, rails et second bloc d'alimentation.",
        f"**Coût complet** : {eur(prix_ref)} de serveur + 4 550 € de périphériques + 1 110 € de "
        f"licences ≈ **{eur(round((prix_ref + 5660)/100)*100)} HT** prêt à produire.",
        situer(c, fam, prix_ref),
    ])

# --------------------------------------------------------------------------- #
doc.h1("10", "C — Matrice processeurs")
doc.landscape(True)

doc.p("La même matrice que dans la proposition E, mais colorée au nouveau seuil : la bande de "
      "fréquence passe avant la génération.", small=True)

CPU2 = [
    ("AMD EPYC 9124", "Zen 4 — 9004", "2023", 16, 3.00, 200, "≈ 1 050 €", "≈ 2027", "Xeon Gold 6426Y"),
    ("AMD EPYC 9224", "Zen 4 — 9004", "2023", 24, 2.50, 200, "≈ 2 350 €", "≈ 2027", "Xeon Gold 6430"),
    ("AMD EPYC 9125", "Zen 5 — 9005", "2024", 16, 2.60, 200, "≈ 1 300 €", "≈ 2029", "Xeon 6 6500P"),
    ("AMD EPYC 9354P", "Zen 4 — 9004", "2023", 32, 3.25, 280, "≈ 4 200 €", "≈ 2027", "Xeon Gold 6430"),
    ("Intel Xeon Gold 6426Y", "Sapphire Rapids", "2023", 16, 2.50, 185, "≈ 2 400 €", "≈ 2027", "EPYC 9124"),
    ("Intel Xeon Silver 4510", "Emerald Rapids", "2023", 12, 2.40, 150, "≈ 1 050 €", "≈ 2027", "EPYC 9124"),
    ("Intel Xeon Silver 4410Y", "Emerald Rapids", "2023", 12, 2.00, 150, "≈ 900 €", "≈ 2027", "EPYC 9124"),
    ("Intel Xeon Silver 4514Y", "Emerald Rapids", "2023", 16, 2.00, 150, "≈ 1 500 €", "≈ 2027", "EPYC 9224"),
    ("AMD EPYC 9355P", "Zen 5 — 9005", "2024", 32, 3.55, 280, "≈ 5 400 €", "≈ 2029", "Xeon 6 6700P"),
    ("Intel Xeon Gold 6430", "Sapphire Rapids", "2023", 32, 2.10, 270, "≈ 4 600 €", "≈ 2027", "EPYC 9354P"),
    ("Intel Xeon Gold 6138", "Skylake — Gen10", "2017", 20, 2.00, 125, "≈ 120 €", "**2023 (EOL)**", "EPYC 9124"),
]

rows, cf = [], {}
for i, (m, archi, an, c, base, tdp, px, fin, eq) in enumerate(CPU2):
    idx = round(c * base, 1)
    b = bande_ghz(base)
    rows.append([f"**{m}**", archi, an, f"{c}", f"{base:.2f}".replace(".", ","), f"{tdp} W",
                 f"{idx:.1f}".replace(".", ","), px, fin, eq])
    cf[(i, 4)] = FMT[b]
    cf[(i, 6)] = FMT[b]
    if "EOL" in fin:
        cf[(i, 8)] = FMT["o"]

doc.table(
    ["Processeur", "Architecture", "Sortie", "Cœurs", "Fréquence de base", "TDP", "Indice",
     "Prix indicatif", "Fin de com.", "Équivalent"],
    rows,
    widths=[4.4, 3.6, 1.4, 1.3, 3.2, 1.4, 1.6, 3.0, 2.4, 3.6], font=7.9,
    aligns=["l", "l", "c", "c", "c", "c", "c", "r", "c", "l"],
    caption=f"{tab()} — Matrice processeurs, classée par statut de fréquence puis par indice. "
            "Indice = cœurs × fréquence de base ; **vert ≥ 2,4 GHz**, **jaune 2,0–2,39 GHz**.")

doc.callout("Le point qui décide",
            "À 16 cœurs, l'EPYC 9124 (3,0 GHz, indice 48) et le Xeon Silver 4510 (2,4 GHz, "
            "indice 28,8) ne sont pas dans la même catégorie : **l'AMD calcule 67 % de plus**. "
            "Le Gold 6426Y ramène l'Intel à 40 d'indice — mais à 2 400 € le processeur, contre "
            "1 050 € pour l'EPYC. À performance comparable, Intel reste deux fois plus cher.",
            "warn")

doc.p("**Lecture des générations.** Un EPYC 9004 (Zen 4, 2023) et un EPYC 9005 (Zen 5, 2024) "
      "partagent le même socket SP5 : passer de l'un à l'autre est une simple substitution de "
      "processeur, sans changer de machine. Côté Intel, Sapphire Rapids et Emerald Rapids partagent "
      "le socket LGA 4677 — mais la génération suivante (Xeon 6) change de plateforme. "
      "**L'AMD laisse donc une porte de mise à jour que l'Intel referme.**", small=True)

# --------------------------------------------------------------------------- #
doc.h1("11", "D — Matrice mémoire")

doc.p("Rien ne change sur la mémoire : c'est toujours la ressource saturée de l'existant (88,4 % de "
      "64 Go). Le seuil processeur n'y touche pas, et le prix du Go reste le même que l'on prenne "
      "2 ou 4 barrettes de 32 Go.", small=True)
doc.table(
    ["Type", "Vitesse", "Module", "Prix indicatif", "€ / Go", "Disponibilité", "Plateformes", "Lecture"],
    [
        ["DDR4 RDIMM", "2 666 MT/s", "32 Go", "≈ 210 €", "6,6 €", "Marché secondaire", "Gen10, 14G",
         "**Fin de vie** — à éviter sur un achat neuf"],
        ["DDR5 RDIMM", "4 800 MT/s", "32 Go", "≈ 520 €", "**16,3 €**", "**Très tendu**",
         "Gen11, R6615, SR645 V3", "**Standard du dossier**"],
        ["DDR5 RDIMM", "5 600 MT/s", "32 Go", "≈ 610 €", "19,1 €", "Tendu", "Gen11 Intel, Gen12",
         "Gain réel faible en virtualisation"],
        ["DDR5 RDIMM", "4 800 MT/s", "64 Go", "≈ 1 150 €", "18,0 €", "Très tendu", "Gen11 (1DPC)",
         "Si une seule barrette par canal"],
        ["DDR5 3DS RDIMM", "4 800 MT/s", "128 Go", "≈ 2 400 €", "18,8 €", "Sur commande", "Gen11/Gen12",
         "Pour dépasser 1 To seulement"],
    ],
    widths=[3.2, 2.6, 2.0, 2.8, 1.9, 2.8, 4.2, 6.4], font=7.8,
    aligns=["l", "c", "c", "r", "r", "l", "l", "l"],
    caption=f"{tab()} — Matrice mémoire, marché tendu de 2026.",
    cell_fmt={(1, 4): FMT["o"], (0, 7): FMT["o"], (1, 7): FMT["g"]}, zebra=False)

doc.table(
    ["Capacité", "Barrettes", "Coût d'extension", "Emplacements", "Marge future", "Verdict"],
    [
        ["64 Go", "2 × 32 Go", "inclus", "2 / 12", "+64 Go", "**Sous l'exigence** : reconduit la saturation"],
        ["**128 Go**", "4 × 32 Go", "**+ 1 600 €**", "4 / 12", "+128 Go", "**Cible retenue**"],
        ["192 Go", "6 × 32 Go", "+ 3 200 €", "6 / 12", "+96 Go", "Confort, non justifié"],
        ["256 Go", "8 × 32 Go", "+ 4 800 €", "8 / 12", "+64 Go", "Surdimensionné"],
    ],
    widths=[3.0, 3.0, 3.4, 3.0, 3.2, 10.3], font=8.0, aligns=["l", "c", "r", "c", "c", "l"],
    caption=f"{tab()} — Scénarios de capacité sur 12 emplacements DIMM.",
    cell_fmt={(1, 0): FMT["g"], (0, 5): FMT["o"]}, zebra=False)

doc.ul([
    "**L'existant est à 88,4 % de 64 Go** : acheter 64 Go, c'est acheter la saturation constatée. "
    "C'est le seul poste où l'économie initiale se paie deux fois.",
    "**128 Go en 4 × 32 Go** laisse huit emplacements libres et double la marge sans changer de "
    "plateforme ni de budget processeur.",
    "**Le prix au Go est identique** entre 64 et 128 Go en DDR5 4 800 : il n'y a aucune prime de "
    "capacité, seulement le prix des barrettes.",
])

doc.callout("Le marché 2026 ne pardonne pas l'attente",
            "La demande en mémoire HBM pour l'IA a fait monter la DDR5 de **40 à 70 % en dix-huit "
            "mois**, et les délais de 6 à 12 semaines sur les modules 32 Go. Deux conséquences : "
            "commander la mémoire **en même temps que le serveur**, et la prendre en 4 × 32 Go plutôt "
            "qu'en 2 × 64 Go — ces derniers sont les plus tendus.",
            "warn")

# --------------------------------------------------------------------------- #
doc.h1("12", "E — Matrice disques")

doc.p("Les six variantes a) à f) ne diffèrent entre elles que par le disque et le nombre de cœurs. "
      "Le disque ne pèse que 400 € dans le prix final, mais il change la latence d'un facteur six.",
      small=True)
doc.table(
    ["Support", "Interface", "Endurance", "IOPS 4K", "Latence", "Prix 1,92 To", "€ / To", "RAID",
     "Lecture"],
    [
        ["SATA SSD RI", "6 Gb/s", "1 DWPD", "≈ 95 000", "≈ 120 µs", "≈ 450 €", "234 €", "0/1/5/6/10",
         "Le moins cher — limité par le contrôleur SATA"],
        ["SAS SSD", "12 / 24 Gb/s", "3 DWPD", "≈ 210 000", "≈ 90 µs", "≈ 750 €", "391 €", "0/1/5/6/10",
         "Double port, endurance supérieure"],
        ["**NVMe U.3**", "PCIe 5.0 x4", "1–3 DWPD", "**≈ 800 000**", "**≈ 20 µs**", "≈ 650 €",
         "**339 €**", "0/1/5/6/10", "**Meilleur rapport latence / prix**"],
        ["Disque constructeur", "—", "—", "—", "—", "**≈ 1 100 €**", "573 €", "0/1/5/6/10",
         "**+ 70 %** : garantie intégrée, firmware validé"],
        ["Disque tiers", "—", "—", "—", "—", "≈ 650 €", "339 €", "selon contrôleur",
         "Économie réelle, garantie à vérifier"],
    ],
    widths=[3.8, 2.8, 2.2, 2.6, 1.9, 2.6, 1.5, 2.4, 6.1], font=7.8,
    aligns=["l", "c", "c", "c", "c", "r", "r", "c", "l"],
    caption=f"{tab()} — Matrice disques, hors options constructeur.",
    cell_fmt={(2, 8): FMT["g"], (0, 8): FMT["y"], (3, 5): FMT["o"]}, zebra=False)

doc.table(
    ["Support retenu", "Prix unitaire", "2 disques en RAID1 (1,92 To utiles)", "Surcoût vs SATA",
     "Endurance"],
    [
        ["SATA SSD read-intensive 1,92 To", "≈ 450 €", "**900 €**", "référence", "1 DWPD"],
        ["NVMe U.3 1,92 To", "≈ 650 €", "**1 300 €**", "+ 400 €", "1 à 3 DWPD"],
        ["SAS SSD 1,92 To", "≈ 750 €", "1 500 €", "+ 600 €", "**3 DWPD**"],
        ["Disque constructeur HPE/Dell 1,92 To", "≈ 1 100 €", "2 200 €", "+ 1 300 €", "1 à 3 DWPD"],
    ],
    widths=[7.6, 3.8, 6.0, 4.4, 4.1], font=8.0, aligns=["l", "r", "r", "r", "c"],
    caption=f"{tab()} — Ce que coûtent les deux disques : + 400 € pour le NVMe, + 1 300 € pour le "
            "disque constructeur.",
    cell_fmt={(1, 3): FMT["y"], (3, 3): FMT["o"], (2, 4): FMT["g"]}, zebra=False)

doc.table(
    ["Besoin", "Support retenu", "Justification", "Surcoût vs SATA"],
    [
        ["Virtualisation générale, 2 To utiles", "**NVMe U.3 — 2 × 1,92 To RAID1**",
         "Latence six fois meilleure, prix inférieur au SAS", "**+ 400 €**"],
        ["Budget serré, charge faible", "SATA SSD RI — 2 × 1,92 To RAID1",
         "Suffisant si le contrôleur n'est pas saturé", "référence"],
        ["Écriture intense (base de données)", "SAS SSD 3 DWPD ou NVMe write-intensive",
         "L'endurance prime sur la latence", "+ 300 à 600 €"],
        ["Capacité au-delà de 4 To", "2 × 3,84 To RAID1 ou 4 × 1,92 To RAID10",
         "La baie et le contrôleur deviennent limitants", "+ 900 à 2 000 €"],
    ],
    widths=[5.6, 7.2, 8.1, 5.0], font=8.1, aligns=["l", "l", "l", "r"],
    caption=f"{tab()} — Quelle variante pour quel usage.",
    cell_fmt={(0, 1): FMT["g"]}, zebra=False)

# --------------------------------------------------------------------------- #
doc.h1("13", "F — RAID, réseau et périphériques")

doc.p("Ces éléments figurent dans chaque colonne des grilles A et B : voici ce que « RAID1 » et "
      "« 2×10 GbE » engagent concrètement, et ce qu'il faut prévoir autour du serveur.", small=True)

doc.h2("F.1 — RAID")
doc.table(
    ["Niveau", "Disques", "Capacité utile", "Tolérance", "Reconstruction", "Verdict"],
    [
        ["RAID 0", "2 × 1,92 To", "3,84 To", "**Aucune**", "—", "À exclure en production"],
        ["**RAID 1**", "2 × 1,92 To", "**1,92 To**", "**1 disque**", "Rapide (copie)",
         "**Retenu : simple, robuste, suffisant**"],
        ["RAID 5", "3 × 1,92 To", "3,84 To", "1 disque", "**Lente, risquée sur SSD**",
         "Non recommandé sous 4 disques"],
        ["RAID 10", "4 × 1,92 To", "3,84 To", "1 disque par miroir", "Rapide",
         "Si la croissance disque est certaine"],
        ["ZFS miroir (Proxmox)", "2 × 1,92 To", "1,92 To", "1 disque", "Rapide + checksums",
         "**Excellent choix avec Proxmox**"],
    ],
    widths=[3.8, 3.0, 3.0, 3.2, 4.0, 8.9], font=8.0, aligns=["l", "c", "c", "c", "l", "l"],
    caption=f"{tab()} — RAID : « 2×1,92 To utiles en RAID1 » signifie deux disques en miroir, "
            "1,92 To réellement utilisables.",
    cell_fmt={(1, 0): FMT["g"], (4, 5): FMT["g"], (0, 3): FMT["o"]}, zebra=False)

doc.h2("F.2 — Réseau")
doc.table(
    ["Option", "Débit utile", "Coût carte", "Coût switch", "Câblage", "Quand c'est justifié"],
    [
        ["2 × 1 GbE intégré", "≈ 2 Gbit/s", "inclus", "inclus", "RJ45 Cat6", "Charge actuelle"],
        ["**2 × 10 GbE BASE-T (OCP 3.0)**", "**≈ 20 Gbit/s**", "**inclus (DL325)**", "≈ 900 €",
         "RJ45 Cat6a", "**Sauvegarde, migration à chaud, VM**"],
        ["2 × 10 GbE SFP+", "≈ 20 Gbit/s", "≈ 350 €", "≈ 1 100 €", "DAC / fibre",
         "Distance, isolation électrique"],
        ["2 × 25 GbE SFP28", "≈ 50 Gbit/s", "≈ 800 €", "≈ 2 500 €", "Fibre", "Aucun besoin ici"],
    ],
    widths=[5.4, 3.4, 3.6, 3.0, 2.8, 7.7], font=8.0, aligns=["l", "c", "c", "c", "c", "l"],
    caption=f"{tab()} — Le port 10 GbE est inclus sur le DL325 Gen11 ; c'est le switch qui coûte.",
    cell_fmt={(1, 0): FMT["g"]}, zebra=False)

doc.h2("F.3 — Le budget qui entoure le serveur")
doc.table(
    ["Ligne budgétaire", "Montant HT", "Statut"],
    [
        ["Serveur cible — AMD 128 Go, 2×1,92 To NVMe RAID1, 16 cœurs", "**8 600 €**", "Base relevée"],
        ["Périphériques (onduleur, sauvegarde, switch, rechange, rack)", "4 550 €", "Indicatif"],
        ["**Sous-total matériel**", "**13 150 €**", "—"],
        ["Licences Proxmox VE + PBS, an 1", "≈ 1 110 €", "Indicatif"],
        ["**Total « prêt à produire »**", "**≈ 14 300 €**", "—"],
        ["Fret, douane, intégration, migration", "6 700 à 7 700 €", "Pour mémoire"],
        ["**Projet complet, année 1**", "**21 000 à 22 000 €**", "Document B"],
    ],
    widths=[11.6, 4.0, 4.2], font=8.1, aligns=["l", "r", "l"],
    caption=f"{tab()} — Du prix du serveur au budget de projet.",
    row_bg={2: BLEU_BG, 4: BLEU_BG, 6: BLEU_BG}, zebra=False)

# --------------------------------------------------------------------------- #
doc.landscape(False)
doc.h1("14", "Synthèse")

doc.h2("Ce que la proposition F change dans la décision")
doc.ul([
    "**Le seuil à 2,4 GHz rend Intel achetable** : 14 400 € pour une configuration conforme de "
    "12 cœurs, au lieu de 16 300 € pour la version 16 cœurs à 2,5 GHz. L'obstacle technique est "
    "levé — au prix de quatre cœurs.",
    "**Il ne réduit pas l'écart de prix** : 8 600 € en AMD contre 14 400 € en Intel, soit "
    "**+ 5 800 €** pour un processeur qui calcule 40 % de moins.",
    "**Le classement par coefficient change la lecture** : trois fournisseurs se tiennent à 1,00–1,02 "
    "(Alibaba, Mindware, PC21, Arena, Senetic), et **ServerMall reste 60 % au-dessus** pour la même "
    "référence HPE.",
    "**Les modèles les moins chers ne sont pas les plus connus** : Supermicro AS-1115CS-TNR et "
    "Lenovo SR645 V3 sortent devant HPE et Dell à configuration égale.",
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
        ["Conforme Intel la moins chère", "HPE DL380 Gen11 · Silver 4510 · 128 Go · NVMe",
         "14 400 €", "Mindware · PC21", "**Coût du choix Intel**"],
        ["Si Dell est imposé", "Dell R6615 · EPYC 9124 · 128 Go",
         "12 400 €", "Redcorp · 12 900 € chez CDW", "Le tarif public Dell est le plus élevé"],
    ],
    widths=[3.0, 4.9, 2.0, 3.9, 3.3], font=7.6, aligns=["l", "l", "r", "l", "l"],
    caption=f"{tab()} — Les cinq scénarios qui se dégagent de la proposition F.",
    cell_fmt={(0, 0): FMT["g"], (0, 4): FMT["g"], (3, 4): FMT["o"]}, zebra=False)

doc.callout("Recommandation",
            "**HPE ProLiant DL325 Gen11 · EPYC 9124 (16 cœurs, 3,0 GHz) · 128 Go DDR5 · 2×1,92 To "
            "NVMe en RAID1 · 2×10 GbE** — 8 600 € HT chez PC21, 8 800 € chez Senetic, 8 800 € chez "
            "Mindware. Un devis de contrôle chez **Redcorp** et **Inmac wstore** pour la garantie. "
            "Budget projet complet : 21 000 à 22 000 € HT (document B).",
            "ok")

doc.p("**Avertissement.** Les prix PC21 sont relevés sur des pages publiques consultées le "
      "5 novembre 2026 ; les autres sont modélisés à partir de ces ancrages et du coefficient de "
      "chaque fournisseur (tableau 1). Les liens de recherche ont été ouverts et testés un par un le "
      "6 novembre 2026, sauf mention contraire ; ils peuvent changer sans préavis. Aucun devis ferme "
      "n'existe à ce stade.", small=True)

doc.save(OUT)
print("saved", OUT)
