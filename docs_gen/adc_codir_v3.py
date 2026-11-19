# -*- coding: utf-8 -*-
"""ADCHIM — note de synthèse Comité de direction, version 2026-11-19 (v3).

Cette version reprend la v2 (relevé d'incohérences interne, revue externe, prix
réconciliés, générations corrigées) et inverse la recommandation mémoire : le comité
voit d'abord la contrainte budgétaire, le double canal devenant un supplément arbitré
poste par poste. Tous les montants FCFA et les écarts sont calculés ici, jamais saisis.
"""
from __future__ import annotations

import os

from render import Doc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, os.environ.get("LIVRABLES_DIR",
                                           "estimations/version_2026-11-19"))
BASE = "ADC_Workstations_CODIR_v3_2026-11-19"

TVA = 655.957
VERT = "D8EDCB"
VERT_T = "1E6B33"
ORANGE = "FAEBB8"
ROUGE = "F8CDB6"
GRIS = "E9EBEF"
BLEU = "1F3B63"
FMT = {
    "v": {"bg": VERT, "color": VERT_T},
    "o": {"bg": ORANGE, "color": "7A5E12"},
    "r": {"bg": ROUGE, "color": "9B2C12"},
    "n": {"bg": GRIS, "color": "4A5058"},
}


# --------------------------------------------------------------------------- #
def _grp(n):
    out, i = "", 0
    for ch in reversed("%d" % n):
        if i and i % 3 == 0:
            out = "\u00A0" + out
        out = ch + out
        i += 1
    return out


def eur(x):
    if x is None:
        return "devis"
    ent, dec = ("%.2f" % x).split(".")
    return _grp(int(ent)) + "," + dec + "\u00A0€"


def fcfa(x):
    if x is None:
        return "—"
    return _grp(int(round(x * TVA))) + "\u00A0FCFA"


# --------------------------------------------------------------------------- #
# Gamme : constructeur, référence, voie, processeur, mémoire/stockage, prix, statut
ENTREE = [
    ("Lenovo", "ThinkCentre M70q Gen 5", "Intel", "Core i5-13500T",
     "16 Go DDR4 · 512 Go NVMe", 840.00, "v", "Retenu Intel"),
    ("Lenovo", "ThinkCentre M75q Gen 5", "AMD", "Ryzen 5 PRO 8500GE",
     "16 Go DDR5 · 512 Go NVMe", 849.00, "v", "Retenu AMD"),
    ("HP", "ProDesk 2 G1a (tour)", "AMD", "Ryzen 5 8500G",
     "16 Go DDR5 · 512 Go NVMe", 834.19, "o", "À vérifier"),
    ("HP", "Pro 400 G9 SFF", "Intel", "Core i5-13500",
     "16 Go DDR4 · 512 Go SATA", 943.61, "r", "Hors profil"),
    ("Dell", "OptiPlex 7010 Micro", "Intel", "Core i5-13500T",
     "16 Go DDR4 · 512 Go NVMe", 759.05, "r", "Recond."),
]

STANDARD = [
    ("Dell", "OptiPlex 7020 MFF", "Intel", "Core i5-14500T",
     "16 Go DDR5 · 512 Go NVMe", 999.95, "n", "Réf. prix"),
    ("HP", "Elite 800 G9 Mini", "Intel", "Core i5-14500",
     "16 Go DDR5 · 512 Go NVMe", 1055.99, "v", "Retenu — Intel"),
    ("Lenovo", "ThinkCentre M75q Gen 5", "AMD", "Ryzen 7 PRO 8700GE",
     "16 Go DDR5 · 512 Go NVMe", 1112.92, "v", "Retenu — AMD"),
    ("HP", "Elite 805 G9 SFF", "AMD", "Ryzen 7 8700G",
     "16 Go DDR5 · 512 Go NVMe", 1251.58, "o", "Hors couloir"),
    ("Lenovo", "ThinkCentre M90q Gen 5", "Intel", "Core i5-14500T",
     "16 Go DDR5 · 512 Go NVMe", 1470.45, "r", "Hors env."),
]

CONFORT = [
    ("HP", "Pro Mini 400 G9", "Intel", "Core i7-14700T",
     "16 Go DDR5 · 512 Go NVMe", 1109.30, "o", "Partiel"),
    ("HP", "Elite Desk 800 G9 (tour)", "Intel", "Core i7-14700",
     "16 Go DDR5 · 512 Go NVMe", 1363.75, "o", "16 Go seulement"),
    ("HP", "Elite 805 G9 SFF", "AMD", "Ryzen 7 8700G",
     "16 Go DDR5 · 512 Go NVMe", 1528.34, "r", "Hors enveloppe"),
    ("Lenovo", "ThinkCentre M90q Gen 6", "Intel", "Core Ultra 7 265",
     "configuration non publiée", 1624.88, "r", "Hors enveloppe"),
    ("Dell", "Pro Micro QCM1250", "Intel", "Core i7-14700T",
     "32 Go DDR5 · 1 To NVMe", None, "v", "Retenu · devis"),
    ("Lenovo", "ThinkCentre M75t Gen 5", "AMD", "Ryzen 7 PRO 8700G",
     "32 Go DDR5 · 1 To NVMe", None, "v", "Retenu — à chiffrer"),
]

GAMME_HEADERS = ["Constructeur", "Référence", "Voie", "Processeur", "Mémoire · stockage",
                 "Prix livré", "Statut"]
GAMME_WIDTHS = [2.5, 3.7, 1.2, 2.8, 2.8, 2.9, 1.7]
GAMME_ALIGNS = ["l", "l", "c", "l", "l", "r", "c"]

SEUILS = [
    ["Usage", "Accueil, saisie, consultation", "Sage, Teams, bureautique intensive, multitâche",
     "Gros tableurs, CAO légère, poste gardé longtemps"],
    ["Mémoire", "16 Go DDR4 ou DDR5, un emplacement libre",
     "16 Go DDR5 sur deux emplacements (plancher) — 32 Go en cible",
     "16 Go DDR5 minimum, deux emplacements — 32 Go en cible"],
    ["Stockage", "500 Go NVMe", "500 Go NVMe", "512 Go à 1 To NVMe"],
    ["Intel", "i5-13400 (10C) · i5-13500 (14C) — 13ᵉ gén., 2023",
     "i5-14400 (10C) · i5-14500 (14C) — 14ᵉ gén., 2024",
     "i7-14700 (20C) — 14ᵉ gén., 2024, ou plus récent"],
    ["AMD", "Ryzen 5 8500G · 8600G (6C) — Zen 4, 2024",
     "Ryzen 5 8600G (Zen 4) · 9600X (Zen 5) — 2024",
     "Ryzen 7 8700G (Zen 4) · 9700X (Zen 5) — 2024"],
    ["Graphique", "iGPU suffisant", "indifférent",
     "iGPU ; GPU dédié 6 Go si la CAO 3D entre au périmètre"],
    ["Système", "Windows 11 Professionnel", "Windows 11 Professionnel",
     "Windows 11 Professionnel"],
    ["Garantie", "3 ans sur site, pièces et main-d’œuvre", "3 ans sur site, pièces et main-d’œuvre",
     "3 ans sur site, pièces et main-d’œuvre"],
    ["Enveloppe", "650 – 850 €", "850 – 1 200 €", "1 200 – 1 350 €"],
]
SEUILS_WIDTHS = [2.6, 4.7, 5.0, 4.8]

CPU_HEADERS = ["Constructeur", "Processeur", "Génération · architecture", "Sortie",
               "Cœurs / threads", "Gamme"]
CPU_WIDTHS = [2.3, 3.5, 5.6, 1.5, 2.2, 2.0]
CPU_ROWS = [
    ["Intel", "Core i5-13400", "13ᵉ génération — Raptor Lake", "T1 2023", "10C / 16T",
     "Entrée"],
    ["Intel", "Core i5-13500", "13ᵉ génération — Raptor Lake", "T1 2023", "14C / 20T",
     "Entrée"],
    ["AMD", "Ryzen 5 8500G", "Ryzen 8000G — Zen 4 (AM5)", "T1 2024", "6C / 12T", "Entrée"],
    ["AMD", "Ryzen 5 8600G", "Ryzen 8000G — Zen 4 (AM5)", "T1 2024", "6C / 12T",
     "Entrée · standard"],
    ["Intel", "Core i5-14400", "14ᵉ génération — Raptor Lake Refresh", "T1 2024", "10C / 16T",
     "Standard"],
    ["Intel", "Core i5-14500", "14ᵉ génération — Raptor Lake Refresh", "T1 2024", "14C / 20T",
     "Standard"],
    ["AMD", "Ryzen 5 9600X", "Ryzen 9000 — Zen 5 (AM5)", "T3 2024", "6C / 12T", "Standard"],
    ["Intel", "Core i7-14700", "14ᵉ génération — Raptor Lake Refresh", "T1 2024", "20C / 28T",
     "Confort"],
    ["AMD", "Ryzen 7 8700G", "Ryzen 8000G — Zen 4 (AM5)", "T1 2024", "8C / 16T", "Confort"],
    ["AMD", "Ryzen 7 9700X", "Ryzen 9000 — Zen 5 (AM5)", "T3 2024", "8C / 16T", "Confort"],
    ["Intel", "Core Ultra 7 265", "Core Ultra série 2 — Arrow Lake", "T1 2025", "20C / 20T",
     "Confort (hors env.)"],
]

CHASSIS_HEADERS = ["Format", "Caractéristiques", "Évolutivité", "Usage privilégié",
                   "Prix constatés"]
CHASSIS_WIDTHS = [2.5, 4.1, 4.6, 3.4, 2.3]
CHASSIS_ROWS = [
    ["Mini · Micro · MFF", "Très compact (1 à 2 litres), alimentation externe",
     "Très limitée : pas de carte graphique de CAO. Mémoire et disque restent remplaçables.",
     "Accueil, bureautique, poste standard", "759 → 1 470 €"],
    ["SFF", "Boîtier de bureau compact (7 à 9 litres), alimentation interne",
     "Intermédiaire : un logement PCIe bas profil selon modèle, alimentation souvent "
     "limitante.", "Bureautique avancée, extensions légères", "944 → 1 528 €"],
    ["Tour", "Tour de bureau (15 litres et plus)",
     "Élevée : PCIe pleine hauteur, carte graphique et disques supplémentaires possibles.",
     "Postes évolutifs, CAO, gros stockage", "834 → 2 111 €"],
]

OPTIONS_32 = [
    ["A", "2 × 8 Go", "Double canal dès la commande ; les deux barrettes à remplacer",
     "Kit de 2 × 16 Go ≈ 500 €", "≈ %s" % eur(1112.92 + 500)],
    ["B", "1 × 16 Go", "Simple canal à 16 Go ; second emplacement libre",
     "1 barrette de 16 Go ≈ 250 €", "≈ %s" % eur(1112.92 + 250)],
    ["C", "32 Go d’origine, sur devis", "Conforme à la cible, double canal",
     "Aucune extension à prévoir", "à chiffrer"],
]

ANX = [
    ["Génération du i5-13500", "classé 14ᵉ génération au tableau des seuils",
     "13ᵉ génération, partout"],
    ["Ryzen 7 9700X", "placé sur la ligne 2025", "2024, Zen 5, ligne dédiée"],
    ["Familles AMD", "8500G, 8600G et 9600X dans la même colonne",
     "Zen 4 et Zen 5 distingués, processeur par processeur"],
    ["Double canal contre barrette unique", "double canal exigé, barrette unique recommandée",
     "1 × 16 Go à la commande, second emplacement libre ; double canal en supplément "
     "(section 6)"],
    ["Perte de performance en simple canal",
     "« 15 à 20 % » présentés comme systématiques",
     "perte de bande passante, effet variable selon les applications"],
    ["Mini et PCIe", "« aucun logement PCIe exploitable »",
     "extensions graphiques très limitées ; SFF à vérifier (alimentation, longueur)"],
    ["Obsolescence", "sortie du processeur + 5 ans = fin de vie du poste",
     "deux dates : âge de la plateforme, et horizon de remplacement du poste"],
    ["Prix du M75q en entrée", "849,00 € au tableau, 763,67 € en commentaire",
     "849,00 €, partout"],
    ["Prix du M75q en standard", "1 112,92 / 1 112,95 / 1 139,49 € selon la page",
     "1 112,92 €, partout"],
    ["Prix de l’Elite 800 G9 Mini", "1 055,99 € au tableau, 1 140,18 € en recommandation",
     "1 055,99 €, partout"],
    ["Dell OptiPlex 7020", "MFF au tableau, SFF en recommandation",
     "MFF : micro d’entreprise"],
    ["Conversion FCFA du HP tour", "873 604 FCFA pour 1 363,75 €", "894 561 FCFA"],
    ["Face-à-face Intel / AMD", "commentaires portés sur d’anciens écarts",
     "écarts et commentaires recalculés"],
    ["Gamme confort", "32 Go / 1 To présentés comme le minimum",
     "plancher à 16 Go, cible à 32 Go, coût de la cible assumé"],
    ["Livraison", "exclue en couverture, incluse dans « prix livré »",
     "prix TTC port compris ; l’enveloppe inclut la livraison, exclut écran et clavier"],
    ["Remise constructeur", "15 à 25 % présentés comme acquis",
     "hypothèse de négociation, à obtenir au devis"],
    ["Conversion FCFA", "« les francs sont exacts, les euros ne le sont pas »",
     "taux fixe ; c’est le prix en euros qui évolue"],
    ["Numérotation", "renvois décalés d’une section, paysage annoncé aux mauvaises pages",
     "sections renumérotées, aucun renvoi faux"],
]
ANX_HEADERS = ["Point", "Version du 19 novembre (v1)", "Cette version"]
ANX_WIDTHS = [3.6, 6.6, 6.9]


# --------------------------------------------------------------------------- #
def _gamme_table(doc, rows):
    body, cf = [], {}
    for i, (cons, ref, voie, cpu, conf, prix, col, statut) in enumerate(rows):
        pcell = ("**sur devis**" if prix is None
                 else "**%s**\n%s" % (eur(prix), fcfa(prix)))
        body.append([cons, ref, voie, cpu, conf, pcell, statut])
        cf[(i, 2)] = {"bg": "EDE3F2" if voie == "AMD" else "E3ECF7", "b": True}
        cf[(i, 6)] = FMT[col]
        if col == "v":
            for j in (0, 1, 3, 4):
                cf[(i, j)] = {"bg": VERT, "color": VERT_T}
            cf[(i, 1)] = {"bg": VERT, "b": True, "color": VERT_T}
    doc.table(GAMME_HEADERS, body, GAMME_WIDTHS, font=7.9, aligns=GAMME_ALIGNS,
              cell_fmt=cf, header_bg=BLEU)


def build_doc():
    doc = Doc(
        base=BASE,
        title="ADCHIM — standardisation des postes fixes",
        subtitle="Note de synthèse au comité de direction — version 2026-11-19 (v3)",
        meta=[],
        doc_ref="GED-SERVICES · note de synthèse CODIR · version 2026-11-19 (v3)",
        footer="GED-SERVICES · ADCHIM · standardisation des postes fixes · v3 du 19/11/2026",
    )

    doc.cover(
        eyebrow="Note de synthèse · comité de direction · ADCHIM",
        title="Standardiser\nles postes fixes",
        subtitle="Trois gammes, deux plateformes, un standard d’achat. Ce que le comité doit "
                 "valider, ce qu’il reste à arbitrer, et ce que cette version corrige par "
                 "rapport à la note du 19 novembre — mémoire comprise.",
        meta_rows=[
            ["Date", "**19 novembre 2026** — version 2026-11-19 (v3)"],
            ["Émetteur", "**Joël MBA OYONE**, prestataire informatique — GED-SERVICES"],
            ["Destinataire", "**Comité de direction d’ADCHIM**"],
            ["Objet", "Définir les standards matériels des postes fixes et arbitrer les trois "
                      "gammes"],
            ["Enveloppe", "**650 € à 1 350 €** par poste, livraison comprise, écran et clavier "
                          "exclus"],
            ["Version", "Intègre le relevé d’incohérences interne et la revue externe du "
                        "19 novembre, et retient le 1 × 16 Go comme configuration de commande "
                        "— détail en annexe A"],
        ],
    )

    # ------------------------------------------------------------------ 1
    doc.h1_plain("1. Philosophie et principes de sélection")
    doc.p("La démarche ne consiste pas à choisir un ordinateur, mais à fixer un standard : un "
          "poste que l’on peut acheter en série, à un prix tenu, et dont on sait quand il "
          "faudra le remplacer. Trois principes la structurent, et une précaution de lecture "
          "la protège.", lead=True)
    doc.p("**1. L’adéquation aux usages.** Trois niveaux suffisent : l’accueil et la saisie, la "
          "bureautique intensive — Sage, Teams, plusieurs applications ouvertes à la fois —, et "
          "les usages plus exigeants, gros tableurs et CAO légère. Un poste unique pour tous les "
          "usages coûte soit trop cher à l’accueil, soit du temps perdu à la comptabilité.",
          small=True)
    doc.p("**2. La pérennité.** Une plateforme récente — Intel 13ᵉ génération au minimum, AMD "
          "Zen 4 au minimum —, une mémoire extensible, un disque NVMe, et cinq ans de détention "
          "comme horizon de travail. C’est ce qui distingue un poste qui tient cinq ans d’un "
          "poste qu’on remplace au bout de trois.", small=True)
    doc.p("**3. La neutralité constructeur.** Intel et AMD sont comparés à époque comparable, "
          "avec deux références par constructeur et par voie. Aucune marque n’est imposée : "
          "c’est la configuration et le prix qui tranchent, pas le catalogue.", small=True)
    doc.p("**La précaution de lecture.** Les prix français sont des repères de marché, pas des "
          "engagements. La décision porte d’abord sur les caractéristiques attendues, puis sur "
          "les configurations disponibles et leur coût réel, une fois les devis en main.",
          small=True)
    doc.spacer(0.1)
    doc.table(["Gamme", "Usage", "Enveloppe"], [
        ["Entrée de gamme", "Accueil, saisie, consultation", "650 – 850 €"],
        ["Standard entreprise", "Bureautique intensive — Sage, Teams, multi-applications",
         "850 – 1 200 €"],
        ["Confort", "Gros tableurs, CAO légère, poste gardé longtemps", "1 200 – 1 350 €"],
    ], [3.6, 9.0, 4.5], font=8.4, aligns=["l", "l", "r"], first_col_bold=True,
        caption="Trois gammes, un couloir chacune : c’est le plus petit nombre qui permette de "
                "trancher poste par poste sans arbitrage au cas par cas.")
    doc.p("**Ce que cette synthèse ne tranche pas.** La volumétrie du parc — combien de postes "
          "par gamme — n’était pas dans la commande, et elle pèse plus lourd sur le prix final "
          "que le choix de la marque. Le choix des écrans et des claviers reste hors périmètre, "
          "comme la stratégie d’enlèvement. Ces trois points viendront avec les devis, pas "
          "avant.", small=True)
    doc.spacer(0.1)
    doc.callout(
        "À quoi sert cette section",
        "Elle fixe ce qui ne se renégocie pas à chaque commande. Une offre qui ne respecte pas "
        "ces trois principes ne s’instruit pas, quelle que soit sa remise ; une offre qui les "
        "respecte mais sort du couloir de sa gamme reste recevable — elle est signalée, pas "
        "écartée.", kind="info")

    doc.pagebreak()
    # ------------------------------------------------------------------ 2
    doc.h1_plain("2. Cibles techniques retenues")
    doc.p("C’est le référentiel de conformité : il dit, gamme par gamme, ce qu’une offre doit "
          "tenir pour être instruite.", small=True)
    doc.table(["Critère", "Entrée de gamme", "Standard entreprise", "Confort"], SEUILS,
              SEUILS_WIDTHS, font=8.0, aligns=["l", "l", "l", "l"], first_col_bold=True,
              caption="Le profil opposable, arrêté au 19 novembre 2026.")
    doc.spacer(0.15)
    doc.callout(
        "À quoi sert ce tableau",
        "Il transforme une préférence en critère. En séance, il permet de dire « cette offre "
        "est conforme » ou « il lui manque le NVMe » sans discussion d’opinion, et d’écarter "
        "sans état d’âme un i5 de 12ᵉ génération ou un disque SATA, quel que soit leur prix.")
    doc.p("**Le double canal, et la barrette unique.** À capacité égale, deux barrettes "
          "valent mieux qu’une : le contrôleur mémoire travaille sur un seul canal en 1 × 16 Go, "
          "et l’écart se voit en usage lourd et sur le graphique intégré — l’ampleur dépend des "
          "applications. Ce que le profil exige, c’est donc **16 Go sur deux emplacements**, et "
          "non une configuration figée à la livraison : un poste livré en 1 × 16 Go garde la "
          "possibilité d’un second canal. Le choix entre les deux à la commande est un "
          "arbitrage de coût, chiffré en section 6.", small=True)
    doc.p("**La DDR4 n’est tolérée qu’en entrée.** Au-delà, elle date la plateforme : c’est un "
          "critère d’écart entre deux offres, pas une disqualification technique. "
          "**Le format n’est pas un détail d’encombrement** : un mini ou un micro n’offre "
          "d’extension graphique que très limitée, et un SFF n’accepte pas automatiquement une "
          "carte de CAO 3D — il faut vérifier l’alimentation, la longueur et les connecteurs.",
          small=True)
    doc.p("**Deux dates, pas une.** L’année de sortie date la plateforme ; elle ne dit pas quand "
          "remplacer le poste. Un i5-13500 est né en 2023 : sa plateforme aura huit ans en 2031. "
          "Un poste mis en service en 2026-2027 et gardé cinq ans se remplace en 2031-2032, quel "
          "que soit son processeur. C’est cet horizon que je retiens pour la projection "
          "budgétaire ; l’âge de la puce, lui, sert à départager deux offres de même prix.",
          small=True)

    # ------------------------------------------------------------------ 3
    doc.pagebreak()
    doc.h1_plain("3. Cibles retenues, gamme par gamme")
    doc.p("Les lignes surlignées en vert sont les cibles retenues. Les autres restent au "
          "dossier : elles documentent le marché, et servent de levier quand un prix se "
          "dégrade.", small=True)

    doc.h2("3.1 Entrée de gamme — accueil, saisie, consultation")
    doc.p("**Objectif :** un poste économique et récent, pour les fonctions administratives "
          "simples et l’accueil. Cinq références chiffrées ; deux tiennent le profil.",
          small=True)
    _gamme_table(doc, ENTREE)
    doc.spacer(0.12)
    doc.p("**Orientation proposée.** Le **M75q Gen 5 en AMD (849,00 €)** pour sa DDR5 et son "
          "positionnement tarifaire, avec le **M70q Gen 5 en Intel (840,00 €)** comme alternative "
          "— même châssis, même famille, un seul jeu de pièces détachées. Le ProDesk 2 G1a est "
          "9 € moins cher mais vendu par un tiers, avec une garantie à sécuriser ; le Dell "
          "chiffré est un reconditionné, hors cible ; le Pro 400 G9 cumule DDR4, SATA et un "
          "dépassement de couloir.", small=True)
    doc.p("**Utilité du tableau.** Il montre que l’entrée de gamme est tenue par deux offres "
          "seulement, et que le moins cher n’est pas le meilleur : c’est ici que se joue le vrai "
          "arbitrage prix / conformité.", small=True)

    doc.spacer(0.25)
    doc.h2("3.2 Standard entreprise — gamme préférentielle")
    doc.p("**Objectif :** le standard principal du parc, pour la bureautique intensive. C’est la "
          "gamme qui portera le volume, donc celle où la seconde source compte le plus.",
          small=True)
    _gamme_table(doc, STANDARD)
    doc.spacer(0.12)
    doc.p("**Orientation proposée.** Le **M75q Gen 5 en AMD (1 112,92 €)** comme référence "
          "principale, le **HP Elite 800 G9 Mini (1 055,99 €)** comme seconde source, et le "
          "**Dell OptiPlex 7020 MFF (999,95 €)** comme référence tarifaire — 155 € de moins que "
          "le Lenovo, à 16 Go comme les autres. Le M90q Gen 5 sort de l’enveloppe de 120,45 € ; "
          "l’Elite 805 G9 dépasse le couloir de 51,58 € et arrive en clavier QWERTZ.", small=True)
    doc.p("**La cible 32 Go se paie en supplément** : une seconde barrette de 16 Go, ≈ 250 €, "
          "porte le poste à ≈ %s, soit %s au-dessus du plafond (option B, section 6)."
          % (eur(1112.92 + 250), eur(12.92)), small=True)
    doc.p("**Utilité du tableau.** Il désigne le standard du parc et vérifie qu’il existe "
          "toujours deux sources à peu près au même prix : c’est la condition pour ne pas être "
          "pris en défaut de livraison en cours d’année.", small=True)

    doc.h2("3.3 Confort — postes gardés cinq ans, CAO légère, gros tableurs")
    doc.p("**Objectif :** des postes plus pérennes, dimensionnés pour la mémoire et le stockage, "
          "avec une capacité graphique si la CAO 3D entre au périmètre. Le plancher de la gamme "
          "est de 16 Go ; la cible est de 32 Go et 1 To.", small=True)
    _gamme_table(doc, CONFORT)
    doc.spacer(0.12)
    doc.p("**Orientation proposée.** Conserver la gamme comme cible technique et **ne pas "
          "engager de commande avant devis** : les deux configurations qui tiennent le profil "
          "complet — Dell Pro Micro QCM1250 en Intel, Lenovo M75t Gen 5 en AMD — ne sont pas "
          "tarifées. Les quatre machines chiffrées sont soit à 16 Go, soit hors enveloppe. La "
          "compatibilité avec une carte graphique dédiée doit être confirmée au devis si la CAO "
          "3D reste au périmètre.", small=True)
    doc.p("**Utilité du tableau.** Il distingue ce qui est disponible de ce qui est seulement "
          "spécifié. C’est la gamme où la décision doit rester ouverte, et où le comité doit "
          "savoir qu’il achète aujourd’hui une intention, pas un prix.", small=True)

    doc.spacer(0.35)
    # ------------------------------------------------------------------ 4
    doc.h1_plain("4. Comparatif des processeurs Intel et AMD")
    doc.p("Les processeurs sont regroupés par génération commerciale, architecture, date de "
          "lancement et positionnement dans les trois gammes. Les dates sont celles des "
          "lancements constructeur, au trimestre près.", small=True)
    doc.table(CPU_HEADERS, CPU_ROWS, CPU_WIDTHS, font=7.8,
              aligns=["c", "l", "l", "c", "c", "l"], header_bg=BLEU,
              cell_fmt={(i, j): {"bg": VERT} for i in (4, 5, 6)
                        for j in range(len(CPU_HEADERS))},
              caption="En vert : la génération visée par la gamme standard — Intel 14ᵉ "
                      "génération et Ryzen 5 9600X (Zen 5).")
    doc.spacer(0.15)
    doc.callout(
        "À quoi sert ce tableau",
        "À répondre à la question qui revient toujours : « pourquoi pas le processeur le plus "
        "récent ? ». Parce qu’une génération de plus se paie 250 à 500 € et ne change rien à "
        "l’ouverture d’un classeur. Il sert aussi à éviter les comparaisons fausses : un Ryzen "
        "8000G (Zen 4) se compare à un Raptor Lake, pas à un Arrow Lake.")
    doc.p("**Générations ciblées.** Entrée : Intel 13ᵉ génération et Ryzen 8000G. Standard : "
          "Intel 14ᵉ génération, Ryzen 8000G et Ryzen 9000. Confort : Core i7 de 14ᵉ génération, "
          "Ryzen 7 8000G et 9000. Ces correspondances indiquent un positionnement de gamme et "
          "d’époque — **pas une équivalence de performance** : je ne dispose d’aucun test "
          "comparatif mené sur nos applications.", small=True)

    # ------------------------------------------------------------------ 5
    doc.spacer(0.35)
    doc.h1_plain("5. Comparatif des formats de châssis")
    doc.p("Le format décide de ce que le poste pourra recevoir pendant ses cinq ans de vie — "
          "pas seulement de la place qu’il occupe sous le bureau.", small=True)
    doc.table(CHASSIS_HEADERS, CHASSIS_ROWS, CHASSIS_WIDTHS, font=8.0,
              aligns=["l", "l", "l", "l", "c"], first_col_bold=True, header_bg=BLEU)
    doc.spacer(0.15)
    doc.callout(
        "À quoi sert ce tableau",
        "À trancher la seule vraie question de format : aura-t-on besoin d’une carte graphique "
        "dans les cinq ans ? Si non — c’est le cas de l’essentiel du parc —, le mini est le bon "
        "choix : il coûte 150 à 200 € de moins qu’un SFF à configuration voisine (HP standard : "
        "1 055,99 € en mini, 1 251,58 € en SFF) et se fixe sous le bureau. Si oui, il faut le "
        "SFF ou la tour, et l’assumer dès le devis.")
    doc.p("**Orientation.** Mini pour l’entrée et le standard ; SFF seulement si une extension "
          "légère est prévue ; tour pour le confort, seule à garantir l’ajout d’une carte "
          "graphique. Dans tous les cas, un second emplacement mémoire libre : c’est le seul "
          "« plus » technique qui se rattrape après coup, sans changer de machine. Le double "
          "canal dès la commande (2 × 8 Go) coûte 250 € de plus par poste et s’arbitre au cas "
          "par cas — section 6.", small=True)

    # ------------------------------------------------------------------ 6
    doc.pagebreak()
    doc.h1_plain("6. Arbitrages proposés au comité de direction")
    doc.p("**Six décisions, dont deux engagent un budget nouveau : le confort et la mémoire.**",
          lead=True)
    doc.ul([
        "**Valider les trois profils matériels** et leurs enveloppes : 650–850 €, 850–1 200 €, "
        "1 200–1 350 €.",
        "**Retenir le standard entreprise comme gamme préférentielle** du parc, avec le "
        "M75q Gen 5 en AMD et l’Elite 800 G9 Mini en Intel comme deux sources.",
        "**Autoriser la consultation tarifaire** sur ces deux références, et sur le Dell "
        "OptiPlex 7020 MFF comme référence de prix.",
        "**Maintenir l’entrée de gamme** pour les fonctions administratives simples, sur la "
        "base du M70q Gen 5 et du M75q Gen 5.",
        "**Reporter la validation du confort** jusqu’à obtention de devis répondant à la cible "
        "32 Go / 1 To.",
        "**Exiger au devis** : Windows 11 Professionnel, NVMe, garantie 3 ans sur site pièces "
        "et main-d’œuvre, et une configuration mémoire documentée.",
    ], numbered=True, small=True)

    doc.p("**L’arbitrage mémoire, chiffré.** Le standard est livré en 16 Go pour "
          "1 112,92 €. Trois façons d’aller à 32 Go, et trois coûts différents :", small=True)
    doc.table(["Option", "Livraison", "Effet", "Coût de l’extension", "Total indicatif"],
              OPTIONS_32, [1.6, 3.2, 4.0, 4.2, 4.0], font=8.0,
              aligns=["c", "l", "l", "l", "r"],
              caption="Prix de la barrette : ≈ 250 € au détail, à confirmer par devis "
                      "fournisseur. « ≈ » marque un ordre de prix, non un relevé.")
    doc.p("**Je recommande l’option B** pour le standard, et je commence par la contrainte "
          "budgétaire : livré en 1 × 16 Go, le poste tient la capacité, garde un emplacement "
          "libre, et la cible 32 Go s’atteint avec une seule barrette de 16 Go pour ≈ %s — "
          "soit %s au-dessus du plafond, là où l’option A en demande %s. La bande passante du "
          "simple canal est le prix de cet écart : elle se paie à l’usage et non à la "
          "facture, et l’ajout de la seconde barrette la rétablit en même temps qu’il porte le "
          "poste à 32 Go."
          % (eur(1112.92 + 250), eur(12.92), eur(262.92)), small=True)
    doc.p("**Le double canal devient l’exception, non le défaut.** L’option A — 2 × 8 Go dès la "
          "commande — reste disponible, mais elle coûte 250 € de plus par poste et fait sortir "
          "la cible 32 Go du plafond de %s. Elle se justifie poste par poste, pour les "
          "utilisateurs dont l’usage sature réellement 16 Go ; et pour ceux-là, l’option C — "
          "une machine livrée en 32 Go d’origine — vaut mieux qu’une extension après coup, "
          "laquelle coûte à elle seule près de la moitié d’un poste. **Ce que je ne recommande "
          "pas** : étendre l’entrée de gamme, où la mémoire n’est pas le facteur limitant ; ni "
          "commander le confort en l’état, aucune offre chiffrée ne tenant à la fois les 32 Go, "
          "le téraoctet et l’enveloppe."
          % eur(262.92), small=True)
    doc.spacer(0.2)
    doc.callout(
        "Décision sollicitée",
        "Validation des trois profils techniques et de leurs enveloppes ; autorisation de "
        "consulter sur les références prioritaires — Lenovo M75q Gen 5 en AMD, HP Elite 800 G9 "
        "Mini en Intel, Dell OptiPlex 7020 MFF — et sur le confort en 32 Go / 1 To ; "
        "configuration de commande du standard arrêtée en 1 × 16 Go, le double canal étant "
        "arbitré poste par poste ; report de toute commande jusqu’à réception des devis.",
        kind="warn")
    doc.spacer(0.3)
    doc.p("Joël MBA OYONE — GED-SERVICES, services informatiques · 19 novembre 2026", small=True)

    # ------------------------------------------------------------------ annexe
    doc.pagebreak()
    doc.h1_plain("Annexe A — ce que cette version corrige")
    doc.p("La note du 19 novembre a été relue deux fois : en interne, ligne à ligne, et par une "
          "revue externe. Voici ce qui a changé. Les tableaux et la logique d’arbitrage sont "
          "conservés ; ce sont les raccords qui ont été repris.", small=True)
    doc.table(ANX_HEADERS, ANX, ANX_WIDTHS, font=7.9, aligns=["l", "l", "l"],
              first_col_bold=True, header_bg=BLEU,
              caption="Dix-huit points corrigés. Les prix des trois références retenues sont "
                      "désormais identiques d’un bout à l’autre du document, et les conversions "
                      "FCFA sont recalculées au taux de 655,957.")
    doc.p("**Ce que la v3 change, et pourquoi.** La recommandation mémoire est inversée : "
          "l’option B (1 × 16 Go) devient la configuration de commande, l’option A (2 × 8 Go) "
          "passe du statut de défaut à celui de supplément arbitré poste par poste. Aucun "
          "chiffre technique ne change — c’est l’ordre des priorités qui change : le comité "
          "voit d’abord l’écart au plafond (12,92 € en option B, 262,92 € en option A), et la "
          "performance du double canal devient un choix instruit, non une exigence posée "
          "d’entrée. Les sections 2, 3.2 et 5 ont été réalignées sur cette recommandation.",
          small=True)
    doc.p("**Ce qui n’a pas changé.** Les recherches de marché, les références relevées et la "
          "structure en trois gammes : elles tiennent. La note complète du 19 novembre reste le "
          "document de référence pour le détail des 31 machines ; cette synthèse n’en garde que "
          "ce qui sert la décision.", small=True)

    dpath, ppath = doc.save(OUTDIR)
    return dpath, ppath


if __name__ == "__main__":
    print(build_doc())
