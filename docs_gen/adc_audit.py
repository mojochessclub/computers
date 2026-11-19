# -*- coding: utf-8 -*-
"""Relevé d'incohérences de la note d'arbitrage ADCHIM (version du 19/11/2026).

Le document a été relu ligne à ligne ; chaque entrée renvoie à la page du PDF
`ADC_Workstations_2026-11-18_Note_arbitrage_postes_fixes.pdf` (12 pages) et
propose la correction à appliquer.
"""
from __future__ import annotations

import os

from render import Doc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(ROOT, os.environ.get(
    "LIVRABLES_DIR", "estimations/ADC_Workstations 2026-11-18"))
BASE = "ADC_Workstations_2026-11-18_Releve_incoherences"

ROUGE = "F8CDB6"
ORANGE = "FAEBB8"
GRIS = "E9EBEF"
FMT = {"Bloquant": {"bg": ROUGE, "color": "9B2C12"},
       "À corriger": {"bg": ORANGE, "color": "7A5E12"},
       "Forme": {"bg": GRIS, "color": "4A5058"}}

HEADERS = ["N°", "Page", "Gravité", "Ce que dit le document", "Ce qu'il faut faire"]
WIDTHS = [0.9, 1.2, 2.1, 10.4, 11.3]

ROWS = [
    # ---------------------------------------------------------- bloquants
    ("1", "10", "Bloquant",
     "Les écarts du face-à-face ont été recalculés avec les nouveaux prix (+9,00 € ; "
     "−109,42 € ; +195,59 € ; −357,53 € ; +419,04 €), mais la colonne « Lecture » garde les "
     "anciens chiffres : « AMD 76,33 € moins cher », « 211,70 € », « 388,16 € », « 393,37 € ».",
     "Réécrire les cinq lectures sur les écarts affichés : AMD 9 € plus cher en entrée Lenovo, "
     "109 € moins cher en entrée HP, 196 € plus cher en standard HP, 358 € moins cher en "
     "standard Lenovo, 419 € plus cher en confort HP."),
    ("2", "10", "Bloquant",
     "La ligne « Entrée Lenovo +9,00 € » est en orange et sa lecture affirme l'inverse du "
     "chiffre, alors que la légende annonce « vert quand l'AMD est moins cher ».",
     "Colorer +9,00 € comme un surcoût AMD (orange), et faire dire à la lecture que l'AMD n'est "
     "plus le moins cher en entrée, contrairement à la conclusion de la page 7."),
    ("3", "6", "Bloquant",
     "Tableau de l'enveloppe : les fourchettes en euros (700 → 1 000 ; 750 → 850 ; "
     "850 → 1 600,86 ; 1 286,14 → 1 624,88) ne figurent dans aucun des trois tableaux de "
     "gamme, et les colonnes FCFA de la même ligne correspondent à d'anciens prix "
     "(452 499 FCFA = 689,83 €, 681 684 = 1 039,22 €).",
     "Recalculer les deux colonnes depuis les tableaux 7 à 9 : entrée Intel 840,00 → 943,61 ; "
     "entrée AMD 834,19 → 849,00 ; standard Intel 999,95 → 1 470,45 ; standard AMD "
     "1 112,92 → 1 251,58 ; confort Intel 1 109,30 → 2 111,27 ; confort AMD 1 528,34 ; "
     "FCFA = euros × 655,957."),
    ("4", "6", "Bloquant",
     "Le commentaire sous le tableau cite des prix qui n'existent plus dans la note : "
     "« chez Lenovo autour de 763,67 € », « OptiPlex 7020 à 857,99 € », « Elite 800 G9 Mini à "
     "1 140,18 € » (aujourd'hui 849,00 ; 999,95 ; 1 055,99).",
     "Aligner tous les prix cités en prose sur les tableaux. Une seule source : le tableau."),
    ("5", "7", "Bloquant",
     "HP Pro 400 G9 : trois chiffres pour un seul dépassement — « +94,61 » sous le prix, "
     "« + 100 € » dans la colonne Conformité, « ~100€ € » dans le commentaire. Le calcul réel "
     "donne 943,61 − 850 = 93,61 €.",
     "Écrire une fois : « 943,61 €, soit +93,61 € au-dessus du couloir ». Supprimer les deux "
     "autres mentions et le double symbole €."),
    ("6", "8", "Bloquant",
     "Lenovo M90q Gen 5 : « +270€ » affiché et répété, alors que le dépassement du plafond est "
     "de 120,45 € (1 470,45 − 1 350).",
     "Corriger l'écart en +120,45 €, et le dater (« au-dessus du plafond de 1 350 € »)."),
    ("7", "8", "Bloquant",
     "HP Elite 805 G9 (AMD) : « 1 251,58 € +52€ » et « hors enveloppe », alors que "
     "1 251,58 € est sous le plafond de 1 350 € ; c'est le couloir standard (850–1 200) qui est "
     "dépassé, de 51,58 €. La conformité est écrite « Conforme, Légèrement hors enveloppe », "
     "ce qui se contredit deux fois.",
     "Distinguer les deux notions : conforme techniquement, hors couloir de gamme de 51,58 €, "
     "et dans l'enveloppe. Une seule formulation, la même pour les trois tableaux."),
    ("8", "8", "Bloquant",
     "Les décisions proposées utilisent d'anciens prix : « HP Elite 800 G9 Mini (1 140,18 €) » "
     "quand le tableau affiche 1 055,99 € ; « Dell OptiPlex 7020 SFF (999,95 €) » quand la "
     "ligne du tableau est « OptiPlex 7020 MFF » ; et la lecture annonce 1 112,95 € pour un "
     "prix de 1 112,92 €.",
     "Reprendre les trois montants et le nom exact du châssis (MFF ≠ SFF), centime compris."),
    ("9", "8", "Bloquant",
     "La lecture dit « le M90q Gen 5 en Intel (non chiffré ici) » alors que sa ligne porte "
     "1 470,45 €, et « sort de l'enveloppe max. définie à 1 532,86 € » — un plafond qui n'est "
     "pas celui de la note (1 350 €).",
     "Supprimer « non chiffré ici » et rappeler le seul plafond utile : 1 350 €."),
    ("10", "9", "Bloquant",
     "Conversion fausse : la ligne Elite Desk 800 G9 (1 363,75 €) affiche 873 604 FCFA, qui est "
     "la conversion de 1 331,80 € (≈ 100 € d'écart). Attendu : 894 561 FCFA.",
     "Recalculer, et supprimer les décimales de FCFA (« 619 623,54 » et « 1 384 902,34 ») : "
     "tout le reste du document est arrondi à l'unité."),
    ("11", "7", "Bloquant",
     "Deux autres conversions ne correspondent pas au prix affiché : 834,19 € → 542 192 FCFA "
     "(valeur de 826,56 €, attendu 547 193) et 943,61 € → 619 623 FCFA (valeur de 944,74 €, "
     "attendu 618 882).",
     "Recalculer les trois colonnes FCFA du document et vérifier que la cellule est une formule, "
     "pas une saisie."),
    ("12", "11", "Bloquant",
     "« Sous le plafond de 1 350 € avec environ 250 € de marge » : la marge est de 210,51 € "
     "(1 350 − 1 139,49). Et le chiffrage de la cible utilise 1 139,49 €, prix qui n'apparaît "
     "plus dans les tableaux (M75q en standard : 1 112,92 €).",
     "Réécrire : « marge de 237,08 € pour financer une barrette à ≈ 250 €, soit un dépassement "
     "de 12,92 € » en retenant 1 112,92 €. Le « dépassement de 39 € » devient 12,92 €."),
    ("13", "11", "Bloquant",
     "« Aucune offre chiffrée ne descend sous 1 286 € avec 32 Go et 1 To » : 1 286,14 € n'existe "
     "plus nulle part dans le document.",
     "Remplacer par la formulation exacte : « aucune offre chiffrée ne réunit 32 Go, 1 To et un "
     "i7 dans l'enveloppe ; les deux configurations conformes ne sont pas tarifées »."),

    # ---------------------------------------------------------- à corriger
    ("14", "3", "À corriger",
     "Le tableau « Ce qui est présenté, section par section » utilise l'ancienne numérotation "
     "(2 seuils, 3 processeurs, 4 enveloppe, 5 à 7 benchmark, 8 face-à-face, 9 recommandation) ; "
     "les sections réelles vont de 3 à 10. Même décalage dans « les sections 5 à 7 sont en "
     "paysage » (ce sont 6 à 8).",
     "Décaler d'un cran, ou supprimer les numéros de la colonne « Section » : elle sert à "
     "orienter, pas à numéroter."),
    ("15", "7", "À corriger",
     "Deux lignes n'ont pas de nom de modèle : la ligne HP en AMD (ProDesk 2 G1a) et la ligne "
     "Lenovo en AMD (M75q Gen 5). Le texte y est écrit en cyan sur fond cyan.",
     "Rétablir le nom en noir : sans modèle, la ligne n'est pas consultable en réunion."),
    ("16", "9", "À corriger",
     "Une même ligne porte deux machines : « Elite Desk 800 G9 (Tour) » et « Elite Mini 800 G9 », "
     "avec deux prix (1 363,75 € et 2 111,27 €) et deux conformités. HP se retrouve avec trois "
     "références Intel en confort, ce qui contredit « deux par constructeur ».",
     "Séparer en deux lignes. Le mini à 2 111,27 € peut rester affiché comme cas extrême, mais "
     "sur sa propre ligne."),
    ("17", "4", "À corriger",
     "Seuils : « i5-13500 (14C) – 14e Gén. 2023-2024 ». Le i5-13500 est un 13e génération "
     "(janvier 2023) ; c'est la puce de référence de toute l'entrée de gamme.",
     "Écrire : « i5-13500 (14C) — 13e gén., 2023 ». Vérifier au passage le i5-13400 (10C, 13e)."),
    ("18", "5", "À corriger",
     "La phrase annonce la génération standard « surlignée en vert dans les tableaux » : aucun "
     "surlignage vert n'apparaît sur cette page. Le Ryzen 7 9700X figure aussi deux fois "
     "(ligne 2024 et ligne 2025).",
     "Soit surligner réellement la ligne visée, soit ajouter une colonne « gamme visée ». "
     "Retenir une seule année par puce."),
    ("19", "7-9", "À corriger",
     "Trois systèmes de couleur cohabitent : le fond bleu/violet de la voie, le vert du "
     "surlignage éditorial, l'orange ou le jaune de la cellule. Résultat : la ligne Elite 805 G9 "
     "est surlignée en vert alors qu'elle est hors enveloppe, et la ligne Pro 400 G9 en cyan "
     "alors qu'elle est non conforme.",
     "Un seul code, celui de la légende. Si un surlignage de travail doit rester, le nommer "
     "« à l'étude » et l'expliquer dans la légende."),
    ("20", "7-9", "À corriger",
     "La colonne « Conformité » mélange deux jugements : technique (« DDR4 au lieu de DDR5 ») et "
     "budgétaire (« Hors enveloppe »). Elle contient aussi des phrases (« Non conforme: DDR4, "
     "SATA, + 100€ »).",
     "Deux colonnes : « Conformité technique » (Conforme / Partielle / Non conforme) et "
     "« Position prix » (dans le couloir / hors couloir / hors enveloppe)."),
    ("21", "10", "À corriger",
     "Le face-à-face est introduit par « 16 Go de DDR5 de part et d'autre, 512 Go de NVMe » ; "
     "or la paire entrée HP compare un Pro 400 G9 en DDR4 + SATA à un ProDesk en DDR5.",
     "Signaler la paire comme non strictement comparable, ou la retirer : c'est la seule des "
     "cinq qui ne respecte pas la règle énoncée."),
    ("22", "10", "À corriger",
     "« Chez HP, l'AMD coûte 300 € à 400 € de plus en standard » : l'écart affiché est "
     "+195,59 €. La seconde moitié de la phrase (« 300 à 400 € de moins chez Lenovo ») reste "
     "vraie (−357,53 €).",
     "Écrire « près de 200 € de plus chez HP » et « près de 360 € de moins chez Lenovo »."),
    ("23", "9", "À corriger",
     "La gamme Confort n'a pas de « Décision proposée », contrairement aux deux autres gammes ; "
     "et son « Point de vigilance » recopie mot pour mot la « Lecture de la gamme ».",
     "Ajouter une décision (« traiter en devis sur ces deux configurations ») et fusionner les "
     "deux blocs."),
    ("24", "9", "À corriger",
     "« Aucune des dix références » alors que le tableau compte onze machines ; et le dernier "
     "commentaire se termine par « Hors scope » après avoir dit que c'est « la voie la plus "
     "pertinente si la CAO arrive ».",
     "Compter onze machines, et supprimer « Hors scope » qui contredit la phrase."),
    ("25", "11", "À corriger",
     "« Garantie : trois ans sur site… si possible » : le « si possible » retire le caractère "
     "exigible de la seule clause contractuelle de la note.",
     "« Trois ans sur site, pièces et main-d'œuvre, exigés au devis. »"),
    ("26", "11", "À corriger",
     "Le poste « Lenovo M75q Gen 5 — Ryzen 7 PRO 8700GE » y est à 1 139,49 € alors que le "
     "tableau standard l'affiche à 1 112,92 € : deux prix pour la même machine dans le même "
     "document.",
     "Un seul prix, et le chiffrage de la cible recalculé dessus."),
    ("27", "9", "À corriger",
     "« 16 Go DDR » sans préciser DDR4 ou DDR5 sur le HP Pro Mini 400 G9 en i7 — alors que la "
     "DDR4 est rédhibitoire au-delà de l'entrée de gamme.",
     "Préciser DDR5 (ou DDR4) : c'est un critère de conformité, pas un détail."),
    ("28", "8", "À corriger",
     "« Freq. CPU à 1,5 Ghz » pour un i5-14500T : la fréquence de base est de 1,8 GHz "
     "(2,0 GHz pour le 13500T cité page 7).",
     "Corriger ou supprimer la mention : une fréquence fausse sur une fiche de décision se "
     "retourne vite en réunion."),
    ("29", "7-9", "À corriger",
     "Les tableaux s'appellent « Tableau 2 », « Tableau 3 », « Tableau 4 » : il n'y a pas de "
     "Tableau 1, et les tableaux des pages 4 et 6 ne sont pas numérotés.",
     "Numéroter tous les tableaux de 1 à N, ou aucun — mais pas de trou."),

    # ---------------------------------------------------------- forme
    ("30", "3", "Forme",
     "La légende du code couleur affiche de faux montants : « 000,00 € / 000 000 FCFA ».",
     "Mettre un exemple réel (943,61 € / 618 882 FCFA) ou retirer les montants de la légende."),
    ("31", "2 / 12", "Forme",
     "« Date : 18 novembre 2026 » en couverture et « Date dernière MAJ : 19 novembre 2026 » en "
     "méthode ; le document est par ailleurs daté après la date d'aujourd'hui.",
     "Une seule date, celle de la diffusion."),
    ("32", "2-12", "Forme",
     "Coquilles à corriger : « pourr » (p. 6), « si situer » (p. 3), « Les machine hors scope » "
     "(p. 3), « dhez » et « e, e,trée de Gamme » (p. 7), « reconditionn. » (p. 7), "
     "« QWESRTY » et « les logement PCIe exploitable » (p. 4), « DDR5-SDRAMM » (p. 8), "
     "« évoluutive » (p. 9), « à chiffre » au lieu de « à chiffrer » (p. 6 et 9), "
     "« 5Offre Lenovo) » et « SS512 Go » (p. 8), « Core I 5-13500 » (p. 7), "
     "« Pro Mini 400 G9 Mini » (p. 7), « entre 650 € à 1 350 € » (p. 6), « Gap de Prix » (p. 9).",
     "Passe de relecture finale ; aucune de ces coquilles ne change un chiffre, mais elles "
     "coûtent en crédibilité devant un comité."),
]


def build_doc():
    doc = Doc(
        base=BASE,
        title="Relevé d'incohérences — note d'arbitrage ADCHIM",
        subtitle="Ce qui se contredit, page par page, et ce qu'il faut corriger",
        meta=[],
        doc_ref="GED-SERVICES · relecture de la note du 19 novembre 2026",
        footer="GED-SERVICES · relecture note ADCHIM · relevé d'incohérences",
    )
    doc.cover(
        eyebrow="Relecture · note d'arbitrage postes fixes · ADCHIM",
        title="Relevé\nd'incohérences",
        subtitle="Trente-deux points, dont treize qui se voient à la première lecture : les "
                 "écarts du face-à-face, les conversions FCFA et les dépassements de couloir "
                 "ont été saisis sur des prix qui ne sont plus ceux des tableaux. Rien ne "
                 "remet en cause la démarche ; ce sont des raccords à faire avant diffusion.",
        meta_rows=[
            ["Document relu", "Note d'arbitrage postes fixes — version du 19 novembre 2026 "
                              "(12 pages)"],
            ["Méthode", "Relecture ligne à ligne : chaque montant recalculé, chaque écart "
                        "vérifié contre les tableaux, chaque renvoi de section contrôlé"],
            ["Lecture", "« Bloquant » : un chiffre faux ou contradictoire. « À corriger » : "
                        "une règle de lecture mal tenue. « Forme » : orthographe et mise en page"],
        ],
    )

    doc.h1_plain("1. Ce qu'il faut retenir")
    doc.p("**Le document est bien construit et sa démarche tient.** Les trois gammes, la double "
          "voie Intel / AMD, la grille de conformité et le face-à-face sont une vraie méthode "
          "d'arbitrage : un directeur peut décider sur cette base. Ce qui ne tient pas, c'est "
          "le raccord entre les prix mis à jour et les commentaires qui les expliquent.",
          lead=True)
    doc.p("Treize points sont bloquants, et ils ont tous la même origine : les prix des tableaux "
          "de gamme ont été réactualisés, mais les écarts du face-à-face (p. 10), les conversions "
          "FCFA (p. 6 à 9) et les dépassements de couloir (p. 7 et 8) ont été laissés sur les "
          "montants précédents. Un lecteur qui vérifie une seule ligne trouve l'écart : c'est le "
          "risque principal en réunion.", small=True)
    doc.p("Deux autres familles de défauts sont à traiter avant diffusion : le tableau de "
          "l'enveloppe (p. 6) mélange deux jeux de prix — des fourchettes en euros qui "
          "n'apparaissent nulle part ailleurs et des conversions en FCFA calculées sur les "
          "anciens montants ; et trois lignes de tableau (p. 7 et 9) sont inexploitables telles "
          "quelles, soit parce que le nom du modèle manque, soit parce qu'elles portent deux "
          "machines à la fois.", small=True)

    doc.spacer(0.2)
    doc.h2("Le relevé complet")
    doc.p("Chaque ligne renvoie à la page du PDF et propose la correction à appliquer. Les "
          "montants de la colonne de droite sont recalculés à 1 € = 655,957 FCFA.", small=True)
    doc.landscape(True)
    body, cf = [], {}
    for i, (num, page, sev, constat, corr) in enumerate(ROWS):
        body.append([num, page, sev, constat, corr])
        cf[(i, 2)] = FMT[sev]
    doc.table(HEADERS, body, WIDTHS, font=8.0, aligns=["c", "c", "c", "l", "l"],
              cell_fmt=cf, header_bg="1F3B63",
              caption="Relevé établi sur le PDF de 12 pages. Les numéros de page sont ceux du "
                      "pied de page du document.")
    doc.landscape(False)

    doc.h1_plain("2. Ce que je ne changerais pas")
    doc.p("Trois choix structurent la note et méritent d'être conservés tels quels :", small=True)
    doc.ul([
        "**Les trois gammes**, avec un couloir de prix par gamme : c'est ce qui permet de "
        "trancher poste par poste sans renégocier le principe à chaque commande.",
        "**Le face-à-face à configuration équivalente**, avec l'écart signé : c'est la seule "
        "partie du document qui démontre quelque chose, et elle démontre juste — l'AMD gagne en "
        "entrée de gamme, il perd dès qu'on demande un châssis extensible.",
        "**Le refus d'estimer un prix manquant** : la mention « à chiffrer » est plus utile "
        "qu'un montant inventé, et elle protège la note en réunion.",
    ], small=True)
    doc.p("Le travail restant est un travail de recalcul, pas de réécriture : une heure sur les "
          "tableaux et le face-à-face, et la note est diffusable.", small=True)

    doc.h1_plain("3. Par où commencer, si vous ne voulez pas y passer des heures")
    doc.p("Quatre corrections suffisent à rendre la note exploitable en réunion. Le reste — "
          "coquilles, surlignages, dates — peut attendre une seconde passe.", small=True)
    doc.table(["Ordre", "Quoi", "Temps", "Pourquoi d'abord"], [
        ["1", "Recalculer le tableau de l'enveloppe (p. 6) : deux colonnes de prix cohérentes, "
              "en euros et en FCFA", "20 min",
         "C'est la page qu'un directeur regarde en premier, et la seule dont les deux colonnes "
         "se contredisent visiblement."],
        ["2", "Réécrire les cinq lectures du face-à-face (p. 10) sur les écarts affichés",
         "10 min", "C'est la seule partie du document qui démontre quelque chose : une lecture "
         "fausse annule la démonstration."],
        ["3", "Trancher les trois lignes litigieuses : les deux modèles manquants (p. 7) et la "
              "ligne « deux machines » (p. 9)", "20 min",
         "Sans nom de modèle, la ligne n'est pas consultable en séance."],
        ["4", "Unifier les dépassements : +93,61 €, +120,45 €, +51,58 €, et la distinction "
              "couloir / enveloppe", "20 min",
         "Trois chiffres faux tombent dans les colonnes mêmes que les tableaux de gamme."],
    ], [1.2, 7.4, 1.5, 7.0], font=8.4, aligns=["c", "l", "c", "l"],
        caption="Durées indicatives pour une personne qui connaît déjà les chiffres.")
    doc.p("**La version comité de direction, livrée en même temps que ce relevé, corrige déjà "
          "tout cela.** Elle ne reprend que les prix des tableaux, recalcule les écarts et les "
          "conversions FCFA, sépare conformité technique et position de prix, et ne conserve que "
          "ce qui sert la décision : la philosophie, les cibles, les tableaux de gamme avec les "
          "modèles retenus en vert, le face-à-face des processeurs et les formats de châssis.",
          small=True)

    dpath, ppath = doc.save(OUTDIR)
    return dpath, ppath


if __name__ == "__main__":
    print(build_doc())
