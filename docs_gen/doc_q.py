# -*- coding: utf-8 -*-
"""Note GED-SERVICES sur les postes fixes : cible matérielle, marché, candidat, justifications."""
import os
from render import Doc

BASE = "Q_Note_postes_fixes_cible_marche_et_candidat_HP_Elite_800_G9_Mini"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables")

TVA = 655.957

ANNONCE = "https://www.amazon.fr/HP-Elite-800-Bluetooth-Dual-Mode/dp/B0D76M6T6R"

doc = Doc(
    base=BASE,
    title="Postes fixes professionnels : cible, marché et candidat",
    subtitle="La cible matérielle retenue, les huit machines réellement en vente, "
             "le candidat HP jugé critère par critère, et les justifications",
    meta=[],
    doc_ref="GED-RAP-2026-11 · Confidentiel — usage interne",
    footer="GED-SERVICES · postes fixes professionnels",
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

HP_BAR = PRIX + RAM_1X16
HP_KIT = PRIX + RAM_KIT
M70T_KIT = 899.00 + RAM_KIT
OPT_KIT = 999.00 + RAM_KIT

G, Y, O = "g", "y", "o"

# --------------------------------------------------------------------------- #
doc.cover(
    eyebrow="Note technique — postes fixes",
    title="Postes fixes\nprofessionnels",
    subtitle="La cible matérielle, ce que le marché propose réellement, le candidat HP critère par "
             "critère, et les justifications de la recommandation.",
    meta_rows=[
        ["Destinataire", "**M. Jad, directeur général — ADCHIM**"],
        ["Émetteur", "**Joël MBA OYONE — GED-SERVICES**"],
        ["Objet", "Équipement des postes fixes : cible technique, comparaison du marché, "
                  "arbitrage sur le HP Elite 800 G9 Mini"],
        ["Sources", "Fiches et annonces des distributeurs français (Amazon, Fnac, Cdiscount, LDLC, "
                    "Materiel.net) et prix publics des constructeurs, relevés le 5 novembre 2026"],
        ["Livrables", "Word (.docx) et PDF identiques, produits depuis la même source"],
    ],
)

# --------------------------------------------------------------------------- #
doc.h1("1", "La cible matérielle")

doc.p("La cible se définit par l'usage, pas par un budget. Trois profils suffisent à couvrir les "
      "postes d'ADCHIM ; ils décrivent une progression de charge, du poste d'accueil au poste "
      "technique léger. Le profil **standard entreprise** est celui qui sert de référence d'achat "
      "dans toute la note.", small=True)

doc.table(
    ["Profil", "Usage visé", "Seuil technique retenu"],
    [
        ["**Entrée de gamme**",
         "Accueil, saisie, consultation, poste nomade occasionnel",
         "Core i5 13e génération minimum · 16 Go DDR5 · SSD NVMe 512 Go · Windows 11 Pro · "
         "1 GbE et Wi-Fi 6"],
        ["**Standard entreprise**\n(recommandé)",
         "Bureautique intensive, Sage, Teams, plusieurs applications ouvertes",
         "Core i5 13e/14e ou Core Ultra 5 · **32 Go DDR5** · SSD NVMe 512 Go à 1 To · "
         "Windows 11 Pro · Wi-Fi 6/6E · **garantie 3 ans sur site**"],
        ["**Confort / longue durée**",
         "Utilisateurs exigeants, postes gardés cinq ans, profils techniques légers (CAO, "
         "gros tableurs)",
         "Core i5/i7 14e ou Core Ultra 5/7 · **32 Go extensible à 64 Go** · SSD NVMe 1 To · "
         "Windows 11 Pro · garantie 3 ans sur site"],
    ],
    widths=[3.3, 4.6, 9.2], font=8.2, aligns=["l", "l", "l"],
    cell_fmt={(1, 0): FMT["gl"]},
    caption=f"{tab()} — Les trois profils d'usage et leur seuil technique. Le profil standard est "
            "celui qui doit servir de référence d'achat.",
)

doc.p("**La règle de millésime.** Ce qui compte n'est pas la date de naissance du châssis mais "
      "celle du processeur : **14e génération ou Core Ultra** pour les profils standard et confort, "
      "**13e génération admise en entrée de gamme**, jamais en dessous. Le châssis, lui, doit être "
      "encore fabriqué, encore garanti et suivi par le constructeur. Cette règle s'applique telle "
      "quelle au candidat HP examiné au chapitre 3.", small=True)

doc.p("**Les exigences transversales.** Elles sont les mêmes pour les trois profils : c'est le "
      "socle du cahier des charges, celui qui permet de refuser une offre sans discuter.", small=True)

doc.table(
    ["Exigence", "Seuil retenu"],
    [
        ["**Système**", "Windows 11 Professionnel, licence comprise dans le prix du poste"],
        ["**Processeur**", "Core i5 13e génération minimum ; 14e génération ou Core Ultra 5/7 pour "
                           "les profils standard et confort"],
        ["**Mémoire**", "16 Go DDR5 en entrée de gamme, **32 Go** pour les autres ; deux "
                        "emplacements SO-DIMM ou DIMM, extensibles à 64 Go"],
        ["**Stockage**", "SSD NVMe 512 Go minimum, 1 To pour le profil confort ; un emplacement "
                         "libre pour un second disque"],
        ["**Réseau**", "Ethernet gigabit et Wi-Fi 6 minimum — Wi-Fi 6E préférable"],
        ["**Sécurité**", "TPM 2.0 **activé**, Secure Boot en état de marche, vPro lorsque le "
                         "modèle le propose"],
        ["**Garantie**", "3 ans sur site, pièces et main-d'œuvre, contrat nommé"],
        ["**Format**", "Tour, petit format ou mini, châssis encore fabriqué et suivi par le "
                       "constructeur"],
        ["**Périphériques**", "Clavier et souris ; écran 24 pouces IPS Full HD en sus du poste"],
    ],
    widths=[3.4, 13.7], font=8.2, aligns=["l", "l"],
    cell_fmt={(2, 0): FMT["gl"]},
    caption=f"{tab()} — Le socle exigé pour tout poste fixe, quel que soit le profil.",
)

doc.p("**Sur le format.** Tour, petit format (SFF) ou mini : les trois sont admissibles. Le format "
      "ne change pas la puissance, il change l'implantation — un mini tient sous un écran ou dans "
      "un tiroir, une tour occupe 15 à 40 cm de profondeur et laisse plus de place pour la mémoire "
      "et les disques.", small=True)

# --------------------------------------------------------------------------- #
doc.h1("2", "Ce que le marché propose réellement")

doc.p("Huit machines fixes, relevées chez les distributeurs français, toutes avec 16 Go de mémoire, "
      "512 Go de stockage et Windows 11 Professionnel. C'est le paysage dans lequel le candidat HP "
      "doit être jugé : à processeur égal, il existe moins cher, et le format mini se paie.", small=True)

URL = {
    "Fujitsu Esprimo D7010 SFF": "https://www.amazon.fr/s?k=Fujitsu+Esprimo+D7010+SFF+i5-12400",
    "HP ProDesk 400 G9 SFF": "https://www.amazon.fr/s?k=HP+ProDesk+400+G9+SFF+i5-13500",
    "Lenovo M70q Gen 4 Tiny": "https://www.amazon.fr/s?k=Lenovo+ThinkCentre+M70q+Gen+4+i5-13400T",
    "Lenovo M70t Gen 5 Tower": "https://www.amazon.fr/s?k=Lenovo+ThinkCentre+M70t+Gen+5+i5-14500",
    "Dell OptiPlex 7020 SFF": "https://www.amazon.fr/s?k=Dell+OptiPlex+7020+SFF+i5-14500",
    "**HP Elite 800 G9 Mini**": ANNONCE,
    "Lenovo ThinkStation P3 Tiny Gen 2": "https://www.amazon.fr/s?k=Lenovo+ThinkStation+P3+Tiny+Gen+2",
    "Dell Precision 3680 Tower": "https://www.amazon.fr/s?k=Dell+Precision+3680+Tower+i5-14500",
}

MARCHE = [
    ("Fujitsu Esprimo D7010 SFF", "SFF", "i5-12400", 749.00, "2022", "Entrée de gamme, 12e génération"),
    ("HP ProDesk 400 G9 SFF", "SFF", "i5-13500", 799.00, "2022", "Solide, châssis ancien"),
    ("Lenovo M70q Gen 4 Tiny", "Tiny", "i5-13400T", 799.00, "2023", "Windows 11 Famille"),
    ("Lenovo M70t Gen 5 Tower", "Tour", "i5-14500", 899.00, "2024", "Même processeur, 240 € de moins"),
    ("Dell OptiPlex 7020 SFF", "SFF", "i5-14500", 999.00, "2024", "Même processeur, 140 € de moins"),
    ("**HP Elite 800 G9 Mini**", "**Mini**", "**i5-14500**", 1140.18, "**2024 / 2022**",
     "**Le candidat — puce 2024, châssis 2022**"),
    ("Lenovo ThinkStation P3 Tiny Gen 2", "Tiny", "i5-14500T", 1299.00, "2024", "Station d'entrée, 35 W"),
    ("Dell Precision 3680 Tower", "Tour", "i5-14500", 1599.00, "2024", "Station de travail, extensible"),
]

rows, cf = [], {}
for i, (m, f, c, prix, a, note_) in enumerate(MARCHE):
    rows.append([m, f, c, a, eur(prix), fcfa(prix), note_, f"[voir]({URL[m]})"])
    if i == 5:
        cf[(i, 0)] = FMT["yl"]
        cf[(i, 1)] = FMT["yl"]
        cf[(i, 2)] = FMT["yl"]

doc.table(
    ["Machine", "Format", "Processeur", "Année", "Prix", "Équivalent FCFA", "Remarque", "Lien"],
    rows,
    widths=[3.6, 1.6, 2.0, 1.5, 1.9, 2.4, 3.1, 1.0], font=7.5,
    aligns=["l", "c", "l", "c", "r", "r", "l", "c"], cell_fmt=cf,
    caption=f"{tab()} — Huit fixes professionnels, 16 Go / 512 Go / Windows 11 Pro, prix TTC "
            "relevés le 5 novembre 2026. Le lien ouvre la fiche ou la recherche du modèle chez le "
            "distributeur.",
)

doc.p("**Lecture du tableau.** Le processeur du candidat n'est pas rare : il équipe trois autres "
      "machines de cette liste, dont deux moins chères de 140 à 240 €. Ce que le HP apporte en plus "
      "n'est donc pas la puissance, mais le litre de volume, la finition Elite et le Wi-Fi 6E. "
      "Le prix, lui, suit la génération et le format avant la marque : entre la tour Lenovo à "
      "899 € et la station Dell à 1 599 €, l'écart est un écart de châssis, de garantie et de "
      "service, pas de calcul.", small=True)

doc.p("**Les réserves du tableau.** Aucune de ces huit machines n'est livrée avec un écran. La "
      "troisième, le M70q Gen 4, est en Windows 11 Famille : environ 145 € de licence pour passer "
      "en Professionnel. Et aucune n'affiche sa garantie — c'est la première question à poser au "
      "distributeur, avant de comparer les prix entre eux.", small=True)

# --------------------------------------------------------------------------- #
doc.pagebreak()
doc.h2("Où acheter : cinq distributeurs, un seul modèle neuf")

doc.p("Les cinq distributeurs ne se valent pas sur ce type de machine : les places de marché "
      "référencent le poste, les spécialistes ne le référencent pas. Disponibilité constatée le "
      "5 novembre 2026.", small=True)

doc.table(
    ["Distributeur", "HP Elite 800 G9 Mini", "Lenovo M70t Gen 5", "Dell OptiPlex 7020",
     "Ce qu'il faut savoir", "Lien"],
    [
        ["**Amazon.fr**", "**Oui, 1 140,18 €**", "Place de marché", "Place de marché",
         "Le plus large choix, prix souvent les plus bas ; vérifier « Neuf » et l'identité du vendeur",
         "[voir](https://www.amazon.fr/s?k=HP+Elite+800+G9+Mini+i5-14500)"],
        ["**Fnac**", "Place de marché", "Rare", "Rare",
         "Service après-vente en magasin ; peu de modèles professionnels, configurations changeantes",
         "[voir](https://www.fnac.com/SearchResult/ResultList.aspx?Search=HP+Elite+800+G9+Mini)"],
        ["**Cdiscount**", "Place de marché", "Place de marché", "Place de marché",
         "Prix agressifs, mais beaucoup de reconditionné mêlé au neuf",
         "[voir](https://www.cdiscount.com/search/10/HP+Elite+800+G9+Mini.html)"],
        ["**LDLC**", "Non référencé", "**Oui**", "Non référencé",
         "Le meilleur suivi sur les gammes pro qu'il référence : stock réel, configuration détaillée",
         "[voir](https://www.ldlc.com/recherche/Lenovo%20ThinkCentre%20M70t/)"],
        ["**Materiel.net**", "Reconditionné seulement", "**Oui**", "Reconditionné seulement",
         "Même groupe que LDLC ; comparer les deux avant de commander",
         "[voir](https://www.materiel.net/recherche/Lenovo%20ThinkCentre%20M70t/)"],
    ],
    widths=[2.1, 2.9, 2.2, 2.2, 5.6, 2.1], font=7.5, aligns=["l", "l", "l", "l", "l", "c"],
    cell_fmt={(0, 1): FMT["g"], (3, 2): FMT["g"], (4, 2): FMT["g"],
              (3, 1): FMT["ol"], (4, 1): FMT["ol"]},
    caption=f"{tab()} — Disponibilité constatée le 5 novembre 2026. « Place de marché » signifie "
            "que le produit est vendu par un tiers, pas par l'enseigne.",
)

doc.p("Les deux spécialistes ne référencent pas ce HP en neuf : l'Elite Mini ne peut donc être ni "
      "examiné en magasin ni négocié chez eux. Ils sont en revanche les seuls à vendre le Lenovo "
      "ThinkCentre en neuf, avec la référence exacte et le stock réel — un point qui compte si la "
      "traçabilité et la garantie pèsent autant que le prix.", small=True)

doc.p("**Ce que le canal d'achat change.** Sur une place de marché, la garantie est celle du vendeur "
      "tiers et non celle de l'enseigne : elle se lit sur la fiche, elle ne se présume pas. Chez un "
      "spécialiste, la garantie constructeur s'applique et la référence exacte est affichée. "
      "À prix voisin, le canal le plus traçable reste le plus sûr.", small=True)

doc.p("**Statut des prix.** Montants TTC des fiches consultées le **5 novembre 2026**, convertis à "
      "la parité fixe de 655,957 FCFA pour un euro. Ils évoluent d'une semaine à l'autre, la "
      "mémoire surtout. **Aucun frais de livraison n'est indiqué dans cette note** : ils dépendent "
      "du volume, du mode d'expédition et de la douane, et ne peuvent pas être comparés d'une "
      "machine à l'autre.", small=True)

doc.p("Le candidat, en fiche : [HP Elite 800 G9 Mini — i5-14500 sur Amazon.fr]({0}). Le prix, le "
      "stock et la configuration varient d'un jour à l'autre ; le lien reste la seule source de "
      "vérité.".format(ANNONCE), small=True)


# --------------------------------------------------------------------------- #
doc.h1("3", "Le candidat HP, critère par critère")

doc.p("Vingt et un points, repris du cahier des charges du chapitre 1 et confrontés à l'annonce "
      "du vendeur. Le vert signale ce qui est tenu ou dépassé, le jaune ce qui atteint juste le "
      "plancher ou reste à confirmer, l'orange ce qui manque.", small=True)

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
    rows, widths=[3.6, 4.4, 5.6, 3.5], font=7.8, aligns=["l", "l", "l", "c"], cell_fmt=cf,
    caption=f"{tab()} — Cahier des charges GED-SERVICES contre caractéristiques de l'annonce : "
            "quatorze points conformes, six à surveiller, un bloquant tant qu'il n'est pas levé.",
)

doc.p("**Deux points appellent une explication.** Le millésime : la puce est de janvier 2024, le "
      "châssis Elite 800 G9 de 2022 — c'est une configuration récente montée dans un boîtier de "
      "quatre ans, ce qui explique en partie le prix, et ne remet pas en cause le suivi "
      "constructeur. L'écran : le cahier des charges le dit « idéalement inclus », il s'agit donc "
      "d'un coût à ajouter — 84,95 € pour un 24 pouces IPS Full HD en stock — et non d'un défaut "
      "du poste.", small=True)

doc.p("**Le point bloquant est la garantie.** L'annonce ne la mentionne pas. Sur un poste "
      "professionnel gardé cinq ans, l'absence de garantie sur site se traduit par une "
      "immobilisation de dix à quinze jours en cas de panne, sans prêt de matériel. C'est la "
      "seule ligne du tableau qui puisse, à elle seule, écarter l'offre.", small=True)

# --------------------------------------------------------------------------- #
doc.h1("4", "Les justifications")

doc.h2("Pourquoi 32 Go, et pas 16")
doc.p("Sage, Teams et plusieurs applications ouvertes simultanément consomment, sur un poste "
      "Windows 11 Professionnel, 10 à 14 Go de mémoire vive en usage réel ; 16 Go laissent une "
      "marge de confort qui disparaît dès qu'un tableur volumineux, un client de messagerie lourd "
      "et un navigateur à quinze onglets cohabitent. Le profil standard retenu au chapitre 1 fixe "
      "donc 32 Go. La conséquence technique est simple : il faut **deux emplacements SO-DIMM** et "
      "non une mémoire soudée, sans quoi l'extension est impossible.", small=True)

doc.h2("Ce que coûte le passage à 32 Go")
doc.table(
    ["Configuration livrée", "Ce qu'il faut acheter", "Coût", "En FCFA", "Résultat"],
    [
        ["**1 barrette de 16 Go**, un emplacement libre",
         "1 barrette SO-DIMM 16 Go DDR5-4800 (Corsair Vengeance, LDLC — stock boutique)",
         eur(RAM_1X16), fcfa(RAM_1X16), "32 Go en dual channel"],
        ["**2 barrettes de 8 Go**",
         "Kit 2 × 16 Go DDR5-4800 CL40 (G.Skill RipJaws, LDLC — stock web)",
         eur(RAM_KIT), fcfa(RAM_KIT), "32 Go ; les 2 × 8 Go en réserve"],
        ["**Déjà 32 Go**", "Rien", "0,00 €", "0 FCFA", "Aucune dépense"],
    ],
    widths=[4.0, 5.3, 2.2, 2.9, 2.7], font=7.9, aligns=["l", "l", "r", "r", "l"],
    cell_fmt={(0, 2): FMT["g"], (0, 3): FMT["g"], (1, 2): FMT["yl"], (1, 3): FMT["yl"]},
    caption=f"{tab()} — Les deux scénarios d'extension, chiffrés sur des références en stock chez "
            "LDLC le 5 novembre 2026.",
)

doc.p("La barrette de 16 Go représente 29,5 % du prix du poste, le kit de deux 52,1 % : la mémoire "
      "est devenue la première ligne de budget d'un poste fixe en 2026. C'est pourquoi la "
      "comparaison se fait non pas sur le prix nu, mais sur le prix du poste à 32 Go — ce que fait "
      "le tableau suivant, sur trois machines comparables.", small=True)

doc.table(
    ["Poste (même génération, 16 Go / 512 Go)", "Prix 16 Go", "Mémoire pour 32 Go", "Total 32 Go",
     "Écart", "Total en FCFA"],
    [
        ["**HP Elite 800 G9 Mini — i5-14500**", eur(PRIX), "1 × 16 Go ajoutée : " + eur(RAM_1X16),
         f"**{eur(HP_BAR)}**", "**+29,5 %**", f"**{fcfa(HP_BAR)}**"],
        ["HP Elite 800 G9 Mini — si 2 × 8 Go livrés", eur(PRIX), "Kit 2 × 16 Go : " + eur(RAM_KIT),
         eur(HP_KIT), "+52,1 %", fcfa(HP_KIT)],
        ["Lenovo ThinkCentre M70t Gen 5 — i5-14500", eur(899.00), "Kit 2 × 16 Go : " + eur(RAM_KIT),
         eur(M70T_KIT), "+66,1 %", fcfa(M70T_KIT)],
        ["Dell OptiPlex 7020 SFF — i5-14500", eur(999.00), "Kit 2 × 16 Go : " + eur(RAM_KIT),
         eur(OPT_KIT), "+59,5 %", fcfa(OPT_KIT)],
    ],
    widths=[5.2, 2.1, 3.1, 2.2, 1.8, 2.7], font=7.9, aligns=["l", "r", "l", "r", "c", "r"],
    cell_fmt={(0, 3): FMT["g"], (0, 4): FMT["g"], (1, 3): FMT["yl"], (1, 4): FMT["yl"]},
    caption=f"{tab()} — Face-à-face : ce que coûte le passage de 16 à 32 Go sur trois machines "
            "comparables. Hors écran et hors livraison.",
)

doc.p("Avec 1 × 16 Go livrée, le HP est le moins cher des trois postes à 32 Go, à 1 476,13 €. Avec "
      "2 × 8 Go, il devient le plus cher, à 1 734,13 €. Écran compris, l'ordre est HP 1 561,08 €, "
      "Lenovo M70t 1 577,90 €, Dell OptiPlex 1 677,90 € — et 1 819,08 € si le HP arrive en "
      "2 × 8 Go. Toute la comparaison tient donc à une information que la fiche ne donne pas : "
      "**la configuration mémoire livrée**.", small=True)

doc.h2("Pourquoi le format et l'enveloppe thermique comptent")
doc.p("Un i5-14500 dissipe 65 W en base et jusqu'à 154 W en pointe, dans un litre de volume. "
      "C'est tenable — le châssis est conçu pour cette puce — mais cela explique le niveau sonore "
      "en charge et la nécessité d'un dégagement autour du poste. Une tour, à processeur égal, "
      "respire mieux et accepte des barrettes DIMM standard, moins chères que les SO-DIMM. "
      "L'arbitrage entre mini et tour est donc un arbitrage d'implantation, pas de performance : "
      "le mini s'impose quand le poste doit tenir sur 15 cm de profondeur, la tour quand il peut "
      "être posé au sol.", small=True)

doc.h2("Pourquoi la garantie décide")
doc.p("Trois ans sur site, c'est l'engagement qui permet de garder un poste cinq ans sans "
      "immobilisation. Sans elle, la panne se traite par retour atelier : dix à quinze jours "
      "d'indisponibilité, plus le coût du transport. À l'échelle d'un parc, cette clause pèse "
      "davantage que 140 € d'écart à l'achat.", small=True)

# --------------------------------------------------------------------------- #
doc.h1("5", "Recommandation GED-SERVICES")

doc.p("**Le HP Elite 800 G9 Mini est un bon poste, pas un bon prix.** Sa puce est excellente, sa "
      "connectivité irréprochable, sa finition sérieuse ; mais il arrive en 16 Go, sans écran et "
      "sans garantie annoncée, à 240 € de plus qu'une tour équipée du même processeur. "
      "GED-SERVICES recommande de l'acquérir **sous trois conditions cumulatives**, vérifiables "
      "auprès du vendeur avant commande :", small=True)

doc.ul([
    "**1 × 16 Go livrée**, avec un emplacement mémoire libre — sans quoi l'extension coûte "
    "258 € de plus et le poste perd son avantage.",
    "**TPM 2.0 activé et Secure Boot en état de marche**, exigence de conformité plus que de "
    "performance.",
    "**Garantie 3 ans sur site**, écrite, avec la référence du contrat.",
])

doc.p("Si l'une des trois fait défaut, la tour **Lenovo ThinkCentre M70t Gen 5 à 899 €** fait le "
      "même travail avec plus d'emplacements internes, une garantie plus simple à obtenir et "
      "240 € d'écart à l'achat. Le format mini ne se justifie que par l'implantation — accueil, "
      "salle de réunion, poste sous écran.", small=True)

doc.h2("Sources et méthode")

doc.p("Prix relevés le **5 novembre 2026** : annonce Amazon.fr pour le HP Elite 800 G9 Mini "
      "(1 140,18 €) ; fiches LDLC pour la barrette de 16 Go (335,95 €, annoncée en rupture web), "
      "le kit de deux (593,95 €) et l'écran AOC 24B31H (84,95 €) ; prix publics des constructeurs "
      "pour les sept autres machines du panorama. Conversion à la parité fixe de 655,957 FCFA pour "
      "un euro : les montants en francs sont exacts, les prix ne le sont pas — ils bougent chaque "
      "semaine. Aucun frais de livraison n'est indiqué, et aucun montant ne vaut offre ferme.",
      small=True)

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
_cp.subject = "Postes fixes professionnels — cible, marché et candidat"
_cp.title = "Postes fixes professionnels : cible, marché et candidat"
_d.save(_PATH)

print("saved", OUT)
