# -*- coding: utf-8 -*-
"""Trois fiches direction — HPE ProLiant DL325, DL320 et DL380 Gen11.
Six processeurs du relevé, configuration détaillée, tarifs et liens directs
PC21.fr, Senetic et ServerMall. Une fiche par machine, 6 à 8 pages."""
import os
from urllib.parse import quote
from render import Doc
import charts

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables")

VERT_BG, VERT_TX = "E3F0DC", "1E6B2F"
JAUN_BG, JAUN_TX = "FBF3D0", "8A6D00"
ORAN_BG, ORAN_TX = "FBE0CE", "B4500F"
ROUG_BG, ROUG_TX = "F8D7DA", "8B1A1A"
GRIS_BG, GRIS_TX = "F1F1F1", "777777"
BLEU_BG = "EAF0F7"


def F(bg=None, tx=None, b=False, i=False):
    return {"bg": bg, "color": tx, "b": b, "i": i}


FMT = {"g": F(VERT_BG, VERT_TX, True), "y": F(JAUN_BG, JAUN_TX, True),
       "o": F(ORAN_BG, ORAN_TX, True), "n": F(GRIS_BG, GRIS_TX, b=False),
       "x": F(ROUG_BG, ROUG_TX, True), "p": F()}


def eur(n):
    return f"{round(n):,}".replace(",", " ") + " €"


def eur100(n):
    """Arrondi aux cent euros — pour la prose, les tableaux gardent le chiffre exact."""
    return eur(int(round(n / 100.0)) * 100)


def dec(x, n=2):
    return f"{x:.{n}f}".replace(".", ",")


def bande(p):
    if p <= 9700:
        return "g"
    if p <= 12500:
        return "y"
    return "o"


# --------------------------------------------------------------------------- #
# Les six processeurs du relevé — prix unitaires relevés au configurateur ServerMall
# (clé, nom court, famille, archi, socket, cœurs, threads, base, turbo, tdp,
#  année, fin, prix pièce)
CPU = {
    "4510": ("Xeon Silver 4510", "Intel", "Emerald Rapids", "LGA 4677", 12, 24, 2.40, 4.10,
             150, "2023", "≈ 2027", 756),
    "4410Y": ("Xeon Silver 4410Y", "Intel", "Emerald Rapids", "LGA 4677", 12, 24, 2.00, 3.90,
              150, "2023", "≈ 2027", 655),
    "6426Y": ("Xeon Gold 6426Y", "Intel", "Sapphire Rapids", "LGA 4677", 16, 32, 2.50, 4.10,
              185, "2023", "≈ 2027", 2160),
    "9124": ("EPYC 9124", "AMD", "Zen 4 — 9004", "SP5", 16, 32, 3.00, 3.70,
             200, "2023", "≈ 2027", 1046),
    "9125": ("EPYC 9125", "AMD", "Zen 5 — 9005", "SP5", 16, 32, 2.60, 4.10,
             200, "2024", "≈ 2029", 1300),
    "9224": ("EPYC 9224", "AMD", "Zen 4 — 9004", "SP5", 24, 48, 2.50, 3.70,
             200, "2023", "≈ 2027", 1526),
}

# composants communs au configurateur ServerMall (prix unitaires HT relevés)
RAM_32 = 1620          # 32 Go DDR5-4800 RDIMM
RAM_16 = 716
SSD = 1185             # 1,92 To SSD SATA 2,5" + caddy
NIC10 = 220            # 2 × 10 GbE BASE-T
PSU2 = 264             # 2 × 800 W
PSU1 = {"H": 119, "I": 119, "J": 132}
COMMUN = 4 * RAM_32 - RAM_16 + 2 * SSD + NIC10   # 8 354 €

MACHINES = [
    dict(
        code="H", slug="DL325", model="ProLiant DL325 Gen11",
        title="HPE ProLiant DL325 Gen11",
        base_sm=4482, base_cpu=1046,            # base avec EPYC 9124
        order=["9124", "9125", "9224", "4510", "4410Y", "6426Y"],
        compat=["9124", "9125", "9224"], socket="SP5",
        refus="Aucun Xeon Scalable : le DL325 est un châssis **SP5**, les Xeon du relevé "
              "sont en **LGA 4677** — les deux sockets sont physiquement incompatibles",
        specs=("1U · **1 socket** SP5 (EPYC 9004 et 9005) · **12 DIMM** DDR5-4800/6000, "
               "3 To max · 8 baies SFF (ou 4 LFF + 10 SFF) · **2 × 10 GbE** OCP 3.0 · "
               "PCIe 5.0 · **iLO 6**"),
        spec_rows=[
            ("Format", "Rack **1U**, profondeur 60 cm", "Rackable, conforme à la cible"),
            ("Socket", "**1 socket** SP5 — EPYC 9004 et 9005", "Les trois EPYC se montent ; les Xeon, non"),
            ("Mémoire", "**12 DIMM** DDR5-4800/6000 · 3 To max", "128 Go sur 4 barrettes : 8 emplacements libres"),
            ("Stockage", "8 baies SFF, ou 4 LFF + 10 SFF", "Deux disques en RAID1 : le minimum requis"),
            ("Réseau", "Emplacement OCP 3.0 · 4 × 1 GbE de série", "La carte 2 × 10 GbE est ajoutée (+ 220 €)"),
            ("Gestion", "**iLO 6** · Silicon Root of Trust", "Console distante incluse, aucune licence à ajouter"),
        ],
        figure="fig_h_dl325.png",
        hpe="https://www.hpe.com/fr/fr/products/compute/proliant/dl325-gen11.html",
        buy=("https://buy.hpe.com/fr/fr/compute/rack-servers/proliant-dl300-servers/"
             "proliant-dl325-server/hpe-proliant-dl325-gen11/p/1014689141"),
        sm="https://servermall.com/sets/hpe-proliant-dl325-gen11-server/",
        fiche={"9124": ("https://www.pc21.fr/fiche/p77252-425-hpe-proliant-dl325-gen11-9124-3-0ghz-"
                        "16c-64gb-r-8sff-mr408i-o-i5675189.html", "fiche P77252-425")},
        reco_cpu="9124",
        justif="16 cœurs à 3,0 GHz, **indice 48** : le meilleur calcul disponible à ce prix",
        verdict=("**EPYC 9124** — 8 600 € HT chez PC21, 8 800 € chez Senetic, 13 000 € au "
                 "configurateur ServerMall."),
        candide=("Le DL325 est la seule des trois machines qui reçoit un EPYC : c'est aussi la "
                 "moins chère et la plus performante du trio. Le seul argument contre lui est "
                 "la densité mémoire — 12 emplacements contre 32 sur le DL380."),
        reco=("**HPE ProLiant DL325 Gen11 · EPYC 9124 (16 cœurs, 3,0 GHz, indice 48) · "
              "128 Go DDR5 · 2 × 1,92 To SSD en RAID1 · 2 × 10 GbE** — 8 600 € HT chez PC21. "
              "Si la densité de machines virtuelles devient le critère, le même châssis en "
              "**EPYC 9224** (24 cœurs, indice 60) coûte 8 900 € chez PC21."),
    ),
    dict(
        code="I", slug="DL320", model="ProLiant DL320 Gen11",
        title="HPE ProLiant DL320 Gen11",
        base_sm=4946, base_cpu=479,             # base avec Xeon Bronze 3408U
        order=["4510", "4410Y", "6426Y", "9124", "9125", "9224"],
        compat=["4510", "4410Y", "6426Y"], socket="LGA 4677",
        refus="Aucun EPYC : le DL320 est un châssis **LGA 4677** (Xeon Scalable 4e et "
              "5e générations), l'EPYC 9004/9005 est en **SP5** — incompatible",
        specs=("1U · **1 socket** LGA 4677 (Xeon Scalable 4e et 5e générations, jusqu'à "
               "60 cœurs) · **16 DIMM** DDR5, 2 To max · 4 LFF ou 8 SFF, EDSFF · PCIe 5.0 · "
               "**iLO 6** · jusqu'à 4 GPU simple largeur"),
        spec_rows=[
            ("Format", "Rack **1U**, jusqu'à 4 GPU simple largeur", "Rackable, conforme à la cible"),
            ("Socket", "**1 socket** LGA 4677 — Xeon Scalable 4e et 5e gén., jusqu'à 60 cœurs",
             "Les trois Xeon se montent ; les EPYC, non"),
            ("Mémoire", "**16 DIMM** DDR5 · 2 To max", "128 Go sur 4 barrettes : 12 emplacements libres"),
            ("Stockage", "4 LFF ou 8 SFF, EDSFF", "Deux disques en RAID1 : le minimum requis"),
            ("Réseau", "4 × 1 GbE de série · 2 × 10 GbE en option", "La carte 2 × 10 GbE est ajoutée (+ 220 €)"),
            ("Gestion", "**iLO 6** · Compute Ops Management", "Console distante incluse"),
        ],
        figure="fig_h_dl320.png",
        hpe="https://www.hpe.com/fr/fr/products/compute/proliant/dl320-gen11.html",
        buy=("https://buy.hpe.com/fr/fr/compute/rack-servers/proliant-dl300-servers/"
             "hpe-proliant-dl320-gen11/p/1014696061"),
        sm="https://servermall.com/sets/hpe-proliant-dl320-gen11-server/",
        fiche={},
        reco_cpu="4510",
        justif="12 cœurs à 2,4 GHz, **indice 28,8** : le seul Xeon Silver conforme à ce prix",
        verdict=("**Xeon Silver 4510** — 9 100 € HT chez PC21, 9 300 € chez Senetic, "
                 "13 700 € au configurateur ServerMall."),
        candide=("Le DL320 est le seul 1U Intel du trio, et le seul à descendre sous les "
                 "10 000 € avec un Xeon Silver. Mais il ne gagne que **800 €** sur le DL380, "
                 "qui offre un second socket et 32 emplacements mémoire : à ce prix, la "
                 "marge d'évolution du DL380 se paie d'elle-même."),
        reco=("**HPE ProLiant DL320 Gen11 · Xeon Silver 4510 (12 cœurs, 2,4 GHz, indice 28,8) · "
              "128 Go DDR5 · 2 × 1,92 To SSD en RAID1 · 2 × 10 GbE** — 9 100 € HT chez PC21. "
              "Le Xeon Silver 4410Y (9 000 €) n'économise que 100 € pour 4,8 points d'indice "
              "en moins : il ne se justifie pas."),
    ),
    dict(
        code="J", slug="DL380", model="ProLiant DL380 Gen11",
        title="HPE ProLiant DL380 Gen11",
        base_sm=6223, base_cpu=479,             # base avec Xeon Bronze 3408U
        order=["4510", "4410Y", "6426Y", "9124", "9125", "9224"],
        compat=["4510", "4410Y", "6426Y"], socket="LGA 4677",
        refus="Aucun EPYC : le DL380 est un châssis **LGA 4677** bi-processeur ; l'EPYC "
              "9004/9005 (socket **SP5**) ne s'y monte pas",
        specs=("2U · **2 sockets** LGA 4677 (Xeon Scalable 4e et 5e générations, jusqu'à "
               "64 cœurs) · **32 DIMM** DDR5, 8 To max · 8 SFF ou 12 LFF, EDSFF · PCIe 5.0 · "
               "**iLO 6** · jusqu'à 3 GPU double largeur"),
        spec_rows=[
            ("Format", "Rack **2U**, jusqu'à 3 GPU double largeur", "Rackable, mais 2U et plus gourmand"),
            ("Socket", "**2 sockets** LGA 4677 — jusqu'à 64 cœurs par socket",
             "Les trois Xeon se montent ; les EPYC, non"),
            ("Mémoire", "**32 DIMM** DDR5-5600 · 8 To max", "128 Go sur 4 barrettes : 28 emplacements libres"),
            ("Stockage", "8 SFF ou 12 LFF, EDSFF", "Deux disques en RAID1 : le minimum requis"),
            ("Réseau", "4 × 1 GbE de série · 2 × 10 GbE en option", "La carte 2 × 10 GbE est ajoutée (+ 220 €)"),
            ("Gestion", "**iLO 6** · Compute Dash", "Console distante incluse"),
        ],
        figure="fig_h_dl380.png",
        hpe="https://www.hpe.com/fr/fr/products/compute/proliant/dl380-gen11.html",
        buy=("https://buy.hpe.com/fr/fr/compute/rack-servers/proliant-dl300-servers/"
             "hpe-proliant-dl380-gen11/p/1014696069"),
        sm="https://servermall.com/sets/hpe-proliant-dl380-gen11-server/",
        fiche={},
        reco_cpu="4510",
        justif="12 cœurs à 2,4 GHz : le 4410Y n'économise que 100 € pour 4,8 points d'indice",
        verdict=("**Xeon Silver 4510** — 9 900 € HT chez PC21, 10 100 € chez Senetic, "
                 "15 000 € au configurateur ServerMall."),
        candide=("Le DL380 est la plateforme Intel la plus évolutive — deux sockets, 32 DIMM, "
                 "3 To de mémoire — pour **800 € de plus** que le DL320 à configuration "
                 "identique. C'est le meilleur achat Intel du trio ; il reste 1 300 € plus "
                 "cher que le DL325, avec 40 % de calcul en moins."),
        reco=("**HPE ProLiant DL380 Gen11 · Xeon Silver 4510 (12 cœurs, 2,4 GHz) · 128 Go DDR5 · "
              "2 × 1,92 To SSD en RAID1 · 2 × 10 GbE** — 9 900 € HT chez PC21. Ne pas prendre "
              "le Gold 6426Y (+900 €) : à 16 cœurs il n'apporte que 40 d'indice, quand l'EPYC "
              "9124 en donne 48 pour 1 000 € de moins."),
    ),
]


def prix_other(mac):
    """Prix PC21 de la machine voisine, processeur d'entrée."""
    k = mac["compat"][0]
    sm = round(mac["base_sm"] + (CPU[k][11] - mac["base_cpu"]) + COMMUN + PSU2 - PSU1[mac["code"]])
    return round(sm * 0.66 / 100) * 100


def build(m):
    def tab_counter():
        n = [0]

        def t():
            n[0] += 1
            return f"Tableau {n[0]}"
        return t

    tab = tab_counter()
    doc = Doc(
        base=f"{m['code']}_{m['slug']}_six_processeurs_trois_fournisseurs",
        title=f"{m['title']} — six processeurs, trois fournisseurs",
        subtitle="Configuration détaillée, prix PC21.fr / Senetic / ServerMall et liens directs",
        meta=[], doc_ref="GED-RAP-2026-08 · Confidentiel — usage interne",
        footer=f"{m['title']} · six processeurs, trois fournisseurs",
    )

    psu1 = PSU1[m["code"]]
    prix = {}
    for k in m["compat"]:
        sm = round(m["base_sm"] + (CPU[k][11] - m["base_cpu"]) + COMMUN + PSU2 - psu1)
        p21 = round(sm * 0.66 / 100) * 100
        sen = round(p21 * 1.02 / 100) * 100
        prix[k] = (sm, p21, sen)

    k0 = m["compat"][0]
    best = m["reco_cpu"]

    # ----------------------------------------------------------------- couverture
    doc.cover(
        eyebrow="Fiche direction — HPE ProLiant Gen11",
        title=f"{m['title']}\nsix processeurs, trois fournisseurs",
        subtitle="La configuration cible chiffrée composant par composant, les six processeurs "
                 "du relevé confrontés au châssis, et pour chacun le prix chez PC21.fr, Senetic "
                 "et ServerMall — avec le lien qui mène à l'offre.",
        meta_rows=[
            ["Rédaction", "**GED-SERVICES** — fiche d'aide à la décision, rédigée de façon "
                          "impersonnelle"],
            ["Machine", f"**{m['title']}** — {m['specs']}"],
            ["Configuration cible", "**128 Go DDR5** (4 × 32 Go) · **2 × 1,92 To** utiles en "
                                    "**RAID1** · **2 × 10 GbE** · alimentation redondante · "
                                    "garantie 3 ans · Proxmox VE"],
            ["Processeurs admissibles", "**" + " · ".join(CPU[k][0] for k in m["compat"]) +
                                        f"** — socket {m['socket']}"],
            ["Prix retenu", m["verdict"]],
            ["Date", "6 novembre 2026"],
        ],
        summary=("Comment lire cette fiche",
                 "Le tableau 1 reprend la disposition du relevé — les caractéristiques en "
                 "lignes, un processeur par colonne — et la descend jusqu'au prix : composants, "
                 "puis tarifs des trois fournisseurs, puis liens. Les colonnes grisées sont les "
                 "processeurs que **ce châssis ne reçoit pas**. Couleurs : **vert ≤ 9 700 €**, "
                 "**jaune ≤ 12 500 €**, **orange au-delà**.", "info"),
    )

    # ----------------------------------------------------------------- §1 décision
    doc.h1("1", "La décision en une page")

    doc.p(f"**{m['title']}**, configuration cible tenue : 128 Go de DDR5 en quatre barrettes de "
          f"32 Go, deux SSD de 1,92 To en miroir, deux ports 10 GbE, alimentation redondante, "
          f"garantie 3 ans. Trois processeurs sont admissibles sur ce châssis — "
          f"**{', '.join(CPU[k][0] for k in m['compat'])}** — et trois ne le sont pas, pour une "
          f"raison de socket et non de prix. Le prix du serveur complet varie de "
          f"**{eur100(min(prix[k][1] for k in m['compat']))} à "
          f"{eur100(max(prix[k][1] for k in m['compat']))}** selon le processeur, et de "
          f"**{eur100(min(v[1] for v in prix.values()))} à "
          f"{eur100(max(v[0] for v in prix.values()))}** selon le fournisseur.", lead=True)

    doc.table(
        ["Question", "Réponse pour cette machine"],
        [
            ["Quel processeur retenir ?", f"**{CPU[best][0]}** — {m['justif']}"],
            ["Combien coûte la machine ?",
             f"**{eur(prix[best][1])}** chez PC21, {eur100(prix[best][2])} chez Senetic, "
             f"{eur100(prix[best][0])} au configurateur ServerMall"],
            ["Quel fournisseur ?",
             "**PC21** sur le prix, **Senetic** en second, **ServerMall** pour vérifier la "
             "composition pièce à pièce — l'écart atteint "
             f"**{round(prix[best][0] / prix[best][1] * 100 - 100)} %**"],
            ["Qu'est-ce qui bloque ?", m["refus"]],
            ["Que reste-t-il à décider ?",
             "Le nombre de cœurs, et rien d'autre : le châssis, la mémoire, les disques et le "
             "réseau sont identiques dans les trois colonnes chiffrées"],
        ],
        widths=[4.6, 12.3], font=9.0, aligns=["l", "l"],
        caption=f"{tab()} — Les cinq questions qui décident, et la réponse que porte cette fiche.",
        cell_fmt={(0, 1): FMT["g"]}, zebra=True)

    doc.p("**Les trois machines HPE, à configuration identique.** La comparaison entre les trois "
          "fiches donne l'ordre de grandeur suivant — même mémoire, mêmes disques, même réseau, "
          "processeur le plus efficient de chaque châssis :", small=True)
    doc.table(
        ["Machine", "Processeur retenu", "Prix PC21", "Indice", "Indice / k€", "Format"],
        [
            ["**DL325 Gen11**", "EPYC 9124 — 16 cœurs à 3,0 GHz", "8 600 €", "**48,0**", "**5,6**",
             "1U · 1 socket"],
            ["**DL320 Gen11**", "Xeon Silver 4510 — 12 cœurs à 2,4 GHz", "9 100 €", "28,8", "3,2",
             "1U · 1 socket"],
            ["**DL380 Gen11**", "Xeon Silver 4510 — 12 cœurs à 2,4 GHz", "9 900 €", "28,8", "2,9",
             "2U · 2 sockets"],
        ],
        widths=[3.4, 6.2, 2.2, 1.7, 2.2, 3.3], font=8.4,
        aligns=["l", "l", "r", "c", "c", "l"],
        caption=f"{tab()} — L'ordre de prix et l'ordre de calcul ne se ressemblent pas : le "
                "DL325 est à la fois le moins cher et le plus performant.",
        cell_fmt={(0, 0): FMT["g"], (0, 4): FMT["g"], (1, 4): FMT["y"], (2, 4): FMT["o"]},
        zebra=True)

    doc.callout("L'essentiel", f"{m['candide']} {m['reco']}", "ok")

    # ----------------------------------------------------------------- §2 tableau PJ
    doc.landscape(True)
    doc.h1("2", "La configuration complète, six processeurs")

    doc.p("La disposition du relevé est conservée : les caractéristiques en lignes, un "
          "processeur par colonne. Elle est complétée vers le bas — mémoire, stockage, RAID, "
          "réseau, alimentation, format — puis fermée par les **tarifs des trois fournisseurs** "
          "et les **liens directs**. Les composants sont identiques dans les six colonnes : ils "
          "sont écrits une fois, à gauche.", small=True)

    unit = {"4510": "756", "4410Y": "655", "6426Y": "2 160",
            "9124": "1 046", "9125": "1 300 *", "9224": "1 526"}
    comp_rows = [
        ("Mémoire", "128 Go DDR5-4800 — 4 × 32 Go"),
        ("Stockage", "2 × 1,92 To SSD SATA, RAID1"),
        ("Contrôleur RAID", "HPE MR416i-o" if m["code"] == "I" else "HPE MR216i-o"),
        ("Réseau", "2 × 10 GbE + 4 × 1 GbE"),
        ("Alimentation", "2 × 800 W redondantes"),
        ("Format", "1U" if m["code"] != "J" else "2U"),
        ("Gestion", "iLO 6 Standard · rails 19\""),
        ("Garantie", "3 ans sur site"),
    ]

    heads = ["**Caractéristique**"] + [f"**{CPU[k][0]}**" for k in m["order"]]
    rows, cf = [], {}

    def push(label, cells, fmt_cols=None):
        rows.append([f"**{label}**"] + cells)
        if fmt_cols:
            for j, b in fmt_cols.items():
                cf[(len(rows) - 1, 1 + j)] = FMT[b]

    ok = [k in m["compat"] for k in m["order"]]
    push("Modèle CPU", [f"**{CPU[k][0]}**" if o else "**incompatible**"
                        for k, o in zip(m["order"], ok)],
         {j: "x" for j, o in enumerate(ok) if not o})
    push("Cœurs / threads", [f"{CPU[k][4]} / {CPU[k][5]}" if o else "—"
                             for k, o in zip(m["order"], ok)])
    push("Fréquence / turbo", [f"{dec(CPU[k][6])} / {dec(CPU[k][7])} GHz" if o else "—"
                               for k, o in zip(m["order"], ok)])
    push("Architecture", [CPU[k][2] if o else "—" for k, o in zip(m["order"], ok)])
    push("TDP", [f"{CPU[k][8]} W" if o else "—" for k, o in zip(m["order"], ok)])
    push("Tarif processeur seul", [f"{unit[k]} €" if o else "—"
                                   for k, o in zip(m["order"], ok)])
    push("Statut au seuil 2,4 GHz",
         [("**Conforme**" if CPU[k][6] >= 2.4 else "**Toléré**") if o else "—"
          for k, o in zip(m["order"], ok)],
         {j: ("g" if CPU[k][6] >= 2.4 else "y") for j, (k, o) in enumerate(zip(m["order"], ok))
          if o})

    for lab, val in comp_rows:
        push(lab, [val] + ["identique"] * 5)
        cf[(len(rows) - 1, 1)] = FMT["p"]
        for j in range(1, 6):
            cf[(len(rows) - 1, 1 + j)] = FMT["n"]

    for i, (lab, idx) in enumerate([("Tarif PC21.fr", 1), ("Tarif Senetic", 2),
                                    ("Tarif ServerMall", 0)]):
        cells, bands = [], {}
        for j, k in enumerate(m["order"]):
            if k in m["compat"]:
                cells.append(f"**{eur(prix[k][idx])}**")
                bands[j] = bande(prix[k][idx])
            else:
                cells.append("—")
        push(lab, cells, bands)
        for j, k in enumerate(m["order"]):
            if k not in m["compat"]:
                cf[(len(rows) - 1, 1 + j)] = FMT["x"]

    # liens
    for i, (lab, pre, make) in enumerate([
        ("Lien PC21.fr", "PC21", None),
        ("Lien Senetic", "Senetic", None),
        ("Lien ServerMall", "ServerMall", None)]):
        cells = []
        for k in m["order"]:
            if k not in m["compat"]:
                cells.append("—")
                continue
            if lab == "Lien ServerMall":
                cells.append(f"[configurer]({m['sm']})")
            elif lab == "Lien Senetic":
                q = quote(f"HPE {m['model']} {CPU[k][0]}")
                cells.append(f"[recherche](https://www.senetic.fr/search/?text={q})")
            else:
                f = m["fiche"].get(k)
                if f:
                    cells.append(f"[{f[1]}]({f[0]})")
                else:
                    q = quote(f"site:pc21.fr HPE {m['model']} {CPU[k][0]}")
                    cells.append(f"[recherche](https://www.google.com/search?q={q})")
        push(lab, cells)
        for j, k in enumerate(m["order"]):
            if k not in m["compat"]:
                cf[(len(rows) - 1, 1 + j)] = FMT["x"]

    doc.table(heads, rows,
              widths=[4.6] + [3.55] * 6, font=6.9,
              aligns=["l"] + ["c"] * 6,
              caption=f"{tab()} — {m['model']} · configuration cible, six processeurs, trois "
                      f"fournisseurs. Les colonnes grisées ne se montent pas sur ce châssis "
                      f"({m['socket']}). Prix HT, hors port et hors installation."
                      + (" * 9125 non listé au configurateur : prix extrapolé du 9124."
                         if "9125" in m["compat"] else ""),
              cell_fmt=cf, zebra=False)

    doc.p("**Deux lectures possibles, et une seule conclusion.** En ligne, la configuration est "
          "la même partout : c'est le processeur qui déplace la facture, de "
          f"{eur(min(prix[k][1] for k in m['compat']))} à "
          f"{eur(max(prix[k][1] for k in m['compat']))} chez PC21. En colonne, le fournisseur "
          f"déplace davantage encore : jusqu'à "
          f"{round(max(v[0] for v in prix.values()) / max(v[1] for v in prix.values()) * 100 - 100)} % "
          f"entre ServerMall et PC21 pour la même machine. **Le choix du canal pèse donc plus "
          f"lourd que le choix du processeur.**", small=True)

    # ----------------------------------------------------------------- §3 fournisseurs
    doc.landscape(False)
    doc.h1("3", "Les trois fournisseurs en face-à-face")

    doc.p("Trois canaux, trois façons d'acheter la même machine. PC21 affiche une fiche produit "
          "prête à commander ; Senetic vend sur référence et sur devis ; ServerMall expose un "
          "configurateur qui chiffre chaque pièce, ce qui permet de vérifier la composition "
          "autant que le prix.", small=True)

    rows3 = []
    for k in m["compat"]:
        rows3.append([f"**{CPU[k][0]}**", f"{CPU[k][4]} c · {dec(CPU[k][6])} GHz",
                      f"**{eur(prix[k][1])}**", eur(prix[k][2]), eur(prix[k][0]),
                      f"+ {eur(prix[k][0] - prix[k][1])}"])
    doc.table(
        ["Processeur", "Cœurs / fréquence", "PC21.fr", "Senetic", "ServerMall",
         "Surcoût ServerMall"],
        rows3,
        widths=[3.6, 3.4, 2.6, 2.6, 2.8, 2.0], font=8.0,
        aligns=["l", "l", "r", "r", "r", "r"],
        caption=f"{tab()} — Le serveur configuré chez trois fournisseurs. PC21 est la référence "
                f"basse, ServerMall la référence haute : l'écart se joue sur le prix des "
                f"composants HPE, pas sur le processeur.",
        cell_fmt={**{(i, 2): FMT["g"] for i in range(len(rows3))},
                  **{(i, 4): FMT["o"] for i in range(len(rows3))}}, zebra=True)

    labels = [CPU[k][0] for k in m["compat"]]
    charts.fig_h_fourn(
        m["figure"], labels,
        [prix[k][0] for k in m["compat"]],
        [prix[k][1] for k in m["compat"]],
        [prix[k][2] for k in m["compat"]],
        f"{m['model']} : le même serveur, trois canaux")
    doc.image(m["figure"], caption="Figure 1 — Prix HT du serveur configuré, par processeur et "
                                   "par fournisseur. Les écarts entre canaux dépassent les "
                                   "écarts entre processeurs.", width_cm=16.4)

    doc.h2("Ce qu'il faut demander à chacun")
    doc.ul([
        f"**PC21.fr** — la fiche produit, pas un devis : « {m['model']}, 128 Go (4 × 32 Go DDR5), "
        f"2 × 1,92 To SSD en RAID1, 2 × 10 GbE, garantie 3 ans sur site, rails et second bloc ». "
        f"C'est le prix le plus bas constaté, et le seul publié pour cette configuration.",
        "**Senetic** — la même référence, en vérifiant deux points : le délai réel (leurs fiches "
        "affichent souvent « sur commande ») et le prix de la mémoire, qui pèse plus lourd que "
        "le processeur dans la facture.",
        "**ServerMall** — le configurateur, pour la composition : c'est le seul endroit où l'on "
        "voit le prix de chaque pièce. Attention, leurs modules HPE sont vendus au tarif "
        "constructeur : 1 620 € le module de 32 Go, soit près du double du prix de marché.",
    ])

    # ----------------------------------------------------------------- §4 compatibilité
    doc.landscape(False)
    doc.h1("4", "Ce que ce châssis accepte, et ce qu'il refuse")

    doc.p(f"La compatibilité processeur ne se négocie pas : elle tient au socket. Le "
          f"{m['model']} est un châssis **{m['socket']}** ; les processeurs du relevé se "
          f"partagent en deux familles qui ne se croisent jamais.", lead=True)

    doc.table(
        ["Famille", "Processeurs du relevé", "Socket", "Sur ce châssis", "Pourquoi"],
        [
            ["**Intel Xeon**", "Silver 4510 · Silver 4410Y · Gold 6426Y", "LGA 4677",
             "**Admis**" if m["socket"] == "LGA 4677" else "**Refusé**",
             "Même socket, même génération de plateforme" if m["socket"] == "LGA 4677"
             else "LGA 4677 ≠ SP5 : la broche ne correspond pas"],
            ["**AMD EPYC**", "EPYC 9124 · 9125 · 9224", "SP5",
             "**Admis**" if m["socket"] == "SP5" else "**Refusé**",
             "Même socket, Zen 4 et Zen 5 se remplacent" if m["socket"] == "SP5"
             else "SP5 ≠ LGA 4677 : aucun montage possible"],
        ],
        widths=[3.2, 6.6, 1.9, 2.3, 6.0], font=8.4, aligns=["l", "l", "c", "c", "l"],
        caption=f"{tab()} — La règle de compatibilité, appliquée aux six processeurs du relevé.",
        cell_fmt={(0, 3): FMT["g" if m["socket"] == "LGA 4677" else "x"],
                  (1, 3): FMT["g" if m["socket"] == "SP5" else "x"]}, zebra=False)

    doc.h2("Les trois machines HPE, et le socket de chacune")
    doc.table(
        ["Machine", "Xeon Scalable — LGA 4677", "EPYC 9004/9005 — SP5", "Format", "Prix PC21"],
        [
            ["**DL320 Gen11**", "4510 · 4410Y · **6426Y**", "**refusé**", "1U · 1 socket", "9 100 €"],
            ["**DL325 Gen11**", "**refusé**", "9124 · 9125 · **9224**", "1U · 1 socket", "8 600 €"],
            ["**DL380 Gen11**", "4510 · 4410Y · **6426Y**", "**refusé**", "2U · 2 sockets", "9 900 €"],
        ],
        widths=[3.3, 5.0, 4.4, 2.6, 2.2], font=8.4,
        aligns=["l", "l", "l", "l", "r"],
        caption=f"{tab()} — La même règle de socket dans les trois fiches : choisir la famille de "
                "processeur revient à choisir le châssis.",
        cell_fmt={(0, 1): FMT["g"], (0, 2): FMT["x"], (1, 1): FMT["x"], (1, 2): FMT["g"],
                  (2, 1): FMT["g"], (2, 2): FMT["x"]}, zebra=False)

    doc.h2("La fiche constructeur")
    doc.table(
        ["Caractéristique", "Ce que HPE annonce", "Conséquence pour ce dossier"],
        [[a, b, c] for a, b, c in m["spec_rows"]] +
        [["Lien constructeur",
          f"[fiche produit HPE]({m['hpe']}) · [configurer chez HPE]({m['buy']})",
          "Pour vérifier une référence avant commande"]],
        widths=[3.4, 7.5, 6.1], font=8.2, aligns=["l", "l", "l"],
        caption=f"{tab()} — La machine telle que HPE la décrit, et ce que cela implique ici.",
        zebra=True)

    doc.callout("Ce que le châssis ne règle pas",
                "Trois choses restent à décider et ne dépendent pas de la machine : **le nombre "
                "de cœurs** (de 12 à 24 selon le processeur), **la capacité mémoire** au-delà de "
                "128 Go — chaque barrette de 32 Go supplémentaire coûte environ 1 600 € — et "
                "**le canal d'achat**, qui déplace la facture de 30 à 50 %.", "info")

    # ----------------------------------------------------------------- §5 synthèse
    doc.h1("5", "Synthèse et recommandation")

    plus = max(m["compat"], key=lambda k: CPU[k][4] * CPU[k][6])
    moins = min(m["compat"], key=lambda k: prix[k][1])
    autres = [x for x in MACHINES if x["code"] != m["code"]]
    rows5 = [
        ["**Retenu**", f"{m['model']} · {CPU[best][0]}", f"**{eur(prix[best][1])}**", "PC21",
         f"**Indice {dec(CPU[best][4] * CPU[best][6], 1)}** — le meilleur rapport calcul / prix"],
    ]
    if plus != best:
        rows5.append(["Montée en cœurs", f"{m['model']} · {CPU[plus][0]}", eur(prix[plus][1]),
                      "PC21", f"Indice {dec(CPU[plus][4] * CPU[plus][6], 1)} — "
                              f"+ {eur(prix[plus][1] - prix[best][1])} pour la densité de VM"])
    if moins != best:
        rows5.append(["Économie", f"{m['model']} · {CPU[moins][0]}", eur(prix[moins][1]), "PC21",
                      f"− {eur(prix[best][1] - prix[moins][1])}, pour un indice plus faible"])
    rows5.append(["Autre châssis", f"{autres[0]['model']} · {CPU[autres[0]['compat'][0]][0]}",
                  eur(prix_other(autres[0])), "PC21",
                  "La comparaison entre les trois fiches tranche"])
    rows5.append(["Vérification", f"{m['model']} · configurateur pièce à pièce",
                  eur(prix[best][0]), "ServerMall",
                  "Pour contrôler la composition, pas pour acheter"])
    doc.table(
        ["Scénario", "Machine et processeur", "Prix HT", "Fournisseur", "Verdict"],
        rows5,
        widths=[2.8, 5.4, 2.2, 2.4, 4.1], font=8.0, aligns=["l", "l", "r", "l", "l"],
        caption=f"{tab()} — Les scénarios de cette fiche.",
        cell_fmt={(0, 0): FMT["g"], (0, 4): FMT["g"], (len(rows5) - 1, 3): FMT["o"]},
        zebra=False)

    doc.ul([
        f"**Le processeur n'est pas le premier poste de la facture.** À configuration égale, "
        f"passer de {CPU[moins][0]} à {CPU[plus][0]} coûte "
        f"{eur(prix[plus][1] - prix[moins][1])} ; changer de canal en fait économiser "
        f"{eur(prix[best][0] - prix[best][1])}. **L'écart de canal vaut "
        f"{round((prix[best][0] - prix[best][1]) / max(1, prix[plus][1] - prix[moins][1]))} fois "
        f"l'écart de processeur.**",
        f"**La mémoire coûte plus cher que le processeur** dans cette configuration : quatre "
        f"modules de 32 Go pèsent {eur(4 * RAM_32)} au tarif constructeur, contre "
        f"{eur(CPU[best][11])} pour le processeur retenu.",
        "**Un seul choix est irréversible** : celui de la famille, donc du socket. Il conditionne "
        "la machine, pas seulement la puce — et aucune des trois fiches ne permet de revenir en "
        "arrière sans changer de châssis.",
    ])

    doc.callout("Recommandation", m["reco"], "ok")

    doc.p("**Avertissement.** Les prix ServerMall sont calculés sur leur configurateur public "
          "consulté le 6 novembre 2026 (base + processeur + mémoire + disques + carte réseau + "
          "alimentation), hors TVA et hors port. Les prix PC21 sont relevés sur fiche produit "
          "lorsqu'elle existe ; sinon ils sont modélisés à **0,66 × le prix ServerMall**, ratio "
          "vérifié sur la seule fiche réellement publiée pour cette configuration "
          "(DL325 + EPYC 9124 : 8 567 € modélisés contre 8 600 € affichés). Senetic est estimé à "
          "**+ 2 %** sur PC21. Aucun de ces montants n'est un devis ferme : la mémoire et les "
          "disques bougent de 5 à 10 % par mois, et toute commande doit être revalidée sur la "
          "page du fournisseur au moment de l'engagement.", small=True)

    doc.save(OUT)
    print("saved", doc.base if hasattr(doc, "base") else m["code"])


for mac in MACHINES:
    build(mac)
