# -*- coding: utf-8 -*-
"""Postes de travail 2024+ : portables et fixes, trois tranches de prix,
cinq distributeurs français avec lien direct. Word + PDF."""
import os
from urllib.parse import quote_plus
from render import Doc

BASE = "L_Portables_et_fixes_trois_tranches_de_prix_cinq_distributeurs"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables")

doc = Doc(
    base=BASE,
    title="Portables et fixes : trois tranches, cinq distributeurs",
    subtitle="Dix-huit modèles, critères expliqués un par un, et pour chacun cinq liens d'achat français",
    meta=[], doc_ref="GED-RAP-2026-10 · Confidentiel — usage interne",
    footer="Portables et fixes · trois tranches de prix, cinq distributeurs",
)

VERT_BG, VERT_TX = "E3F0DC", "1E6B2F"
JAUN_BG, JAUN_TX = "FBF3D0", "8A6D00"
ORAN_BG, ORAN_TX = "FBE0CE", "B4500F"
BLEU_BG = "EAF0F7"
ROUG_BG, ROUG_TX = "F8D7DA", "8B1A1A"


def F(bg=None, tx=None, b=False, i=False):
    return {"bg": bg, "color": tx, "b": b, "i": i}


GRIS_BG, GRIS_TX = "EDEDED", "5A5A5A"
FMT = {"g": F(VERT_BG, VERT_TX, True), "y": F(JAUN_BG, JAUN_TX, True),
       "n": F(GRIS_BG, GRIS_TX, True),
       "o": F(ORAN_BG, ORAN_TX, True), "p": F(), "i": F(BLEU_BG),
       "h": F(ROUG_BG, ROUG_TX, True)}

_NT = [0]


def tab():
    _NT[0] += 1
    return f"Tableau {_NT[0]}"


def eur(n):
    return f"{round(n):,}".replace(",", "\u00a0") + "\u00a0€"


# --------------------------------------------------------------------------- #
# Liens de recherche : le slug est construit depuis le nom exact du modèle
def liens(q, court):
    """Marketplaces : requête complète (specs comprises) ; revendeurs spécialistes :
    référence seule, leurs filtres étant plus fiables que le texte libre."""
    s, c = quote_plus(q), court.replace(" ", "%20")
    return {
        "Amazon": f"https://www.amazon.fr/s?k={s}",
        "Fnac": f"https://www.fnac.com/SearchResult/ResultList.aspx?Search={s}",
        "Cdiscount": f"https://www.cdiscount.com/search/10/{s}.html",
        "LDLC": f"https://www.ldlc.com/recherche/{c}/",
        "Materiel.net": f"https://www.materiel.net/recherche/{c}/",
    }


# (tranche, marque, modèle, cpu, cœurs/threads, fréquences, ram/ssd, os, prix, requête, année)
PORTABLES = [
    ("Entrée", "Asus", "ExpertBook B1502CVA", "i5-1335U", "10 c / 12 t", "1,3 – 4,6 GHz",
     "16 Go / 512 Go", "Pro", 749, "Asus ExpertBook B1502CVA i5 16 Go 512 Go", 2023),
    ("Entrée", "HP", "250 G10", "i5-1334U", "10 c / 12 t", "1,3 – 4,6 GHz",
     "16 Go / 512 Go", "Home", 649, "HP 250 G10 i5-1334U 16 Go 512 Go", 2023),
    ("Entrée", "Lenovo", "V15 Gen 4", "i5-13420H", "8 c / 12 t", "2,1 – 4,6 GHz",
     "16 Go / 512 Go", "Home", 599, "Lenovo V15 Gen 4 i5-13420H 16 Go 512 Go", 2023),
    ("Moyenne", "Lenovo", "ThinkPad E14 Gen 6", "Core Ultra 5 125U", "12 c / 14 t", "1,3 – 4,3 GHz",
     "16 Go / 512 Go", "Pro", 1049, "Lenovo ThinkPad E14 Gen 6 Ultra 5 125U 16 Go 512 Go", 2024),
    ("Moyenne", "HP", "ProBook 450 G11", "Core Ultra 5 125U", "12 c / 14 t", "1,3 – 4,3 GHz",
     "16 Go / 512 Go", "Pro", 999, "HP ProBook 450 G11 Ultra 5 125U 16 Go 512 Go", 2024),
    ("Moyenne", "Dell", "Latitude 3450", "Core Ultra 5 125U", "12 c / 14 t", "1,3 – 4,3 GHz",
     "16 Go / 512 Go", "Pro", 949, "Dell Latitude 3450 Ultra 5 125U 16 Go 512 Go", 2024),
    ("Haute", "Lenovo", "ThinkPad T14 Gen 5", "Core Ultra 5 125U", "12 c / 14 t", "1,3 – 4,3 GHz",
     "16 Go / 512 Go", "Pro", 1449, "Lenovo ThinkPad T14 Gen 5 Ultra 5 125U 16 Go 512 Go", 2024),
    ("Haute", "HP", "EliteBook 640 G11", "Core Ultra 5 125U", "12 c / 14 t", "1,3 – 4,3 GHz",
     "16 Go / 512 Go", "Pro", 1549, "HP EliteBook 640 G11 Ultra 5 125U 16 Go 512 Go", 2024),
    ("Haute", "Dell", "Latitude 5450", "Core Ultra 5 135U", "12 c / 14 t", "1,3 – 4,4 GHz",
     "16 Go / 512 Go", "Pro", 1499, "Dell Latitude 5450 Ultra 5 135U 16 Go 512 Go", 2024),
]

FIXES = [
    ("Entrée", "Fujitsu", "Esprimo D7010 SFF", "i5-12400", "6 c / 12 t", "2,5 – 4,4 GHz",
     "16 Go / 512 Go", "Pro", 749, "Fujitsu Esprimo D7010 i5-12400 16 Go 512 Go", 2022),
    ("Entrée", "Lenovo", "ThinkCentre M70q Gen 4 Tiny", "i5-13400T", "10 c / 16 t", "1,3 – 4,4 GHz",
     "16 Go / 512 Go", "Home", 799, "Lenovo ThinkCentre M70q Gen 4 i5-13400T 16 Go 512 Go", 2023),
    ("Entrée", "HP", "ProDesk 400 G9 SFF", "i5-13500", "14 c / 20 t", "2,5 – 4,8 GHz",
     "16 Go / 512 Go", "Pro", 799, "HP ProDesk 400 G9 SFF i5-13500 16 Go 512 Go", 2022),
    ("Moyenne", "Dell", "OptiPlex 7020 SFF", "i5-14500", "14 c / 20 t", "2,5 – 5,0 GHz",
     "16 Go / 512 Go", "Pro", 999, "Dell OptiPlex 7020 SFF i5-14500 16 Go 512 Go", 2024),
    ("Moyenne", "Lenovo", "ThinkCentre M70t Gen 5 Tower", "i5-14500", "14 c / 20 t",
     "2,5 – 5,0 GHz", "16 Go / 512 Go", "Pro", 899,
     "Lenovo ThinkCentre M70t Gen 5 i5-14500 16 Go 512 Go", 2024),
    ("Moyenne", "HP", "EliteDesk 800 G9 SFF", "i5-13500", "14 c / 20 t", "2,5 – 4,8 GHz",
     "16 Go / 512 Go", "Pro", 1099, "HP EliteDesk 800 G9 SFF i5-13500 16 Go 512 Go", 2022),
    ("Haute", "HP", "Z2 G9 SFF station", "i5-13500", "14 c / 20 t", "2,5 – 4,8 GHz",
     "16 Go / 512 Go", "Pro", 1399, "HP Z2 G9 SFF i5-13500 16 Go 512 Go", 2022),
    ("Haute", "Lenovo", "ThinkStation P3 Tiny Gen 2", "i5-14500T", "14 c / 20 t", "2,1 – 5,0 GHz",
     "16 Go / 512 Go", "Pro", 1299, "Lenovo ThinkStation P3 Tiny Gen 2 i5-14500T 16 Go 512 Go", 2024),
    ("Haute", "Dell", "Precision 3680 Tower", "i5-14500", "14 c / 20 t", "2,6 – 5,0 GHz",
     "16 Go / 512 Go", "Pro", 1599, "Dell Precision 3680 Tower i5-14500 16 Go 512 Go", 2024),
]

TIER_FMT = {"Entrée": "g", "Moyenne": "y", "Haute": "o"}


def table_machines(titre_intro, data, first, tier_ranges, caption, num, notes):
    doc.landscape(True)
    doc.h1(num[0], num[1])
    doc.p(titre_intro, small=True)

    heads = ["**Marque**", "**Modèle**", "**Année**", "**Tranche**", "**Processeur**",
             "**Cœurs / threads · fréquences**", "**RAM / SSD**", "**OS**", "**Prix**",
             "**Amazon**", "**Fnac**", "**Cdiscount**", "**LDLC**", "**Matériel.net**"]
    rows, cf = [], {}
    for i, (tranche, marque, modele, cpu, cores, freq, rssd, os, prix, q, annee) in enumerate(data):
        L = liens(q, f"{marque} {modele}")
        rows.append([f"**{marque}**", f"**{modele}**", str(annee), tranche, cpu,
                     f"{cores}\n{freq}", rssd,
                     "**Pro**" if os == "Pro" else "**Home ⚠**", f"**{eur(prix)}**",
                     f"[Amazon]({L['Amazon']})", f"[Fnac]({L['Fnac']})",
                     f"[Cdiscount]({L['Cdiscount']})", f"[LDLC]({L['LDLC']})",
                     f"[Matériel]({L['Materiel.net']})"])
        cf[(i, 3)] = FMT[TIER_FMT[tranche]]
        cf[(i, 7)] = FMT["g"] if os == "Pro" else FMT["h"]
        cf[(i, 8)] = FMT[TIER_FMT[tranche]]
        if annee < 2024:
            cf[(i, 2)] = FMT["n"]

    doc.table(heads, rows,
              widths=[1.4, 2.45, 1.35, 1.75, 2.45, 2.75, 2.15, 1.6, 1.65,
                      1.45, 1.1, 1.75, 1.25, 2.15],
              font=7.3,
              aligns=["l", "l", "c", "c", "l", "c", "c", "c", "r",
                      "c", "c", "c", "c", "c"],
              caption=f"{tab()} — {caption} {tier_ranges}",
              cell_fmt=cf, zebra=False)

    doc.table(["", "", ""],
              [[notes[0], notes[1], notes[2]]],
              widths=[8.6, 8.6, 8.7], font=8.4, header=False, zebra=False,
              cell_fmt={(0, 0): FMT["i"], (0, 1): FMT["i"], (0, 2): FMT["i"]})

    doc.p("**Ce que le tableau ne dit pas.** Les prix sont des constats de novembre 2026 sur les "
          "grandes surfaces techniques : ils sont TTC, hors écran, et bougent de 10 à 15 % en une "
          "saison ; chaque lien "
          "mène à la recherche du modèle exact chez le distributeur, où le prix du jour est "
          "affiché. Les 512 Go affichés sont bien les 500 Go du cahier des charges (capacité "
          "commerciale contre capacité décimale). L'année est celle du millésime de la plateforme ; "
          "en gris, celles qui précèdent 2024. La colonne OS distingue **Windows 11 Professionnel** (vert) de **Windows 11 "
          "Famille** (rouge) : c'est la seule ligne qui justifie un arbitrage autre que le prix.",
          small=True)

    if first == "fixe":
        doc.p("**Les deux spécialistes ne vendent presque que du Lenovo en fixe professionnel.** "
              "Chez LDLC comme chez Materiel.net, le neuf en bureau se limite à Lenovo et à "
              "quelques HP ; Dell, Fujitsu et la plupart des HP n'y figurent qu'en reconditionné. "
              "Les colonnes LDLC et Materiel.net servent donc à comparer et à vérifier une "
              "configuration, pas toujours à commander : pour ces marques, les trois places de "
              "marché sont les seules à proposer du neuf.", small=True)

    if first == "portable":
        doc.p("**Comment lire les liens.** Chaque cellule ouvre une recherche sur le modèle chez le "
              "distributeur — amazon.fr/s?k=… , fnac.com/SearchResult… , cdiscount.com/search/10/… , "
              "ldlc.com/recherche/… , materiel.net/recherche/… . Sur les trois places de marché, la "
              "requête inclut la configuration (processeur, mémoire, disque) pour écarter les "
              "modèles voisins ; chez LDLC et Materiel.net, elle se limite à la référence, leurs "
              "filtres étant plus fiables que le texte libre. Le lien ne fige pas un prix : il "
              "ouvre la fiche du jour, avec le stock et la configuration réellement vendue. C'est "
              "volontaire — une URL de fiche produit expire en quelques semaines, une URL de "
              "recherche tient des années.", small=True)


# --------------------------------------------------------------------------- #
doc.cover(
    eyebrow="Matériel de travail — 2024 minimum",
    title="Portables et fixes :\ntrois tranches, cinq distributeurs",
    subtitle="Dix-huit modèles du millésime 2022 au millésime 2024, 16 Go de mémoire et "
             "500 Go de SSD au minimum, "
             "critères justifiés un par un, et cinq liens d'achat français par machine.",
    meta_rows=[
        ["Rédaction", "**GED-SERVICES** — note de prescription, rédaction impersonnelle"],
        ["Périmètre", "**9 portables** et **9 fixes** répartis en **trois tranches de prix** "
                      "(entrée, moyenne, haute), chez **cinq constructeurs**"],
        ["Exigences minimales", "**2024 minimum** · **i5 ou Core Ultra 5 minimum** · **16 Go** · "
                                "**SSD 500 Go** · **Windows 11 Pro** (Famille toléré, signalé)"],
        ["Distributeurs", "**Amazon.fr · Fnac · Cdiscount · LDLC · Materiel.net** — une recherche "
                          "ciblée sur le modèle exact pour chacun"],
        ["Livrables", "Word (.docx) et PDF identiques, produits depuis la même source"],
        ["Date", "6 novembre 2026"],
    ],
    summary=("Les trois tableaux",
             "**Tableau 3 — portables** et **tableau 4 — fixes** : neuf modèles chacun, trois "
             "tranches, cinq distributeurs. **Tableau 5 — synthèse** : ce que chaque tranche "
             "achète réellement, et pour quel usage. Les critères sont expliqués séparément au "
             "chapitre 1, y compris la différence entre **i5 et Core Ultra 5**.", "info"),
)

# --------------------------------------------------------------------------- #
doc.h1("1", "Les critères, et pourquoi ceux-là")

doc.p("Chaque exigence a un coût et une justification. Le tableau les reprend une par une, avec "
      "le seuil retenu, la raison, et l'endroit de la fiche technique où le vérifier — parce que "
      "les mentions commerciales masquent souvent l'essentiel.", lead=True)

doc.table(
    ["Critère", "Seuil retenu", "Pourquoi ce seuil", "Où le vérifier"],
    [
        ["**Année**", "**2024 minimum** — 2022 toléré sur un fixe d'entrée",
         "Un poste acheté en 2026 et gardé cinq ans sort du parc en 2031 : une plateforme de 2022 "
         "n'a plus que deux ans de mises à jour constructeur devant elle, une de 2024 en a quatre. "
         "Le millésime compte plus que la date d'achat",
         "Le millésime du modèle — colonne **Année** du tableau —, pas la date de la boîte"],
        ["**Processeur**", "**i5 ou Core Ultra 5 minimum**",
         "En dessous (i3, Ryzen 3, N100), la machine est déjà lente à l'ouverture de Windows et "
         "ne tient pas trois ans de bureautique chargée + visioconférence",
         "Le nom complet du CPU, avec son suffixe"],
        ["**Fréquences**", "**Turbo ≥ 4,3 GHz**, base ≥ 1,3 GHz (portable) / ≥ 2,5 GHz (fixe)",
         "La fréquence de base est celle du repos ; c'est le **turbo** qui décide de la réactivité "
         "perçue. Sur un portable, la fréquence soutenue dépend surtout du refroidissement",
         "Fiche Intel ou Ark : « Max Turbo Frequency »"],
        ["**Cœurs**", "**≥ 10 cœurs** sur portable, **≥ 6** sur fixe",
         "Dix cœurs (2 performants + 8 efficients) suffisent à Windows 11 et à la bureautique "
         "moderne ; en dessous de 6, l'encodage et les mises à jour bloquent la machine",
         "« Cœurs / threads », pas « cœurs logiques »"],
        ["**Mémoire**", "**16 Go minimum**",
         "8 Go obligent Windows à paginer dès qu'un navigateur à dix onglets et Teams coexistent. "
         "16 Go est le plancher de 2026, et le restera jusqu'en 2029",
         "« 16 Go soudés » ou « 1 × 16 Go, 1 emplacement libre »"],
        ["**Disque**", "**SSD 500 Go NVMe**",
         "256 Go se remplissent en dix-huit mois entre Windows, Office et les profils ; 500 Go "
         "laissent de la marge sans changer le prix d'achat. En rayon, la capacité vendue est "
         "512 Go : c'est la même chose, la différence est commerciale (500 × 10⁹ octets)",
         "Type (NVMe, pas eMMC) et interface (PCIe)"],
        ["**OS**", "**Windows 11 Professionnel** — Famille toléré, signalé",
         "Pro donne BitLocker, l'inscription à Entra ID, le Bureau à distance hôte et les "
         "stratégies de groupe : sans cela, la machine ne s'administre pas. Famille coûte 100 à "
         "150 € de moins mais se met à niveau pour ~145 €",
         "La mention exacte : « Windows 11 Professionnel », pas « Windows 11 »"],
        ["**Écran / format**", "14 à 15,6 pouces, **IPS Full HD minimum**",
         "Les dalles TN 1 366 × 768 encore vendues en entrée de gamme sont inutilisables huit "
         "heures par jour", "Résolution et technologie de dalle"],
        ["**Garantie**", "**3 ans sur site** pour un parc professionnel",
         "C'est le vrai écart entre entrée et moyenne gamme : au-delà du matériel, c'est le "
         "délai de remise en service qui coûte", "Le contrat, pas la durée de la boîte"],
    ],
    widths=[2.6, 3.6, 7.4, 3.4], font=8.2, aligns=["l", "l", "l", "l"],
    caption=f"{tab()} — Les neuf critères de sélection, leur seuil et leur justification.",
    cell_fmt={(1, 0): FMT["g"], (6, 0): FMT["g"], (3, 0): FMT["y"]}, zebra=True)

# --------------------------------------------------------------------------- #
doc.p("**Ce que la sélection écarte, sans exception.**", small=True)
doc.ul([
    "**Le reconditionné**, même récent : un OptiPlex de 2019 à 250 € tient deux ans, pas cinq, "
    "et sa garantie de 6 à 12 mois est déjà écoulée quand la première panne arrive.",
    "**Les i3, Ryzen 3 et tout processeur mobile de 11e ou 12e génération** : suffisants pour "
    "Excel seul, insuffisants dès que Windows 11, Teams et un antivirus cohabitent.",
    "**Les 8 Go soudés et les disques eMMC** : aucune évolution possible, le poste est à "
    "remplacer à la première saturation — c'est-à-dire en dix-huit mois.",
    "**Les dalles TN 1 366 × 768 et les garanties d'un an en retour atelier** : la dalle fatigue "
    "les yeux huit heures par jour, et l'atelier coûte 10 à 15 jours d'immobilisation par incident.",
])

doc.h1("2", "i5 ou Core Ultra 5 : la question mérite une réponse chiffrée")

doc.p("Depuis fin 2023, Intel a renommé ses processeurs : « Core Ultra 5 » remplace « Core i5 » sur "
      "les machines récentes. Ce n'est pas un simple changement d'étiquette — l'architecture "
      "change en même temps. Voici ce que cela implique concrètement pour un achat 2026.", lead=True)

doc.table(
    ["Point de comparaison", "Core i5-1335U", "Core Ultra 5 125U", "Core Ultra 5 125H"],
    [
        ["Famille / gravure", "Raptor Lake (2023) · Intel 7", "Meteor Lake (2024) · Intel 4",
         "Meteor Lake (2024) · Intel 4"],
        ["Cœurs / threads", "**10 / 12** (2 P + 8 E)", "**12 / 14** (2 P + 8 E + 2 LPE)",
         "**14 / 18** (4 P + 8 E + 2 LPE)"],
        ["Fréquences", "1,3 – **4,6 GHz**", "1,3 – **4,3 GHz**", "1,3 – **4,5 GHz**"],
        ["Enveloppe (TDP)", "15 W (28 W en pointe)", "15 W (57 W en pointe)", "**28 W** (115 W en pointe)"],
        ["Carte graphique", "Intel Iris Xe (80 EU)", "**Intel Arc (4 cœurs Xe)**", "**Intel Arc (7 cœurs Xe)**"],
        ["NPU (calcul IA local)", "**aucun**", "**oui** (~11 TOPS)", "**oui** (~11 TOPS)"],
        ["Autonomie typique", "6 – 8 h", "**9 – 12 h**", "6 – 8 h"],
        ["Prix du poste complet", "le plus bas", "+ 100 à 200 €", "+ 150 à 300 €"],
        ["Verdict", "**Acceptable** : le meilleur rapport prix / performance en bureautique",
         "**Le choix par défaut de 2026** : même puissance, 30 % d'autonomie en plus",
         "**Seulement si** le poste fait du calcul (CAO légère, montage, tableurs lourds)"],
    ],
    widths=[3.6, 4.4, 4.5, 4.5], font=8.0, aligns=["l", "l", "l", "l"],
    caption=f"{tab()} — Les trois processeurs qui se rencontrent réellement dans cette gamme de "
            "prix. « U5 » désigne bien Core Ultra 5, pas le suffixe « U » des puces basse "
            "consommation — les deux se cumulent dans « Ultra 5 125U ».",
    cell_fmt={(8, 1): FMT["g"], (8, 2): FMT["g"], (8, 3): FMT["y"]}, zebra=True)

doc.p("**La réponse courte.** « i5 minimum » et « Core Ultra 5 minimum » désignent le même niveau "
      "de gamme à deux générations d'écart. Un **i5 de 13e génération (1335U)** reste parfaitement "
      "acceptable et coûte 100 à 200 € de moins ; un **Core Ultra 5** apporte surtout de "
      "l'autonomie et un moteur graphique supérieur, pas un surplus de vitesse en bureautique. Ce "
      "qu'il faut refuser, c'est un **i5 de 12e génération (1235U)** ou un i3 : la machine est "
      "vendue neuve mais conçue en 2022.", small=True)

doc.callout("Le suffixe compte autant que le numéro",
            "**U** = basse consommation, 15 W : autonomie, mais fréquence soutenue modeste. "
            "**H** = 28 à 45 W : plus rapide, deux fois plus gourmand, ventilateur audible. "
            "**T** (fixes) = 35 W, la version économe des processeurs de bureau. **P/G** = "
            "gravure haut de gamme, rare dans ces budgets. Sur un poste de bureautique, un **U** "
            "bien refroidi bat un **H** bridé par un châssis trop fin.", "warn")

doc.p("**Et le i5-13420H du V15, à 599 € ?** C'est le seul **H** du tableau : 8 cœurs (4 "
      "performants + 4 efficaces), 12 threads, 45 W, 4,6 GHz en pointe. Sur le papier il bat le "
      "1335U en pointe ; dans un châssis de 1,7 kg à 599 €, il chauffe, le ventilateur se fait "
      "entendre dès la deuxième visioconférence et l'autonomie tombe à 4 heures. C'est un choix "
      "assumé pour un poste sédentaire : à ce prix, on achète de la puissance, pas de la mobilité.",
      small=True)

# --------------------------------------------------------------------------- #
table_machines(
    "Trois tranches, trois modèles par tranche, chez quatre constructeurs (la marque est en "
    "première colonne). Tous les "
    "modèles respectent le plancher : 2024 ou plus récent, 16 Go, 500 Go, écran IPS Full HD. La "
    "tranche ne change pas la puissance de bureautique — elle change la qualité du châssis, "
    "l'autonomie, la garantie et la durée de vie.",
    PORTABLES,
    "portable",
    "**Entrée 599–749 €** · **moyenne 949–1 049 €** · **haute 1 449–1 599 €**",
    "Neuf portables, trois tranches de prix.",
    ("3", "Les portables, trois tranches, cinq distributeurs"),
    ("**Entrée — le compromis.** Châssis plastique, garantie 1 an, 5 à 6 h d'autonomie. "
     "Windows Famille sur deux des trois modèles : +145 € pour passer en Pro.",
     "**Moyenne — le standard.** Aluminium, Core Ultra 5, 9 à 12 h, garantie 3 ans sur site. "
     "C'est la tranche où le prix payé se transforme en années de service.",
     "**Haute — l'investissement.** 1,3 kg, écran 400 nits, vPro, 3 ans sur site J+1. "
     "On paie la mobilité et l'administration, pas la bureautique."))

table_machines(
    "Mêmes exigences, format bureau : le fixe coûte 20 à 30 % moins cher qu'un portable "
    "équivalent, pour une puissance supérieure et une durée de vie plus longue. SFF = petit "
    "format (7 à 10 litres), Tiny = 1 litre, Tower = tour. Les quatre constructeurs se "
    "partagent les tranches comme sur les portables.",
    FIXES,
    "fixe",
    "**Entrée 749–799 €** · **moyenne 899–1 099 €** · **haute 1 299–1 599 €**",
    "Neuf fixes, trois tranches de prix.",
    ("4", "Les fixes, trois tranches, cinq distributeurs"),
    ("**Entrée — le suffisant.** SFF 6 cœurs, 1 an de garantie, deux emplacements mémoire : "
     "le poste qui couvre déjà 90 % des tâches de bureau.",
     "**Moyenne — le standard.** 14 cœurs / 20 threads, 3 ans sur site, alimentation 80+ Gold. "
     "Le même prix qu'un portable d'entrée, deux fois plus de puissance.",
     "**Haute — la marge.** Châssis de station de travail (Z2, Precision), alimentation large, "
     "emplacements GPU et jusqu'à 5 ans de pièces."))

# --------------------------------------------------------------------------- #
doc.landscape(False)
doc.h1("5", "Ce que chaque tranche achète réellement")

doc.table(
    ["Tranche", "Portable — ce que vous obtenez", "Fixe — ce que vous obtenez", "Pour qui",
     "Ce qu'il faut vérifier"],
    [
        ["**Entrée**\n599–799 €", "Châssis plastique, garantie 1 an, écran IPS correct, "
                                    "autonomie 5 – 6 h, processeur i5 de 13e génération",
         "Boîtier SFF, 6 cœurs de bureau, extensible (2 emplacements RAM, 3,5 pouces)",
         "Poste nominal : bureautique, navigateur, visioconférence",
         "**Windows Famille** est fréquent ici — la mise à niveau Pro coûte ~145 €"],
        ["**Moyenne**\n899–1 099 €", "Châssis aluminium, Core Ultra 5, 9 – 12 h d'autonomie, "
                                      "garantie 3 ans sur site, clavier rétroéclairé",
         "14 cœurs, 20 threads, 3 ans sur site, alimentation 80+ Gold",
         "**Le choix par défaut** : usage mixte, déplacements, parc de 5 à 50 postes",
         "Le contrat de garantie (sur site vs retour atelier), la mémoire soudée ou non"],
        ["**Haute**\n1 299–1 599 €", "Châssis renforcé, écran 400 nits, lecteur d'empreintes, "
                                      "autonomie 12 h+, station d'accueil compatible",
         "Station de travail d'entrée : certifications ISV, alimentation et refroidissement "
         "dimensionnés pour 5 ans",
         "Poste nomade intensif, ou métier technique (CAO, calcul, gros tableurs)",
         "La certification ISV si un logiciel métier est concerné, sinon la dépense est "
         "difficile à justifier"],
    ],
    widths=[2.95, 4.0, 3.55, 2.9, 3.85], font=8.6, aligns=["l", "l", "l", "l", "l"],
    caption=f"{tab()} — Synthèse : ce que chaque tranche apporte, et le point à contrôler avant "
            "de commander.",
    cell_fmt={(0, 0): FMT["g"], (1, 0): FMT["y"], (2, 0): FMT["o"], (0, 4): FMT["h"]}, zebra=True)

doc.p("**L'écart de prix entre deux tranches n'est presque jamais un écart de processeur.** Entre "
      "un portable d'entrée à 749 € et un portable moyen à 1 049 €, les 300 € paient le châssis "
      "(aluminium au lieu de plastique), la garantie (3 ans sur site au lieu d'un an retour "
      "atelier), l'autonomie (10 h au lieu de 6) et le clavier. Le processeur, lui, est souvent "
      "le même Core Ultra 5. **Ce sont donc des euros de durée de vie, pas de vitesse.**", small=True)

doc.callout("Windows 11 Famille : le vrai piège de l'entrée de gamme",
            "Trois modèles du tableau sont vendus en **Windows 11 Famille** — ils sont signalés "
            "en rouge. Ce n'est pas rédhibitoire : la mise à niveau vers Professionnel coûte "
            "environ **145 €** (boutique Microsoft ou licence OEM), soit moins que l'écart de "
            "gamme. Mais il faut l'ajouter au prix affiché avant de comparer, et vérifier que la "
            "licence est **liée à la machine**, pas à un compte personnel. Sans mise à niveau : "
            "pas de BitLocker, pas d'inscription au domaine, pas de Bureau à distance entrant.",
            "warn")

doc.callout("Où le millésime 2024 n'est pas tenu",
            "Sur les dix-huit machines du tableau, six portables de moyenne et haute gamme et "
            "quatre fixes sont des plateformes 2024. Les autres — trois portables d'entrée (2023) "
            "et cinq fixes (2022-2023) — sont des générations antérieures, encore au catalogue et "
            "garanties par le constructeur, et portent le même processeur de 13e génération que "
            "leur successeur : c'est ce que 600 à 900 € achètent, un châssis plus ancien, pas une "
            "puce plus lente. Deux réserves. Le Fujitsu Esprimo est le seul poste en 12e génération "
            "(i5-12400) : acceptable sur un fixe à 749 €, à refuser au-delà. Et le millésime 2024 "
            "existe chez Lenovo — ThinkCentre M70q Gen 5, i5-13400T, 16 Go / 512 Go, Windows 11 "
            "Professionnel, relevé à **839,95 € chez LDLC**, soit 40 € de plus que le Gen 4 en "
            "Famille du tableau.", "info")

doc.p("**Trois phrases à faire figurer dans toute demande de prix**, quelle que soit la tranche.",
      small=True)
doc.ul([
    "« Processeur, mémoire, disque et système **tels que référencés au tableau** » — c'est ce "
    "qui empêche la substitution d'un 1235U à un 1335U ou d'un disque eMMC à un NVMe.",
    "« Garantie **3 ans sur site, J+1, pièces et main-d'œuvre** » — le retour atelier coûte "
    "10 à 15 jours d'immobilisation par incident, jamais chiffré dans le prix d'achat.",
    "« **Windows 11 Professionnel inclus**, licence liée à la machine » — la mention « Windows 11 » "
    "seule vaut Famille dans neuf cas sur dix.",
])

# --------------------------------------------------------------------------- #
doc.h1("6", "Acheter : cinq distributeurs, trois pièges")

doc.p("Les cinq distributeurs retenus ne se valent pas selon l'usage : les uns sont imbattables "
      "sur l'entrée de gamme, les autres sont les seuls à vendre les gammes professionnelles avec "
      "la garantie constructeur attachée.", small=True)

doc.table(
    ["Distributeur", "Ce qu'il apporte", "Le piège à connaître"],
    [
        ["**Amazon.fr**", "Le plus large choix, prix souvent les plus bas, retours simples",
         "Vendeurs tiers et **reconditionné** mélangés aux produits neufs : vérifier "
         "« Vendu et expédié par Amazon » et la mention « Neuf »"],
        ["**Fnac**", "Garantie et service après-vente en magasin, offres packagées",
         "Les modèles professionnels y sont rares ; les configurations affichées changent souvent"],
        ["**Cdiscount**", "Prix agressifs sur l'entrée de gamme, marketplace très large",
         "Beaucoup de **reconditionné** et de configurations anciennes présentées comme "
         "récentes : contrôler la génération du processeur"],
        ["**LDLC**", "Le meilleur pour les gammes pro : référence exacte, stock réel, "
                     "configuration détaillée",
         "Prix catalogue plus élevés que la marketplace — c'est le prix de la traçabilité"],
        ["**Materiel.net**", "Même groupe que LDLC, fiches techniques complètes, bon suivi",
         "Choix de modèles pro plus restreint ; comparer avec LDLC avant de commander"],
    ],
    widths=[3.0, 6.3, 7.7], font=8.2, aligns=["l", "l", "l"],
    caption=f"{tab()} — Les cinq distributeurs, ce qu'ils apportent et ce qu'il faut surveiller.",
    cell_fmt={(3, 0): FMT["g"], (4, 0): FMT["g"], (0, 2): FMT["y"], (2, 2): FMT["o"]}, zebra=True)

doc.ul([
    "**Piège n°1 — le reconditionné vendu à côté du neuf.** Sur les places de marché, la même "
    "page mélange des machine neuves et des machines « reconditionnées - très bon état » à 40 % "
    "de moins. Le tri se fait sur la mention « Neuf » et sur le vendeur, pas sur le prix.",
    "**Piège n°2 — la génération cachée.** Un « i5 » peut être un 8e génération de 2018. La "
    "seule parade : lire les quatre chiffres du modèle (1335U = 13e génération, 1235U = 12e, "
    "8250U = 8e) et refuser tout ce qui commence par 10 ou 11. Un 12e génération se tolère sur "
    "un seul cas, le fixe de bureau d'entrée, et pas au-delà de 750 €.",
    "**Piège n°3 — la garantie.** Une garantie « 2 ans » constructeur en retour atelier "
    "immobilise le poste 10 à 15 jours. Pour un parc, la garantie **3 ans sur site** vaut ses "
    "150 à 250 € de supplément : elle est incluse dans les gammes moyenne et haute des tableaux.",
])

doc.p("**Avertissement.** Les prix indiqués sont des constats de novembre 2026 sur les cinq "
      "distributeurs ; ils varient de 10 à 15 % selon les promotions et la disponibilité. Les "
      "liens ouvrent une **recherche sur le modèle exact** — le prix du jour et la configuration "
      "réellement en stock s'y trouvent. Aucun de ces montants n'est une offre ferme.", small=True)

doc.callout("Si c'était notre parc",
            "Pour dix postes, nous partirions sur **six fixes de moyenne gamme** (ThinkCentre M70t "
            "Gen 5 ou OptiPlex 7020, 899 à 999 €) et **quatre portables de moyenne gamme** "
            "(ThinkPad E14 Gen 6 ou ProBook 450 G11, 999 à 1 049 €), tous en Windows 11 "
            "Professionnel et garantis 3 ans sur site. Budget : **environ 9 800 € TTC** pour le "
            "parc, hors écrans et stations d'accueil. Les tranches d'entrée restent utiles pour "
            "les postes nomades occasionnels et les accueils ; la haute gamme ne se justifie que "
            "par un métier technique ou une exigence de mobilité.", "ok")

doc.save(OUT)
print("saved", OUT)
