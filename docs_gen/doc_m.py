# -*- coding: utf-8 -*-
"""HP Elite 800 G9 Mini — i5-14500 : comparaison au cahier des charges GED-SERVICES,
mise en perspective du prix (€ et FCFA) et chiffrage du passage à 32 Go. Word + PDF."""
import os
from render import Doc

BASE = "M_HP_Elite_800_G9_Mini_i5-14500_arbitrage_prix_et_memoire"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables")

TVA = 655.957  # parité fixe franc CFA / euro

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
    title="HP Elite 800 G9 Mini — i5-14500 : ce que le poste vaut, ce qu'il coûte",
    subtitle="Comparaison au cahier des charges GED-SERVICES, prix en euros et en francs CFA, "
             "chiffrage du passage à 32 Go",
    meta=[], doc_ref="GED-RAP-2026-11 · Confidentiel — usage interne",
    footer="HP Elite 800 G9 Mini · arbitrage prix et mémoire",
)

VERT_BG, VERT_TX = "E3F0DC", "1E6B2F"
JAUN_BG, JAUN_TX = "FBF3D0", "806000"
ORAN_BG, ORAN_TX = "FBE0CE", "A8480C"
BLEU_BG = "EAF0F7"


def F(bg=None, tx=None, b=False, i=False):
    return {"bg": bg, "color": tx, "b": b, "i": i}


FMT = {"g": F(VERT_BG, VERT_TX, True), "y": F(JAUN_BG, JAUN_TX, True),
       "o": F(ORAN_BG, ORAN_TX, True), "p": F(), "i": F(BLEU_BG),
       "gl": F(VERT_BG, VERT_TX), "yl": F(JAUN_BG, JAUN_TX), "ol": F(ORAN_BG, ORAN_TX)}

_NT = [0]


def tab():
    _NT[0] += 1
    return f"Tableau {_NT[0]}"


def eur(n):
    s = f"{n:,.2f}".replace(",", "\u00a0").replace(".", ",")
    return s + "\u00a0€"


def fcfa(n_eur):
    v = round(n_eur * TVA)
    return f"{v:,}".replace(",", "\u00a0") + "\u00a0FCFA"


PRIX = 1140.18          # poste livré, relevé Amazon du 5 novembre 2026
RAM_1X16 = 335.95       # SO-DIMM 16 Go DDR5-4800 (Corsair Vengeance, LDLC)
RAM_KIT = 593.95        # kit 2 x 16 Go DDR5-4800 CL40 (G.Skill RipJaws, LDLC)
ECRAN = 84.95           # AOC 24B31H 23,8" IPS Full HD (LDLC)

TOTAL_RAM1 = PRIX + RAM_1X16 + ECRAN
TOTAL_KIT = PRIX + RAM_KIT + ECRAN

# --------------------------------------------------------------------------- #
doc.cover(
    eyebrow="Poste de travail — note d'arbitrage",
    title="HP Elite 800 G9 Mini — i5-14500\nCe que le poste vaut,\nce qu'il coûte",
    subtitle="Comparaison au cahier des charges GED-SERVICES, prix en euros et en francs CFA, "
             "et chiffrage documenté du passage à 32 Go.",
    meta_rows=[
        ["Objet", "**HP Elite 800 G9 Mini — Core i5-14500, 16 Go, SSD 512 Go, Windows 11 Pro**"],
        ["Source des caractéristiques", "Annonce du vendeur, place de marché Amazon.fr, consultée "
                                        "le 5 novembre 2026"],
        ["Prix relevé", f"**{eur(PRIX)}** — soit **{fcfa(PRIX)}**, livraison comprise"],
        ["Rédaction", "**GED-SERVICES** — note de prescription, rédaction impersonnelle"],
        ["Livrables", "Word (.docx) et PDF identiques, produits depuis la même source"],
        ["Date", "6 novembre 2026"],
    ],
    summary=("La réponse en trois lignes",
             "**Conforme sur l'essentiel** : processeur de 14e génération, 14 cœurs, 20 threads, "
             "Wi-Fi 6E, Windows 11 Pro — le poste dépasse le plancher technique. **Trois "
             "réserves** : 16 Go seulement, 512 Go seulement, et pas d'écran : le prix affiché "
             "n'est pas le coût du poste. **32 Go coûte cher en 2026** : 336 € s'il reste un "
             "emplacement libre, 594 € s'il faut remplacer les deux barrettes, soit 30 à 52 % du "
             "prix du poste.", "info"),
)

# --------------------------------------------------------------------------- #
doc.h1("1", "La cible GED-SERVICES, en une page")

doc.p("Toute la note se juge contre la même grille : celle qui sert à équiper les postes "
      "professionnels du parc, arrêtée en novembre 2026. Elle tient en quatre lignes, et c'est "
      "elle qui départage les machines — pas la fiche commerciale du vendeur.", small=True)

doc.table(
    ["Ce que nous exigeons", "Seuil retenu", "Pourquoi"],
    [
        ["**Processeur**", "Core i5 13e ou 14e génération, ou Core Ultra 5 — **6 cœurs minimum, "
                           "8 recommandés**, 12 threads",
         "Six cœurs suffisent à Office, Sage et Teams ; huit laissent de la marge pour cinq ans"],
        ["**Mémoire**", "**16 Go minimum, 32 Go préférable**",
         "16 Go est le plancher de 2026 ; 32 Go évite de remplacer le poste quand les profils "
         "Chrome et Teams grossissent"],
        ["**Stockage**", "**SSD NVMe 512 Go minimum, 1 To préférable**",
         "Windows, Office et les profils occupent 200 Go ; le reste est de la marge documentaire"],
        ["**Système et service**", "**Windows 11 Professionnel**, TPM 2.0 et Secure Boot, "
                                   "**garantie 3 ans sur site**",
         "Sans Pro, ni BitLocker ni stratégie de groupe ; sans garantie sur site, 10 à 15 jours "
         "d'immobilisation par incident"],
    ],
    widths=[3.4, 6.6, 7.2], font=8.6, aligns=["l", "l", "l"],
    cell_fmt={(0, 0): FMT["i"], (1, 0): FMT["i"], (2, 0): FMT["i"], (3, 0): FMT["i"]},
    caption=f"{tab()} — Le cahier des charges des postes professionnels, réduit à ses quatre "
            "exigences structurantes.",
)

doc.callout("La cible, en clair",
            "**Core i5 13e/14e génération ou Core Ultra 5 · 16 Go (32 idéal) · SSD NVMe 512 Go "
            "(1 To idéal) · Windows 11 Pro · Wi-Fi 6 · garantie 3 ans sur site · écran Full HD "
            "inclus.** Le poste examiné ici est comparé à cette ligne, critère par critère, au "
            "chapitre 2.", "info")

doc.p("**La fiche du poste, telle qu'annoncée.** Avant de comparer, il faut savoir de quoi l'on "
      "parle : voici ce que le vendeur met dans la boîte, sans interprétation.", small=True)

doc.table(
    ["Élément", "Ce qui est annoncé", "Élément", "Ce qui est annoncé"],
    [
        ["**Constructeur / gamme**", "HP — Elite 800", "**Système**", "Windows 11 Pro"],
        ["**Modèle**", "Elite 800 G9 Mini (réf. annonce B0D76M6T6R)", "**Réseau**",
         "1 GbE, Wi-Fi 6E, Bluetooth 5.3"],
        ["**Processeur**", "Intel Core i5-14500, 14 cœurs / 20 threads",
         "**Format**", "Mini PC — 1 litre"],
        ["**Mémoire**", "16 Go (DDR5 — type à confirmer)", "**Contenu du carton**",
         "Poste, clavier, souris, alimentation — **sans écran**"],
        ["**Stockage**", "SSD NVMe 512 Go", "**Prix**", f"{eur(PRIX)} — {fcfa(PRIX)}, livré"],
    ],
    widths=[3.6, 5.1, 3.2, 5.3], font=8.2, aligns=["l", "l", "l", "l"],
    caption=f"{tab()} — La configuration annoncée, lue sans commentaire.",
)

# --------------------------------------------------------------------------- #
doc.h1("2", "Le poste, critère par critère")

doc.p("Vingt et un points sont passés en revue. Le vert signale ce qui est tenu ou dépassé, le "
      "jaune ce qui atteint tout juste le plancher ou reste à confirmer, l'orange ce qui manque. "
      "Les caractéristiques proviennent de l'annonce du vendeur ; les mentions « non précisé » ne "
      "sont pas des défauts, mais des questions à poser avant l'achat.", small=True)

G, Y, O = "g", "y", "o"
ROWS = [
    ("Année de commercialisation", "2024 minimum", "Processeur de 14e génération (2024) ; châssis "
     "Elite 800 G9 né en 2022", "Conforme sur le processeur", G),
    ("Gamme", "Professionnelle", "HP Elite 800 — gamme entreprise", "Très bien", G),
    ("Format", "Tour, SFF ou Mini", "Mini PC, 1 litre", "Conforme", G),
    ("Processeur", "Core i5 13e/14e gén. ou Core Ultra 5 minimum", "Core i5-14500",
     "Très bien", G),
    ("Génération du processeur", "2024 minimum souhaité", "14e génération (Raptor Lake Refresh, "
     "1er trimestre 2024)", "Conforme", G),
    ("Nombre de cœurs", "6 minimum, 8 recommandés ou plus", "14 cœurs (6 performance + 8 efficaces)",
     "Excellent", G),
    ("Nombre de threads", "12 minimum souhaités", "20 threads", "Excellent", G),
    ("Fréquence de base", "Environ 2,5 GHz minimum", "2,6 GHz sur les cœurs performance",
     "Conforme", G),
    ("Fréquence Turbo", "4,0 GHz minimum, 4,5 recommandé", "Jusqu'à 5,0 GHz", "Excellent", G),
    ("Mémoire vive", "16 Go minimum, 32 Go idéal", "16 Go", "Minimum atteint", Y),
    ("Type de mémoire", "DDR5 préférable", "Non précisé dans l'annonce ; deux emplacements "
     "SO-DIMM DDR5 sur ce châssis", "À vérifier", Y),
    ("Stockage", "SSD NVMe 512 Go minimum, 1 To idéal", "SSD NVMe 512 Go", "Minimum atteint", Y),
    ("Carte graphique", "Intégrée acceptable", "Intel UHD Graphics 770", "Conforme", G),
    ("Ethernet", "Gigabit minimum", "1 GbE", "Conforme", G),
    ("Wi-Fi", "Wi-Fi 6 minimum", "Wi-Fi 6E", "Très bien", G),
    ("Bluetooth", "Souhaité", "Bluetooth 5.3 (description du vendeur)", "Conforme", G),
    ("Système", "Windows 11 Professionnel préféré", "Windows 11 Pro", "Conforme", G),
    ("TPM / Secure Boot", "Obligatoires en environnement professionnel", "Non détaillés",
     "À vérifier", Y),
    ("Écran", "Full HD, idéalement inclus", "Non inclus", "Non conforme au pack", O),
    ("Clavier / souris", "Souhaités", "Annoncés dans le contenu du carton", "Inclus", G),
    ("Garantie", "3 ans sur site souhaités", "Non précisée dans l'annonce", "À vérifier", Y),
]

rows = [[c, cible, constate, ev] for c, cible, constate, ev, _ in ROWS]
cf = {(i, 3): FMT[ROWS[i][4]] for i in range(len(ROWS))}
doc.table(
    ["Critère", "Caractéristique attendue", "HP Elite 800 G9 Mini — constaté", "Évaluation"],
    rows, widths=[3.5, 4.6, 5.5, 3.6], font=7.9, aligns=["l", "l", "l", "c"], cell_fmt=cf,
    caption=f"{tab()} — Cahier des charges GED-SERVICES contre caractéristiques de l'annonce : "
            "quinze points conformes ou dépassés, cinq à surveiller, un manquant.",
)

doc.p("**Lecture.** Le poste tient quinze des vingt et un points, dont les trois qui comptent le "
      "plus dans la durée : le processeur, les cœurs et le système d'exploitation professionnel. "
      "Cinq points restent en jaune : deux planchers tout juste atteints (16 Go, 512 Go) et trois "
      "mentions absentes de l'annonce (type de mémoire, TPM, garantie), qui se lèvent en une "
      "question au vendeur. La seule vraie non-conformité est l'absence d'écran, qui déplace le "
      "budget de 85 € au minimum.", small=True)

# --------------------------------------------------------------------------- #
doc.h1("3", "Le processeur : i5-14500")

doc.table(
    ["Caractéristique", "Valeur", "Ce que cela change"],
    [
        ["Architecture", "Raptor Lake Refresh — 14e génération, socket LGA 1700",
         "Une génération de plus que le plancher demandé : le poste ne sera pas dépassé avant 2029"],
        ["Cœurs / threads", "**14 (6 performance + 8 efficaces) / 20**",
         "Le double du minimum : Sage, Teams et dix onglets cohabitent sans ralentissement"],
        ["Fréquence", "2,6 GHz de base, **5,0 GHz en turbo**",
         "La réactivité perçue vient du turbo ; il tient tant que le refroidissement suit"],
        ["Cache L3", "24 Mo", "Beaucoup de travail entre la mémoire et le processeur : peu de "
                              "ralentissements sur les gros fichiers"],
        ["Enveloppe thermique", "65 W de base, jusqu'à 154 W en pointe",
         "C'est un processeur de tour : dans un litre de volume, les fréquences soutenues "
         "baissent — point à vérifier à l'usage"],
        ["Carte graphique", "Intel UHD Graphics 770", "Suffisante pour deux écrans Full HD, pas "
                                                      "pour du calcul graphique"],
    ],
    widths=[3.2, 5.6, 8.4], font=8.4, aligns=["l", "l", "l"],
    cell_fmt={(0, 0): FMT["i"], (1, 0): FMT["i"], (2, 0): FMT["i"], (3, 0): FMT["i"],
              (4, 0): FMT["i"], (5, 0): FMT["i"]},
    caption=f"{tab()} — Le processeur du poste, et l'effet concret de chaque ligne.",
)

doc.p("**Ce que ce processeur couvre sans difficulté.** Microsoft Office et plusieurs applications "
      "simultanées ; Sage Gestion commerciale et Sage Paie ; Teams et visioconférences ; Edge ou "
      "Chrome avec de nombreux onglets ; Acrobat et le traitement documentaire ; le multitâche "
      "professionnel quotidien. Sur ce profil, la puissance n'est pas le sujet : c'est la mémoire "
      "et le disque qui limitent.", small=True)

doc.p("**Une réserve de conception.** Le châssis Elite 800 G9 Mini est conçu à l'origine pour des "
      "processeurs de 35 W (série T). Le i5-14500 en consomme 65 : la machine fonctionne, mais "
      "elle ventile davantage et soutient moins longtemps ses fréquences hautes qu'une tour de "
      "même génération. Ce n'est pas rédhibitoire pour de la bureautique ; c'est à contrôler sur "
      "les tâches longues — calculs Sage, indexation, gros documents PDF.", small=True)

doc.p("**Ce qu'il ne faut pas lui demander.** Le poste est un excellent outil de bureautique "
      "intensive, pas une station de travail :", small=True)
doc.ul([
    "**Du montage vidéo ou de la retouche lourde** — la partie graphique intégrée (UHD 770) ne "
    "suit pas, et le format un litre ne dissipe pas la charge.",
    "**Plus de deux écrans 4K** — la connectique et le chipset graphique limitent à deux écrans "
    "confortables en Full HD, un seul en 4K.",
    "**Des machines virtuelles locales** — 16 Go de mémoire ne laissent pas de place à un "
    "hyperviseur de poste ; c'est le rôle du serveur.",
])

# --------------------------------------------------------------------------- #
doc.h1("4", "Le prix, en euros et en francs CFA")

doc.p("Le prix relevé est de 1 140,18 € livraison comprise, soit 747 909 FCFA à la parité fixe de "
      "655,957 FCFA pour un euro. Ce montant correspond au poste nu : il ne comprend ni écran, ni "
      "mémoire supplémentaire, ni extension de garantie.", small=True)

doc.table(
    ["Ce qui est acheté", "Euros (TTC)", "Francs CFA", "Commentaire"],
    [
        ["**Poste livré** — i5-14500, 16 Go, 512 Go, Windows 11 Pro", eur(PRIX), fcfa(PRIX),
         "Le prix de l'annonce, port compris"],
        ["Écran 24\" IPS Full HD (AOC 24B31H)", eur(ECRAN), fcfa(ECRAN),
         "Relevé LDLC, en stock — non inclus dans l'annonce"],
        ["Mémoire : 1 barrette de 16 Go DDR5-4800", eur(RAM_1X16), fcfa(RAM_1X16),
         "Relevé LDLC — si un emplacement est libre"],
        ["Mémoire : kit 2 × 16 Go DDR5-4800", eur(RAM_KIT), fcfa(RAM_KIT),
         "Relevé LDLC — si les deux barrettes doivent être remplacées"],
        ["**Poste complet, 32 Go et écran — barrette ajoutée**", f"**{eur(TOTAL_RAM1)}**",
         f"**{fcfa(TOTAL_RAM1)}**", "L'hypothèse la plus favorable"],
        ["**Poste complet, 32 Go et écran — kit de deux barrettes**", f"**{eur(TOTAL_KIT)}**",
         f"**{fcfa(TOTAL_KIT)}**", "L'hypothèse la plus défavorable"],
    ],
    widths=[7.4, 2.6, 3.2, 4.0], font=8.3, aligns=["l", "r", "r", "l"],
    cell_fmt={(3, 0): FMT["yl"], (4, 0): FMT["yl"], (5, 0): FMT["yl"],
              (4, 1): FMT["y"], (5, 1): FMT["y"], (4, 2): FMT["y"], (5, 2): FMT["y"]},
    caption=f"{tab()} — Le prix du poste et le coût réel d'un poste complet (1 € = 655,957 FCFA).",
)

doc.p("**Mise en perspective.** À 1 140 €, le poste se situe au-dessus de la tranche haute de "
      "notre grille de fixes (1 299 à 1 599 € pour des configurations complètes, écran non "
      "compris) alors qu'il n'embarque que 16 Go. Le même processeur, dans une tour Dell OptiPlex "
      "7020 ou Lenovo ThinkCentre M70t Gen 5, s'achète entre 899 et 999 € — avec des emplacements "
      "mémoire et disque, et sans la contrainte thermique du format un litre. Ce que l'Elite Mini "
      "apporte en plus est ailleurs : l'encombrement, la finition, le Wi-Fi 6E et la classe de "
      "gamme.", small=True)

doc.p("**Le même processeur, trois façons de l'acheter.** Le i5-14500 n'est pas propre à HP : on "
      "le trouve dans des tours et des petits formats, à des prix inférieurs, avec plus de place "
      "pour la mémoire.", small=True)

doc.table(
    ["Machine", "Format", "Prix constaté", "Ce qu'elle apporte"],
    [
        ["Lenovo ThinkCentre M70t Gen 5", "Tour", "899,00 €",
         "Plus d'emplacements mémoire et de baies internes, refroidissement sans contrainte"],
        ["Dell OptiPlex 7020 SFF", "Petit format", "999,00 €",
         "Deux emplacements mémoire, une baie 3,5 pouces, encombrement modéré"],
        ["**HP Elite 800 G9 Mini**", "**Mini 1 litre**", f"**{eur(PRIX)}**",
         "**Encombrement minimal, Wi-Fi 6E, finition de gamme — mais deux emplacements mémoire "
         "seulement**"],
    ],
    widths=[4.9, 2.3, 3.7, 6.1], font=8.2, aligns=["l", "c", "r", "l"],
    cell_fmt={(2, 0): FMT["yl"], (2, 1): FMT["yl"], (2, 2): FMT["yl"]},
    caption=f"{tab()} — Trois porteurs du même processeur, à configuration équivalente "
            "(16 Go, 512 Go, Windows 11 Pro).",
)

doc.callout("Ce que le prix ne dit pas",
            f"Les **747 909 FCFA** couvrent un poste nu de 16 Go. Le poste réellement livrable — "
            f"32 Go et un écran — coûte entre **{eur(TOTAL_RAM1)}** et **{eur(TOTAL_KIT)}**, soit "
            f"**{fcfa(TOTAL_RAM1)}** à **{fcfa(TOTAL_KIT)}**. C'est cette fourchette qu'il faut "
            "mettre en face d'une offre concurrente, pas le prix d'appel.", "warn")

doc.p("Annonce du vendeur : [HP Elite 800 G9 Mini — i5-14500 sur Amazon.fr](" + ANNONCE + "), "
      "consultée le 5 novembre 2026. Le prix et la disponibilité y évoluent quotidiennement ; le "
      "lien est la seule source de vérité pour le montant du jour.", small=True)

# --------------------------------------------------------------------------- #
doc.h1("5", "Passer à 32 Go : ce que cela coûte vraiment")

doc.p("Le châssis Elite 800 G9 Mini dispose de **deux emplacements SO-DIMM DDR5**, accessibles par "
      "la trappe inférieure, pour un maximum de 64 Go. La question n'est donc pas de savoir si "
      "l'extension est possible — elle l'est — mais ce qu'elle coûte, et cela dépend d'une seule "
      "inconnue : la façon dont les 16 Go sont installés d'origine.", small=True)

doc.table(
    ["Configuration livrée", "Ce qu'il faut acheter", "Coût", "En FCFA", "Résultat"],
    [
        ["**1 barrette de 16 Go**, 1 emplacement libre", "1 barrette SO-DIMM 16 Go DDR5-4800 "
         "(Corsair Vengeance, LDLC — en stock en boutique, rupture web)", eur(RAM_1X16),
         fcfa(RAM_1X16),
         "32 Go en dual channel — le meilleur cas"],
        ["**2 barrettes de 8 Go**", "Kit 2 × 16 Go DDR5-4800 CL40 (G.Skill RipJaws, LDLC)",
         eur(RAM_KIT), fcfa(RAM_KIT), "32 Go ; les deux barrettes de 8 Go deviennent une réserve"],
        ["**Déjà 32 Go**", "Rien", "0,00 €", "0 FCFA", "Aucune dépense — à négocier ainsi"],
    ],
    widths=[4.4, 5.6, 2.1, 3.0, 3.8], font=8.0, aligns=["l", "l", "r", "r", "l"],
    cell_fmt={(0, 2): FMT["g"], (0, 3): FMT["g"], (1, 2): FMT["yl"], (1, 3): FMT["yl"]},
    caption=f"{tab()} — Les deux scénarios d'extension mémoire, chiffrés sur des références en "
            "stock chez LDLC le 5 novembre 2026.",
)

doc.p("**Pourquoi ces prix.** La mémoire DDR5 SO-DIMM est devenue, en 2026, le composant le plus "
      "cher du poste après le processeur : 335,95 € la barrette de 16 Go, 593,95 € le kit de deux, "
      "relevés chez LDLC le 5 novembre 2026. Rapportée au prix du poste, l'extension coûte donc "
      "**29 % dans le meilleur cas et 52 % dans le pire** — davantage que le processeur lui-même. "
      "C'est le principal argument contre l'achat d'un poste livré en 16 Go : la mémoire n'est plus "
      "un accessoire, c'est une ligne de budget.", small=True)

doc.callout("La question à poser avant de payer",
            "« **Quelle est la configuration mémoire exacte : 1 × 16 Go ou 2 × 8 Go ?** » La "
            "réponse détermine un écart de 258 € sur la facture finale. Si le vendeur ne sait pas "
            "répondre, il faut considérer l'hypothèse haute (594 €) et négocier en conséquence — ou "
            "chercher un poste déjà livré en 32 Go.", "info")

doc.p("**Les références exactes relevées** — pour que les prix de cette note soient vérifiables et "
      "rejouables :", small=True)

doc.table(
    ["Référence", "Prix relevé", "Où"],
    [
        ["Corsair Vengeance SO-DIMM 16 Go DDR5-4800 CL40 (réf. CMSX16GX5M1A4800C40)",
         eur(RAM_1X16), "[fiche LDLC](https://www.ldlc.com/fiche/PB00495929.html)"],
        ["G.Skill RipJaws SO-DIMM 32 Go — kit 2 × 16 Go DDR5-4800 CL40 (réf. F5-4800S4039A16GX2-RS)",
         eur(RAM_KIT), "[fiche LDLC](https://www.ldlc.com/fiche/PB00503733.html)"],
        ["AOC 24B31H — écran 23,8 pouces IPS Full HD 120 Hz", eur(ECRAN),
         "[fiche LDLC](https://www.ldlc.com/fiche/PB00705865.html)"],
        ["HP Elite 800 G9 Mini i5-14500, 16 Go / 512 Go, Windows 11 Pro", eur(PRIX),
         "[annonce Amazon](" + ANNONCE + ")"],
    ],
    widths=[10.2, 2.6, 4.2], font=8.2, aligns=["l", "r", "l"],
    caption=f"{tab()} — Prix unitaires TTC relevés le 5 novembre 2026, avec leur source.",
)

# --------------------------------------------------------------------------- #
doc.h1("6", "Ce qu'il faut vérifier, et notre avis")

doc.ul([
    "**La configuration mémoire** : 1 × 16 Go ou 2 × 8 Go, et le nombre d'emplacements encore "
    "libres — c'est ce qui décide du coût de l'extension (chapitre 5).",
    "**La garantie réelle** : la mention « 3 ans » d'une annonce n'est pas un contrat. Demander le "
    "numéro de HP Care Pack, sa durée, son délai d'intervention et s'il est sur site.",
    "**TPM 2.0 et Secure Boot activés** : indispensables pour BitLocker et pour l'inscription au "
    "domaine. À faire confirmer par une capture de l'écran de sécurité Windows.",
    "**La version de BIOS et le support du 14e génération** : le châssis 800 G9 est né avec les "
    "processeurs de 12e génération. Un poste vendu en 2026 doit être à jour, sinon la garantie "
    "constructeur peut être discutée.",
    "**L'écran et les périphériques** : clavier et souris sont annoncés dans le carton, l'écran "
    "non. Prévoir 85 € au minimum, et vérifier la connectique disponible (DisplayPort, HDMI).",
])

doc.table(
    ["Domaine évalué", "Note", "Commentaire"],
    [
        ["Processeur (i5-14500)", "10 / 10", "Deux fois le minimum exigé, génération 2024"],
        ["Mémoire (16 Go)", "7 / 10", "Plancher atteint, extension coûteuse en 2026"],
        ["Stockage (512 Go NVMe)", "7 / 10", "Plancher atteint, 1 To préférable"],
        ["Connectivité (1 GbE, Wi-Fi 6E, BT 5.3)", "9 / 10", "Rien à redire"],
        ["Gamme professionnelle (Elite 800)", "9 / 10", "Châssis et finition de gamme entreprise"],
        ["Évolutivité", "6 / 10", "Deux emplacements mémoire, mais format compact et alimentation "
                                  "externe"],
        ["Pack complet (écran)", "5 / 10", "Écran absent du prix affiché"],
        ["**Évaluation globale**", "**8,5 / 10**", "**Très bon candidat technique, à condition "
                                                    "d'ajuster le prix ou la mémoire**"],
    ],
    widths=[7.0, 2.4, 7.8], font=8.6, aligns=["l", "c", "l"],
    cell_fmt={(7, 0): FMT["g"], (7, 1): FMT["g"], (7, 2): FMT["g"], (0, 1): FMT["gl"],
              (1, 1): FMT["yl"], (2, 1): FMT["yl"], (6, 1): FMT["ol"]},
    caption=f"{tab()} — Évaluation indicative selon les critères professionnels retenus, et non "
            "une note du constructeur.",
)

doc.callout("Notre avis",
            "Techniquement, ce poste répond très bien au cahier des charges : son processeur est "
            "supérieur au minimum attendu et son châssis est de gamme entreprise. Mais à "
            "**1 140,18 € (747 909 FCFA)** pour 16 Go et 512 Go, sans écran, il est cher — et "
            "l'extension à 32 Go le rend plus cher encore. **Deux issues acceptables** : soit le "
            "vendeur confirme un emplacement libre et consent un prix cohérent avec l'ajout d'une "
            "barrette (environ 1 476 € tout compris, écran exclu), soit l'on préfère une tour "
            "i5-14500 à 899–999 € que l'on équipe de 32 Go sans contrainte de place. "
            "**Acheter en l'état, sans réponse sur la mémoire, n'est pas raisonnable.**", "ok")

doc.save(OUT)

# --- métadonnées du fichier Word : GED-SERVICES, et rien d'autre
import docx as _docx
_PATH = os.path.join(OUT, BASE + ".docx")
_d = _docx.Document(_PATH)
_cp = _d.core_properties
_cp.author = "GED-SERVICES"
_cp.last_modified_by = "GED-SERVICES"
_cp.comments = ""
_cp.keywords = ""
_cp.category = ""
_cp.subject = "HP Elite 800 G9 Mini — i5-14500 : comparaison au cahier des charges, prix et mémoire"
_cp.title = "HP Elite 800 G9 Mini — i5-14500 : ce que le poste vaut, ce qu'il coûte"
_d.save(_PATH)

print("saved", OUT)
