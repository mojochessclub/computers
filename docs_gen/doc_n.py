# -*- coding: utf-8 -*-
"""Version B — note comparative sur les postes fixes professionnels, à l'attention de Jad (ADCHIM).
Après fiabilisation de la première lecture : chiffres vérifiés, cohérence rétablie, panorama marché."""
import os
from render import Doc

BASE = "N_Note_a_Jad_postes_fixes_HP_Elite_800_G9_Mini_version_B"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables")

TVA = 655.957

ANNONCE = ("https://www.amazon.fr/HP-Elite-800-Bluetooth-Dual-Mode/dp/B0D76M6T6R"
           "/ref=sr_1_1?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2GE6XFUEQK18I"
           "&dib=eyJ2IjoiMSJ9.-vcz4wq2A5rCSIf9H15i0f8IW3FCD6CJBj6raRO-W4mOCiUtV9s6qODIQP4-ous2nt1m"
           "XshNvmoSL-JVpf21iiDGG_h8V3ymUNiEtqhs3VQbi4s3jECRua3ksbes4fpUGnH4jj-0Y2Ew3HhV_xHnTmBO2aS"
           "_XZwWkyNYzlz9L2d3i26qLI-uKlSrsWR1Jl0ofMRPhZ2k855Ybo-INjQ4zZIqyJUpz-Kf1m8teIJTw_FihUsxvLD3"
           "JL4LybcYF94H-sSmUWtUXtelhpcLYYxan9yPGtHz9zIFy5xH0tNYgSg.7sXacdWwiD6ugZDpdRHsnzy9yfJI7O1"
           "Vo2qz58JvSjI&dib_tag=se&keywords=HP+Elite+800+G9+Mini+%E2%80%93+i5-14500&qid=1794193668"
           "&s=computers&sprefix=hp+elite+800+g9+mini+i5-14500%2Ccomputers%2C298&sr=1-1")

doc = Doc(
    base=BASE,
    title="Postes fixes professionnels : étude comparative et recommandation",
    subtitle="À l'attention de Jad, directeur général d'ADCHIM — version B, après fiabilisation",
    meta=[], doc_ref="GED-RAP-2026-11-B · Confidentiel — usage interne",
    footer="Note à Jad · postes fixes professionnels · version B",
)

VERT_BG, VERT_TX = "E3F0DC", "1E6B2F"
JAUN_BG, JAUN_TX = "FBF3D0", "806000"
ORAN_BG, ORAN_TX = "FBE0CE", "A8480C"
BLEU_BG = "EAF0F7"


def F(bg=None, tx=None, b=False, i=False):
    return {"bg": bg, "color": tx, "b": b, "i": i}


FMT = {"g": F(VERT_BG, VERT_TX, True), "y": F(JAUN_BG, JAUN_TX, True),
       "o": F(ORAN_BG, ORAN_TX, True), "i": F(BLEU_BG),
       "gl": F(VERT_BG, VERT_TX), "yl": F(JAUN_BG, JAUN_TX), "ol": F(ORAN_BG, ORAN_TX)}

_NT = [0]


def tab():
    _NT[0] += 1
    return f"Tableau {_NT[0]}"


def eur(n):
    s = f"{n:,.2f}".replace(",", "\u00a0").replace(".", ",")
    return s + "\u00a0€"


def fcfa(n_eur):
    return f"{round(n_eur * TVA):,}".replace(",", "\u00a0") + "\u00a0FCFA"


PRIX = 1140.18
RAM_1X16 = 335.95
RAM_KIT = 593.95
ECRAN = 84.95

HP_BAR = PRIX + RAM_1X16          # barrette ajoutée, écran exclu
HP_KIT = PRIX + RAM_KIT           # kit de deux barrettes, écran exclu
HP_BAR_ECRAN = HP_BAR + ECRAN
HP_KIT_ECRAN = HP_KIT + ECRAN
M70T_KIT = 899.00 + RAM_KIT
OPT_KIT = 999.00 + RAM_KIT

# --------------------------------------------------------------------------- #
doc.cover(
    eyebrow="Note comparative — version B",
    title="Postes fixes\nprofessionnels :\nétude comparative",
    subtitle="Ce que propose le marché français, ce que vaut le candidat HP, et ce que coûte "
             "réellement un poste à 32 Go. Version corrigée après une première lecture critique.",
    meta_rows=[
        ["Destinataire", "**M. Jad, directeur général — ADCHIM**"],
        ["Expéditeur", "**Joël MBA OYONE — GED-SERVICES**"],
        ["Objet", "Postes fixes professionnels : comparaison technique, prix en euros et en "
                  "francs CFA, recommandation"],
        ["Version", "**B** — reprend la note du 6 novembre 2026 après vérification des chiffres "
                    "et de la cohérence"],
        ["Sources", "Annonces et fiches des distributeurs français (Amazon, Fnac, Cdiscount, "
                    "LDLC, Materiel.net), relevés du 5 novembre 2026"],
        ["Livrables", "Word (.docx) et PDF identiques, produits depuis la même source"],
    ],
    summary=("Ce que change cette version",
             "La première note tenait l'essentiel : le poste est **techniquement bon**. Elle "
             "comportait quatre fragilités que cette version corrige — une conformité de "
             "millésime surestimée, une note globale incohérente avec ses propres sous-notes, un "
             "« choix premium » qui ne tenait pas le profil recommandé du même document, et "
             "l'absence de comparaison de marché dans une étude annoncée comparative. **La "
             "recommandation change : le bon achat n'est pas le poste nu à 16 Go, c'est un poste "
             "à 32 Go négocié — ou le même processeur dans une tour.**", "info"),
)

# --------------------------------------------------------------------------- #
doc.h1("1", "Bonjour Jad")

doc.p("J'espère que tu vas bien. Je reviens vers toi avec la note comparative sur les postes fixes, "
      "dans une version B : après ta première lecture, j'ai repris chaque chiffre et chaque "
      "jugement, et j'ai corrigé ce qui ne tenait pas. Le fond reste le tien — une base technique "
      "plutôt qu'un cahier des charges budgétaire, puisque nous n'avons pas d'enveloppe arrêtée — "
      "mais deux choses ont changé.", lead=True)

doc.p("La première, c'est la **rigueur des chiffres** : une conformité annoncée un peu vite sur le "
      "millésime de la plateforme, une note globale calculée au ressenti plutôt qu'à partir de ses "
      "propres sous-notes, et un coût d'extension mémoire qui manquait alors qu'il décide de tout. "
      "La seconde, c'est la **comparaison** : une étude comparative qui n'examine qu'un seul "
      "produit n'est pas une étude comparative. Le marché propose le même processeur dès 899 €, et "
      "il fallait le montrer.", small=True)

doc.p("Tu trouveras donc, dans l'ordre : les trois profils de poste que tu as définis, ramenés à "
      "une seule règle cohérente ; le panorama de huit machines réellement en vente ; le candidat "
      "HP repris critère par critère ; le prix en euros et en francs CFA, et le coût complet ; la "
      "question des 32 Go, chiffrée ; la liste de ce qui a été corrigé ; et mon avis, qui n'est "
      "plus tout à fait le même.", small=True)

doc.callout("En une phrase",
            "Le **HP Elite 800 G9 Mini i5-14500** est un excellent poste de bureautique, mais ce "
            "n'est pas, à 1 140 € et en 16 Go, le meilleur achat pour ton parc : à ce prix, deux "
            "machines équivalentes — une tour et un petit format — s'achètent entre 899 et 999 €, "
            "et l'extension à 32 Go coûte de "
            "336 à 594 € quel que soit le châssis. **Le bon arbitrage porte sur la mémoire et la "
            "garantie, pas sur le processeur.**", "warn")

# --------------------------------------------------------------------------- #
doc.h1("2", "Trois profils, une seule règle", newpage=False)

doc.p("Tes trois profils sont bons : ils décrivent une progression d'usage, pas une hiérarchie de "
      "gamme. Ils comportaient en revanche deux règles contradictoires — « 2023, G10, G9 accepté » "
      "dans le texte, « 2024 minimum » dans le tableau comparatif. Voici la règle unique que je te "
      "propose de retenir, et qui sert de référence à toute la note.", small=True)

doc.table(
    ["Profil", "Usage visé", "Seuil technique retenu", "Prix cible"],
    [
        ["**Entrée de gamme**", "Accueil, saisie, consultation, poste nomade occasionnel",
         "Core i5 13e génération minimum · 16 Go DDR5 · SSD NVMe 512 Go · Windows 11 Pro · "
         "1 GbE et Wi-Fi 6", "600 à 800 €"],
        ["**Standard entreprise**\n(recommandé)",
         "Bureautique intensive, Sage, Teams, plusieurs applications ouvertes",
         "Core i5 13e/14e ou Core Ultra 5 · **32 Go DDR5** · SSD NVMe 512 Go à 1 To · "
         "Windows 11 Pro · Wi-Fi 6/6E · **garantie 3 ans sur site**", "900 à 1 200 €"],
        ["**Confort / longue durée**", "Utilisateurs exigeants, postes à garder cinq ans, "
                                       "profils techniques légers (CAO, gros tableurs)",
         "Core i5/i7 14e ou Core Ultra 5/7 · **32 Go extensible à 64 Go** · SSD NVMe 1 To · "
         "Windows 11 Pro · garantie 3 ans sur site", "1 200 à 1 600 €"],
    ],
    widths=[3.1, 4.1, 7.1, 2.8], font=8.2, aligns=["l", "l", "l", "c"],
    cell_fmt={(1, 0): FMT["gl"], (1, 3): FMT["gl"]},
    caption=f"{tab()} — Les trois profils, avec un seuil unique et un prix cible. Le profil "
            "standard est celui qui doit servir de référence d'achat.",
)

doc.p("**La règle de millésime, désormais unique.** Ce qui compte n'est pas la date de "
      "naissance du châssis mais celle du processeur : **14e génération ou Core Ultra** pour les "
      "profils standard et confort, **13e génération admise en entrée de gamme** — jamais en "
      "dessous. Le châssis, lui, doit être encore fabriqué, encore garanti, et suivi par le "
      "constructeur. C'est cette règle qui s'applique au candidat HP du chapitre 4 — et c'est "
      "elle qui oblige à nuancer la mention « plateforme 2024 » de la première version.", small=True)

# --------------------------------------------------------------------------- #
doc.h1("3", "Ce que le marché propose réellement")

doc.p("Huit machines fixes, relevées chez les distributeurs français, toutes avec 16 Go, 512 Go et "
      "Windows 11 Pro. C'est le paysage dans lequel le candidat HP doit être jugé : à processeur "
      "égal, il existe moins cher, et le format mini se paie.", small=True)

MARCHÉ = [
    ("Fujitsu Esprimo D7010 SFF", "SFF", "i5-12400", 749.00, "2022", "Entrée de gamme, 12e génération"),
    ("HP ProDesk 400 G9 SFF", "SFF", "i5-13500", 799.00, "2022", "Solide, châssis ancien"),
    ("Lenovo M70q Gen 4 Tiny", "Tiny", "i5-13400T", 799.00, "2023", "Windows 11 Famille"),
    ("Lenovo M70t Gen 5 Tower", "Tour", "i5-14500", 899.00, "2024", "Le même processeur, 240 € de moins"),
    ("Dell OptiPlex 7020 SFF", "SFF", "i5-14500", 999.00, "2024", "Le même processeur, 140 € de moins"),
    ("**HP Elite 800 G9 Mini**", "**Mini**", "**i5-14500**", 1140.18, "**2024 / 2022**",
     "**Le candidat — puce 2024, châssis 2022**"),
    ("Lenovo ThinkStation P3 Tiny Gen 2", "Tiny", "i5-14500T", 1299.00, "2024", "Station d'entrée, 35 W"),
    ("Dell Precision 3680 Tower", "Tour", "i5-14500", 1599.00, "2024", "Station de travail, extensible"),
]

rows, cf = [], {}
for i, (m, f, c, prix, a, note_) in enumerate(MARCHÉ):
    rows.append([m, f, c, a, eur(prix), fcfa(prix), note_])
    if i == 5:
        cf[(i, 0)] = FMT["yl"]; cf[(i, 5)] = FMT["yl"]

doc.table(
    ["Machine", "Format", "Processeur", "Année", "Prix", "Équivalent FCFA", "Remarque"],
    rows, widths=[4.5, 1.7, 2.2, 1.7, 1.9, 2.6, 3.6], font=7.8, aligns=["l", "c", "l", "c", "r", "r", "l"],
    cell_fmt=cf,
    caption=f"{tab()} — Huit fixes professionnels, 16 Go / 512 Go / Windows 11 Pro, prix TTC "
            "relevés le 5 novembre 2026.",
)

doc.p("**Ce que le tableau dit.** Le processeur du candidat n'est pas rare : il équipe trois autres "
      "machines de cette liste, dont deux moins chères de 140 à 240 €. Ce que le HP apporte en plus "
      "n'est donc pas la puissance — c'est le **litre de volume**, la finition Elite et le Wi-Fi 6E. "
      "Reste à savoir si ces trois éléments valent 240 € pour ton usage ; pour un poste de bureau "
      "sous un comptoir ou dans un open space contraint, la réponse peut être oui.", small=True)

doc.p("**Ce que le tableau ne dit pas.** Aucune de ces huit machines n'est livrée avec un écran ; "
      "la troisième (M70q Gen 4) est en Windows 11 Famille, ce qui ajoute environ 145 € pour passer "
      "en Professionnel ; et aucune n'affiche sa garantie — c'est la question à poser aux "
      "distributeurs avant de comparer les prix entre eux.", small=True)

doc.callout("La question à te poser",
            "Si le poste doit être **posé au sol ou sous un bureau**, la tour à 899 € fait le même "
            "travail avec plus de place pour la mémoire. Si le poste doit **tenir sur 15 cm de "
            "profondeur**, en accueil ou en salle de réunion, le format mini justifie son écart. "
            "C'est un arbitrage d'implantation, pas de performance.", "info")

# --------------------------------------------------------------------------- #
doc.h1("4", "Le candidat HP, critère par critère")

doc.p("Vingt et un points, dont deux ont été corrigés par rapport à la première version : le "
      "millésime de la plateforme et la qualification de l'écran. Le vert signale ce qui est tenu "
      "ou dépassé, le jaune ce qui atteint le plancher ou reste à confirmer, l'orange ce qui "
      "manque.", small=True)

G, Y, O = "g", "y", "o"
ROWS = [
    ("Millésime du processeur", "14e génération ou Core Ultra", "i5-14500 — 14e génération, "
     "lancée en janvier 2024", "Conforme", G),
    ("Millésime du châssis", "Plateforme récente, encore fabriquée", "Elite 800 G9 — châssis de "
     "2022, toujours au catalogue", "Tolérable, à connaître", Y),
    ("Gamme", "Professionnelle", "HP Elite 800 — gamme entreprise", "Très bien", G),
    ("Format", "Tour, SFF ou Mini", "Mini PC, 1 litre", "Conforme", G),
    ("Processeur", "Core i5 13e/14e ou Core Ultra 5", "Core i5-14500", "Très bien", G),
    ("Nombre de cœurs", "6 minimum, 8 recommandés ou plus", "14 cœurs (6 performance + 8 efficaces)",
     "Excellent", G),
    ("Nombre de threads", "12 minimum", "20 threads", "Excellent", G),
    ("Fréquence de base", "≈ 2,5 GHz minimum", "2,6 GHz sur les cœurs performance", "Conforme", G),
    ("Fréquence Turbo", "4,0 GHz minimum, 4,5 recommandé", "Jusqu'à 5,0 GHz", "Excellent", G),
    ("Enveloppe thermique", "Adaptée au châssis", "65 W de base, 154 W en pointe, dans 1 litre",
     "Point de vigilance", Y),
    ("Mémoire vive", "16 Go minimum, **32 Go recommandé**", "16 Go", "Sous la cible", Y),
    ("Type de mémoire", "DDR5 préférable", "DDR5 SO-DIMM, 2 emplacements, 64 Go maximum",
     "Conforme", G),
    ("Stockage", "SSD NVMe 512 Go minimum, 1 To idéal", "SSD NVMe 512 Go", "Minimum atteint", Y),
    ("Carte graphique", "Intégrée acceptable", "Intel UHD Graphics 770", "Conforme", G),
    ("Ethernet", "Gigabit minimum", "1 GbE", "Conforme", G),
    ("Wi-Fi / Bluetooth", "Wi-Fi 6 minimum", "Wi-Fi 6E et Bluetooth 5.3", "Très bien", G),
    ("Système", "Windows 11 Professionnel", "Windows 11 Pro", "Conforme", G),
    ("Sécurité", "TPM 2.0, Secure Boot, idéalement vPro", "TPM 2.0 de série ; activation et vPro "
     "à confirmer", "À vérifier", Y),
    ("Écran", "Idéalement inclus dans le pack", "Non inclus — 84,95 € pour un 24\" Full HD",
     "Coût à ajouter", Y),
    ("Clavier / souris", "Souhaités", "Annoncés dans le carton", "Inclus", G),
    ("Garantie", "3 ans sur site exigés", "Non précisée dans l'annonce", "À obtenir avant achat", O),
]

rows = [[c, cible, constate, ev] for c, cible, constate, ev, _ in ROWS]
cf = {(i, 3): FMT[ROWS[i][4]] for i in range(len(ROWS))}
doc.table(
    ["Critère", "Cahier des charges", "Constaté sur l'annonce", "Évaluation"],
    rows, widths=[3.6, 4.4, 5.6, 3.6], font=7.8, aligns=["l", "l", "l", "c"], cell_fmt=cf,
    caption=f"{tab()} — Cahier des charges GED-SERVICES contre caractéristiques de l'annonce : "
            "quatorze points conformes, six à surveiller, un bloquant tant qu'il n'est pas levé.",
)

doc.p("**Ce qui a changé sur ce tableau.** La première version écrivait « année de "
      "commercialisation 2024 — conforme ». C'est vrai de la puce, faux du châssis : l'Elite 800 G9 "
      "est né en 2022, avec les processeurs de 12e génération ; la version que tu as vue est une "
      "configuration 2024 montée dans ce châssis. Ce n'est pas rédhibitoire — HP garantit la "
      "machine et le BIOS est à jour — mais cela doit se savoir, parce que c'est ce qui explique le "
      "prix : tu paies une puce récente dans un boîtier de quatre ans.", small=True)

doc.p("**Deuxième correction.** L'écran n'est pas « non conforme » : ton cahier des charges dit "
      "« idéalement inclus ». C'est donc un **coût à ajouter** — 84,95 € pour un 24 pouces IPS Full "
      "HD en stock — et non un défaut du poste.", small=True)

# --------------------------------------------------------------------------- #
doc.h1("5", "Le prix, en euros et en francs CFA")

doc.p("Le prix relevé est de 1 140,18 € livraison comprise, soit 747 909 FCFA à la parité fixe de "
      "655,957 FCFA pour un euro. Dans le corps de cette note, je l'arrondis à **1 140 €, soit "
      "748 000 FCFA** : le prix d'une place de marché bouge chaque semaine, et un montant au franc "
      "près donne une fausse impression de stabilité.", small=True)

doc.table(
    ["Ce que tu achètes", "Euros (TTC)", "Francs CFA", "Observation"],
    [
        ["**Poste livré** — i5-14500, 16 Go, 512 Go, Windows 11 Pro", eur(PRIX), fcfa(PRIX),
         "Le prix de l'annonce, port compris"],
        ["Écran 24 pouces IPS Full HD (AOC 24B31H)", eur(ECRAN), fcfa(ECRAN),
         "Relevé LDLC, en stock"],
        ["1 barrette de 16 Go DDR5-4800", eur(RAM_1X16), fcfa(RAM_1X16),
         "Si un emplacement mémoire est libre"],
        ["Kit 2 × 16 Go DDR5-4800", eur(RAM_KIT), fcfa(RAM_KIT),
         "Si les deux barrettes doivent être remplacées"],
        ["**Poste à 32 Go, écran compris — barrette ajoutée**", f"**{eur(HP_BAR_ECRAN)}**",
         f"**{fcfa(HP_BAR_ECRAN)}**", "L'hypothèse favorable"],
        ["**Poste à 32 Go, écran compris — kit de deux barrettes**", f"**{eur(HP_KIT_ECRAN)}**",
         f"**{fcfa(HP_KIT_ECRAN)}**", "L'hypothèse défavorable"],
    ],
    widths=[7.0, 2.8, 3.3, 4.1], font=8.2, aligns=["l", "r", "r", "l"],
    cell_fmt={(4, 1): FMT["g"], (4, 2): FMT["g"], (5, 1): FMT["yl"], (5, 2): FMT["yl"]},
    caption=f"{tab()} — Le poste et son coût réel, écran et mémoire compris (1 € = 655,957 FCFA).",
)

doc.p("**Ce que le prix ne dit pas, et qu'il faut dire.** L'annonce vend un poste nu : ni écran, ni "
      "mémoire supplémentaire, ni garantie de trois ans. Le poste réellement livrable coûte donc "
      "entre **{0} et {1}**, soit **{2} à {3}**. C'est cette fourchette qu'il faut comparer aux "
      "autres offres — pas le prix d'appel.".format(eur(HP_BAR_ECRAN), eur(HP_KIT_ECRAN),
                                                    fcfa(HP_BAR_ECRAN), fcfa(HP_KIT_ECRAN)),
      small=True)

doc.p("Annonce du vendeur : [HP Elite 800 G9 Mini — i5-14500 sur Amazon.fr](" + ANNONCE + "). "
      "Le prix, le stock et la configuration varient d'un jour à l'autre ; le lien reste la seule "
      "source de vérité.", small=True)

# --------------------------------------------------------------------------- #
doc.h1("6", "La mémoire : 32 Go, et ce que cela coûte", newpage=False)

doc.p("C'est le point qui change la décision, et il manquait dans la première version. Le châssis "
      "Elite 800 G9 Mini dispose de **deux emplacements SO-DIMM DDR5** (64 Go maximum), accessibles "
      "par la trappe inférieure. Tout dépend donc d'une seule inconnue : les 16 Go livrés sont-ils "
      "**une** barrette ou **deux** ?", small=True)

doc.table(
    ["Configuration livrée", "Ce qu'il faut acheter", "Coût", "En FCFA", "Résultat"],
    [
        ["**1 barrette de 16 Go**, un emplacement libre",
         "1 barrette SO-DIMM 16 Go DDR5-4800 (Corsair Vengeance, LDLC — stock boutique)",
         eur(RAM_1X16), fcfa(RAM_1X16), "32 Go en dual channel"],
        ["**2 barrettes de 8 Go**", "Kit 2 × 16 Go DDR5-4800 CL40 (G.Skill RipJaws, LDLC — stock web)",
         eur(RAM_KIT), fcfa(RAM_KIT), "32 Go ; les 2 × 8 Go en réserve"],
        ["**Déjà 32 Go**", "Rien", "0,00 €", "0 FCFA", "Aucune dépense"],
    ],
    widths=[4.4, 5.9, 2.1, 2.9, 3.6], font=7.9, aligns=["l", "l", "r", "r", "l"],
    cell_fmt={(0, 2): FMT["g"], (0, 3): FMT["g"], (1, 2): FMT["yl"], (1, 3): FMT["yl"]},
    caption=f"{tab()} — Les deux scénarios d'extension, chiffrés sur des références en stock chez "
            "LDLC le 5 novembre 2026.",
)

doc.p("**Le classement change selon la réponse.** J'ai comparé ce que coûte un poste à 32 Go, "
      "écran compris, pour quatre machines du panorama. La conclusion n'est pas celle que la "
      "première note laissait entendre : si le HP arrive avec une barrette et un emplacement libre, "
      "**il devient la voie la moins chère vers 32 Go** — 1 561 € contre 1 578 € pour la tour "
      "Lenovo et 1 678 € pour l'OptiPlex. S'il arrive en 2 × 8 Go, il devient la plus chère.", small=True)

doc.table(
    ["Machine", "Machine + mémoire", "Avec écran", "En FCFA (avec écran)"],
    [
        ["**HP Elite 800 G9 Mini — 1 × 16 Go livrés**", f"{eur(HP_BAR)}", f"**{eur(HP_BAR_ECRAN)}**",
         f"**{fcfa(HP_BAR_ECRAN)}**"],
        ["HP Elite 800 G9 Mini — 2 × 8 Go livrés", eur(HP_KIT), eur(HP_KIT_ECRAN),
         fcfa(HP_KIT_ECRAN)],
        ["Lenovo ThinkCentre M70t Gen 5 + kit 32 Go", eur(M70T_KIT), eur(M70T_KIT + ECRAN),
         fcfa(M70T_KIT + ECRAN)],
        ["Dell OptiPlex 7020 SFF + kit 32 Go", eur(OPT_KIT), eur(OPT_KIT + ECRAN),
         fcfa(OPT_KIT + ECRAN)],
    ],
    widths=[7.6, 3.4, 3.2, 3.0], font=8.2, aligns=["l", "r", "r", "r"],
    cell_fmt={(0, 2): FMT["g"], (0, 3): FMT["g"], (1, 0): FMT["yl"], (1, 1): FMT["yl"]},
    caption=f"{tab()} — Coût d'un poste à 32 Go, écran Full HD compris, selon la machine et la "
            "configuration mémoire livrée.",
)

doc.p("**Ce que cela veut dire concrètement.** La mémoire est devenue, en 2026, la première ligne de "
      "budget d'un poste : 336 € la barrette de 16 Go, 594 € le kit de deux, soit 29 à 52 % du prix "
      "de la machine. Aucun châssis ne se compare donc sur son prix nu : il faut comparer **le prix "
      "du poste à 32 Go, écran compris**, ce que fait le tableau ci-dessus. Et poser une seule "
      "question au vendeur avant de payer : « la configuration est-elle en 1 × 16 Go ou 2 × 8 Go ? »",
      small=True)

# --------------------------------------------------------------------------- #
doc.h1("7", "Ce qui a été corrigé depuis la première lecture", newpage=False)

doc.p("Par honnêteté, et pour que tu puisses juger de la solidité de cette version, voici la liste "
      "des points qui ne tenaient pas — ou qui manquaient — dans la note précédente.", small=True)

CORR = [
    ("« Plateforme 2024 — conforme »", "La puce est de 2024, le châssis Elite 800 G9 de 2022",
     "La conformité porte sur le processeur ; le millésime du châssis est désormais affiché"),
    ("« 8,5 / 10 »", "La moyenne des sept sous-notes donne 7,6 — et 7,0 en tenant compte du prix",
     "La note globale est recalculée à **7,0 / 10**"),
    ("« Choix premium long terme » à 16 Go", "Le profil standard de la même note exige 32 Go",
     "Le poste ne tient pas son propre cahier des charges : il passe en « bon poste, à équiper »"),
    ("Extension mémoire non chiffrée", "335,95 € (une barrette) à 593,95 € (kit de deux)",
     "Le poste complet est comparé aux autres machines à 32 Go"),
    ("« Écran non conforme au pack »", "Le cahier des charges dit « idéalement inclus »",
     "Requalifié en coût à ajouter : 84,95 €"),
    ("Garantie « non précisée », avis maintenu", "Sans garantie 3 ans sur site, l'achat ne passe pas",
     "Devient une **condition suspensive** de la commande"),
    ("« Étude comparative » sur un seul produit", "Le marché propose le même processeur dès 899 €",
     "Panorama de huit machines ajouté (chapitre 3)"),
    ("Enveloppe thermique non relevée", "65 W de base, 154 W en pointe, dans un litre",
     "Nouvelle ligne du tableau comparatif ; fréquences soutenues à vérifier"),
    ("« 2023, G10, G9 accepté » et « 2024 minimum »", "Deux règles opposées dans le même document",
     "Une règle unique : puce 2024 minimum, châssis encore fabriqué et garanti"),
    ("TPM « à vérifier » au même niveau que le reste", "Le TPM 2.0 est de série sur cette gamme",
     "La vraie question est son activation, celle de Secure Boot et la présence de vPro"),
    ("Prix au franc près : 747 909 FCFA", "Le prix d'une place de marché bouge chaque semaine",
     "Arrondi à 748 000 FCFA dans le texte, montant exact dans le tableau"),
]

doc.table(
    ["Ce que disait la première version", "Ce qui est exact", "Ce que cela change"],
    [[a, b, c] for a, b, c in CORR],
    widths=[4.9, 6.4, 5.9], font=7.9, aligns=["l", "l", "l"],
    caption=f"{tab()} — Onze corrections. Les quatre premières modifient la recommandation.",
)

doc.p("**Ce que ces corrections changent dans la décision.** Trois d'entre elles pèsent directement "
      "sur l'achat : la conformité de millésime — le poste ne porte pas une plateforme 2024, il en "
      "porte le processeur ; le coût de la mémoire, qui représente 29 à 52 % du prix du poste ; et "
      "l'absence de garantie annoncée, qui devient une condition suspensive. Les autres corrigent "
      "la présentation et le calcul de la note, pas le jugement technique.", small=True)

# --------------------------------------------------------------------------- #
doc.h1("8", "Mon avis, et ce que je te propose")

doc.table(
    ["Domaine évalué", "Note", "Commentaire"],
    [
        ["Processeur (i5-14500)", "9 / 10", "Très au-dessus du besoin ; 65 W dans un litre "
                                            "coûtent un point"],
        ["Mémoire (16 Go)", "6 / 10", "Sous la cible de 32 Go ; extension coûteuse"],
        ["Stockage (512 Go NVMe)", "7 / 10", "Plancher atteint, 1 To préférable"],
        ["Connectivité (1 GbE, Wi-Fi 6E, BT 5.3)", "9 / 10", "Rien à redire"],
        ["Gamme professionnelle (Elite 800)", "9 / 10", "Châssis et finition de gamme entreprise"],
        ["Évolutivité", "5 / 10", "Deux emplacements mémoire seulement, alimentation externe"],
        ["Pack complet (écran, garantie)", "4 / 10", "Ni écran, ni garantie de trois ans annoncée"],
        ["**Évaluation globale**", "**7,0 / 10**", "**Très bon poste, achat à conditions**"],
    ],
    widths=[7.0, 2.4, 7.8], font=8.6, aligns=["l", "c", "l"],
    cell_fmt={(7, 0): FMT["g"], (7, 1): FMT["g"], (7, 2): FMT["g"], (0, 1): FMT["gl"],
              (1, 1): FMT["yl"], (5, 1): FMT["ol"], (6, 1): FMT["ol"]},
    caption=f"{tab()} — Évaluation indicative selon les critères professionnels retenus, et non "
            "une note du constructeur.",
)

doc.p("**Ce que je te propose**, dans l'ordre de préférence :", small=True)
doc.ul([
    "**Si le vendeur confirme 1 × 16 Go, un emplacement libre, TPM activé et une garantie 3 ans "
    "sur site** : prends-le, ajoute une barrette de 16 Go (336 €) et un écran (85 €). Tu obtiens un "
    "poste à 32 Go, garanti, pour **1 561 € — 1 024 000 FCFA**. C'est, à ce jour, la voie la moins "
    "chère vers un poste à 32 Go.",
    "**S'il est livré en 2 × 8 Go** : le poste complet monte à 1 819 € — 1 193 000 FCFA, au-dessus "
    "d'une tour Dell OptiPlex 7020 équipée (1 678 €). Négocie alors le poste à 1 000 €, ou passe "
    "à la tour.",
    "**Si la garantie de trois ans n'est pas démontrable** : renonce, quel que soit le prix. Un "
    "poste professionnel sans garantie sur site coûte 10 à 15 jours d'immobilisation par incident — "
    "c'est plus cher que les 240 € d'écart avec la tour.",
    "**Pour un poste posé au sol**, la tour Lenovo M70t Gen 5 à 899 € fait le même travail, avec "
    "plus d'emplacements. Le format mini ne se justifie que par l'implantation.",
])

doc.callout("En résumé",
            "Le HP Elite 800 G9 Mini est **un bon poste, pas un bon prix**. Sa puce est excellente, "
            "sa connectivité irréprochable, sa finition sérieuse — mais il arrive à 16 Go, sans "
            "écran et sans garantie annoncée, à 240 € de plus qu'une tour équipée du même "
            "processeur. **Trois questions au vendeur, et une seule décision** : la configuration "
            "mémoire, l'activation du TPM, la garantie réelle. Si les trois réponses sont bonnes, "
            "c'est un achat que je signe ; sinon, la tour.", "ok")

doc.save(OUT)

# métadonnées Word : GED-SERVICES, rien d'autre
import docx as _docx
_PATH = os.path.join(OUT, BASE + ".docx")
_d = _docx.Document(_PATH)
_cp = _d.core_properties
_cp.author = "GED-SERVICES"
_cp.last_modified_by = "GED-SERVICES"
_cp.comments = ""
_cp.keywords = ""
_cp.category = ""
_cp.subject = "Postes fixes professionnels — étude comparative, version B"
_cp.title = "Postes fixes professionnels : étude comparative et recommandation"
_d.save(_PATH)

print("saved", OUT)
