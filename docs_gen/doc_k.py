# -*- coding: utf-8 -*-
"""Demande de devis ferme — trois machines HPE, neuf configurations, trois fournisseurs.
Dossier prêt à envoyer (PC21, Senetic, ServerMall) + grille de dépouillement."""
import os
from urllib.parse import quote
from render import Doc

BASE = "K_Demande_de_devis_ferme_trois_machines_trois_fournisseurs"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables")

doc = Doc(
    base=BASE,
    title="Demande de devis ferme — trois machines, neuf configurations",
    subtitle="Dossier prêt à envoyer à PC21.fr, Senetic et ServerMall, et grille de dépouillement",
    meta=[], doc_ref="GED-RAP-2026-09 · Confidentiel — usage interne",
    footer="Demande de devis ferme · HPE ProLiant DL325, DL320, DL380",
)

VERT_BG, VERT_TX = "E3F0DC", "1E6B2F"
JAUN_BG, JAUN_TX = "FBF3D0", "8A6D00"
ORAN_BG, ORAN_TX = "FBE0CE", "B4500F"
BLEU_BG = "EAF0F7"


def F(bg=None, tx=None, b=False, i=False):
    return {"bg": bg, "color": tx, "b": b, "i": i}


FMT = {"g": F(VERT_BG, VERT_TX, True), "y": F(JAUN_BG, JAUN_TX, True),
       "o": F(ORAN_BG, ORAN_TX, True), "p": F(), "i": F(BLEU_BG)}

_NT = [0]


def tab():
    _NT[0] += 1
    return f"Tableau {_NT[0]}"


def eur(n):
    return f"{round(n):,}".replace(",", " ") + " €"


# --------------------------------------------------------------------------- #
CONFIGS = [
    # machine, cpu, cœurs/ghz, estimation interne PC21
    ("DL325 Gen11", "EPYC 9124", "16 c / 3,00 GHz", 8600),
    ("DL325 Gen11", "EPYC 9125", "16 c / 2,60 GHz", 8700),
    ("DL325 Gen11", "EPYC 9224", "24 c / 2,50 GHz", 8900),
    ("DL320 Gen11", "Xeon Silver 4510", "12 c / 2,40 GHz", 9100),
    ("DL320 Gen11", "Xeon Silver 4410Y", "12 c / 2,00 GHz", 9000),
    ("DL320 Gen11", "Xeon Gold 6426Y", "16 c / 2,50 GHz", 10000),
    ("DL380 Gen11", "Xeon Silver 4510", "12 c / 2,40 GHz", 9900),
    ("DL380 Gen11", "Xeon Silver 4410Y", "12 c / 2,00 GHz", 9800),
    ("DL380 Gen11", "Xeon Gold 6426Y", "16 c / 2,50 GHz", 10800),
]

OBJET = "Demande de devis ferme — HPE ProLiant Gen11, 9 configurations, garantie 3 ans sur site"
CORPS_TECH = (
    "Configuration commune aux neuf lignes : serveur HPE ProLiant Gen11 neuf, 1 unité par ligne ; "
    "128 Go de DDR5 en 4 × 32 Go RDIMM 4 800 MT/s ; 2 × 1,92 To SSD 2,5\" (SAS ou NVMe selon "
    "disponibilité) livrés avec caddies, montés en RAID1 ; contrôleur RAID HPE MR416i-o ou "
    "équivalent avec au moins 2 Go de cache protégé ; 2 × 10 GbE BASE-T sur carte OCP 3.0 ou "
    "PCIe ; 2 × 800 W redondantes ; kit rails 19 pouces ; iLO 6 ; garantie constructeur 3 ans "
    "sur site, intervention J+1 ouvré ; sans système d'exploitation (Proxmox VE installé par "
    "nos soins).")
CORPS_DEMANDE = (
    "Merci de nous adresser, pour chacune des neuf lignes : le prix unitaire HT rendu "
    "Libreville (DDP, fret et douane inclus) ou, à défaut, le prix HT départ entrepôt ; le "
    "numéro de produit HPE (Product Number) exact ; le délai de livraison ferme ; la durée de "
    "validité de l'offre. Merci d'y ajouter, en options séparées : la seconde unité identique, "
    "le module de 32 Go DDR5 supplémentaire, et la carte 2 × 10 GbE si elle n'est pas incluse.")
CORPS_FIN = ("Réponse souhaitée sous cinq jours ouvrés. Le document attendu est un devis daté, "
             "numéroté et signé, et non une cotation indicative : il servira de base à "
             "l'engagement. Nous restons disponibles pour tout ajustement de référence.")

MAILTO_SM = ("mailto:info@servermall.com?subject=" + quote(OBJET) +
             "&body=" + quote("Bonjour,\n\n" + CORPS_TECH + "\n\n" + CORPS_DEMANDE + "\n\n" +
                              CORPS_FIN + "\n\nCordialement,\nGED-SERVICES"))


# --------------------------------------------------------------------------- #
doc.cover(
    eyebrow="Dossier de consultation — HPE ProLiant Gen11",
    title="Demande de devis ferme :\ntrois machines, neuf configurations",
    subtitle="Le cahier des charges exact, les neuf lignes à chiffrer, les trois canaux de "
             "consultation avec le message prêt à envoyer, et la grille qui départagera les "
             "offres au retour.",
    meta_rows=[
        ["Rédaction", "**GED-SERVICES** — dossier de consultation, rédaction impersonnelle"],
        ["Objet", "Obtenir un **devis ferme** — daté, numéroté, avec délai et durée de validité — "
                  "pour neuf configurations HPE, avant d'engager la dépense"],
        ["Machines", "**DL325 Gen11** (1U, SP5, EPYC) · **DL320 Gen11** (1U, LGA 4677, Xeon) · "
                     "**DL380 Gen11** (2U, LGA 4677, Xeon)"],
        ["Consultés", "**PC21.fr** (formulaire de devis et téléphone) · **Senetic** (formulaire de "
                      "demande) · **ServerMall** (courriel et messagerie)"],
        ["Ce que ce dossier n'est pas", "Un devis. Un devis n'existe que dans le document émis "
                                        "par le fournisseur : ce dossier est ce qu'on lui envoie "
                                        "pour l'obtenir, et ce qui permet de le comparer"],
        ["Date", "6 novembre 2026"],
    ],
    summary=("Comment s'en servir",
             "Le **chapitre 2** contient le cahier des charges à copier tel quel. Le **chapitre 3** "
             "liste les neuf lignes à chiffrer, avec une colonne d'estimation interne qui sert "
             "seulement à repérer une offre aberrante. Le **chapitre 4** donne, pour chacun des "
             "trois fournisseurs, le canal, le message prêt à envoyer et le lien. Le "
             "**chapitre 5** est la grille où l'on reporte les devis reçus pour les départager.",
             "info"),
)

# --------------------------------------------------------------------------- #
doc.h1("1", "Un devis ferme ne se déduit pas, il se demande")

doc.p("Les fiches DL325, DL320 et DL380 s'appuient sur des prix **relevés** — la fiche PC21 "
      "P77252-425 — et, pour les autres lignes, sur un modèle économique construit à partir du "
      "configurateur ServerMall. Ce modèle est cohérent, il n'est pas engageant : il ne dit pas "
      "ce qu'un fournisseur signera demain. Un devis ferme, lui, porte une date, un numéro, une "
      "durée de validité, un délai de livraison et une signature. Il n'y a qu'un moyen de "
      "l'obtenir : le demander, avec un cahier des charges assez précis pour que les réponses "
      "soient comparables.", lead=True)

doc.table(
    ["Statut du prix", "Ce qu'il vaut", "Ce qu'il permet", "Ce qu'il ne permet pas"],
    [
        ["**Relevé**", "Le prix affiché sur une page publique, à une date donnée",
         "Situer le marché, vérifier un ordre de grandeur", "Engager une dépense"],
        ["**Modélisé**", "Un calcul à partir d'un relevé et d'un écart constaté",
         "Comparer des configurations entre elles", "Prétendre à un prix réel"],
        ["**Devis ferme**", "Un engagement du fournisseur, daté, numéroté, avec validité et délai",
         "**Commander**", "— c'est le seul qui vaut signature"],
    ],
    widths=[3.0, 6.4, 4.4, 3.1], font=8.4, aligns=["l", "l", "l", "l"],
    caption=f"{tab()} — Les trois statuts d'un prix. Les fiches précédentes vivent dans les deux "
            "premières lignes ; ce dossier a pour objet d'atteindre la troisième.",
    cell_fmt={(2, 0): FMT["g"], (2, 1): FMT["g"]}, zebra=False)

doc.p("**Ce qu'un devis ferme doit contenir, sans quoi il ne l'est pas.** La référence HPE exacte "
      "(Product Number) et non une description ; le prix unitaire HT et le total ; la livraison "
      "en **DDP** ou, à défaut, le partage clair des frais et du risque ; le **délai de livraison "
      "ferme**, pas « environ » ; la **durée de validité** de l'offre ; le niveau de garantie "
      "constructeur (3 ans sur site, J+1 ouvré) ; et la signature d'une personne habilitée. "
      "**Un prix sans délai n'est pas un prix** : c'est une intention.", small=True)

doc.callout("Pourquoi neuf lignes et non trois",
            "Les trois fournisseurs ne chiffrent pas de la même façon selon le processeur : l'un "
            "a du stock sur le 9124 et commande le 9224, l'autre fait l'inverse. Demander les "
            "neuf configurations d'un coup — trois machines × trois processeurs admissibles — "
            "coûte le même effort au fournisseur et donne la vraie grille de prix. C'est aussi "
            "le seul moyen de vérifier si l'écart entre processeurs que nous modélisons existe "
            "réellement dans un devis.", "info")

# --------------------------------------------------------------------------- #
doc.h1("2", "Le cahier des charges à envoyer tel quel")

doc.p("Le texte ci-dessous est celui qui part chez les trois fournisseurs. Il est volontairement "
      "court et entièrement chiffré : chaque ligne correspond à une référence commandable, ce qui "
      "évite les devis « à partir de ».", small=True)

doc.table(
    ["Poste", "Spécification exigée", "Tolérance admise"],
    [
        ["**Serveur**", "HPE ProLiant **Gen11** neuf, 1 unité par ligne — DL325 (1U, SP5), "
                        "DL320 (1U, LGA 4677) ou DL380 (2U, LGA 4677)",
         "Aucune : génération et modèle imposés"],
        ["**Processeur**", "Celui de la ligne, monté d'usine, jamais en seconde monte",
         "Aucune"],
        ["**Mémoire**", "**128 Go DDR5** en **4 × 32 Go** RDIMM 4 800 MT/s",
         "4 × 32 Go imposé (une barrette de 128 Go est refusée : elle bloque la montée à 256 Go)"],
        ["**Stockage**", "**2 × 1,92 To SSD** 2,5 pouces avec caddies, en **RAID1** (1,92 To utiles)",
         "SAS ou NVMe selon disponibilité, à prix égal ou inférieur"],
        ["**Contrôleur RAID**", "HPE **MR416i-o**, ou équivalent avec ≥ 2 Go de cache protégé",
         "MR416i-o préféré ; à défaut, préciser la référence"],
        ["**Réseau**", "**2 × 10 GbE BASE-T** (OCP 3.0 ou PCIe) + 4 × 1 GbE",
         "SFP+ accepté si le prix du switch est indiqué en option"],
        ["**Alimentation**", "**2 × 800 W** redondantes, câbles inclus", "Aucune"],
        ["**Rails et gestion**", "Kit rails 19 pouces · **iLO 6** (licence standard)",
         "iLO Advanced en option chiffrée à part"],
        ["**Garantie**", "**3 ans sur site, J+1 ouvré**, pièces et main-d'œuvre",
         "4 ou 5 ans acceptés en option chiffrée"],
        ["**Système**", "Sans OS — Proxmox VE installé par nos soins", "Aucune"],
        ["**Livraison**", "**DDP Libreville** (fret et douane inclus) ou prix départ entrepôt "
                          "clairement identifié", "Préciser l'Incoterm dans tous les cas"],
    ],
    widths=[2.8, 8.6, 5.5], font=8.0, aligns=["l", "l", "l"],
    caption=f"{tab()} — Le cahier des charges. C'est ce bloc qui garantit que les trois devis "
            "parleront de la même machine.",
    cell_fmt={(3, 0): FMT["g"], (8, 0): FMT["g"], (10, 0): FMT["g"]}, zebra=True)

doc.p("**Ce que nous refusons, et qui doit être écrit dans la demande.** Du matériel "
      "reconditionné ou de démonstration présenté comme neuf ; un processeur posé en seconde "
      "monte ; de la mémoire non HPE sur une machine sous garantie constructeur ; une garantie "
      "de type retour atelier ; et une offre sans référence produit. Ces quatre points éliminent "
      "d'eux-mêmes la moitié des réponses approximatives.", small=True)

doc.p("**Les trois options à chiffrer séparément**, pour éviter qu'elles soient fondues dans un "
      "prix global : la **seconde unité identique** (elle révèle le vrai prix de gros), le "
      "**module de 32 Go DDR5 supplémentaire** (le poste le plus volatil du marché), et la "
      "**carte 2 × 10 GbE** si elle n'est pas incluse de série.", small=True)

doc.callout("La livraison, à préciser dès la demande",
            "Le serveur part pour **Libreville**. Trois fournisseurs sur trois cotent en "
            "**EXW ou DAP Europe** par défaut : demander explicitement le **DDP Libreville** "
            "évite de comparer des prix qui ne couvrent pas le même trajet. À faire figurer au "
            "devis : le mode d'expédition (aérien ou maritime), le dédouanement, la part de "
            "fret, et le délai **porte à porte** — comptez 3 à 6 semaines selon le mode. Si le "
            "fournisseur refuse le DDP, demander un forfait de fret séparé, identique pour les "
            "neuf lignes : c'est la seule façon de comparer.", "warn")

# --------------------------------------------------------------------------- #
doc.landscape(True)
doc.h1("3", "Les neuf lignes à chiffrer")

doc.p("Chaque ligne est une configuration complète, pas un processeur. La colonne « estimation "
      "interne » vient du modèle construit sur le configurateur ServerMall ; elle ne sert qu'à "
      "repérer une réponse aberrante — un devis à 6 000 € ou à 20 000 € pour le DL325 doit être "
      "justifié avant d'être retenu.", small=True)

rows = []
for i, (mac, cpu, cc, est) in enumerate(CONFIGS):
    rows.append([f"**L{i+1}**", mac, f"**{cpu}** · {cc}", f"{est:,}".replace(",", " ") + " €",
                 "", "", "", ""])

doc.table(
    ["Ligne", "Machine", "Processeur · cœurs · fréquence", "Estimation interne",
     "Prix HT (fournisseur)", "Réf. HPE", "Délai ferme", "Validité"],
    rows,
    widths=[1.3, 3.0, 7.4, 2.6, 3.2, 2.8, 2.6, 2.4], font=10.0,
    aligns=["c", "l", "l", "r", "r", "c", "c", "c"],
    caption=f"{tab()} — Les neuf configurations à faire chiffrer, une unité par ligne. Les "
            "quatre colonnes de droite sont à remplir par le fournisseur ; l'estimation interne "
            "ne doit pas lui être communiquée.",
    cell_fmt={**{(i, 3): FMT["i"] for i in range(9)},
              **{(i, j): FMT["p"] for i in range(9) for j in (4, 5, 6, 7)}},
    zebra=False)

doc.h2("Les trois options, à chiffrer à part")
doc.table(
    ["Option", "Contenu", "Prix HT", "Intérêt pour la décision"],
    [
        ["**Seconde unité**", "La même configuration que L1 (DL325 · EPYC 9124), à l'identique",
         "", "Révèle le vrai prix de gros : l'écart avec la première unité mesure la marge de "
             "négociation"],
        ["**Module mémoire**", "1 × 32 Go DDR5-4800 RDIMM HPE, pour passer de 128 à 160 Go",
         "", "Le poste le plus volatil du marché : c'est là que se joue la revalorisation à six "
             "mois"],
        ["**Carte réseau**", "2 × 10 GbE BASE-T (OCP 3.0 ou PCIe), si elle n'est pas incluse",
         "", "À comparer au prix du switch : 900 € environ, quel que soit le fournisseur"],
    ],
    widths=[2.8, 10.0, 3.2, 9.6], font=9.0, aligns=["l", "l", "r", "l"],
    caption=f"{tab()} — Les trois options à demander en plus des neuf lignes. Elles évitent les "
            "prix globaux où l'on ne sait plus ce qui est payé.",
    cell_fmt={(i, 2): FMT["p"] for i in range(3)}, zebra=True)

doc.p("**Comment envoyer.** Le plus efficace est un message unique par fournisseur, avec les neuf "
      "lignes en tableau dans le corps du message et, en pièce jointe, la version Word de ce "
      "document. Les trois canaux sont décrits au chapitre 4, avec le message prêt à copier.", small=True)

# --------------------------------------------------------------------------- #
doc.landscape(False)
doc.h1("4", "Les trois demandes, prêtes à envoyer")

doc.table(
    ["Fournisseur", "Canal", "Ce qu'il faut faire", "Réponse attendue"],
    [
        ["**PC21.fr**", "Formulaire **« Demande de Prix »** et ligne directe "
                        "**01 43 00 43 08**",
         "Déposer le message du chapitre 2 sur le formulaire, puis appeler le lendemain en "
         "rappelant le numéro de la demande", "Devis ferme sous 24 à 48 h"],
        ["**Senetic**", "Formulaire **« Demande »** (panier de devis)",
         "Créer la demande en y collant les neuf lignes ; leur outil renvoie un numéro de "
         "dossier", "Cotation sous 2 à 5 jours"],
        ["**ServerMall**", "Courriel **info@servermall.com** ou messagerie "
                           "(+370 661 08395)",
         "Envoyer le message pré-rempli ; leur configurateur donne déjà la composition, reste à "
         "obtenir le devis signé", "Offre sous 24 h, « dans l'heure » selon leur page"],
    ],
    widths=[2.8, 5.4, 6.2, 2.5], font=8.2, aligns=["l", "l", "l", "l"],
    caption=f"{tab()} — Les trois canaux de consultation, vérifiés le 6 novembre 2026.",
    cell_fmt={(0, 0): FMT["g"], (1, 0): FMT["g"], (2, 0): FMT["g"]}, zebra=True)

doc.h2("Le message, prêt à copier")
doc.p("**Objet :** " + OBJET, small=True)

doc.callout("Le corps du message", "Bonjour, " + CORPS_TECH, "info")
doc.p(CORPS_DEMANDE + " " + CORPS_FIN, small=True)

doc.h2("Les liens")
doc.table(
    ["Fournisseur", "Lien direct", "Ce qu'il ouvre"],
    [
        ["**PC21.fr**", "[Demande de devis gratuit](https://www.pc21.fr/devis-gratuit.php)",
         "Le formulaire de devis, avec le numéro de téléphone du service client"],
        ["**PC21.fr**", "[Nous contacter](https://www.pc21.fr/nous_contacter.php)",
         "Le formulaire de contact général, pour un dossier de plusieurs lignes"],
        ["**Senetic**", "[Demande de devis](https://www.senetic.fr/inquiry/form)",
         "Le panier de devis Senetic : on y ajoute les références, puis on demande la cotation"],
        ["**ServerMall**", f"[Écrire à ServerMall]({MAILTO_SM})",
         "Un courriel pré-rempli (objet et corps du message) vers info@servermall.com"],
        ["**ServerMall**", "[Configurateur DL325](https://servermall.com/sets/"
                           "hpe-proliant-dl325-gen11-server/) · "
                           "[DL320](https://servermall.com/sets/hpe-proliant-dl320-gen11-server/) · "
                           "[DL380](https://servermall.com/sets/hpe-proliant-dl380-gen11-server/)",
         "Les trois configurateurs, pour vérifier la composition avant de demander le devis"],
    ],
    widths=[2.8, 8.2, 5.9], font=8.0, aligns=["l", "l", "l"],
    caption=f"{tab()} — Les cinq liens utiles. Les formulaires sont des pages publiques ; le "
            "courriel ServerMall est déjà rédigé.",
    zebra=True)

# --------------------------------------------------------------------------- #
doc.h1("5", "La grille de dépouillement")

doc.p("Au retour des devis, on reporte les prix dans cette grille. Elle ne compare que ce qui est "
      "comparable : le prix **DDP** (ou le prix départ entrepôt majoré du fret), la garantie, le "
      "délai et la validité. Un devis moins cher mais à 60 jours de délai n'est pas moins cher : "
      "il décale le projet de deux mois.", small=True)

rows2 = []
for mac, cpu, cc, est in CONFIGS:
    rows2.append([mac, f"**{cpu}**", f"{est:,}".replace(",", " ") + " €", "", "", "", "", ""])
doc.table(
    ["Machine", "Processeur", "Estimation", "PC21", "Senetic", "ServerMall", "Meilleur", "Écart"],
    rows2,
    widths=[2.4, 3.9, 1.9, 1.7, 1.7, 2.3, 1.9, 1.2], font=7.8,
    aligns=["l", "l", "r", "r", "r", "r", "r", "c"],
    caption=f"{tab()} — Grille à remplir au retour des trois devis. La colonne « écart » est le "
            "pourcentage entre le meilleur prix et l'estimation interne.",
    cell_fmt={(i, 2): FMT["i"] for i in range(len(rows2))}, zebra=True)

doc.h2("Les quatre règles qui départagent")
doc.ul([
    "**Prix rendu, pas prix affiché.** Un devis EXW moins cher de 8 % ne l'est plus une fois le "
    "fret et la douane ajoutés : on compare en **DDP Libreville**, ou on ajoute le même forfait à "
    "toutes les lignes.",
    "**Garantie au même niveau.** 3 ans sur site J+1 ouvré chez tous, sinon on chiffre l'extension "
    "manquante avant de comparer. Une garantie retour atelier n'a pas le même prix.",
    "**Délai ferme.** On retient la date d'engagement, pas la fourchette. Au-delà de trois "
    "semaines, on demande une date de livraison contractuelle.",
    "**Validité de l'offre.** Trente jours minimum. En dessous, le prix ne vaut que pour la "
    "discussion, pas pour la commande.",
])

doc.callout("Ce qui se passe ensuite",
            "Dès que les trois devis sont revenus, les fiches DL325, DL320 et DL380 sont "
            "**remises à jour avec les prix fermes** : les colonnes « tarif PC21 », « tarif "
            "Senetic » et « tarif ServerMall » passent du statut *modélisé* au statut *devisé*, "
            "avec le numéro de devis et sa date de validité. C'est l'affaire d'une passe de "
            "correction, pas d'une réécriture.", "ok")

doc.p("**Avertissement.** Les estimations internes de ce dossier proviennent du configurateur "
      "public ServerMall (relevé du 6 novembre 2026) et du modèle PC21 décrit dans les fiches "
      "précédentes. Elles ne sont communiquées à aucun fournisseur. Les délais de réponse "
      "annoncés sont ceux que les sites affichent, pas des engagements : seul le devis reçu fait "
      "foi.", small=True)

doc.save(OUT)
print("saved", OUT)
