# -*- coding: utf-8 -*-
"""Données partagées : existant, offres, benchmarks, scores, TCO."""

# ----------------------------------------------------------------------------
# 1. EXISTANT
# ----------------------------------------------------------------------------
EXISTANT = {
    "hyperviseur": "Hyperviseur Online / Scaleway (bare metal)",
    "cpu_pct": 15.0,
    "ram_go": 64,
    "ram_pct": 88.4,
    "disque_go": 960,
    "disque_pct": 89.9,
    "swap_pct": 99.0,
}

# ----------------------------------------------------------------------------
# 2. OFFRES DU DOSSIER JOËL (ServerMall) — prix HT indicatifs
# ----------------------------------------------------------------------------
# champs : nom, gen, etat, cpu, cores, ghz, ram, disque, reseau, prix, note
OFFRES_JOEL = [
    dict(nom="DL325 Gen11", ref="HPE DL325 Gen11 — 64 Go", gen="Gen11", etat="Neuf",
         cpu="AMD EPYC 9124", cores=16, ghz=3.00, ram=64, disque="n.c.",
         reseau="2×10GbE + 4×1GbE", prix=9174, famille="HPE"),
    dict(nom="DL320 Gen11", ref="HPE DL320 Gen11 — 64 Go", gen="Gen11", etat="Neuf",
         cpu="Xeon Silver 4410Y", cores=12, ghz=2.00, ram=64, disque="n.c.",
         reseau="2×10GbE + 4×1GbE", prix=9504, famille="HPE"),
    dict(nom="ML110 Gen11", ref="HPE ML110 Gen11 — 64 Go / Gold", gen="Gen11", etat="Neuf",
         cpu="Xeon Gold 6426Y", cores=16, ghz=2.50, ram=64, disque="n.c.",
         reseau="2×1GbE intégré", prix=9676, famille="HPE"),
    dict(nom="DL180 Gen10 2×1,92 To", ref="HPE DL180 Gen10 — 128 Go / 2×1,92 To", gen="Gen10", etat="Reconditionné",
         cpu="CPU non spécifié", cores=0, ghz=0, ram=128, disque="2×1,92 To",
         reseau="2×10GbE + 2×1GbE", prix=5621, famille="HPE"),
    dict(nom="DL180 Gen10 2×3,84 To", ref="HPE DL180 Gen10 — 128 Go / 2×3,84 To", gen="Gen10", etat="Reconditionné",
         cpu="CPU non spécifié", cores=0, ghz=0, ram=128, disque="2×3,84 To",
         reseau="2×10GbE + 2×1GbE", prix=6850, famille="HPE"),
    dict(nom="DL180 Gen10 1,92+3,84", ref="HPE DL180 Gen10 — 128 Go / 1,92+3,84 To", gen="Gen10", etat="Reconditionné",
         cpu="CPU non spécifié", cores=0, ghz=0, ram=128, disque="1,92 + 3,84 To",
         reseau="2×10GbE + 2×1GbE", prix=9427, famille="HPE"),
    dict(nom="DL180 Gen10 4×3,84 To", ref="HPE DL180 Gen10 — 128 Go / 4×3,84 To", gen="Gen10", etat="Reconditionné",
         cpu="CPU non spécifié", cores=0, ghz=0, ram=128, disque="4×3,84 To",
         reseau="2×10GbE + 2×1GbE", prix=10657, famille="HPE"),
]

# ----------------------------------------------------------------------------
# 3. RÉFÉRENCES DE PRIX CONSTATÉES SUR LE MARCHÉ (relevés début novembre 2026)
# ----------------------------------------------------------------------------
PRIX_MARCHE = [
    ("HPE DL325 Gen11 — EPYC 9124 / 64 Go / 8SFF / MR408i-o (réf. P77252-425)", "5 726 € HT", "PC21.fr"),
    ("HPE DL325 Gen11 — socle configurateur EPYC 9124 (sans option mémoire)", "5 423 € HT", "Configurateur ServerMall"),
    ("HPE DL325 Gen11 — EPYC 9224 / 64 Go / 2×480 Go SSD (réf. P77239-425)", "10 216 € HT", "MonParcInformatique.fr"),
    ("HPE DL380 Gen10 reconditionné — 2×Xeon Gold 6138 / 128 Go (garantie 24 mois)", "1 500 – 1 800 € HT", "OPP! Shop / Cycle IT"),
    ("Dell PowerEdge R6615 — EPYC 9354 / 64 Go (tarif constructeur, avant remise)", "16 411 € HT", "Dell.fr"),
    ("Proxmox VE — abonnement Basic (par socket / an)", "370 €", "Proxmox (tarif oct. 2026)"),
    ("Proxmox VE — abonnement Standard (par socket / an)", "550 €", "Proxmox (tarif oct. 2026)"),
    ("Proxmox Backup Server — abonnement Basic (par serveur / an)", "560 €", "Proxmox (tarif oct. 2026)"),
]

# ----------------------------------------------------------------------------
# 4. SCORES QUALITÉ / PRIX / PERFORMANCE — dossier A (périmètre Joël)
# ----------------------------------------------------------------------------
POIDS_A = [
    ("CPU (perf. & évolutivité)", 20),
    ("Mémoire (capacité & extension)", 20),
    ("Stockage (baies / disques)", 20),
    ("Réseau (10 GbE)", 10),
    ("Pérennité / garantie", 15),
    ("Prix d'acquisition", 15),
]

SCORES_A = {
    # offre : (cpu, ram, stockage, reseau, perennite, prix)
    "DL325 Gen11":        (9, 6, 5, 9, 9, 6),
    "DL320 Gen11":        (6, 6, 5, 8, 9, 4),
    "ML110 Gen11":        (8, 6, 4, 2, 8, 4),
    "DL180 Gen10 2×1,92 To": (3, 9, 8, 8, 3, 9),
    "DL180 Gen10 2×3,84 To": (3, 9, 9, 8, 3, 8),
    "DL180 Gen10 1,92+3,84": (3, 9, 9, 8, 3, 6),
    "DL180 Gen10 4×3,84 To": (3, 9, 10, 8, 3, 5),
}

# ----------------------------------------------------------------------------
# 5. CANDIDATS DU BENCHMARK — document B
# ----------------------------------------------------------------------------
# prix : valeur retenue pour le benchmark (HT), statut : constaté / estimé
CANDIDATS_B = [
    dict(code="R1", nom="HPE DL325 Gen12", config="EPYC 9124+ (5e gén.) / 128 Go DDR5 / 2×1,92 To NVMe / 2×10 GbE",
         vendor="HPE", gen="Gen12", etat="Neuf", cores=16, ghz=3.00, ram=128, ram_max=6144,
         baies=8, prix=14500, statut="Estimé", garantie="3/3/3"),
    dict(code="R2", nom="HPE DL325 Gen11", config="EPYC 9124 (16C/3,0) / 128 Go DDR5 / 2×1,92 To NVMe / 2×10 GbE",
         vendor="HPE", gen="Gen11", etat="Neuf", cores=16, ghz=3.00, ram=128, ram_max=3072,
         baies=8, prix=8900, statut="Constaté partiel", garantie="3/3/3"),
    dict(code="R3", nom="HPE DL320 Gen11", config="Xeon Silver 4410Y (12C/2,0) / 128 Go DDR5 / 2×1,92 To / 2×10 GbE",
         vendor="HPE", gen="Gen11", etat="Neuf", cores=12, ghz=2.00, ram=128, ram_max=1024,
         baies=8, prix=11800, statut="Estimé", garantie="3/3/3"),
    dict(code="R4", nom="HPE DL380 Gen11", config="Xeon Silver 4510 (12C/2,4) / 128 Go DDR5 / 8SFF / 2×10 GbE",
         vendor="HPE", gen="Gen11", etat="Neuf", cores=12, ghz=2.40, ram=128, ram_max=8192,
         baies=8, prix=13900, statut="Estimé", garantie="3/3/3"),
    dict(code="D1", nom="Dell PowerEdge R6615", config="EPYC 9354P (32C/3,25) / 128 Go DDR5 / 2×1,92 To / 2×10 GbE",
         vendor="Dell", gen="16G", etat="Neuf", cores=32, ghz=3.25, ram=128, ram_max=3072,
         baies=10, prix=11500, statut="Estimé", garantie="3 ans NBD"),
    dict(code="D2", nom="Dell PowerEdge R6615 (recond.)", config="EPYC 9354P / 128 Go / 2×1,92 To SSD",
         vendor="Dell", gen="16G", etat="Reconditionné", cores=32, ghz=3.25, ram=128, ram_max=3072,
         baies=10, prix=6500, statut="Estimé", garantie="12–24 mois"),
    dict(code="L1", nom="Lenovo ThinkSystem SR645 V3", config="EPYC 9124 / 128 Go DDR5 / 2×1,92 To / 2×10 GbE",
         vendor="Lenovo", gen="V3", etat="Neuf", cores=16, ghz=3.00, ram=128, ram_max=3072,
         baies=8, prix=9800, statut="Estimé", garantie="3 ans"),
    dict(code="S1", nom="Supermicro AS-1115CS-TNR", config="EPYC 9124 / 128 Go DDR5 / 2×1,92 To / 2×10 GbE",
         vendor="Supermicro", gen="—", etat="Neuf", cores=16, ghz=3.00, ram=128, ram_max=3072,
         baies=10, prix=7600, statut="Estimé", garantie="3 ans (revendeur)"),
    dict(code="H1", nom="HPE DL380 Gen10 (recond.)", config="2×Xeon Gold 6138 (40C) / 128 Go DDR4 / 2×1,92 To SSD",
         vendor="HPE", gen="Gen10", etat="Reconditionné", cores=40, ghz=2.00, ram=128, ram_max=1536,
         baies=8, prix=3200, statut="Constaté partiel", garantie="12–24 mois"),
]

POIDS_B = [
    ("Performance CPU utile", 15),
    ("Mémoire : capacité + extensibilité", 20),
    ("Stockage : baies, NVMe, RAID", 15),
    ("Réseau / I-O", 10),
    ("Pérennité & génération", 15),
    ("Support & garantie", 10),
    ("Prix d'acquisition", 15),
]

SCORES_B = {
    # code : (cpu, ram, stockage, reseau, perennite, support, prix)
    "R1": (9, 10, 9, 9, 10, 9, 4),
    "R2": (9, 9, 9, 9, 7, 9, 8),
    "R3": (6, 7, 7, 9, 7, 9, 5),
    "R4": (6, 9, 9, 9, 7, 9, 5),
    "D1": (10, 9, 9, 9, 9, 8, 6),
    "D2": (10, 9, 9, 9, 6, 5, 9),
    "L1": (9, 9, 8, 8, 8, 8, 7),
    "S1": (9, 9, 9, 8, 7, 6, 9),
    "H1": (6, 9, 7, 7, 2, 4, 10),
}

# ----------------------------------------------------------------------------
# 6. TCO / HYPOTHÈSES (Libreville)
# ----------------------------------------------------------------------------
TCO = dict(
    eur_xaf=655.957,
    duree_ans=5,
    prix_serveur=12500,       # cible Gen11/Gen12 128 Go équipé
    peripheriques=2800,       # switch 10 GbE, onduleur, rack, câblage, module
    fret_douane_pct=0.20,     # fret + droits + transitaire, sur matériel
    proxmox_an=550,           # Standard, 1 socket
    pbs_an=560,               # sauvegarde, 1 serveur (option)
    energie_eur_an=290,       # ~250 W moyens, 0,12 €/kWh + pertes onduleur
    sauvegarde_hors_site_an=300,  # petit stockage objet conservé dans le cloud
    prestation_an=1200,       # run/maintien, 1 j/mois
    cloud_mensuel=250,        # hypothèse facture actuelle, à confirmer
)


def note_ponderee(scores, poids):
    total_poids = sum(p for _, p in poids)
    return round(sum(s * p for s, (_, p) in zip(scores, poids)) / total_poids / 10 * 100, 1)
