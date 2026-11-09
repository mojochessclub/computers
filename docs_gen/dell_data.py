# -*- coding: utf-8 -*-
"""Relevé Dell — page de résultats Amazon.fr fournie, 5 novembre 2026.

Même recherche que le dossier HP (« ordinateur de bureau », état Neuf, 750 à
1 250 €, marques Dell et HP), page 1 sur 2 : 48 annonces visibles sur 58.
Onze annonces Dell concernent un poste fixe ; six affichent un prix, cinq
sont en « voir les options ». Les portables, le client léger et les annonces
sans prix sont listés à part, avec leur motif d'exclusion.

Aucune valeur n'est déduite : ce qui n'est pas écrit dans l'annonce vaut
« n. c. ».
"""
from __future__ import annotations

from hp_bench import fcfa, freq_pair  # noqa: F401  (réexporté pour le générateur)

TVA = 655.957


def livré(prix, port):
    return round(prix + port, 2)


def _row(**kw):
    r = dict(
        format="", cpu="n. c.", année="n. c.", cœurs="n. c.", fréquence="n. c.",
        ram="n. c.", ram_type="n. c.", disque="n. c.", disque_type="n. c.",
        écran="non inclus", os="n. c.", licence="n. c.", réseau="n. c.",
        garantie="n. c.", périph="n. c.", motif="",
    )
    r.update(kw)
    r["livré"] = livré(r["prix"], r["port"])
    r["livré_fcfa"] = int(round(r["livré"] * TVA))
    r["lien"] = "https://www.amazon.fr/dp/%s" % r["asin"]
    return r


# Ordre de saisie ; le tri par total livré se fait dans dell_bench.
MACHINES = [
    _row(
        modèle="Dell Slim DS1265", format="Slim", cpu="Ryzen 5 150",
        année=2025, cœurs="n. c.", fréquence="n. c.",
        ram="16 Go", ram_type="DDR5 4800", disque="512 Go", disque_type="SSD M.2 NVMe",
        os="Windows 11 Famille", licence="Famille", réseau="non précisé",
        périph="Clavier et souris Dell inclus",
        prix=851.62, port=74.40, asin="B0H9LKCN2T",
        motif="Windows 11 Famille, année et référence du processeur à confirmer",
    ),
    _row(
        modèle="Dell 24 AIO EC24250", format="AiO 24\"", cpu="Core i5-1334U",
        année=2023, cœurs="10 cœurs / 12 threads", fréquence="1,3 – 4,6",
        ram="n. c.", ram_type="n. c.", disque="n. c.", disque_type="n. c.",
        écran="23,8\" Full HD inclus", os="Windows 11 Famille", licence="Famille",
        réseau="Wi-Fi 6E",
        périph="Clavier et souris sans fil inclus",
        prix=832.50, port=42.24, asin="B0GKJLFQ14",
        motif="Mémoire et disque non annoncés : impossible de conclure",
    ),
    _row(
        modèle="Dell OptiPlex 3060 MFF", format="Mini", cpu="Core (jeu H370, 8ᵉ gén.)",
        année=2018, cœurs="n. c.", fréquence="2,1",
        ram="n. c.", ram_type="n. c.", disque="n. c.", disque_type="n. c.",
        os="n. c.", réseau="Gigabit (port série annoncé)",
        prix=804.43, port=0.0, asin="B07DMKJXFT",
        motif="Plateforme 2018, ni mémoire, ni disque, ni système annoncés",
    ),
    _row(
        modèle="Dell OptiPlex 7070 Micro + écran 27\"", format="Mini", cpu="Core i9 (9ᵉ gén.)",
        année=2019, cœurs="n. c.", fréquence="n. c.",
        ram="16 Go", ram_type="DDR4", disque="512 Go", disque_type="SSD NVMe",
        écran="27\" Full HD inclus", os="Windows 11 Pro", licence="Pro",
        garantie="36 mois (vendeur, reconditionné)",
        prix=655.01, port=135.90, asin="B0H415LBD6",
        motif="Reconditionné ; plateforme 2019 (turbo annoncé à 5,0 GHz) malgré 16 Go et Windows 11 Pro",
    ),
    _row(
        modèle="Dell OptiPlex 7010 Micro (reconditionné)", format="Mini", cpu="Core i5-13500T",
        année=2023, cœurs="14 cœurs / 20 threads", fréquence="1,6 – 4,6",
        ram="16 Go", ram_type="DDR4 3200", disque="512 Go", disque_type="SSD NVMe",
        os="Windows 11 Pro", licence="Pro", garantie="vendeur (reconditionné)",
        prix=665.83, port=24.00, asin="B0HKDSCK9X",
        motif="Seule machine à réunir les quatre points, mais reconditionnée : "
              "seule la garantie du vendeur s'applique",
    ),
    _row(
        modèle="Dell OptiPlex 3080 SFF", format="SFF", cpu="Core i5-10505",
        année=2020, cœurs="6 cœurs / 12 threads", fréquence="3,2 – 4,6",
        ram="8 Go", ram_type="DDR4", disque="256 Go", disque_type="SSD",
        os="n. c.",
        prix=652.97, port=70.50, asin="B096G8GFS8",
        motif="8 Go et 256 Go seulement ; plateforme 2020 ; système non précisé",
    ),
]

# Annonces Dell écartées du tableau 3, avec leur motif.
ECARTEES = [
    ["Dell Pro Micro QCM1250", "i5-14500T · 16 Go · 512 Go · Windows 11 Pro · Wi-Fi",
     "Voir les options", "Prix non affiché : la seule configuration Dell qui tienne "
     "le socle, à chiffrer par devis", "B0FK1TZSKZ"],
    ["Dell Pro Micro QCM1250", "Core Ultra 5 235T · 8 Go · 512 Go · Windows 11 Pro",
     "Voir les options", "Prix non affiché ; 8 Go soudés, hors socle", "B0FR2R9C8P"],
    ["Dell Pro Micro QCM1250", "i5-14500T · 8 Go · 512 Go · Windows 11 Pro (version allemande)",
     "Voir les options", "Prix non affiché ; 8 Go, clavier allemand", "B0FR2M1187"],
    ["Dell Pro Micro QCM1250", "i7-14700T · 16 Go · 512 Go · Windows 11 Pro · Wi-Fi 6E",
     "Voir les options", "Prix non affiché ; i7 surdimensionné pour la bureautique", "B0FR2MXBX6"],
    ["Dell 27 AIO EC27250", "i5-1334U · Windows 11 Famille · Wi-Fi 6",
     "Voir les options", "Prix non affiché ; mémoire et disque non annoncés", "B0GVPV5YL9"],
    ["Dell 15 (portable)", "i5-1334U · 8 Go · 512 Go", "707,50 €",
     "Portable : hors périmètre des postes fixes", "B0H6CQHRWZ"],
    ["Dell 15 (portable)", "i5-1334U · 16 Go · 512 Go", "832,50 €",
     "Portable : hors périmètre des postes fixes", "B0GKDX2J81"],
    ["Dell Wyse C90LE7", "client léger, Celeron, sans disque local", "780,04 €",
     "Client léger : ne remplace pas un poste de travail", "B0044UCJI8"],
]
