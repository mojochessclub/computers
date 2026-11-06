# -*- coding: utf-8 -*-
"""Document E — 15 fournisseurs × 24 configurations, puis matrices composants."""
import os
from render import Doc

BASE = "E_Quinze_fournisseurs_et_matrices_composants"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables")

doc = Doc(
    base=BASE,
    title="Quinze fournisseurs, quatre familles de configurations",
    subtitle="Grille de prix, matrices CPU / mémoire / disques / RAID-réseau",
    meta=[],
    doc_ref="GED-RAP-2026-05 · Confidentiel — usage interne",
    footer="Quinze fournisseurs · grille de prix et matrices",
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

# compteur de tableaux : évite les collisions de numérotation
_NT = [0]


def tab():
    _NT[0] += 1
    return f"Tableau {_NT[0]}"


# --------------------------------------------------------------------------- #
# 1. Les quinze fournisseurs
FOURNISSEURS = [
    ("PC21.fr", "France", "Configurateur + catalogue", "https://www.pc21.fr/", 1.00,
     "Pages produit consultées"),
    ("ServerMall", "France", "Configurateur en ligne", "https://servermall.com/", 1.60,
     "Configurateur consulté"),
    ("Senetic", "France / UE", "Catalogue en ligne", "https://www.senetic.fr/", 1.02,
     "Page produit consultée"),
    ("MonParcInformatique", "France", "Catalogue en ligne", "https://www.monparcinformatique.fr/", 1.05,
     "Page produit consultée"),
    ("LDLC Pro", "France", "Catalogue B2B", "https://www.ldlc.pro/", 1.18, "Domaine vérifié"),
    ("Inmac wstore", "France", "Intégrateur (groupe Bechtle)", "https://www.inmac-wstore.com/", 1.22,
     "Domaine vérifié"),
    ("Bechtle", "Allemagne / UE", "Intégrateur", "https://www.bechtle.com/", 1.12, "Domaine vérifié"),
    ("Redcorp", "Belgique / UE", "Catalogue en ligne", "https://www.redcorp.com/", 1.04,
     "Page produit consultée"),
    ("Insight", "UE / États-Unis", "Intégrateur", "https://fr.insight.com/", 1.15, "Domaine vérifié"),
    ("Arena Bilgisayar", "Turquie", "Distributeur", "https://www.arena.com.tr/", 1.02, "Domaine vérifié"),
    ("Mindware", "Émirats / Dubaï", "Distributeur VAD", "https://www.mindware.net/", 1.00, "Domaine vérifié"),
    ("Alibaba.com", "Chine", "Place de marché / grossistes", "https://www.alibaba.com/", 0.85,
     "Non testé (plateforme)"),
    ("Mustek", "Afrique du Sud", "Distributeur", "https://www.mustek.co.za/", 1.10, "Domaine vérifié"),
    ("GED-SERVICES", "Gabon / Libreville", "Intégrateur local", "mailto:joel.mbaoyone@gedservices.pro", 1.25,
     "Partenaire — contact direct"),
    ("CDW", "États-Unis", "Catalogue B2B", "https://www.cdw.com/", 1.08, "Domaine vérifié"),
]

RELEVES = ("PC21.fr", "ServerMall", "Senetic", "MonParcInformatique", "Redcorp")

# --------------------------------------------------------------------------- #
# 2. Modèle de prix (transparence)
ANCRAGES = [
    ("HPE DL325 Gen11 — EPYC 9124, 64 Go, 8SFF (P77252-425)", "5 726 €", "**Relevé** — PC21.fr"),
    ("HPE DL380 Gen11 — Xeon Silver 4510, 2U (P71675-425)", "10 655 €", "**Relevé** — PC21.fr"),
    ("HPE DL380 Gen11 — Xeon Silver 4514Y, 128 Go (P77242-425)", "16 861 €", "**Relevé** — PC21.fr"),
    ("Dell PowerEdge R6615 — EPYC 9354P, 64 Go", "16 411 €", "**Relevé** — Dell.fr (direct)"),
    ("Lenovo SR645 V3 — EPYC 9124, 32 Go (7D9CA014EA)", "4 947 €", "**Relevé** — Redcorp"),
    ("Supermicro AS-1115CS-TNR — barebone 1U", "2 040 €", "**Relevé** — Senetic"),
    ("HPE DL325 Gen11 — EPYC 9124, 64 Go (même référence)", "9 174 €", "**Relevé** — ServerMall (écart +60 %)"),
]

OPTIONS = [
    ("Base AMD — DL325 Gen11, EPYC 9124 16C/3,0, 64 Go DDR5, 8SFF, 2×10 GbE", "5 726 €", "Relevé"),
    ("Base Intel — DL380 Gen11, Xeon Silver 4510 12C/2,4, 2U, 64 Go DDR5", "11 455 €", "Relevé + mémoire"),
    ("Passage AMD 16C → 24C (EPYC 9224, 2,5 GHz)", "+ 1 300 €", "Estimé"),
    ("Passage Intel 12C/2,4 → 16C/2,5 (Xeon Gold 6426Y)", "+ 1 900 €", "Estimé"),
    ("Mémoire 64 Go → 128 Go (2 barrettes DDR5 32 Go)", "+ 1 600 €", "Estimé"),
    ("Disques 2×1,92 To SATA SSD read-intensive (RAID1)", "+ 900 €", "Estimé"),
    ("Disques 2×1,92 To SAS SSD (RAID1)", "+ 1 500 €", "Estimé"),
    ("Disques 2×1,92 To NVMe U.3 (RAID1)", "+ 1 300 €", "Estimé"),
]

BASE_AMD, BASE_INTEL = 5726, 11455
CPU_AMD_24C, CPU_INTEL_16C = 1300, 1900
RAM_128 = 1600
DISK = {"SATA": 900, "SAS": 1500, "NVMe": 1300}

# variantes a..f : (lettre, disque, cœurs demandés)
VAR = [("a", "SATA", 12), ("b", "SAS", 12), ("c", "NVMe", 16),
       ("d", "SATA", 16), ("e", "SAS", 12), ("f", "NVMe", 16)]

# la liste de la Direction répète deux variantes : e) = b) et f) = c)
DOUBLON = {"e": "b", "f": "c"}


def prix(base, disque, coeurs, famille):
    p = base + DISK[disque]
    if famille == "AMD":
        p += CPU_AMD_24C if coeurs == 12 else 0
    else:
        p += CPU_INTEL_16C if coeurs == 16 else 0
    return p


def bande(p):
    if p <= 9500:
        return "g"
    if p <= 12500:
        return "y"
    return "o"


def eur(n):
    return f"{round(n):,}".replace(",", " ") + " €"


# --------------------------------------------------------------------------- #
doc.cover(
    eyebrow="Proposition E — grille fournisseurs",
    title="Quinze fournisseurs,\nquatre familles de configurations",
    subtitle="Chaque configuration chiffrée chez quinze revendeurs répartis sur sept zones, "
             "puis les matrices de référence : processeurs, mémoire, disques, RAID et réseau.",
    meta_rows=[
        ["Pour", "**Jad — Direction Générale**"],
        ["Objet", "Comparer le coût des configurations cibles chez quinze fournisseurs, "
                  "puis fixer les critères techniques de choix des composants"],
        ["Cible rappelée", "**128 Go DDR5** · **2×1,92 To utiles en RAID1** · **12 à 16 cœurs ≥ 2,5 GHz** · "
                           "**2×10 GbE** · rackable · Proxmox VE"],
        ["Périmètre", "2 familles de processeurs (AMD / Intel) × 2 capacités mémoire (64 / 128 Go) × "
                      "6 variantes disques = **24 configurations**"],
        ["Fournisseurs", "7 zones : France, UE, Turquie, Émirats, Chine, Afrique, États-Unis"],
        ["Statut des prix", "7 ancrages **relevés** ; les autres prix sont **modélisés** "
                            "(base + options, puis coefficient fournisseur)"],
        ["Date", "5 novembre 2026"],
    ],
    summary=("Comment lire ce document",
             "Les tableaux A et B se lisent par ligne : un fournisseur, six configurations. "
             "Les **prix en vert** tiennent dans l'enveloppe cible (≤ 9 500 €), en **jaune** dans "
             "l'enveloppe haute (≤ 12 500 €), en **orange** au-delà. Un point **•** signale un "
             "fournisseur sur lequel au moins un prix a été relevé ; partout ailleurs le prix est "
             "**indicatif** et modélisé.",
             "info"),
)

# --------------------------------------------------------------------------- #
doc.h1("1", "Les quinze fournisseurs")

doc.p("Quinze fournisseurs, sept zones. Trois familles d'acteurs : les **configurateurs et "
      "catalogues en ligne** (prix les plus bas, conseil variable), les **intégrateurs** (garantie "
      "mieux suivie, remise à négocier), les **distributeurs régionaux** (proximité logistique, "
      "fret et douane à ajouter).", lead=True)

rows, cf = [], {}
for i, (nom, zone, typ, url, coef, verif) in enumerate(FOURNISSEURS):
    lib = nom + (" •" if nom in RELEVES else "")
    rows.append([f"**{i+1}**", f"**{lib}**", zone, typ, f"[catalogue]({url})",
                 f"{coef:.2f}".replace(".", ","), verif])
    cf[(i, 5)] = FMT["g"] if coef <= 1.05 else (FMT["y"] if coef <= 1.18 else FMT["o"])

doc.table(
    ["#", "Fournisseur", "Zone", "Type d'acteur", "Catalogue / configurateur", "Coef.", "Vérification du lien"],
    rows,
    widths=[0.8, 3.9, 2.3, 3.1, 2.6, 1.2, 3.2], font=7.6,
    aligns=["c", "l", "l", "l", "l", "c", "l"],
    caption=f"{tab()} — Les quinze fournisseurs et leur coefficient de prix. « • » : au moins un prix "
            "relevé sur ce fournisseur. Coefficient : écart constaté ou estimé avec PC21.fr "
            "(indice 1,00). **Vert ≤ 1,05** · **jaune ≤ 1,18** · **orange au-delà**.",
    cell_fmt=cf, zebra=False)

doc.callout("Ce que le coefficient signifie — et ne signifie pas",
            "Il ne s'agit pas d'une marge, mais d'un **écart de prix constaté ou estimé** sur une "
            "nomenclature identique. Il est mesuré là où un relevé existe (ServerMall : +60 % sur la "
            "même référence HPE) et estimé ailleurs par analogie de canal. Il sert à **hiérarchiser**, "
            "pas à commander : seul un devis engage.",
            "warn")

doc.h2("Statut de vérification des liens")
doc.ul([
    "**Pages produit consultées** : le lien a été ouvert et la fiche lue (PC21, ServerMall, Senetic, "
    "MonParcInformatique, Redcorp) — le prix provient de cette page.",
    "**Domaines vérifiés** : le site du fournisseur existe et est bien celui annoncé, mais aucune "
    "fiche produit n'a été ouverte dans le cadre de cette note.",
    "**Non testé** : Alibaba.com est une place de marché ; aucun prix ne peut y être considéré comme "
    "ferme, et la qualité de garantie y est très variable.",
])

# --------------------------------------------------------------------------- #
doc.h1("2", "Comment les prix sont construits")

doc.p("Vingt-quatre configurations × quinze fournisseurs représentent 360 prix. Nous n'en avons "
      "relevé qu'une poignée : la grille est donc **construite à partir de sept ancrages réels**, "
      "puis étendue par un modèle explicite. C'est la seule façon de rester factuel.")

doc.table(
    ["Ancrage relevé", "Prix HT", "Source"],
    [[a, f"**{b}**", c] for a, b, c in ANCRAGES],
    widths=[9.4, 2.4, 5.3], font=7.9, aligns=["l", "r", "l"],
    caption=f"{tab()} — Les sept points de repère relevés le 5 novembre 2026.")

doc.table(
    ["Poste du modèle", "Montant", "Statut"],
    [[a, f"**{b}**", c] for a, b, c in OPTIONS],
    widths=[9.4, 2.4, 5.3], font=7.9, aligns=["l", "r", "l"],
    caption=f"{tab()} — Construction du prix de base et des options. "
            "Le prix d'une configuration = base + options, puis × coefficient fournisseur.",
    row_bg={0: BLEU_BG, 1: BLEU_BG})

doc.callout("Pourquoi AMD et Intel ne partent pas du même prix",
            "Les deux bases sont des **relevés réels**, et l'écart est brutal : 5 726 € pour un 1U AMD "
            "à 16 cœurs, 11 455 € pour un 2U Intel à 12 cœurs à 2,4 GHz. À configuration équivalente, "
            "**l'Intel coûte le double** — sans apporter plus de mémoire ni plus de disques.",
            "bad")

doc.h2("Deux avertissements de lecture, avant les tableaux")
doc.ul([
    "**Les six variantes de la Direction se réduisent à quatre prix.** La liste demande deux fois "
    "la même chose : e) SAS 12 cœurs = b) et f) NVMe 16 cœurs = c). Les six colonnes sont conservées "
    "à l'identique pour rester fidèle à la demande, mais e) et f) portent les mêmes valeurs que b) et c).",
    "**Chez AMD, la variante 12 cœurs est la plus chère.** Aucun EPYC 9004 ne compte 12 cœurs : le "
    "premier palier est le **EPYC 9224 (24 cœurs à 2,5 GHz)**, facturé 1 300 € de plus que l'EPYC 9124 "
    "à 16 cœurs, qui satisfait pourtant déjà l'exigence (« au moins 12 cœurs à 2,5 GHz »). Les colonnes "
    "12 cœurs AMD se lisent donc comme une **borne haute**, pas comme un choix économique.",
])

# --------------------------------------------------------------------------- #
def table_prix(famille, ram_go, num, titre, intro, lecture=None, recommandation=None):
    base = BASE_AMD if famille == "AMD" else BASE_INTEL
    doc.landscape(True)
    doc.h1(num, titre)
    doc.p(intro, small=True)

    heads = ["**Fournisseur**", "**Zone**"]
    for lettre, disque, coeurs in VAR:
        extra = f" · (= {DOUBLON[lettre]})" if lettre in DOUBLON else ""
        if famille == "AMD":
            ghz = "2,5 GHz" if coeurs == 12 else "3,0 GHz"
            if coeurs == 12:
                coeurs = "12 cœurs*"
        else:
            ghz = "2,4 GHz" if coeurs == 12 else "2,5 GHz"
        c_lib = coeurs if isinstance(coeurs, str) else f"{coeurs} cœurs"
        heads.append(f"**{lettre}) {disque}**\n{c_lib} \u00b7 {ghz}{extra}")

    rows, cf, mat = [], {}, []
    for i, (nom, zone, typ, url, coef, verif) in enumerate(FOURNISSEURS):
        row = [f"**{nom}**" + (" •" if nom in RELEVES else ""), zone]
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
              widths=[3.9, 2.3] + [3.28] * 6, font=7.6,
              aligns=["l", "l"] + ["r"] * 6,
              caption=f"{tab()} — {famille} · {ram_go} Go DDR5 · six variantes disques · prix HT "
                      f"indicatifs par fournisseur (coefficient du tableau 1 appliqué à la base du "
                      f"tableau 3). Cible rappelée : 2×1,92 To utiles en **RAID1**, **2×10 GbE**, "
                      f"rackable. Référence : "
                      f"{'DL325 Gen11 / EPYC 9124-9224' if famille == 'AMD' else 'DL380 Gen11 / Xeon Silver 4510 - Gold 6426Y'}. "
                      + ("Fréquences toutes **au-dessus du seuil** de 2,5 GHz ; (*) aucun EPYC 9004 "
                         "à 12 cœurs, ces colonnes portent l'EPYC 9224 (24 cœurs)."
                         if famille == "AMD" else
                         "Les colonnes à **2,4 GHz** sont **sous le seuil** exigé."),
              cell_fmt=cf, zebra=False)

    if lecture:
        # quelques chiffres utiles, calculés sur la colonne recommandée
        col = lecture[0]
        idx = [l for l, _, _ in VAR].index(col)
        vals = [(mat[i][idx], FOURNISSEURS[i][0]) for i in range(len(FOURNISSEURS))]
        lo = min(vals)
        hi = max(vals)
        sous = sum(1 for v, _ in vals if v <= 9500)
        items = [
            f"**Colonne {col}) la plus disputée** : {eur(lo[0])} chez **{lo[1]}**, {eur(hi[0])} chez "
            f"**{hi[1]}** — soit **+ {round((hi[0]/lo[0]-1)*100)} %** pour un serveur identique ; "
            + (f"{sous} fournisseurs sur 15 restent sous 9 500 €." if sous
               else "**aucun** des quinze ne passe sous 9 500 €."),
        ]
        if recommandation:
            items.append(recommandation)
        doc.ul(items)

    doc.p("**Statut des prix** — relevés : PC21 (P77252-425, P71675-425, P77242-425), ServerMall "
          "(même référence DL325), Senetic (Supermicro), MonParcInformatique, Redcorp (Lenovo SR645 V3) ; "
          "indicatifs partout ailleurs (modèle du tableau 3 × coefficient du tableau 1). Aucun devis ferme.",
          small=True)


table_prix("AMD", 64, "3", "A.1 — AMD ≥ 2,5 GHz · 64 Go DDR5",
           "Cible : 2×1,92 To utiles en RAID1, 12 à 16 cœurs à 2,5 GHz minimum, 2×10 GbE, 64 Go DDR5. "
           "Aucun EPYC 9004 ne compte 12 cœurs : les variantes 12 cœurs prennent l'EPYC 9224 (24 cœurs "
           "à 2,5 GHz), les variantes 16 cœurs l'EPYC 9124 (3,0 GHz), moins cher.",
           lecture=("d",),
           recommandation="**À retenir** : la variante d) — SATA, 16 cœurs — est la moins chère de la "
                          "ligne et dépasse déjà l'exigence ; la 12 cœurs AMD est une borne haute.")

table_prix("AMD", 128, "4", "A.2 — AMD ≥ 2,5 GHz · 128 Go DDR5",
           "Même famille, mémoire portée à 128 Go : +1 600 € d'extension, soit le seul écart avec A.1. "
           "C'est le bloc qui contient la configuration recommandée du dossier.",
           lecture=("f",),
           recommandation="**Recommandation** : 2×1,92 To NVMe en RAID1, EPYC 9124 16 cœurs, 128 Go, "
                          "2×10 GbE = 8 600 € chez PC21, 8 800 € chez Senetic, 9 000 € chez Redcorp — "
                          "la seule configuration qui tient toutes les exigences à 9 000 € ou moins.")

# --------------------------------------------------------------------------- #
doc.h1("5", "Le seuil des 2,5 GHz sur Intel : une exigence qui coûte cher")
doc.p("La contrainte « 12 cœurs à 2,5 GHz minimum » **n'est pas satisfaite** par l'offre Intel Gen11 "
      "courante : le Xeon Silver 4510 plafonne à 2,4 GHz et le 4410Y à 2,0 GHz. Le premier palier "
      "conforme est le Xeon Gold 6426Y — 16 cœurs à 2,5 GHz, +1 900 €. Les tableaux B.1 et B.2 "
      "chiffrent les deux niveaux, en signalant les variantes non conformes.", small=True)
doc.table(
    ["Processeur Intel", "Cœurs / threads", "Fréquence de base", "Turbo", "TDP", "Statut vs exigence 2,5 GHz"],
    [
        ["Xeon Silver 4410Y", "12 / 24", "2,0 GHz", "3,9 GHz", "150 W", "**Non conforme** — 2,0 GHz"],
        ["Xeon Silver 4510", "12 / 24", "2,4 GHz", "4,1 GHz", "150 W", "**Non conforme** — 2,4 GHz"],
        ["Xeon Silver 4514Y", "16 / 32", "2,0 GHz", "3,5 GHz", "150 W", "**Non conforme** — 2,0 GHz"],
        ["**Xeon Gold 6426Y**", "16 / 32", "**2,5 GHz**", "4,1 GHz", "185 W", "**Conforme** — retenu pour B"],
        ["Xeon Gold 6430", "32 / 64", "2,1 GHz", "3,4 GHz", "270 W", "Non conforme, mais très performant"],
    ],
    widths=[4.4, 2.6, 3.0, 2.4, 1.8, 5.8], font=8.2, aligns=["l", "c", "c", "c", "c", "l"],
    caption=f"{tab()} — La contrainte de fréquence élimine les Xeon Silver de la génération actuelle.",
    cell_fmt={(0, 5): FMT["o"], (1, 5): FMT["o"], (2, 5): FMT["o"], (3, 5): FMT["g"],
              (4, 5): FMT["y"], (3, 0): FMT["g"]}, zebra=False)

doc.table(
    ["Processeur AMD", "Cœurs / threads", "Fréquence de base", "Turbo", "TDP", "Statut vs exigence 2,5 GHz"],
    [
        ["**EPYC 9124**", "16 / 32", "**3,0 GHz**", "3,7 GHz", "200 W", "**Conforme** — retenu (16 cœurs)"],
        ["EPYC 9224", "24 / 48", "2,5 GHz", "3,7 GHz", "200 W", "**Conforme** — plancher exact 2,5 GHz"],
        ["EPYC 9254", "24 / 48", "2,9 GHz", "4,15 GHz", "200 W", "Conforme"],
        ["EPYC 9354P", "32 / 64", "3,25 GHz", "3,8 GHz", "280 W", "Conforme — au-delà du besoin"],
        ["— aucun EPYC 9004 à 12 cœurs", "12", "—", "—", "—", "L'entrée de gamme est à 16 cœurs"],
    ],
    widths=[4.4, 2.6, 3.0, 2.4, 1.8, 5.8], font=8.2, aligns=["l", "c", "c", "c", "c", "l"],
    caption=f"{tab()} — Côté AMD, la contrainte est tenue dès la première référence : le problème "
            "ne se pose que chez Intel.",
    cell_fmt={(0, 5): FMT["g"], (1, 5): FMT["g"], (4, 0): FMT["y"], (4, 5): FMT["y"]}, zebra=False)

doc.callout("Ce que cela change pour la décision",
            "Chez Intel, tenir les 2,5 GHz impose de payer un Xeon Gold : **+ 1 900 €** de processeur, "
            "et souvent + 4 000 à 5 000 € de machine. Chez AMD, la même exigence est tenue par le "
            "processeur d'entrée de gamme, sans surcoût. À charge de calcul comparable, l'écart entre "
            "les blocs A et B est donc **structurel**, pas commercial.",
            "warn")

doc.ul([
    "**Coût de la conformité chez Intel** : + 1 900 € de processeur, soit **+ 17 %** sur la machine "
    "de base (11 455 € → 13 355 €), avant disques et avant mémoire.",
    "**Écart avec AMD à configuration identique** : 16 300 € (Intel 128 Go NVMe conforme) contre "
    "8 600 € (AMD 128 Go NVMe) — **7 600 €**, soit 88 % de plus pour le même service rendu.",
    "**Troisième voie** : rester sur un Xeon Silver à 2,4 GHz et assumer une **dérogation écrite** au "
    "seuil des 2,5 GHz. C'est défendable si la charge reste sous 30 % de CPU, mais cela doit être dit.",
])

table_prix("Intel", 64, "6", "B.1 — Intel ≥ 2,5 GHz · 64 Go DDR5",
           "Les variantes 12 cœurs s'appuient sur le Xeon Silver 4510 (2,4 GHz) : elles sont chiffrées "
           "mais **sous le seuil**. Les variantes 16 cœurs utilisent le Xeon Gold 6426Y (2,5 GHz), seul "
           "processeur Intel conforme.",
           lecture=("c",),
           recommandation="**À retenir** : les colonnes 12 cœurs (a, b, e) reposent sur le Xeon Silver "
                          "4510 à 2,4 GHz — **sous le seuil des 2,5 GHz**, donc non conformes.")

table_prix("Intel", 128, "7", "B.2 — Intel ≥ 2,5 GHz · 128 Go DDR5",
           "Le même bloc avec 128 Go. À configuration conforme (16 cœurs, 128 Go, RAID1, 10 GbE), "
           "l'Intel dépasse 15 000 € chez la plupart des fournisseurs : c'est le prix de l'exigence "
           "de fréquence chez Intel.",
           lecture=("f",),
           recommandation="**À retenir** : la seule variante conforme de ce bloc (f, NVMe 16 cœurs) "
                          "coûte 16 300 € chez PC21 — près du double de son équivalent AMD (8 600 €).")

# --------------------------------------------------------------------------- #
doc.h1("8", "C — Matrice processeurs : AMD et Intel en perspective")

doc.p("Les processeurs proposés dans les blocs A et B, replacés dans leur génération et comparés par "
      "un indice de calcul brut transparent : **cœurs × fréquence de base**. Cet indice ne remplace pas "
      "un benchmark applicatif, mais il classe correctement les machines pour une charge de "
      "virtualisation peu dépendante de la fréquence pure.", small=True)

CPU = [
    # modèle, archi, sortie, cœurs, base, turbo, tdp, prix, fin com., équivalent
    ("AMD EPYC 9124", "Zen 4 — 9004", "2023", 16, 3.00, 3.70, 200, "≈ 1 050 €", "≈ 2027", "Xeon Gold 6426Y"),
    ("AMD EPYC 9224", "Zen 4 — 9004", "2023", 24, 2.50, 3.70, 200, "≈ 2 350 €", "≈ 2027", "Xeon Gold 6430"),
    ("AMD EPYC 9254", "Zen 4 — 9004", "2023", 24, 2.90, 4.15, 200, "≈ 3 100 €", "≈ 2027", "—"),
    ("AMD EPYC 9354P", "Zen 4 — 9004", "2023", 32, 3.25, 3.80, 280, "≈ 4 200 €", "≈ 2027", "Xeon Gold 6430"),
    ("AMD EPYC 9125", "Zen 5 — 9005", "2024", 16, 2.60, 4.10, 200, "≈ 1 300 €", "≈ 2029", "Xeon 6 — 6500P"),
    ("AMD EPYC 9355P", "Zen 5 — 9005", "2024", 32, 3.55, 4.40, 280, "≈ 5 400 €", "≈ 2029", "Xeon 6 — 6700P"),
    ("Intel Xeon Silver 4410Y", "Emerald Rapids", "2023", 12, 2.00, 3.90, 150, "≈ 900 €", "≈ 2027", "EPYC 9224"),
    ("Intel Xeon Silver 4510", "Emerald Rapids", "2023", 12, 2.40, 4.10, 150, "≈ 1 050 €", "≈ 2027", "EPYC 9224"),
    ("Intel Xeon Silver 4514Y", "Emerald Rapids", "2023", 16, 2.00, 3.50, 150, "≈ 1 500 €", "≈ 2027", "EPYC 9124"),
    ("Intel Xeon Gold 6426Y", "Sapphire Rapids", "2023", 16, 2.50, 4.10, 185, "≈ 2 400 €", "≈ 2027", "EPYC 9124"),
    ("Intel Xeon Gold 6430", "Sapphire Rapids", "2023", 32, 2.10, 3.40, 270, "≈ 4 600 €", "≈ 2027", "EPYC 9354P"),
    ("Intel Xeon Gold 6138", "Skylake — Gen10", "2017", 20, 2.00, 3.70, 125, "≈ 120 € (occasion)", "**2023 (EOL)**", "EPYC 9124"),
]


def bande_cpu(idx):
    if idx >= 100:
        return "S", "g"
    if idx >= 50:
        return "A", "a"
    if idx >= 30:
        return "B", "y"
    return "C", "o"


VERT2_BG, VERT2_TX = "CFE6C6", "1B5E20"
FMT["a"] = F(VERT2_BG, VERT2_TX, True)

rows, cf = [], {}
for i, (m, archi, an, c, base, turbo, tdp, px, fin, eq) in enumerate(CPU):
    idx = round(c * base, 1)
    let, col = bande_cpu(idx)
    rows.append([f"**{m}**", archi, an, f"{c}", f"{base:.2f}".replace(".", ","),
                 f"{turbo:.2f}".replace(".", ","), f"{tdp} W", f"**{let}**",
                 f"{idx:.1f}".replace(".", ","), px, fin, eq])
    cf[(i, 7)] = FMT[col]
    cf[(i, 8)] = FMT[col]
    if "Gen10" in archi or "EOL" in fin:
        cf[(i, 10)] = FMT["o"]
    if "Zen 5" in archi:
        cf[(i, 1)] = FMT["g"]

doc.table(
    ["Processeur", "Architecture", "Sortie", "Cœurs", "Base", "Turbo", "TDP", "Bande", "Indice",
     "Prix indicatif", "Fin de com.", "Équivalent"],
    rows,
    widths=[3.9, 3.1, 1.4, 1.3, 1.3, 1.3, 1.2, 1.4, 1.5, 2.9, 2.2, 3.4], font=7.4,
    aligns=["l", "l", "c", "c", "c", "c", "c", "c", "c", "r", "c", "l"],
    caption=f"{tab()} — Matrice CPU. Indice = cœurs × fréquence de base (GHz). Bandes : "
            "**S ≥ 100 · A 50–99 · B 30–49 · C < 30**. La colonne « Fin de com. » indique la date "
            "d'arrêt de commercialisation estimée : au-delà, plus de pièces ni de firmware.")

doc.table(
    ["Bande", "Indice", "Ce que cela couvre", "Usage recommandé", "Présent dans les blocs A / B"],
    [
        ["**S**", "≥ 100", "32 cœurs et plus à fréquence élevée", "Consolidation lourde, 40 VM et plus",
         "Non — surdimensionné"],
        ["**A**", "50–99", "16 cœurs à 3 GHz, 24 cœurs à 2,5 GHz", "**Cible du dossier** : 15 à 30 VM",
         "A variantes 16 cœurs (48), A variantes 12 cœurs (60)"],
        ["**B**", "30–49", "16 cœurs à 2,0–2,5 GHz, 12 cœurs rapides", "10 à 15 VM, marge limitée",
         "B variantes 16 cœurs (40)"],
        ["**C**", "< 30", "12 cœurs à 2,0–2,4 GHz", "Charge actuelle seulement, sans marge",
         "B variantes 12 cœurs (24 à 28,8)"],
    ],
    widths=[1.3, 1.6, 5.0, 4.6, 5.4], font=8.2, aligns=["c", "c", "l", "l", "l"],
    caption=f"{tab()} — Bandes de performance, reprises dans les tableaux A et B pour qualifier "
            "chaque configuration.",
    cell_fmt={(0, 0): FMT["g"], (1, 0): FMT["a"], (2, 0): FMT["y"], (3, 0): FMT["o"]}, zebra=False)

doc.callout("Le point qui décide",
            "L'EPYC 9124 (16 cœurs à 3,0 GHz, indice 48, ≈ 1 050 €) coûte **moins de la moitié** du "
            "Xeon Gold 6426Y (16 cœurs à 2,5 GHz, indice 40, ≈ 2 400 €) et le dépasse de 20 % en "
            "calcul. Au-delà du prix du processeur, c'est tout l'écosystème qui suit : plateforme 1U "
            "moins chère, un seul socket, une seule licence Proxmox.",
            "ok")

# --------------------------------------------------------------------------- #
doc.h1("9", "D — Matrice mémoire")

doc.p("La mémoire est la ressource saturée de l'existant : c'est le seul poste où l'on ne doit pas "
      "économiser. Attention au contexte 2026 : la demande en mémoire HBM pour l'IA a fait monter les "
      "prix DDR5 de 40 à 70 % en dix-huit mois.", small=True)
doc.table(
    ["Type", "Vitesse", "Capacité module", "Prix indicatif", "€ / Go", "Disponibilité", "Plateformes", "Lecture"],
    [
        ["DDR4 RDIMM", "2 666 MT/s", "32 Go", "≈ 210 €", "6,6 €", "Marché secondaire", "Gen10, 14G",
         "**Fin de vie** — à éviter sur un achat neuf"],
        ["DDR4 RDIMM", "3 200 MT/s", "64 Go", "≈ 480 €", "7,5 €", "Stock résiduel", "Gen10 v2",
         "Reconditionné uniquement"],
        ["DDR5 RDIMM", "4 800 MT/s", "32 Go", "≈ 520 €", "**16,3 €**", "**Très tendu**",
         "Gen11, R6615, SR645 V3", "**Standard du dossier**"],
        ["DDR5 RDIMM", "5 600 MT/s", "32 Go", "≈ 610 €", "19,1 €", "Tendu", "Gen11 Intel, Gen12",
         "Gain réel faible en virtualisation"],
        ["DDR5 RDIMM", "4 800 MT/s", "64 Go", "≈ 1 150 €", "18,0 €", "Très tendu", "Gen11 (1DPC)",
         "Intéressant si 1 barrette par canal"],
        ["DDR5 3DS RDIMM", "4 800 MT/s", "128 Go", "≈ 2 400 €", "18,8 €", "Sur commande", "Gen11/Gen12",
         "Pour dépasser 1 To seulement"],
    ],
    widths=[3.2, 2.4, 2.6, 2.8, 1.9, 2.6, 3.9, 6.5], font=7.6,
    aligns=["l", "c", "c", "r", "r", "l", "l", "l"],
    caption=f"{tab()} — Matrice mémoire (prix indicatifs, marché tendu de 2026).",
    cell_fmt={(2, 4): FMT["o"], (0, 7): FMT["o"], (2, 7): FMT["g"]}, zebra=False)

doc.table(
    ["Capacité cible", "Barrettes", "Coût d'extension", "Emplacements utilisés", "Extension future", "Verdict"],
    [
        ["64 Go", "2 × 32 Go", "inclus", "2 / 12", "+64 Go possible", "**Sous l'exigence** : reconduit la saturation"],
        ["**128 Go**", "4 × 32 Go", "**+ 1 600 €**", "4 / 12", "+128 Go possible", "**Cible retenue**"],
        ["192 Go", "6 × 32 Go", "+ 3 200 €", "6 / 12", "+96 Go possible", "Confort, non justifié aujourd'hui"],
        ["256 Go", "8 × 32 Go", "+ 4 800 €", "8 / 12", "+64 Go possible", "Surdimensionné pour la charge"],
    ],
    widths=[3.4, 2.8, 3.4, 3.6, 3.6, 9.1], font=8.0, aligns=["l", "c", "r", "c", "c", "l"],
    caption=f"{tab()} — Scénarios de capacité, calculés sur 12 emplacements DIMM (DL325 Gen11).",
    cell_fmt={(1, 0): FMT["g"], (0, 5): FMT["o"]}, zebra=False)

doc.ul([
    "**L'existant est à 88,4 % de 64 Go** : acheter 64 Go, c'est acheter la saturation constatée.",
    "**128 Go en 4 × 32 Go** laisse 8 emplacements libres et double la marge sans changer de plateforme.",
    "**Le prix au Go est identique** entre 64 et 128 Go en DDR5 4 800 : on ne paie pas de prime de capacité.",
])

# --------------------------------------------------------------------------- #
doc.h1("10", "E — Matrice disques")

doc.p("Les six variantes des blocs A et B ne diffèrent que par le support : SATA, SAS ou NVMe. "
      "Le choix n'est pas neutre — ni en prix, ni en latence, ni en endurance.", small=True)
doc.table(
    ["Support", "Interface", "Endurance type", "IOPS 4K lecture", "Latence", "Prix 1,92 To", "€ / To",
     "RAID possible", "Lecture"],
    [
        ["SATA SSD RI", "6 Gb/s", "1 DWPD", "≈ 95 000", "≈ 120 µs", "≈ 450 €", "234 €", "0/1/5/6/10",
         "Le moins cher — limité par le contrôleur SATA"],
        ["SAS SSD", "12 / 24 Gb/s", "3 DWPD", "≈ 210 000", "≈ 90 µs", "≈ 750 €", "391 €", "0/1/5/6/10",
         "Double port, endurance supérieure"],
        ["**NVMe U.3**", "PCIe 5.0 x4", "1–3 DWPD", "**≈ 800 000**", "**≈ 20 µs**", "≈ 650 €", "**339 €**",
         "0/1/5/6/10", "**Meilleur rapport latence / prix**"],
        ["NVMe U.2", "PCIe 4.0 x4", "1 DWPD", "≈ 600 000", "≈ 25 µs", "≈ 520 €", "271 €", "0/1/5/6/10",
         "Alternative si U.3 indisponible"],
        ["Disque constructeur (HPE/Dell)", "—", "—", "—", "—", "**≈ 1 100 €**", "573 €", "0/1/5/6/10",
         "**+70 %** : garantie intégrée, firmware validé"],
        ["Disque tiers compatible", "—", "—", "—", "—", "≈ 650 €", "339 €", "selon contrôleur",
         "Économie réelle, garantie à vérifier"],
    ],
    widths=[3.6, 2.6, 2.2, 2.6, 1.9, 2.4, 1.5, 2.4, 6.7], font=7.4,
    aligns=["l", "c", "c", "c", "c", "r", "r", "c", "l"],
    caption=f"{tab()} — Matrice disques. Prix indicatifs pour un SSD 1,92 To, hors options constructeur.",
    cell_fmt={(2, 8): FMT["g"], (0, 8): FMT["y"], (4, 5): FMT["o"]}, zebra=False)

doc.table(
    ["Besoin", "Support retenu", "Justification", "Surcoût vs SATA"],
    [
        ["Virtualisation générale, 2 To utiles", "**NVMe U.3 — 2 × 1,92 To RAID1**",
         "Latence 6× meilleure, prix inférieur au SAS", "**+ 400 €**"],
        ["Budget serré, charge faible", "SATA SSD RI — 2 × 1,92 To RAID1",
         "Suffisant si le contrôleur n'est pas saturé", "référence"],
        ["Écriture intense (base de données)", "SAS SSD 3 DWPD ou NVMe write-intensive",
         "L'endurance prime sur la latence", "+ 300 à 600 €"],
        ["Capacité au-delà de 4 To", "2 × 3,84 To RAID1 ou 4 × 1,92 To RAID10",
         "La baie et le contrôleur deviennent limitants", "+ 900 à 2 000 €"],
    ],
    widths=[5.4, 7.0, 8.4, 5.1], font=8.0, aligns=["l", "l", "l", "r"],
    caption=f"{tab()} — Quelle variante pour quel usage.",
    cell_fmt={(0, 1): FMT["g"]}, zebra=False)

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
    caption=f"{tab()} — Ce que coûtent réellement les deux disques : c'est le poste où le choix "
            "constructeur / tiers pèse le plus lourd.",
    cell_fmt={(1, 3): FMT["y"], (3, 3): FMT["o"], (2, 4): FMT["g"]}, zebra=False)

doc.ul([
    "**Le meilleur euro du dossier est le NVMe** : + 400 € sur la configuration pour une latence "
    "divisée par six. Le SAS coûte 600 € de plus pour moins de latence — il ne se justifie que par "
    "son endurance en écriture.",
    "**Le disque constructeur ajoute 1 300 €** sur les deux disques (firmware validé, garantie "
    "intégrée). La capacité, elle, n'est pas le sujet : 960 Go utiles aujourd'hui, 1,92 To en RAID1 "
    "demain, soit 50 % de marge.",
])

# --------------------------------------------------------------------------- #
doc.h1("11", "F — RAID, réseau et périphériques")

doc.p("Le RAID et le réseau figurent dans chaque colonne des tableaux A et B : voici ce que ces "
      "mentions engagent réellement, et ce qu'il faut prévoir autour du serveur.", small=True)

doc.h2("F.1 — RAID : capacité utile et tolérance")
doc.table(
    ["Niveau", "Disques", "Capacité utile", "Tolérance", "Reconstruction", "IOPS écriture",
     "Verdict pour ce dossier"],
    [
        ["RAID 0", "2 × 1,92 To", "3,84 To", "**Aucune**", "—", "Maximum", "À exclure en production"],
        ["**RAID 1**", "2 × 1,92 To", "**1,92 To**", "**1 disque**", "Rapide (copie)", "2 disques",
         "**Retenu : simple, robuste, suffisant**"],
        ["RAID 5", "3 × 1,92 To", "3,84 To", "1 disque", "**Lente, risquée sur SSD**", "Pénalisé",
         "Non recommandé sous 4 disques"],
        ["RAID 6", "4 × 1,92 To", "3,84 To", "2 disques", "Lente", "Très pénalisé",
         "Pour de la capacité, pas ici"],
        ["RAID 10", "4 × 1,92 To", "3,84 To", "1 disque par miroir", "Rapide", "Bon",
         "Si la croissance disque est certaine"],
        ["ZFS miroir (Proxmox)", "2 × 1,92 To", "1,92 To", "1 disque", "Rapide", "Bon + checksums",
         "**Excellent choix avec Proxmox**"],
    ],
    widths=[3.4, 2.4, 2.6, 3.0, 3.4, 3.0, 8.1], font=7.8,
    aligns=["l", "c", "c", "c", "l", "c", "l"],
    caption=f"{tab()} — RAID : ce que chaque niveau donne et coûte. « 2×1,92 To utiles en RAID1 » "
            "signifie deux disques de 1,92 To en miroir, soit 1,92 To réellement utilisables.",
    cell_fmt={(1, 0): FMT["g"], (5, 6): FMT["g"], (0, 3): FMT["o"]}, zebra=False)

doc.h2("F.2 — Réseau : quand le 10 GbE sert vraiment")
doc.table(
    ["Option", "Débit utile", "Coût carte / module", "Coût switch", "Câblage", "Quand c'est justifié"],
    [
        ["2 × 1 GbE intégré", "≈ 2 Gbit/s agrégés", "inclus", "inclus", "RJ45 Cat6",
         "Charge actuelle, sauvegarde légère"],
        ["**2 × 10 GbE BASE-T (OCP 3.0)**", "**≈ 20 Gbit/s**", "**inclus sur DL325 Gen11**",
         "≈ 900 €", "RJ45 Cat6a", "**Sauvegarde, migration à chaud, VM**"],
        ["2 × 10 GbE SFP+", "≈ 20 Gbit/s", "≈ 350 €", "≈ 1 100 €", "DAC / fibre",
         "Distance, isolation électrique"],
        ["2 × 25 GbE SFP28", "≈ 50 Gbit/s", "≈ 800 €", "≈ 2 500 €", "Fibre", "Aucun besoin ici"],
        ["Switch 10 GbE 8 ports", "—", "—", "**≈ 900 à 1 400 €**", "—",
         "Indispensable si ports 10 GbE utilisés"],
    ],
    widths=[5.0, 3.6, 3.8, 3.0, 2.6, 7.9], font=7.8,
    aligns=["l", "c", "c", "c", "c", "l"],
    caption=f"{tab()} — Le port 10 GbE est inclus sur le DL325 Gen11 ; c'est le switch qui coûte.",
    cell_fmt={(1, 0): FMT["g"], (4, 3): FMT["y"]}, zebra=False)

doc.h2("F.3 — Périphériques et options à ne pas oublier")
doc.table(
    ["Poste", "Référence / spécification", "Prix indicatif", "Statut", "Conséquence si absent"],
    [
        ["Alimentation redondante", "2 × 500 W ou 800 W Platinum", "inclus", "Indispensable",
         "Une panne d'alim arrête tout"],
        ["iLO Advanced (HPE)", "Licence 3 ans", "≈ 350 €", "Recommandé",
         "Console distante limitée depuis Libreville"],
        ["Onduleur", "2 000 VA en ligne + PDU", "≈ 900 €", "**Obligatoire**",
         "Coupures et micro-coupures locales"],
        ["Rails / kit rack", "Kit 1U ou 2U", "≈ 350 €", "Indispensable", "Matériel posé au sol"],
        ["Disque de rechange à froid", "1 × 1,92 To identique", "≈ 650 €", "**Fortement recommandé**",
         "Indisponibilité de plusieurs semaines"],
        ["Cible de sauvegarde", "NAS ou serveur PBS + copie externe", "≈ 1 200 €", "**Obligatoire**",
         "Aucune protection en cas de perte du serveur"],
        ["Switch 10 GbE", "8 ports + optiques / DAC", "≈ 1 100 €", "Recommandé",
         "Ports 10 GbE inutilisés"],
    ],
    widths=[3.8, 6.0, 3.0, 3.2, 9.9], font=7.8,
    aligns=["l", "l", "r", "l", "l"],
    caption=f"{tab()} — Périphériques et options : environ 4 500 € au-dessus du serveur nu.",
    cell_fmt={(2, 3): FMT["o"], (5, 3): FMT["o"], (4, 3): FMT["g"]}, zebra=False)

doc.h2("F.4 — Le budget qui entoure le serveur")
doc.table(
    ["Ligne budgétaire", "Montant HT", "Statut", "Source"],
    [
        ["Serveur cible — AMD 128 Go, 2×1,92 To NVMe RAID1, 16 cœurs, 2×10 GbE",
         "**8 600 €**", "Modélisé sur relevé", "Tableau 5 (A.2 f, PC21)"],
        ["Périphériques et options (onduleur, sauvegarde, switch, rechange, rack)",
         "4 550 €", "Indicatif", "Tableau 18"],
        ["**Sous-total matériel**", "**13 150 €**", "—", "—"],
        ["Licences Proxmox VE Standard + Proxmox Backup Server, an 1", "≈ 1 110 €", "Indicatif",
         "Grille éditeur 2026"],
        ["**Total « prêt à produire »**", "**≈ 14 300 €**", "—", "—"],
        ["Fret, douane, intégration, migration, formation", "6 700 à 7 700 €", "Pour mémoire",
         "Document B"],
        ["**Projet complet, année 1**", "**21 000 à 22 000 €**", "—", "Document B"],
    ],
    widths=[10.2, 3.2, 3.0, 9.5], font=7.9, aligns=["l", "r", "l", "l"],
    caption=f"{tab()} — Du prix du serveur au budget de projet : ce qui s'ajoute entre les deux.",
    row_bg={2: BLEU_BG, 4: BLEU_BG, 6: BLEU_BG})

doc.callout("Ce que ce document ne chiffre pas",
            "Le fret et la douane dépendent de l'incoterm retenu ; la migration des machines "
            "virtuelles dépend de leur nombre et de leur taille ; la reprise de l'existant (licences, "
            "nom de domaine, adresses IP) n'est pas un poste matériel. Ces trois lignes sont traitées "
            "dans le document B, qui conclut à **21 000–22 000 € HT** pour l'année 1.",
            "info")

# --------------------------------------------------------------------------- #
doc.h1("12", "Les prix en une image")

doc.p("Deux lectures graphiques de la grille, avec les couleurs des tableaux : vert ≤ 9 500 €, "
      "jaune ≤ 12 500 €, orange au-delà.", small=True)

doc.image("fig_e_fournisseurs.png",
          "Figure 1 — La cible (AMD 128 Go, NVMe RAID1, 16 cœurs, 2×10 GbE) chez les quinze fournisseurs.",
          width_cm=21.0)

doc.image("fig_e_familles.png",
          "Figure 2 — Même besoin, deux familles : l'écart AMD / Intel (≈ 88 %) dépasse l'écart entre "
          "le fournisseur le moins cher et le plus cher de la figure 1. Prix PC21.", width_cm=21.0)

# --------------------------------------------------------------------------- #
doc.landscape(False)
doc.h1("13", "Synthèse : quelle configuration, chez quel fournisseur")

doc.h2("Ce que la grille montre")
doc.ul([
    "**Le prix du serveur varie de 1 à 1,9 selon le fournisseur** pour une nomenclature identique : "
    "de 5 700 € (PC21, Senetic, Redcorp) à 9 200 € chez ServerMall sur la même référence HPE.",
    "**L'écart AMD / Intel dépasse l'écart entre fournisseurs** : à 128 Go et NVMe, la cible AMD "
    "coûte 8 600 € chez PC21 et 13 800 € chez ServerMall ; la même configuration chez Intel, 16 300 € "
    "chez PC21 et 26 000 € chez ServerMall — deux fois le prix, quel que soit le canal.",
    "**Le disque change peu le prix, beaucoup la performance** : 400 € d'écart entre SATA et NVMe, "
    "pour une latence divisée par six.",
    "**Les zones lointaines ne sont pas moins chères** : Chine (Alibaba) affiche le prix le plus bas "
    "mais sans garantie constructeur ; Dubaï et Turquie sont au niveau français, hors fret ; "
    "l'Afrique du Sud et le Gabon ajoutent 10 à 25 %.",
])

doc.table(
    ["Scénario", "Configuration", "Fournisseurs les plus bas", "Prix HT", "Verdict"],
    [
        ["**Cible recommandée**", "AMD · 128 Go · NVMe · 16 cœurs (A.2 c/f)", "PC21 · Senetic · Redcorp",
         "**≈ 8 600 €**", "**Retenir**"],
        ["Variante économique", "AMD · 128 Go · SATA · 16 cœurs (A.2 d)", "PC21 · Redcorp",
         "≈ 8 200 €", "Si le budget prime"],
        ["Variante endurance", "AMD · 128 Go · SAS · 24 cœurs (A.2 b/e)", "PC21 · Senetic",
         "≈ 10 100 €", "Si écriture intense"],
        ["Contrainte Intel", "Intel · 128 Go · NVMe · 16 cœurs (B.2 c/f)", "Aucun sous 13 800 €",
         "≈ 16 300 €", "**Coût de l'exigence 2,5 GHz**"],
        ["Plancher absolu", "AMD · 64 Go · NVMe · 16 cœurs (A.1 c/f)", "Alibaba (hors garantie)",
         "≈ 6 000 €", "**Sous l'exigence mémoire**"],
    ],
    widths=[2.6, 5.0, 3.6, 2.2, 3.7], font=7.8, aligns=["l", "l", "l", "r", "l"],
    caption=f"{tab()} — Les cinq scénarios qui se dégagent de la grille.",
    cell_fmt={(0, 0): FMT["g"], (0, 4): FMT["g"], (3, 4): FMT["o"], (4, 4): FMT["o"]}, zebra=False)

doc.callout("Recommandation",
            "**AMD · 128 Go DDR5 · 2×1,92 To NVMe en RAID1 · 16 cœurs à 3,0 GHz · 2×10 GbE**, commandé "
            "chez **PC21.fr** (8 600 €) ou **Senetic** (8 800 €), avec un devis de contrôle chez "
            "**Redcorp** et **Inmac wstore** pour la garantie. Budget projet complet : 21 000 à "
            "22 000 € HT, fret et périphériques inclus (voir document B).",
            "ok")

doc.h2("Trois décisions à prendre")
doc.ul([
    "**La famille de processeurs** : AMD à 8 600 € ou Intel à 16 300 € pour le même service rendu. "
    "Cet arbitrage vaut 7 700 € et ne dépend pas du fournisseur.",
    "**Le canal d'achat** : PC21 ou Senetic pour le prix, Redcorp ou Inmac wstore pour le suivi de "
    "garantie. Un devis de contrôle chez deux d'entre eux suffit à valider la grille.",
    "**L'enveloppe** : 14 300 € « prêt à produire » dans ce document, 21 000 à 22 000 € pour le "
    "projet complet (document B). À comparer aux 411 €/mois de location actuelle : le seuil de "
    "bascule est à 550 €/mois de loyer (document A).",
])

doc.p(" ", small=True)
doc.p("**Avertissement.** Sept prix sont relevés sur des pages publiques consultées le "
      "5 novembre 2026 ; les autres sont modélisés à partir de ces ancrages et du coefficient de "
      "chaque fournisseur (tableau 1). Ils servent à comparer des ordres de grandeur et à orienter "
      "une négociation, jamais à engager une dépense. Les liens des fournisseurs ont été vérifiés "
      "au niveau du domaine, les pages produit de PC21, ServerMall, Senetic, MonParcInformatique et "
      "Redcorp ont été consultées. Aucun devis ferme n'existe à ce stade.", small=True)

doc.save(OUT)
print("saved", OUT)
