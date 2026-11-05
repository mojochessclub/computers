# -*- coding: utf-8 -*-
"""Document B — analyse indépendante de A à Z + benchmark et recommandation d'appro serveur."""
import os
from render import Doc
from data import (CANDIDATS_B, SCORES_B, POIDS_B, PRIX_MARCHE, note_ponderee, TCO)

BASE = "B_Analyse_independante_benchmark_appro"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables")


def eur(n):
    return f"{n:,.0f}".replace(",", " ") + " €"


def d(n, dec=1):
    return f"{n:,.{dec}f}".replace(",", " ").replace(".", ",")


doc = Doc(
    base=BASE,
    title="Benchmark serveur & recommandation d'appro",
    subtitle="Rapatriement de l'hyperviseur — analyse indépendante",
    meta=[],
    doc_ref="GED-RAP-2026-02 · Confidentiel — usage interne",
    footer="Benchmark serveur & recommandation d'appro",
)

# ---------------------------------------------------------------------------
doc.cover(
    eyebrow="Analyse indépendante & benchmark d'approvisionnement",
    title="Quel serveur pour rapatrier\nl'hyperviseur ?",
    subtitle="Analyse construite de zéro, sans reprendre les conclusions de l'étude initiale : "
             "lecture de l'existant, dimensionnement, quatre recommandations HPE, alternatives "
             "constructeurs, circuits d'achat et budget complet.",
    meta_rows=[
        ["Pour", "**Jad — Direction Générale**"],
        ["Objet", "Acquisition d'une plateforme serveur pour rapatrier l'infrastructure "
                  "hébergée chez Online / Scaleway"],
        ["Hyperviseur cible", "**Proxmox VE** + Proxmox Backup Server"],
        ["Périmètre", "Benchmark de 9 configurations, 4 constructeurs, 4 circuits d'achat"],
        ["Statut des prix", "Relevés publics du 5 novembre 2026 et estimations encadrées — "
                            "**aucun prix ferme sans devis**"],
        ["Décision attendue", "Validation de l'architecture cible, de l'enveloppe et du lancement "
                              "de l'appel à devis"],
        ["Date", "5 novembre 2026"],
    ],
    summary=("La conclusion en quatre lignes",
             "Le besoin réel n'est pas de la puissance de calcul mais de la **mémoire et du "
             "stockage** : 128 Go et 2 To utiles constituent le plancher technique.\n"
             "La recommandation principale est le **HPE DL325 Gen11 en 128 Go** (≈ 8 900 € HT "
             "matériel), avec le **DL325 Gen12** en option de pérennité et le **DL380 Gen10 "
             "reconditionné** en nœud secondaire uniquement.\n"
             "Le projet complet, rendu à Libreville et sauvegardé, coûte **≈ 21 300 € HT en année 1 "
             "et ≈ 33 000 € HT sur 5 ans** — soit deux à trois fois le prix du serveur affiché.",
             "info"),
)

# ---------------------------------------------------------------------------
doc.h1("1", "Synthèse pour la Direction Générale")

doc.p("Cette note ne reprend pas les conclusions de l'étude initiale : elle reconstruit l'analyse "
      "depuis les mesures de l'existant, puis compare neuf configurations chez quatre constructeurs "
      "et quatre circuits d'achat. Les prix sont des ordres de grandeur encadrés, destinés à "
      "positionner une enveloppe — pas des offres fermes.", lead=True)

doc.kpi([("128 Go", "mémoire minimale retenue"),
         ("2 To", "stockage utile minimal"),
         ("≈ 8 900 €", "matériel recommandé (HT)"),
         ("≈ 21 300 €", "projet complet année 1 (HT)")])

doc.h2("Cinq conclusions")
doc.ul([
    "**Le CPU n'est pas le sujet.** À 15 % d'occupation, 8 cœurs suffiraient. On retient 12 à "
    "16 cœurs pour la marge à cinq ans, pas pour la charge actuelle.",
    "**La mémoire décide.** 64 Go à 88 % de charge : le plancher défendable est 128 Go. Toute offre "
    "à 64 Go doit être écartée du rôle d'hôte principal.",
    "**Le stockage doit être exprimé en capacité utile**, pas en capacité brute : 2×1,92 To en RAID1 "
    "donnent 1,92 To utiles — et non 3,84 To.",
    "**Proxmox supprime le coût par cœur** : la licence est facturée par socket (550 €/an en "
    "Standard). Le choix du processeur redevient purement technique.",
    "**Le prix du serveur n'est pas le coût du projet** : réseau, onduleur, sauvegarde, fret, "
    "douane et migration ajoutent 40 à 50 % à la facture.",
])

doc.callout("Ce que la Direction Générale doit arbitrer",
            "Trois décisions, dans cet ordre : **(1)** accepte-t-on d'investir 21 300 € HT en année 1 "
            "plutôt que 9 200 € ? **(2)** accepte-t-on un serveur unique en local, donc un point de "
            "défaillance unique, avec sauvegarde hors site ? **(3)** quel horizon d'exploitation "
            "vise-t-on — 3 ans (reconditionné) ou 7 ans (neuf) ?",
            "warn")

doc.h2("Tableau de bord du projet")
doc.table(
    ["Poste", "Montant HT", "Part du projet", "Commentaire"],
    [
        ["Serveur équipé (128 Go, 2×1,92 To + rechange) et rails", "10 126 €", "48 %", "Prix marché relevé, à confirmer par devis"],
        ["Réseau 10 GbE + onduleur", "2 000 €", "9 %", "Sans eux, le serveur ne fonctionne pas"],
        ["Licences Proxmox + PBS (3 ans)", "3 330 €", "16 %", "550 €/an + 560 €/an"],
        ["Sauvegarde hors site (3 ans)", "900 €", "4 %", "La meilleure police d'assurance du projet"],
        ["Fret, douane, transitaire", "2 425 €", "11 %", "20 % du matériel — systématiquement oublié"],
        ["Intégration, migration, documentation", "2 500 €", "12 %", "Bascule, adresses IP, DNS, certificats"],
        ["**Total année 1**", "**≈ 21 300 €**", "**100 %**", "**≈ 14,0 M FCFA** (1 € = 655,957 FCFA)"],
    ],
    widths=[6.0, 2.8, 2.3, 6.0], font=8.2, aligns=["l", "r", "c", "l"],
    caption="Tableau 1 — Coût complet du projet en année 1.",
    row_bg={6: "EAF0F7"})

# ---------------------------------------------------------------------------
doc.h1("2", "Méthode, hypothèses et limites")

doc.h2("Comment cette analyse est construite")
doc.p("Quatre étapes, dans cet ordre : **(a)** lecture critique des mesures de l'existant et "
      "vérification du bien-fondé du dimensionnement ; **(b)** définition de règles de "
      "dimensionnement explicites (pas de reproduction à l'identique) ; **(c)** comparaison de neuf "
      "configurations selon une grille pondérée de sept critères ; **(d)** chiffrage du coût complet, "
      "y compris les postes hors matériel et le coût de location actuel.")

doc.table(
    ["Critère", "Poids", "Ce qu'il mesure"],
    [[c, f"{p} %", m] for (c, p), m in zip(POIDS_B, [
        "Cœurs × fréquence, mais aussi nombre de cœurs réellement disponibles pour les VM",
        "Capacité livrée et possibilité d'extension future sans remplacer les barrettes",
        "Nombre de baies, type de disques (NVMe/SAS), niveau RAID, contrôleur",
        "Ports 10 GbE natifs, emplacements OCP et PCIe disponibles",
        "Génération, horizon de support, disponibilité des pièces dans 5 ans",
        "Garantie constructeur, délais, couverture sur site au Gabon",
        "Prix d'acquisition rapporté au service rendu",
    ])],
    widths=[6.2, 1.6, 9.3], font=8.2, aligns=["l", "r", "l"],
    caption="Tableau 2 — Grille d'évaluation pondérée (7 critères, 100 points).",
    first_col_bold=True)

doc.h2("Ce que cette note ne traite pas")
doc.ul([
    "**La haute disponibilité matérielle** (deux nœuds avec redémarrage automatique des VM) : elle "
    "doublerait l'investissement matériel et suppose un budget supérieur à 25 k€. La parade retenue "
    "ici est la sauvegarde, pas la redondance.",
    "**Les applications elles-mêmes** : aucune revue des performances applicatives n'est faite ; un "
    "défaut de conception (requêtes non optimisées, absence de cache) ne se corrige pas avec un serveur.",
    "**La conduite du changement** : la migration des VM, le changement d'adresses IP et la "
    "communication aux utilisateurs sont budgétés en prestation, pas détaillés ici.",
])

doc.callout("Limites à assumer",
            "Les prix des configurations non relevées publiquement sont des **estimations** "
            "construites par analogie (socle + options). Elles servent à comparer des ordres de "
            "grandeur, pas à engager une dépense. Deux chiffres doivent être obtenus avant toute "
            "décision : la **facture de location actuelle** (montant mensuel HT) et le **devis ferme "
            "128 Go** sur la configuration retenue.",
            "warn")

# ---------------------------------------------------------------------------
doc.h1("3", "Partir de l'existant : lire les chiffres correctement")

doc.p("Les mesures disponibles décrivent une plateforme saturée en mémoire et en stockage, avec un "
      "processeur largement disponible. Elles sont suffisantes pour décider du sens de "
      "l'investissement, mais insuffisantes pour dimensionner au gigaoctet près — d'où les mesures "
      "complémentaires proposées.")

doc.table(
    ["Indicateur", "Valeur", "Ce qu'elle prouve", "Ce qu'elle ne dit pas", "Mesure à ajouter"],
    [
        ["CPU moyen", "≈ 15 %", "Le processeur n'est pas la contrainte",
         "Ni les pics, ni le temps d'attente des VM (%ready / steal)", "Percentile 95 et pics sur 30 jours"],
        ["RAM", "88,4 %", "La mémoire est le premier goulot",
         "La répartition entre VM, la surallocation, l'effet du cache", "Consommation par VM, RAM allouée vs utilisée"],
        ["Disque", "89,9 %", "Le stockage est le second goulot",
         "Les IOPS réelles, la latence, la croissance mensuelle", "IOPS et latence p95, croissance sur 6 mois"],
        ["SWAP", "≈ 100 %", "Débordement mémoire effectif",
         "Si la cause est un manque de RAM ou une fuite applicative", "Suivi du swap par VM, date de démarrage"],
    ],
    widths=[2.3, 1.6, 3.9, 4.6, 4.7], font=7.8,
    caption="Tableau 3 — Lecture critique des mesures disponibles.",
    first_col_bold=True)

doc.callout("Une précaution avant de commander",
            "Un SWAP à 100 % peut aussi révéler un **sur-provisionnement de mémoire par VM** ou une "
            "fuite applicative, et non un manque de RAM physique. Trente jours de mesure par VM "
            "coûtent zéro euro et évitent d'acheter 128 Go si 96 Go suffisaient — ou l'inverse.",
            "info")

doc.h2("Règles de dimensionnement retenues")
doc.table(
    ["Composant", "Règle appliquée", "Calcul", "Résultat"],
    [
        ["Mémoire", "Somme des besoins VM + 20 % pour l'hyperviseur et la marge",
         "≈ 100 Go utiles constatés → arrondi à la capacité standard", "**128 Go**"],
        ["Stockage utile", "Occupation actuelle + croissance 3 ans + 30 % de libre (snapshots)",
         "960 Go × 1,25 × 1,3 ≈ 1,56 To → arrondi", "**2 To utiles minimum**"],
        ["Processeur", "Surallocation ≤ 4 vCPU par cœur physique, usage généraliste",
         "Charge à 15 % ; 12 cœurs couvrent 48 vCPU", "**12 à 16 cœurs**"],
        ["Réseau", "2×10 GbE si switch et sauvegarde réseau suivent ; sinon agrégation 1 GbE",
         "Débit utile des sauvegardes et migrations à chaud", "**2×10 GbE**"],
        ["Résilience", "Disques en RAID1 + disque de rechange à froid + sauvegarde hors site",
         "Aucune redondance matérielle sur un hôte unique", "**RAID1 + PBS + copie externe**"],
    ],
    widths=[2.5, 5.2, 6.4, 3.0], font=8.0,
    caption="Tableau 4 — Règles de dimensionnement et résultats.",
    first_col_bold=True)

# ---------------------------------------------------------------------------
doc.h1("4", "Architecture cible sous Proxmox")

doc.p("Proxmox VE est retenu comme hyperviseur : licence par socket (et non par cœur), fonctions de "
      "haute disponibilité incluses, sauvegarde dédupliquée avec Proxmox Backup Server. Pour un site "
      "unique, l'architecture tient en cinq couches.")

doc.table(
    ["Couche", "Choix retenu", "Justification"],
    [
        ["Hyperviseur", "Proxmox VE 9 — Standard, 1 socket (550 €/an)",
         "Support éditeur 4 h, dépôt entreprise ; coût indépendant du nombre de cœurs"],
        ["Calcul", "1 nœud, 12 à 16 cœurs, 128 Go de RAM",
         "Suffisant pour la charge ; la haute disponibilité matérielle reste hors budget"],
        ["Stockage", "2×1,92 To NVMe/SAS en RAID1 (ZFS ou contrôleur matériel) + 1 disque de rechange",
         "2 To utiles, latence faible, reconstruction rapide"],
        ["Sauvegarde", "Proxmox Backup Server (local) + copie hors site (stockage objet)",
         "Règle 3-2-1 : la seule protection contre l'incendie, le vol ou le chiffrement malveillant"],
        ["Réseau / énergie", "2×10 GbE + 2×1 GbE ; onduleur + PDU ; iLO sur VLAN d'administration",
         "Redondance d'alimentation, administration hors bande à distance"],
    ],
    widths=[2.5, 6.8, 7.8], font=8.0,
    caption="Tableau 5 — Architecture technique cible.",
    first_col_bold=True)

doc.h2("Nomenclature chiffrée du projet")
bom = [
    ("HPE DL325 Gen11 — EPYC 9124, 64 Go, 8SFF, MR408i-o, 2×10 GbE, 3/3/3", "1", "5 726 €", "5 726 €"),
    ("Extension à 128 Go — 4×32 Go DDR5 4800 RDIMM", "1 lot", "2 400 €", "2 400 €"),
    ("SSD 1,92 To read-intensive (2 en RAID1 + 1 de rechange)", "3", "550 €", "1 650 €"),
    ("Rails et kit de montage rack", "1", "350 €", "350 €"),
    ("Switch 10 GbE 8 ports + optiques / DAC", "1", "1 100 €", "1 100 €"),
    ("Onduleur 2 000 VA + PDU", "1", "900 €", "900 €"),
    ("Proxmox VE Standard — 3 ans (1 socket)", "3", "550 €", "1 650 €"),
    ("Proxmox Backup Server — 3 ans", "3", "560 €", "1 680 €"),
    ("Sauvegarde hors site — 3 ans", "3", "300 €", "900 €"),
    ("Intégration, migration, documentation, formation", "1", "2 500 €", "2 500 €"),
    ("Sous-total", "", "", "**18 856 €**"),
    ("Fret, douane et transitaire (20 % du matériel)", "", "", "2 425 €"),
    ("**Total année 1**", "", "", "**≈ 21 300 €**"),
]
doc.table(
    ["Poste", "Qté", "P.U. HT", "Total HT"],
    [[a, b, c, d_] for a, b, c, d_ in bom],
    widths=[9.2, 1.4, 2.6, 3.1], font=7.9, aligns=["l", "c", "r", "r"],
    caption="Tableau 6 — Nomenclature complète (prix relevés et estimés, HT). "
            "Total ≈ 21 300 € HT, soit ≈ 14,0 M FCFA.",
    row_bg={10: "F2F2F2", 12: "EAF0F7"})

# ---------------------------------------------------------------------------
doc.h1("5", "Quatre recommandations HPE")

doc.p("HPE est privilégié : disponibilité des pièces, densité des gammes, iLO pour l'administration "
      "hors bande (décisif quand le serveur est à Libreville et l'administrateur ailleurs), et "
      "reconnaissance du marché. Quatre configurations couvrent quatre logiques d'achat.")

doc.table(
    ["", "Configuration", "Prix HT", "Pour qui", "Limite"],
    [
        ["**R1**", "**DL325 Gen12** — EPYC 9124+ (5e gén.), 128 Go DDR5, 2×1,92 To, 2×10 GbE, iLO 7",
         "≈ 14 500 €", "Horizon 7 ans, budget disponible, volonté de ne pas racheter avant longtemps",
         "Surcoût de 5 à 6 k€ par rapport à une Gen11 équivalente"],
        ["**R2**", "**DL325 Gen11** — EPYC 9124 (16 cœurs / 3,0 GHz), 128 Go DDR5, 2×1,92 To, 2×10 GbE",
         "**≈ 8 900 €**", "**Le meilleur rapport performance / prix / pérennité du benchmark**",
         "Génération en fin de cycle commercial : exiger une remise"],
        ["**R3**", "**DL320 Gen11** — Xeon Silver 4410Y (12 cœurs / 2,0 GHz), 128 Go DDR5, 2×10 GbE",
         "≈ 11 800 €", "Contrainte d'homogénéité Intel (parc, outillage, compétences)",
         "Plus cher et moins rapide que R2 : la préférence Intel doit être justifiée"],
        ["**R4**", "**DL380 Gen11** — Xeon Silver 4510 (12 cœurs), 128 Go DDR5, 8SFF, 2×10 GbE",
         "≈ 13 900 €", "Croissance attendue du nombre de VM ou des baies disques",
         "1 à 2 k€ de plus qu'un 1U ; encombrement 2U"],
    ],
    widths=[1.0, 6.4, 2.0, 4.7, 3.0], font=7.8, aligns=["c", "l", "r", "l", "l"],
    caption="Tableau 7 — Les quatre recommandations HPE.",
    row_bg={2: "EDF5EC"})

doc.h2("R2 — la recommandation principale, en détail")
doc.table(
    ["Élément", "Choix retenu", "Pourquoi"],
    [
        ["Modèle", "HPE ProLiant DL325 Gen11, 1U / 1 socket", "Densité maximale, un seul socket donc une seule licence Proxmox"],
        ["Processeur", "AMD EPYC 9124 — 16 cœurs / 3,0 GHz (boost 3,7), PCIe 5.0",
         "Marge de calcul à 5 ans ; 128 lignes PCIe 5.0 pour le NVMe et le réseau"],
        ["Mémoire", "128 Go DDR5 4800 (4×32 Go) sur 12 emplacements", "128 Go livrés, 8 emplacements libres pour viser 256–384 Go"],
        ["Stockage", "2×1,92 To NVMe en RAID1 + 1 disque de rechange",
         "2 To utiles, latence faible ; baies 8 SFF pour la croissance"],
        ["Réseau", "2×10 GbE BASE-T (OCP 3.0) + emplacements PCIe libres", "10 GbE natif, pas d'option à acheter"],
        ["Gestion", "HPE iLO 6", "Redémarrage, console et firmware à distance — indispensable hors site"],
        ["Garantie", "3/3/3 (pièces, main-d'œuvre, intervention)", "Couvre la période d'amortissement minimale"],
        ["Prix cible", "**8 900 € HT** équipé (hors fret, licences, réseau)", "À obtenir par devis sur nomenclature identique"],
    ],
    widths=[2.3, 6.6, 8.2], font=8.0,
    caption="Tableau 8 — Configuration détaillée de la recommandation principale.",
    first_col_bold=True)

doc.callout("Pourquoi pas un 2U, pas 32 Go, pas un reconditionné en hôte principal",
            "**Pas 32 Go** : ce serait diviser par deux la mémoire d'un système déjà à 88 % de charge. "
            "**Pas un 2U** : le surcoût ne se justifie que si l'on prévoit plus de huit disques. "
            "**Pas un reconditionné Gen10 en hôte unique** : horizon de 2 à 3 ans, garantie revendeur, "
            "et pièces de plus en plus difficiles à trouver — acceptable en second nœud, pas en "
            "production unique.",
            "ok")

# ---------------------------------------------------------------------------
doc.h1("6", "Alternatives constructeurs")

doc.p("HPE n'est pas le seul choix rationnel. Trois constructeurs proposent des plateformes "
      "comparables, avec des écarts de prix et de support qui peuvent atteindre 30 %.")

doc.table(
    ["Constructeur", "Modèle", "CPU / RAM max", "Prix HT estimé", "Forces", "Limites", "Verdict"],
    [
        ["**HPE**", "DL325 Gen11", "EPYC 9124 / 3 To", "8 900 €", "iLO 6, réseau 10 GbE natif, pièces, réseau de revendeurs",
         "Prix des options constructeur élevé", "**Référence**"],
        ["**Dell**", "PowerEdge R6615 (16G)", "EPYC 9354P 32C / 3 To", "11 500 €", "32 cœurs, iDRAC 9, écosystème très large",
         "Tarif constructeur très élevé (16 400 € HT en direct) : passer par revendeur", "Alternative sérieuse"],
        ["**Lenovo**", "ThinkSystem SR645 V3", "EPYC 9124 / 3 To", "9 800 €", "XClarity, bonne densité, tarifs négociables",
         "Moins de revendeurs spécialisés en Afrique de l'Ouest/Centre", "Alternative"],
        ["**Supermicro**", "AS-1115CS-TNR", "EPYC 9124 / 3 To", "**7 600 €**", "Prix le plus bas à configuration égale, 10 baies",
         "Support souvent limité au revendeur, pas de couverture mondiale", "Option budget"],
        ["**HPE**", "DL380 Gen10 reconditionné", "2×Xeon Gold 6138 (40C) / 1,5 To", "3 200 €", "Prix imbattable, 40 cœurs, 128 Go DDR4",
         "Génération 2017, DDR4, garantie 12–24 mois, consommation élevée", "**Second nœud uniquement**"],
    ],
    widths=[1.8, 3.4, 3.2, 1.8, 3.0, 2.9, 1.9], font=7.4, aligns=["l", "l", "l", "r", "l", "l", "l"],
    caption="Tableau 9 — Alternatives à HPE (prix estimés à configuration équivalente : 128 Go, 2 To utiles, 10 GbE).",
    row_bg={2: "EAF0F7"})

doc.image("fig_bench_prix.png", "Figure 1 — Prix HT équipé des neuf candidats. Les barres hachurées correspondent au reconditionné.")

doc.callout("Le piège du constructeur direct",
            "Le tarif public Dell pour un R6615 à 64 Go dépasse **16 400 € HT** — soit 40 à 50 % "
            "au-dessus du prix revendeur pour la même machine. Le tarif constructeur n'est donc pas "
            "un prix d'achat : c'est une **référence haute** qui permet de mesurer la remise obtenue. "
            "La règle vaut pour HPE comme pour Dell.",
            "info")

# ---------------------------------------------------------------------------
doc.h1("7", "Où acheter : quatre circuits, quatre usages")

doc.p("Le même serveur peut varier de 40 % selon le circuit d'achat. La bonne pratique n'est pas de "
      "chercher le prix le plus bas, mais d'obtenir **trois devis sur une nomenclature identique**, "
      "puis de comparer le coût complet — garantie, délai, fret et support inclus.")

doc.table(
    ["Circuit", "Exemples", "Prix", "Garantie / support", "À utiliser pour"],
    [
        ["Configurateurs et revendeurs en ligne",
         "ServerMall, PC21, Senetic, MonParcInformatique",
         "**Les plus bas** (relevé : DL325 Gen11 64 Go à 5 726 € HT)",
         "Garantie constructeur enregistrée à l'achat ; conseil variable",
         "Établir le **prix de référence** et le plancher de négociation"],
        ["Intégrateurs et grossistes IT",
         "Bechtle, Insight, Computacenter/SCC, Inmac Wstore",
         "5 à 20 % au-dessus du moins-disant, remise volume à négocier",
         "Meilleure : contrat de support, interlocuteur unique, facturation propre",
         "**Achat de production** : c'est là que se joue la couverture de garantie"],
        ["Spécialistes du reconditionné",
         "OPP! Shop, DIB, Cycle IT, ServeurConsulting",
         "60 à 75 % sous le neuf",
         "12 à 36 mois, atelier en France, stock immédiat",
         "Second nœud, pièces détachées, environnement de test"],
        ["Constructeur en direct",
         "Dell.fr, HPE Store",
         "**Le plus élevé** (R6615 : 16 411 € HT)",
         "Contractuelle, mais sans remise revendeur",
         "Servir de **référence de prix**, jamais d'achat sauf opération flash"],
    ],
    widths=[3.1, 3.9, 3.4, 3.6, 3.1], font=7.6,
    caption="Tableau 10 — Circuits d'achat comparés.",
    first_col_bold=True)

doc.table(
    ["Référence / prestation", "Prix relevé", "Source"],
    [[r[0], f"**{r[1]}**", r[2]] for r in PRIX_MARCHE],
    widths=[10.4, 3.4, 3.3], font=7.9, aligns=["l", "r", "l"],
    caption="Tableau 11 — Relevés de prix du 5 novembre 2026 (publics, indicatifs).")

# ---------------------------------------------------------------------------
doc.h1("8", "Benchmark chiffré des neuf candidats")

rows = []
for c in sorted(CANDIDATS_B, key=lambda x: -note_ponderee(SCORES_B[x["code"]], POIDS_B)):
    rows.append([
        f'**{c["code"]}**', c["nom"], c["gen"], c["etat"],
        f'{c["cores"]}C', f'{d(c["ghz"],2)}', f'{c["ram"]} Go',
        f'{c["baies"]}', f'{eur(c["prix"])}', c["statut"],
        f'**{d(note_ponderee(SCORES_B[c["code"]], POIDS_B))}**',
    ])
doc.table(
    ["#", "Modèle", "Gén.", "État", "Cœurs", "GHz", "RAM", "Baies", "Prix HT", "Statut prix", "Score"],
    rows,
    widths=[0.8, 4.0, 1.2, 1.9, 1.1, 1.0, 1.2, 1.0, 1.9, 2.1, 1.2], font=7.4,
    aligns=["c", "l", "l", "l", "c", "c", "c", "c", "r", "l", "c"],
    caption="Tableau 12 — Benchmark complet, classé par score pondéré. "
            "« Constaté » = relevé public ; « estimé » = construit par analogie.",
    row_bg={0: "EDF5EC", 1: "EDF5EC"})

doc.image("fig_scores_b.png", "Figure 2 — Décomposition du score : la mémoire et la pérennité séparent les candidats, le prix ne suffit pas à les départager.")

doc.image("fig_bench_perf.png", "Figure 3 — Puissance de calcul brute rapportée au prix : le reconditionné 40 cœurs est hors jeu sur la pérennité, pas sur la performance.")

doc.h2("Analyse de valeur")
val = []
for c in CANDIDATS_B:
    utile = 1.92
    val.append([c["code"], c["nom"], eur(round(c["prix"] / c["ram"])),
                eur(round(c["prix"] / c["cores"])), eur(round(c["prix"] / utile)),
                d(note_ponderee(SCORES_B[c["code"]], POIDS_B))])
doc.table(
    ["#", "Modèle", "€ / Go RAM", "€ / cœur", "€ / To utile (machine)", "Score"],
    val, widths=[0.9, 5.4, 2.6, 2.4, 2.8, 1.8], font=7.9,
    aligns=["c", "l", "r", "r", "r", "c"],
    caption="Tableau 13 — Indicateurs de valeur. Le prix par gigaoctet de mémoire est le plus "
            "discriminant pour ce dossier ; la colonne « €/To utile » rapporte le prix de la machine "
            "au stockage utile livré (1,92 To en RAID1).")

doc.callout("Ce que le benchmark démontre",
            "Le classement n'est pas piloté par le prix : les deux moins chers du panel (H1 à 3 200 € et "
            "D2 à 6 500 €) terminent en bas, pénalisés par la pérennité et le support. Inversement, les "
            "deux mieux classés (R2 et R1) sont au-dessus du prix médian. **Le bon achat est celui qui "
            "minimise le coût par année de service rendu**, pas le prix d'entrée.",
            "ok")

# ---------------------------------------------------------------------------
doc.h1("9", "Coût total et point d'équilibre")

doc.p("Rapatrier n'est pas une décision technique : c'est un arbitrage financier entre un "
      "investissement et une dépense récurrente. Le calcul ci-dessous suppose 5 ans de détention, "
      "un prix de l'électricité de 0,12 €/kWh et une consommation moyenne de 250 W.")

doc.table(
    ["Poste", "Montant sur 5 ans", "Commentaire"],
    [
        ["Matériel + fret + douane", "18 360 €", "Serveur équipé, réseau, onduleur, rack"],
        ["Proxmox VE + Backup Server", "5 550 €", "1 110 €/an sur 1 socket et 1 serveur de sauvegarde"],
        ["Énergie et onduleur", "1 450 €", "≈ 2 190 kWh/an, pertes comprises"],
        ["Sauvegarde hors site", "1 500 €", "Copie externalisée — non négociable"],
        ["Exploitation et maintien", "6 000 €", "≈ 1 jour par mois de suivi, mises à jour, sauvegardes"],
        ["**Total local (5 ans)**", "**≈ 32 900 €**", "Soit ≈ 6 580 €/an, ou ≈ 21,6 M FCFA"],
    ],
    widths=[5.4, 3.2, 8.5], font=8.2, aligns=["l", "r", "l"],
    caption="Tableau 14 — Coût complet de la solution locale sur 5 ans.",
    row_bg={5: "EAF0F7"})

doc.table(
    ["Facture de location actuelle", "Coût cloud sur 5 ans", "Écart avec le local", "Lecture"],
    [
        ["150 €/mois HT", "9 000 €", "Local +23 900 €", "Le rapatriement coûte 2,6 fois plus cher"],
        ["250 €/mois HT", "15 000 €", "Local +17 900 €", "Aucun intérêt financier"],
        ["400 €/mois HT", "24 000 €", "Local +8 900 €", "Non rentable à 5 ans"],
        ["**≈ 550 €/mois HT**", "33 000 €", "**Équilibre**", "Seuil de bascule"],
        ["700 €/mois HT", "42 000 €", "Local −9 100 €", "Rentable dès la 4e année"],
    ],
    widths=[3.9, 3.2, 3.3, 6.7], font=8.2, aligns=["l", "r", "r", "l"],
    caption="Tableau 15 — Sensibilité au coût de location. Le seuil d'équilibre se situe autour de 550 €/mois HT.",
    row_bg={3: "FDF1E7"})

doc.image("fig_tco.png", "Figure 4 — Comparaison des coûts cumulés et position du seuil d'équilibre.")

doc.callout("La question à poser avant tout devis",
            "**Combien coûte la location aujourd'hui, mensuellement et hors taxes ?** Si la réponse est "
            "inférieure à 550 €/mois, rapatrier est un choix de souveraineté ou de maîtrise — pas une "
            "économie. Il faut alors l'assumer comme tel, et non le présenter comme une réduction de coûts.",
            "bad")

# ---------------------------------------------------------------------------
doc.h1("10", "Tranches d'investissement et enveloppe recommandée")

doc.image("fig_tranches_b.png", "Figure 5 — Quatre tranches d'investissement matériel (hors réseau, licences, fret et migration).")

doc.table(
    ["Tranche", "Matériel HT", "Configuration type", "Service rendu", "Risque"],
    [
        ["1. Reconditionné", "3 – 6 k€", "DL380 Gen10, 128 Go, 2×1,92 To",
         "Capacité immédiate, coût minimal", "Élevé : 2–3 ans d'horizon, garantie courte"],
        ["2. Cible coût", "8 – 10 k€", "DL325 Gen11 128 Go, ou Supermicro",
         "Le meilleur euro par Go utile, plateforme neuve", "Modéré : options de garantie à sécuriser"],
        ["**3. Cible recommandée**", "**11 – 15 k€**", "DL325 Gen11/Gen12 128 Go équipé NVMe, 3 ans de garantie",
         "Les deux contraintes traitées, horizon 5 à 7 ans", "**Faible**"],
        ["4. Confort", "15 – 19 k€", "DL380 Gen11 ou Dell 32 cœurs",
         "Marge de calcul et de baies pour la croissance", "Faible, mais dépense non justifiée par la charge"],
    ],
    widths=[2.8, 2.2, 4.6, 3.9, 3.6], font=7.9,
    caption="Tableau 16 — Quatre tranches d'investissement matériel.",
    row_bg={2: "EDF5EC"})

doc.callout("Recommandation d'enveloppe",
            "**Matériel : 10 000 à 13 000 € HT** (DL325 Gen11 128 Go équipé, rechange inclus). "
            "**Projet complet année 1 : 21 000 à 22 000 € HT**, fret et douane inclus. "
            "**Coût de fonctionnement : ≈ 2 900 € HT/an.** C'est cette dernière ligne qu'il faut "
            "comparer à la facture de location actuelle — pas le prix du serveur.",
            "ok")

# ---------------------------------------------------------------------------
doc.h1("11", "Plan d'approvisionnement en huit semaines")

doc.table(
    ["Phase", "Semaines", "Contenu", "Livrable"],
    [
        ["1. Cadrage et mesure", "S1 – S2", "Mesures par VM sur 30 jours, confirmation de la facture de location, arbitrage 128 Go",
         "Note de dimensionnement signée"],
        ["2. Consultation", "S2 – S4", "Trois devis sur nomenclature identique, quatre constructeurs, questions de conformité",
         "Tableau comparatif d'offres"],
        ["3. Négociation", "S4 – S5", "Remise de fin de génération, garantie 3 ans, délais, conditions de livraison internationale",
         "Bon de commande"],
        ["4. Logistique", "S5 – S7", "Fret, dédouanement, assurance transport, réception et contrôle",
         "Procès-verbal de réception"],
        ["5. Intégration", "S7 – S8", "Proxmox, RAID, réseau, iLO, sauvegarde, documentation, tests de restauration",
         "Plateforme prête et documentée"],
        ["6. Bascule", "S8 + 15 j", "Migration des VM, changement d'adresses IP, DNS, SPF/DKIM, certificats ; conservation du cloud en parallèle",
         "Service basculé, cloud résilié"],
    ],
    widths=[3.0, 2.0, 8.3, 3.8], font=7.9,
    caption="Tableau 17 — Séquence d'approvisionnement et de migration.",
    first_col_bold=True)

doc.table(
    ["Risque", "Impact", "Probabilité", "Mitigation"],
    [
        ["CPU non conforme sur une offre reconditionnée", "Élevé", "Moyenne", "Exiger la référence exacte au devis"],
        ["Fret et douane sous-estimés", "Moyen", "**Élevée**", "Devis transitaire avant commande ; marge de 20 %"],
        ["Absence de pièces dans 3 ans", "Élevé", "Moyenne", "Garantie 3 ans + disque et alimentation de rechange"],
        ["Coupures électriques", "Élevé", "**Élevée**", "Onduleur + groupe ; arrêt propre configuré"],
        ["Perte du serveur unique", "Critique", "Faible", "Sauvegarde PBS + copie hors site + test de restauration trimestriel"],
        ["Changement d'adresses IP mal anticipé", "Moyen", "Élevée", "Baisse des TTL, double période, fenêtre de bascule planifiée"],
    ],
    widths=[5.2, 1.8, 2.2, 7.9], font=7.9, aligns=["l", "c", "c", "l"],
    caption="Tableau 18 — Risques du projet et parades.",
    first_col_bold=True)

# ---------------------------------------------------------------------------
doc.h1("12", "Annexe — questions à poser aux revendeurs")

doc.p("À envoyer tel quel aux trois distributeurs consultés. Une offre qui ne répond pas à ces "
      "questions n'est pas comparable.")

doc.ul([
    "Référence constructeur exacte du serveur, et référence de chacun des composants proposés.",
    "Référence du processeur, nombre de cœurs, fréquence de base et fréquence turbo.",
    "Configuration mémoire : nombre de barrettes, capacité unitaire, nombre d'emplacements libres.",
    "Prix de l'extension à 128 Go (puis 256 Go) réalisée **à la commande** et réalisée **plus tard**.",
    "Contrôleur RAID fourni, mémoire cache, et compatibilité NVMe.",
    "Référence, endurance (DWPD) et garantie des disques proposés ; prix d'un disque de rechange identique.",
    "Nombre de baies libres après la configuration proposée.",
    "Ports réseau fournis, type de connecteur (BASE-T ou SFP+), emplacements PCIe et OCP libres.",
    "Alimentations : nombre, redondance, puissance.",
    "Garantie : durée, niveau (NBD ou 4 h), couverture sur site au Gabon, procédure d'intervention.",
    "Délai de livraison ferme et conditions d'expédition internationale (Incoterm, assurance, export).",
    "Poids et dimensions colis, pour chiffrer le fret.",
    "Firmware et BIOS livrés à jour, et prestation de configuration avant expédition.",
    "Pour le reconditionné : rapport de diagnostic, heures de fonctionnement, grade esthétique.",
    "Validité de l'offre et remise applicable pour un achat avant fin d'année.",
])

doc.p("**Avertissement.** Cette note est une analyse indépendante fondée sur des relevés publics du "
      "5 novembre 2026 et sur des estimations construites par analogie, signalées comme telles. "
      "Elle ne constitue ni une offre commerciale ni un engagement de prix. Les configurations citées "
      "doivent être confirmées par devis détaillé avant tout engagement.", small=True)

doc.save(OUT)
print("saved", OUT)
