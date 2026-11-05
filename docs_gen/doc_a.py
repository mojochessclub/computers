# -*- coding: utf-8 -*-
"""Document A — reformulation de l'analyse de Joël, orientée qualité / prix / performance."""
import os
from render import Doc
from data import (OFFRES_JOEL, SCORES_A, POIDS_A, PRIX_MARCHE, EXISTANT,
                  note_ponderee, TCO)

BASE = "A_Analyse_Joel_reformulee_qualite_prix_performance"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables")


def eur(n):
    return f"{n:,.0f}".replace(",", " ") + " €"


def d(n, dec=1):
    return f"{n:,.{dec}f}".replace(",", " ").replace(".", ",")


doc = Doc(
    base=BASE,
    title="Rapatriement de l'hyperviseur",
    subtitle="Note de décision — lecture qualité / prix / performance",
    meta=[],
    doc_ref="GED-RAP-2026-01 · Confidentiel — usage interne",
    footer="Rapatriement de l'hyperviseur · note de décision",
)

# ---------------------------------------------------------------------------
doc.cover(
    eyebrow="Note de décision — Direction Générale",
    title="Rapatrier l'hyperviseur :\nquelle offre, pour quel budget",
    subtitle="Reformulation de l'analyse technique du 4 novembre 2026, "
             "relue sous l'angle qualité / prix / performance et présentée en trois tranches "
             "d'investissement.",
    meta_rows=[
        ["Destinataire", "**Jad — Direction Générale**"],
        ["Objet", "Choix de la plateforme serveur pour le rapatriement de l'infrastructure "
                  "aujourd'hui hébergée chez Online / Scaleway"],
        ["Base de travail", "Analyse et chiffrages transmis par Joël MBA OYONE (GED-SERVICES), "
                            "revendeur ServerMall, complétés par des relevés de prix marché"],
        ["Décision attendue", "Choix d'une **tranche d'investissement** et autorisation de lancer "
                              "un appel à devis sur la configuration cible"],
        ["Hyperviseur retenu", "**Proxmox VE** (licence par socket, sans coût par cœur)"],
        ["Date", "5 novembre 2026"],
    ],
    summary=("Ce qu'il faut retenir",
             "L'existant n'est pas limité par le processeur mais par la **mémoire (88 %) et le "
             "stockage (90 %)**. Toute configuration à 64 Go de RAM reconduit donc la saturation.\n"
             "Deux offres seulement méritent la décision : le **DL325 Gen11 neuf** (cible technique, "
             "9 174 € HT) et le **DL180 Gen10 reconditionné 128 Go** (tranche basse, 5 621 € HT). "
             "Le prix affiché ne représente que 40 à 50 % du coût réel du projet.",
             "warn"),
)

# ---------------------------------------------------------------------------
doc.h1("1", "La décision en une page")

doc.p("L'analyse de Joël est solide sur le diagnostic : elle identifie correctement que le "
      "processeur est sous-employé et que la mémoire et le stockage sont les deux ressources "
      "saturées. Cette note conserve ce diagnostic et le traduit en termes de décision : "
      "**ce que l'on achète, ce que l'on paie, et ce que l'on sacrifie** à chaque niveau de budget.",
      lead=True)

doc.kpi([("88 %", "RAM occupée sur 64 Go"),
         ("90 %", "disque occupé"),
         ("15 %", "CPU occupé"),
         ("4", "configurations réellement comparables")])

doc.h2("Les deux offres qui méritent la décision")

doc.table(
    ["Critère", "**Offre n°1 — DL325 Gen11**", "**Offre n°2 — DL180 Gen10 128 Go**"],
    [
        ["Génération / état", "Gen11 · **neuf**, garantie constructeur 3 ans", "Gen10 · **reconditionné**, garantie revendeur"],
        ["Processeur", "AMD EPYC 9124 — **16 cœurs / 3,0 GHz**", "**non spécifié** dans le chiffrage (point bloquant)"],
        ["Mémoire", "64 Go DDR5 (12 emplacements, extensible à 3 To)", "**128 Go DDR4** immédiats"],
        ["Stockage", "8 baies SFF — disques non chiffrés", "2×1,92 To → **1,92 To utiles en RAID1**"],
        ["Réseau", "2×10 GbE incluse", "2×10 GbE + 2×1 GbE"],
        ["Prix HT indicatif", "**9 174 €**", "**5 621 €**"],
        ["Prix au Go de RAM", "143 € / Go", "**44 € / Go**"],
        ["Score qualité / prix / perf.", "**71,5 / 100**", "66,0 / 100"],
        ["Ce que l'on achète", "La pérennité : plateforme moderne, DDR5, garantie, horizon 5–7 ans", "La capacité : mémoire et disque immédiats, à moitié prix"],
        ["Ce que l'on sacrifie", "La marge mémoire : 64 Go ne règle pas la saturation constatée", "La pérennité : DDR4 en fin de vie, CPU inconnu, garantie 12–24 mois"],
        ["Verdict", "**Cible technique** — à condition de passer à 128 Go", "**Repli budgétaire** — si l'enveloppe est plafonnée à 7 k€"],
    ],
    widths=[3.5, 6.7, 6.9], font=7.9, caption="Tableau 1 — Les deux seules offres qui résistent à l'analyse comparative (prix HT indicatifs, hors transport et douane).",
    row_bg={5: "EAF0F7", 7: "EAF0F7"})

doc.callout("Recommandation en une phrase",
            "Partir sur le **DL325 Gen11 en 128 Go de mémoire** (et non 64 Go) : c'est la seule "
            "configuration qui traite simultanément les deux contraintes constatées — mémoire et "
            "stockage — tout en restant sur une plateforme neuve garantie 3 ans sous Proxmox. "
            "Enveloppe matérielle cible : **11 000 à 13 000 € HT**, soit 2 000 à 3 000 € de plus "
            "que l'enveloppe de 9–10 k€ évoquée dans l'analyse initiale.",
            "ok")

doc.h2("Ce que cette note ajoute à l'analyse initiale")

doc.ul([
    "**Le classement est objectivé** : six critères pondérés, un score comparable — au lieu d'une "
    "préférence de constructeur.",
    "**Les 64 Go sont écartés comme cible** : ils reconduisent la saturation mesurée. Le minimum "
    "technique défendable est 128 Go.",
    "**Les prix sont confrontés au marché** : la même référence DL325 Gen11 est relevée à 5 726 € HT "
    "chez un distributeur français, contre 9 174 € dans le chiffrage étudié.",
    "**Proxmox change l'arbitrage** : la licence est facturée par socket, pas par cœur — l'argument "
    "« Intel moins cher en licences » ne tient plus.",
    "**Le coût complet est chiffré** : matériel, réseau, onduleur, sauvegarde, fret et douane, "
    "puis comparaison avec le coût de location actuel.",
])

# ---------------------------------------------------------------------------
doc.h1("2", "L'existant en chiffres")

doc.p("Un hyperviseur se juge sur quatre indicateurs, pas un seul. Les moyennes relevées sur la "
      "période d'observation donnent une lecture sans ambiguïté : la plateforme est **étranglée par "
      "la mémoire et le stockage**, et le processeur ne participe pas à la contrainte.")

doc.table(
    ["Rubrique", "Élément", "Valeur constatée", "Lecture"],
    [
        ["**Hébergement**", "Hébergeur et type d'offre", "Online / Scaleway — serveur dédié (bare metal)",
         "Hyperviseur installé et administré en interne"],
        ["", "Contrat : engagement, échéance, coût mensuel", "**Non communiqué**",
         "Variable décisive du calcul de rentabilité"],
        ["**Matériel**", "Processeur", "8 cœurs à 2,5 GHz", "Référence exacte non communiquée"],
        ["", "Mémoire vive", "64 Go", "Plafond actuel de la plateforme"],
        ["", "Stockage", "≈ 960 Go (≈ 1 To)", "Niveau RAID et type de disques non communiqués"],
        ["", "Réseau", "Non communiqué", "Débits, adresses IP publiques, redondance"],
        ["**Charge**", "Processeur", "**≈ 15 %**", "Sous-employé — aucune contrainte"],
        ["", "Mémoire vive", "**88,4 %**", "**Saturation — contrainte n°1**"],
        ["", "Disque", "**89,9 %**", "**Saturation — contrainte n°2**"],
        ["", "SWAP", "**≈ 100 %**", "Débordement mémoire effectif"],
        ["**Exploitation**", "Hyperviseur et version", "Non communiqués",
         "Cible retenue pour le remplacement : Proxmox VE"],
        ["", "Nombre de VM hébergées", "Non communiqué", "À relever pour le dimensionnement définitif"],
        ["", "Sauvegarde et restauration", "À confirmer", "Point de vigilance majeur lors du rapatriement"],
        ["", "Supervision et alertes", "À confirmer", "Aucune alerte documentée à ce stade"],
    ],
    widths=[2.75, 4.15, 4.05, 6.15], font=7.9, zebra=False,
    caption="Tableau 2 — Fiche d'identité de l'hyperviseur actuel. En orangé : une information "
            "manquante décisive ; en rouge : les ressources saturées.",
    row_bg={1: "FDF1E7", 6: "FBEAEA", 7: "FBEAEA", 8: "FBEAEA", 9: "FBEAEA"})

doc.image("fig_charge.png", "Figure 1 — Les deux barres rouges commandent l'investissement ; la barre verte indique une ressource à ne pas surdimensionner. Le trait vertical marque le seuil d'alerte à 85 %.", width_cm=13.2)

doc.callout("Le piège à éviter",
            "Dimensionner le nouveau serveur « à l'identique » revient à acheter, pour 9 000 €, "
            "une machine qui affichera 88 % de mémoire occupée le jour de sa mise en service. "
            "Le remplacement n'apporte alors qu'une garantie et une génération plus récente — pas "
            "de marge d'exploitation.",
            "bad")

# ---------------------------------------------------------------------------
doc.h1("3", "Ce que l'existant impose comme cible")

doc.p("Trois règles simples suffisent à dimensionner la cible, sans sur-spécifier ce qui ne "
      "contraint pas.")

doc.table(
    ["Composant", "Aujourd'hui", "Cible recommandée", "Justification"],
    [
        ["Mémoire", "64 Go à 88 %", "**128 Go**",
         "Reproduire 64 Go revient à reconduire la saturation. 128 Go offre deux fois la capacité "
         "et restaure une marge d'exploitation."],
        ["Stockage utile", "≈ 960 Go à 90 %", "**2 To utiles minimum** (2×1,92 To en RAID1, ou 2×3,84 To)",
         "Il faut de la place pour les VM, les snapshots et la croissance à 3 ans. Attention : "
         "1,92 To brut en RAID1 = 1,92 To utiles seulement si les deux disques sont en miroir."],
        ["Processeur", "8 cœurs / 2,5 GHz à 15 %", "**12 à 16 cœurs / 2,5–3,0 GHz**",
         "Le CPU n'est pas la contrainte : on prend 12–16 cœurs pour la marge VM à 5 ans, pas pour "
         "la charge actuelle. Aucun surcoût de licence avec Proxmox."],
        ["Réseau", "n.c.", "**2×10 GbE** (si le LAN et la sauvegarde suivent)",
         "Utile pour la sauvegarde et la migration à chaud. Sans switch 10 GbE, l'agrégation 1 GbE "
         "suffit — c'est un poste de coût à assumer explicitement."],
        ["Hyperviseur", "esxi / autre", "**Proxmox VE** + Proxmox Backup Server",
         "Coût de licence marginal, pas de facturation au cœur, sauvegarde dédupliquée intégrée."],
    ],
    widths=[2.4, 3.0, 4.6, 7.1], font=8.2,
    caption="Tableau 3 — Règles de dimensionnement retenues.",
    first_col_bold=True)

doc.image("fig_existant_cible.png", "Figure 2 — Le passage à 128 Go de mémoire et 2 To utiles, sans surdimensionner le processeur.")

# ---------------------------------------------------------------------------
doc.h1("4", "Proxmox : pourquoi ce choix change l'arbitrage")

doc.p("Le choix de Proxmox VE n'est pas un détail d'exploitation : il modifie directement la "
      "comparaison économique entre les offres.")

doc.table(
    ["Point", "Proxmox VE", "Conséquence sur le choix matériel"],
    [
        ["Modèle de licence", "Par **socket** physique occupée, jamais par cœur", "12 ou 16 cœurs coûtent strictement le même prix en licence"],
        ["Coût annuel", "Community 120 € · Basic 370 € · **Standard 550 €** · Premium 1 100 € / socket / an",
         "Un seul socket ⇒ 550 €/an en Standard, soit ≈ 2 750 € sur 5 ans"],
        ["Fonctions incluses", "Clustering, haute disponibilité, snapshots, migration à chaud, API",
         "Aucune option payante à ajouter pour l'usage visé"],
        ["Sauvegarde", "Proxmox Backup Server : déduplication, restauration instantanée",
         "≈ 560 €/an pour la sauvegarde de l'hôte principal"],
        ["Compétences", "Interface web, documentation abondante, communauté large",
         "Réduit la dépendance à un éditeur unique et le coût de formation"],
    ],
    widths=[2.9, 6.8, 7.4], font=8.2,
    caption="Tableau 4 — Tarifs publics Proxmox (relevé d'octobre 2026), par socket et par an.",
    first_col_bold=True)

doc.h3("Ce que cela implique concrètement")
doc.table(
    ["Brique", "Rôle", "Coût annuel"],
    [
        ["Proxmox VE — Standard, 1 socket", "Hyperviseur de production, dépôt entreprise, support 4 h", "550 €"],
        ["Proxmox Backup Server — Basic", "Sauvegarde dédupliquée, restauration instantanée des VM", "560 €"],
        ["Stockage objet externe (petit volume)", "Copie hors site — la règle 3-2-1 reste applicable", "≈ 300 €"],
        ["**Total licences**", "**Pour un hôte unique en production**", "**≈ 1 410 €/an**"],
    ],
    widths=[4.6, 9.5, 2.9], font=8.2, aligns=["l", "l", "r"],
    caption="Tableau 5 — Coût logiciel complet de la cible, hors matériel.",
    row_bg={3: "EAF0F7"})

doc.callout("Un argument qui tombe",
            "L'analyse initiale retenait le serveur Intel DL320 bien qu'il soit **plus cher et moins "
            "puissant** que le DL325 AMD, au motif d'une préférence de constructeur. Sous VMware, cet "
            "argument avait un fondement : la facturation par cœur rendait un processeur à 12 cœurs "
            "moins coûteux qu'un 16 cœurs. **Avec Proxmox, cet écart disparaît** : le nombre de cœurs "
            "n'a plus aucun effet sur le prix de la licence. Le seul critère qui reste est la "
            "performance par euro dépensé — et il désigne l'AMD.",
            "info")

doc.h3("Ce que la bascule vers Proxmox demande réellement")
doc.table(
    ["Étape", "Contenu", "Charge"],
    [
        ["Inventaire", "Lister les VM : système, vCPU, RAM, disques, dépendances, criticité", "0,5 jour"],
        ["Conversion", "Import des VM depuis l'ESXi d'origine (assistant d'import intégré) ou conversion des disques", "1 jour"],
        ["Réseau", "Ponts, VLAN, **renumérotation des adresses IP publiques**, règles de pare-feu", "1 jour"],
        ["Tests", "Démarrage, performances, sauvegarde **et restauration réelle**", "2 jours"],
        ["Bascule", "Fenêtre planifiée, procédure de retour arrière, cloud conservé un mois en parallèle", "1 jour"],
    ],
    widths=[2.4, 11.6, 3.1], font=8.1, aligns=["l", "l", "r"],
    caption="Tableau 6 — Charge d'intégration à budgéter dans le projet (≈ 5,5 jours).",
    first_col_bold=True)

# ---------------------------------------------------------------------------
doc.h1("5", "Les sept configurations étudiées")

rows = []
for o in sorted(OFFRES_JOEL, key=lambda x: x["prix"]):
    sc = note_ponderee(SCORES_A[o["nom"]], POIDS_A)
    rows.append([
        f'**{o["nom"]}**',
        f'{o["gen"]} · {o["etat"]}',
        o["cpu"],
        f'{o["cores"]}C / {d(o["ghz"],2)}' if o["cores"] else "n.c.",
        f'{o["ram"]} Go',
        o["disque"],
        o["reseau"],
        eur(o["prix"]),
        eur(round(o["prix"] / o["ram"])),
        eur(round(o["prix"] / o["cores"])) if o["cores"] else "n.c.",
        d(sc),
    ])

doc.table(
    ["Offre", "Génération", "Processeur", "Cœurs", "RAM", "Disque", "Réseau", "Prix HT", "€/Go RAM", "€/cœur", "Score"],
    rows,
    widths=[2.7, 2.1, 2.5, 1.4, 1.0, 1.6, 2.2, 1.3, 1.4, 1.1, 1.1], font=7.2,
    aligns=["l", "l", "l", "c", "c", "l", "l", "r", "r", "r", "r"],
    caption="Tableau 7 — Comparatif complet. Les deux indicateurs de valeur (€ par Go de RAM, € par cœur) "
            "révèlent l'écart de positionnement que le prix absolu masque.",
    row_bg={0: "EAF0F7", 4: "EAF0F7"})

doc.image("fig_prix_a.png", "Figure 3 — Prix HT indicatifs. En orange, le reconditionné : deux fois plus de mémoire pour un prix inférieur.")

doc.callout("Ce que le tableau montre en une ligne",
            "Le reconditionné Gen10 coûte **44 € par Go de RAM** quand le neuf Gen11 en coûte **143 €**. "
            "Le prix absolu ne dit donc rien : il faut le rapporter au service rendu, puis corriger "
            "par l'écart de durée de vie — c'est précisément l'objet des scores et de la section 9.",
            "info")

# ---------------------------------------------------------------------------
doc.h1("6", "Classement qualité / prix / performance")

doc.p("Six critères pondérés, notés de 0 à 10, donnent un score unique comparable. Les pondérations "
      "traduisent les contraintes réelles du dossier : la mémoire et le stockage pèsent 40 % du score, "
      "car ce sont les deux ressources saturées.")

doc.table(
    ["Critère", "Poids", "Pourquoi ce poids"],
    [[c, f"{p} %", m] for (c, p), m in zip(POIDS_A, [
        "Marge de calcul à 5 ans, sans surcoût de licence Proxmox",
        "Ressource saturée aujourd'hui : c'est le critère décisif",
        "Seconde ressource saturée ; dépend des baies et des disques chiffrés",
        "Requise pour la sauvegarde et la migration à chaud",
        "Une plateforme neuve tient 5–7 ans ; un reconditionné 2–3 ans",
        "À budget contraint, le prix reste un critère, mais pas le seul",
    ])],
    widths=[5.0, 1.6, 10.5], font=8.2, aligns=["l", "r", "l"],
    caption="Tableau 8 — Grille de notation pondérée.",
    first_col_bold=True)

rows = []
for o in sorted(OFFRES_JOEL, key=lambda x: -note_ponderee(SCORES_A[x["nom"]], POIDS_A)):
    sc = SCORES_A[o["nom"]]
    rows.append([f'**{o["nom"]}**', eur(o["prix"])] + [str(v) for v in sc] +
                [f'**{d(note_ponderee(sc, POIDS_A))}**'])
doc.table(
    ["Offre", "Prix HT", "CPU", "RAM", "Stock.", "Réseau", "Péren.", "Prix", "Score /100"],
    rows,
    widths=[4.2, 2.0, 1.3, 1.3, 1.5, 1.6, 1.5, 1.3, 2.0], font=7.8,
    aligns=["l", "r", "c", "c", "c", "c", "c", "c", "c"],
    caption="Tableau 9 — Notes détaillées par critère (0 à 10), classées par score décroissant.",
    row_bg={0: "EDF5EC", 1: "EDF5EC"})

doc.image("fig_valeur_a.png", "Figure 4 — Prix en abscisse, score en ordonnée : le meilleur compromis se lit en haut à gauche.", width_cm=14.8)

doc.p("Trois enseignements : **le DL325 Gen11 arrive premier** malgré son prix — seul à combiner "
      "16 cœurs, plateforme neuve et garantie 3 ans ; **le DL180 Gen10 reste compétitif** grâce à sa "
      "mémoire et à son prix, mais pâtit d'un CPU non identifié et d'un horizon court ; **le DL320 et "
      "le ML110 tombent sous 62/100** — plus chers, moins performants ou hors critère réseau.")

# ---------------------------------------------------------------------------
doc.h1("7", "Meilleure offre n°1 — HPE DL325 Gen11")

doc.table(
    ["Élément", "Détail"],
    [
        ["Configuration", "HPE ProLiant DL325 Gen11, 1U / 1 socket, 8 baies SFF"],
        ["Processeur", "AMD EPYC 9124 — 16 cœurs, 3,0 GHz (boost 3,7 GHz), PCIe 5.0"],
        ["Mémoire", "64 Go DDR5 4800 RDIMM — **12 emplacements, extensible à 128 Go puis 3 To**"],
        ["Stockage", "8 baies SFF — **disques à chiffrer** (2×1,92 To NVMe en RAID1 recommandé)"],
        ["Réseau", "2×10 GbE BASE-T (OCP 3.0) + 4×1 GbE"],
        ["Gestion", "HPE iLO 6 — administration à distance, indispensable à distance depuis Libreville"],
        ["Garantie", "3/3/3 — 3 ans pièces, main-d'œuvre et intervention"],
        ["Prix HT indicatif", "**9 174 €** — relevé marché de la même référence : **5 726 € HT**"],
        ["Ce qu'il faut demander", "Passage à **128 Go** (4×32 Go), 2×1,92 To en RAID1, prix de l'extension ultérieure"],
    ],
    widths=[3.6, 13.5], font=8.4, caption="Tableau 10 — Fiche technique de l'offre n°1.",
    first_col_bold=True)

doc.callout("Pourquoi elle est première",
            "C'est la seule offre qui coche **toutes** les cases du dossier : processeur de dernière "
            "génération inutilement puissant (donc avec de la marge), DDR5, deux ports 10 GbE natifs, "
            "douze emplacements mémoire pour grandir, garantie constructeur 3 ans et iLO 6 pour "
            "l'administration à distance. Son seul défaut est le même que celui de toutes les offres "
            "Gen11 du dossier : **64 Go ne suffisent pas**.",
            "ok")

doc.h3("Trois façons d'équiper cette machine, trois prix")
doc.table(
    ["Variante", "Contenu", "Prix HT estimé", "Écart vs socle"],
    [
        ["Socle du chiffrage", "64 Go de RAM, sans disques, garantie 3 ans", "9 174 €", "—"],
        ["Socle + stockage", "+ 2×1,92 To NVMe en RAID1", "≈ 10 400 €", "+ 1 200 €"],
        ["**Cible recommandée**", "**+ 128 Go de RAM, 2×1,92 To RAID1, disque de rechange**", "**≈ 12 900 €**", "**+ 3 700 €**"],
    ],
    widths=[3.6, 7.4, 3.2, 2.8], font=8.2, aligns=["l", "l", "r", "r"],
    caption="Tableau 11 — Échelle de prix de l'offre n°1 (options estimées sur prix marché, à confirmer par devis).",
    row_bg={2: "EDF5EC"})

doc.p("**Réserve de prix.** La référence P77252-425 (DL325 Gen11, EPYC 9124, 64 Go, 8 baies, "
      "contrôleur MR408i-o) est relevée à **5 726 € HT** chez un distributeur français, contre "
      "9 174 € dans le chiffrage étudié — soit **+60 %**. L'écart peut s'expliquer par des options "
      "différentes (seconde alimentation, rails, garantie, disques) ; il doit être levé par un devis "
      "détaillé. À budget constant, cet écart finance le passage à 128 Go de mémoire.")

# ---------------------------------------------------------------------------
doc.h1("8", "Meilleure offre n°2 — HPE DL180 Gen10, 128 Go")

doc.table(
    ["Élément", "Détail"],
    [
        ["Configuration", "HPE ProLiant DL180 Gen10 — 2U, reconditionné"],
        ["Processeur", "**Non spécifié** dans le chiffrage — point bloquant : impossible de comparer"],
        ["Mémoire", "128 Go DDR4 2666 — capacité immédiate, mais technologie de génération précédente"],
        ["Stockage", "2×1,92 To (RAID1 ⇒ 1,92 To utiles) — jusqu'à 4×3,84 To selon la version"],
        ["Réseau", "2×10 GbE + 2×1 GbE"],
        ["Garantie", "Revendeur, généralement 12 à 24 mois — pas de couverture constructeur"],
        ["Prix HT indicatif", "**5 621 €** (2×3,84 To : 6 850 € ; 4×3,84 To : 10 657 €)"],
        ["Point de comparaison", "Un DL380 Gen10 reconditionné 128 Go se négocie **1 500 à 1 800 € HT** sur le marché français"],
    ],
    widths=[3.6, 13.5], font=8.4, caption="Tableau 12 — Fiche technique de l'offre n°2.",
    first_col_bold=True)

doc.p("C'est l'offre **la plus honnête en capacité par euro** : 44 € le Go de RAM, deux téraoctets "
      "utiles, pour le prix d'un serveur Gen11 nu. Elle répond même mieux que l'offre n°1 aux deux "
      "contraintes mesurées. Trois réserves expliquent sa deuxième place : le processeur n'est pas "
      "identifié, la garantie n'est pas constructeur, et la plateforme DDR4 est en fin de cycle — "
      "l'horizon réaliste est de 2 à 3 ans, pas 5 à 7 ans.")

doc.h3("Les cinq conditions à inscrire au devis")
doc.table(
    ["Exigence", "Formulation à exiger", "Pourquoi"],
    [
        ["Processeur", "« Référence exacte du ou des processeurs, nombre de cœurs et fréquence »",
         "Sans elle, l'offre n'est pas comparable et la performance est inconnue"],
        ["Garantie", "« 24 mois minimum, pièces et main-d'œuvre, intervention sur site »",
         "C'est la seule couverture en cas de panne d'alimentation ou de carte mère"],
        ["Disques", "« SSD neufs ou testés, taux d'usure et heures de fonctionnement communiqués »",
         "Un SSD en fin de vie est la panne la plus probable sur du matériel reconditionné"],
        ["Firmware", "« BIOS, iLO et firmware à jour, configurés avant expédition »",
         "Évite une demi-journée de mise à jour à distance depuis Libreville"],
        ["État général", "« Rapport de diagnostic complet, pièces d'origine, alimentations redondantes »",
         "Le reconditionné est hétérogène : deux machines identiques peuvent différer"],
    ],
    widths=[2.8, 7.6, 6.7], font=8.0,
    caption="Tableau 13 — Check-list de commande pour l'offre reconditionnée.",
    row_bg={1: "FDF1E7"})

doc.callout("La condition pour la retenir",
            "Si le revendeur ne peut pas fournir ces cinq éléments, l'offre doit être écartée : "
            "l'économie de 3 500 € se transforme alors en risque d'indisponibilité non couvert, "
            "sur un serveur qui portera l'ensemble de la production.",
            "warn")

# ---------------------------------------------------------------------------
doc.h1("9", "Neuf ou reconditionné : ce que l'on échange")

doc.table(
    ["Critère", "Neuf — Gen11", "Reconditionné — Gen10"],
    [
        ["Prix d'acquisition", "9 174 € (64 Go)", "**5 621 € (128 Go)**"],
        ["Mémoire livrée", "64 Go DDR5", "**128 Go DDR4**"],
        ["Garantie", "3 ans constructeur, intervention sur site", "12 à 24 mois, garantie revendeur"],
        ["Disponibilité des pièces", "Constructeur, plusieurs années", "Marché secondaire, aléatoire"],
        ["Horizon d'exploitation", "**5 à 7 ans**", "2 à 3 ans"],
        ["Consommation / performance", "Meilleures (DDR5, PCIe 5.0)", "Correctes, mais génération antérieure"],
        ["Risque principal", "Budget plus élevé", "Hétérogénéité : CPU, SSD usés, firmware"],
        ["Usage recommandé", "**Hôte de production principal**", "Nœud de secours, test, ou hôte unique si budget plafonné"],
    ],
    widths=[3.4, 6.8, 6.9], font=8.3,
    caption="Tableau 14 — Arbitrage neuf / reconditionné.",
    first_col_bold=True, row_bg={6: "EAF0F7"})

doc.image("fig_generations.png", "Figure 5 — Positionnement des générations. La Gen12 est commercialisée depuis juillet 2025 : la Gen11 est donc en fin de cycle commercial, ce qui est un levier de négociation.")

doc.callout("Un levier de négociation à ne pas manquer",
            "Le DL325 **Gen12** est commercialisé depuis juillet 2025 (jusqu'à 6 To de mémoire, "
            "iLO 7). Acheter un Gen11 neuf en novembre 2026 doit donc se traduire par une **remise "
            "significative** sur le tarif catalogue. Si l'écart entre Gen11 remisé et Gen12 dépasse "
            "15 %, il faut basculer sur le Gen12 : sur un horizon de 7 ans, le surcoût est absorbé "
            "par la durée de support.",
            "info")

# ---------------------------------------------------------------------------
doc.h1("10", "Trois tranches de budget")

doc.p("La Direction Générale arbitre un montant, pas une référence constructeur. Voici donc le même "
      "dossier présenté en trois tranches, avec ce que chacune achète réellement.")

doc.image("fig_tranches_a.png", "Figure 6 — Trois tranches d'investissement matériel (hors réseau, onduleur, fret et migration).")

doc.table(
    ["Tranche", "Enveloppe HT", "Configuration", "Ce que l'on obtient", "Ce que l'on sacrifie"],
    [
        ["**1. Basse**", "4 000 – 7 000 €",
         "DL180 Gen10 reconditionné, 128 Go, 2×1,92 To",
         "La capacité immédiate : mémoire et disque traités, à moitié prix",
         "Pérennité, garantie constructeur, DDR4, CPU non identifié"],
        ["**2. Cible**", "8 000 – 10 000 €",
         "DL325 Gen11 neuf, **64 Go**",
         "Une plateforme moderne garantie 3 ans, tenue 5 à 7 ans",
         "**La marge mémoire : 64 Go reconstituent la saturation**"],
        ["**3. Confort**", "11 000 – 14 000 €",
         "DL325 Gen11 neuf, **128 Go**, 2×1,92 To RAID1",
         "Les deux contraintes traitées, sur une plateforme neuve",
         "Rien sur le plan technique ; seul le budget augmente"],
    ],
    widths=[2.2, 2.4, 4.0, 4.5, 4.4], font=8.0,
    caption="Tableau 15 — Lecture budgétaire. La tranche 2 est un piège : elle est chère et ne règle pas le problème mémoire.",
    row_bg={2: "FBEAEA", 3: "EDF5EC"})

doc.callout("Le conseil à retenir",
            "Si l'enveloppe est plafonnée, il vaut mieux **descendre d'une génération (tranche 1) que "
            "de rester à 64 Go sur une plateforme neuve (tranche 2)** : la tranche 2 cumule le coût du "
            "neuf et l'inconfort de l'existant. Si l'enveloppe peut être portée à 11–13 k€, la tranche 3 "
            "est la seule qui règle le problème posé.",
            "warn")

# ---------------------------------------------------------------------------
doc.h1("11", "Ce que le prix affiché ne dit pas")

doc.p("Un serveur ne fonctionne pas seul. Pour un déploiement à Libreville, l'écart entre le prix du "
      "chiffrage et le coût réel du projet est structurel.")

doc.table(
    ["Poste non chiffré", "Ordre de grandeur HT", "Commentaire"],
    [
        ["Switch 10 GbE + optiques / DAC", "800 – 1 500 €", "Sans lui, les ports 10 GbE du serveur ne servent à rien"],
        ["Onduleur et PDU", "600 – 1 500 €", "Indispensable : coupures et micro-coupures fréquentes"],
        ["Rack, rails, câblage", "400 – 900 €", "Souvent oublié dans les devis serveur"],
        ["Disque de rechange à froid", "400 – 700 €", "Le meilleur rapport sécurité/prix du projet"],
        ["Licences Proxmox + PBS (3 ans)", "≈ 3 300 €", "550 € + 560 € par an"],
        ["Fret, douane, transitaire", "**15 à 25 %** du matériel", "Poste systématiquement absent des devis européens"],
        ["Migration / prestation", "1 500 – 3 000 €", "Bascule, changement d'adresses IP, DNS, certificats"],
    ],
    widths=[5.0, 3.6, 8.5], font=8.2, aligns=["l", "r", "l"],
    caption="Tableau 16 — Coûts à ajouter au prix du serveur pour obtenir le coût du projet.",
    first_col_bold=True)

doc.image("fig_tco.png", "Figure 7 — Coût complet : à 250 €/mois de location, le rapatriement ne se justifie pas financièrement. Le seuil d'équilibre se situe autour de 550 €/mois.")

doc.callout("La question que la Direction Générale doit poser",
            "**Combien coûte aujourd'hui la location ?** C'est la seule variable qui décide. En dessous "
            "d'environ 550 €/mois HT, rapatrier coûte plus cher que louer sur 5 ans — et le surcoût "
            "s'explique par le matériel, le fret, l'énergie et le temps d'administration. Au-dessus, "
            "le rapatriement devient rentable dès la troisième année, avec en prime la maîtrise de "
            "l'emplacement des données.",
            "bad")

# ---------------------------------------------------------------------------
doc.h1("12", "Recommandation et prochaines étapes")

doc.h2("Recommandation")
doc.p("**Retenir la tranche 3 : DL325 Gen11 neuf, 128 Go de mémoire, 2×1,92 To en RAID1, sous Proxmox "
      "VE**, avec une enveloppe matérielle de 11 000 à 13 000 € HT. À défaut, si l'enveloppe est "
      "plafonnée à 7 k€, retenir la tranche 1 (DL180 Gen10 128 Go) en imposant par devis un CPU "
      "identifié et une garantie de 24 mois. **Écarter la tranche 2** : c'est le seul scénario qui "
      "n'apporte pas de solution au problème identifié.")

doc.table(
    ["Action", "Responsable", "Échéance"],
    [
        ["Confirmer la facture de location actuelle (montant mensuel HT) et la date d'échéance du contrat",
         "Direction / GED-SERVICES", "Sous 5 jours"],
        ["Demander un devis détaillé 128 Go sur le DL325 Gen11, avec ligne d'extension future",
         "Joël MBA OYONE", "Sous 10 jours"],
        ["Mettre en concurrence trois distributeurs sur la même nomenclature (voir annexe)",
         "Achats", "Sous 15 jours"],
        ["Chiffrer le DL325 Gen12 pour arbitrer l'écart de génération",
         "Achats", "Sous 15 jours"],
        ["Lancer 30 jours de mesure par VM (RAM consommée, croissance disque, IOPS)",
         "Exploitation", "Avant commande"],
        ["Décider de la tranche d'investissement", "**Jad — DG**", "À réception des devis"],
    ],
    widths=[9.9, 3.6, 3.6], font=8.2,
    caption="Tableau 17 — Plan d'action.",
    first_col_bold=False)

# ---------------------------------------------------------------------------
doc.h1("13", "Annexe — références de prix constatées")

doc.table(
    ["Référence / prestation", "Prix relevé", "Source"],
    [[r[0], f"**{r[1]}**", r[2]] for r in PRIX_MARCHE],
    widths=[10.4, 3.4, 3.3], font=7.9, aligns=["l", "r", "l"],
    caption="Tableau 18 — Relevés de prix effectués le 5 novembre 2026, à titre indicatif.")

doc.p("**Avertissement.** Les prix mentionnés proviennent, d'une part, des simulations du "
      "configurateur ServerMall transmises le 4 novembre 2026 et, d'autre part, de relevés publics "
      "effectués le 5 novembre 2026. Ils ne constituent pas des offres fermes : ils servent à "
      "positionner une enveloppe budgétaire et une cible technique. Aucune commande ne devrait être "
      "engagée sans devis détaillé mentionnant la nomenclature complète, la garantie, les délais et "
      "les conditions de livraison internationale.", small=True)

doc.save(OUT)
print("saved", OUT)
