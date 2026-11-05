# -*- coding: utf-8 -*-
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import matplotlib.ticker as mticker

from data import (EXISTANT, OFFRES_JOEL, SCORES_A, POIDS_A, CANDIDATS_B, SCORES_B,
                  POIDS_B, TCO, note_ponderee)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)

BLEU = "#1F4E79"
BLEU_CLAIR = "#2E75B6"
ORANGE = "#C55A11"
ORANGE_CLAIR = "#ED9B5B"
VERT = "#2E7D32"
ROUGE = "#B00020"
GRIS = "#595959"
GRIS_CLAIR = "#BFBFBF"
JAUNE = "#C9A227"
VIOLET = "#6A3D9A"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9,
    "axes.titlesize": 11,
    "axes.titleweight": "bold",
    "axes.labelsize": 9,
    "axes.edgecolor": "#808080",
    "axes.linewidth": 0.8,
    "figure.dpi": 200,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.12,
})

VENDOR_COLOR = {"HPE": BLEU, "Dell": ORANGE, "Lenovo": VIOLET, "Supermicro": VERT}


def _clean(ax, grid_axis="x"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis=grid_axis, color="#DDDDDD", linewidth=0.7, zorder=0)
    ax.set_axisbelow(True)


def _save(fig, name):
    p = os.path.join(OUT, name)
    fig.savefig(p)
    plt.close(fig)
    print("ok", name)


# ---------------------------------------------------------------------------
def fig_charge():
    labels = ["CPU", "Mémoire vive", "Disque", "SWAP"]
    vals = [EXISTANT["cpu_pct"], EXISTANT["ram_pct"], EXISTANT["disque_pct"], EXISTANT["swap_pct"]]
    colors = []
    for v in vals:
        colors.append(VERT if v < 70 else (JAUNE if v < 85 else ROUGE))

    fig, ax = plt.subplots(figsize=(8.2, 3.4))
    y = range(len(labels))
    ax.barh(y, vals, color=colors, height=0.55, zorder=3)
    ax.barh(y, [100] * len(vals), color="#F2F2F2", height=0.55, zorder=1)
    for i, v in enumerate(vals):
        ax.text(v - 2 if v > 25 else v + 2, i, f"{v:.1f} %".replace(".", ","),
                va="center", ha="right" if v > 25 else "left",
                color="white" if v > 25 else GRIS, fontsize=9, fontweight="bold", zorder=4)
    ax.axvline(85, color=ROUGE, linestyle="--", linewidth=1.1, zorder=5)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, fontweight="bold")
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xlabel("Taux d'occupation moyen (%)")
    ax.set_title("Existant : la mémoire et le stockage saturent, le CPU est sous-employé")
    _clean(ax)
    _save(fig, "fig_charge.png")


# ---------------------------------------------------------------------------
def fig_prix_a():
    offres = sorted(OFFRES_JOEL, key=lambda o: o["prix"])
    labels = [f'{o["nom"]}' for o in offres]
    vals = [o["prix"] / 1000 for o in offres]
    colors = [BLEU if o["etat"] == "Neuf" else ORANGE for o in offres]

    fig, ax = plt.subplots(figsize=(8.2, 3.9))
    y = range(len(offres))
    ax.barh(y, vals, color=colors, height=0.62, zorder=3)
    for i, v in enumerate(vals):
        ax.text(v + 0.15, i, f"{v:,.1f} k€".replace(",", " ").replace(".", ","),
                va="center", fontsize=8.5, fontweight="bold", color=GRIS, zorder=4)
    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, fontsize=8.5)
    ax.invert_yaxis()
    ax.set_xlim(0, max(vals) * 1.22)
    ax.set_xlabel("Prix HT indicatif (k€)")
    ax.set_title("Périmètre étudié : sept configurations chiffrées")
    ax.legend(handles=[Patch(facecolor=BLEU, label="Neuf — Gen11"),
                       Patch(facecolor=ORANGE, label="Reconditionné — Gen10")],
              loc="lower right", frameon=False, fontsize=8.5)
    _clean(ax)
    _save(fig, "fig_prix_a.png")


# ---------------------------------------------------------------------------
def fig_valeur_a():
    pts = []
    for o in OFFRES_JOEL:
        sc = SCORES_A[o["nom"]]
        pts.append((o["prix"] / 1000, note_ponderee(sc, POIDS_A), o["nom"], o["etat"]))

    off = {
        "DL325 Gen11": (0.18, 1.1, "left"),
        "DL320 Gen11": (0.18, -1.2, "left"),
        "ML110 Gen11": (0.18, 0.0, "left"),
        "DL180 Gen10 2\u00d71,92 To": (0.18, -1.5, "left"),
        "DL180 Gen10 2\u00d73,84 To": (0.18, 0.9, "left"),
        "DL180 Gen10 1,92+3,84": (-0.18, 0.0, "right"),
        "DL180 Gen10 4\u00d73,84 To": (-0.18, 0.9, "right"),
    }
    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    for x, yv, nom, etat in pts:
        c = BLEU if etat == "Neuf" else ORANGE
        ax.scatter(x, yv, s=140, color=c, edgecolor="white", linewidth=1.2, zorder=4)
        dx, dy, ha = off.get(nom, (0.2, 0.8, "left"))
        ax.annotate(nom, (x + dx, yv + dy), fontsize=7.8, color=GRIS, ha=ha, va="center")
    ax.axhspan(0, 60, color="#FBE9E7", zorder=0)
    ax.text(5.4, 55.5, "zone à écarter", color=ROUGE, fontsize=8, fontweight="bold")
    ax.axhline(60, color=ROUGE, linestyle=":", linewidth=1)
    ax.set_xlabel("Prix HT indicatif (k€)")
    ax.set_ylabel("Score qualité / prix / performance (0–100)")
    ax.set_title("Le meilleur compromis : score élevé à budget contenu")
    ax.set_xlim(5, 11.4)
    ax.set_ylim(52, 78)
    _clean(ax, "both")
    _save(fig, "fig_valeur_a.png")


# ---------------------------------------------------------------------------
def fig_generations():
    rows = [
        ("Gen10 — reconditionné", 2017, 2027, ORANGE, "DDR4 · Xeon Scalable 1re/2e gén. · fin de commercialisation ~2023"),
        ("Gen11 — neuf", 2023, 2029, BLEU, "DDR5 · EPYC 9004 / Xeon 4e gén. · iLO 6"),
        ("Gen12 — neuf", 2025, 2031, BLEU_CLAIR, "DDR5 · EPYC 9005 / Xeon 6 · iLO 7 · hors budget"),
    ]
    fig, ax = plt.subplots(figsize=(8.2, 2.9))
    for i, (nom, deb, fin, c, txt) in enumerate(rows):
        ax.barh(i, fin - deb, left=deb, height=0.42, color=c, alpha=0.9, zorder=3)
        ax.text(deb + 0.15, i + 0.31, txt, fontsize=7.2, color=GRIS, va="bottom")
        ax.text(fin - 0.15, i, f"{fin}", fontsize=7.5, color="white", fontweight="bold",
                ha="right", va="center", zorder=4)
    ax.axvline(2026.85, color=ROUGE, linewidth=1.4, zorder=5)
    ax.text(2026.7, 2.62, "achat visé\n(nov. 2026)", color=ROUGE, fontsize=7.5,
            fontweight="bold", ha="right")
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows], fontsize=8.5, fontweight="bold")
    ax.invert_yaxis()
    ax.set_xlim(2016, 2032)
    ax.set_xticks(range(2017, 2033, 2))
    ax.set_xlabel("Horizon indicatif de commercialisation + support (schématique)")
    ax.set_title("Où se situe chaque génération dans le temps")
    _clean(ax)
    _save(fig, "fig_generations.png")


# ---------------------------------------------------------------------------
def _tranches_chart(rows, title, name):
    """rows = (label, min_k, max_k, couleur, sous_titre)"""
    fig, ax = plt.subplots(figsize=(8.2, 3.1))
    for i, (lab, lo, hi, c, sub) in enumerate(rows):
        ax.barh(i, hi - lo, left=lo, height=0.34, color=c, zorder=3)
        ax.text(lo + (hi - lo) / 2, i, f"{lo:g} – {hi:g} k€", ha="center", va="center",
                color="white", fontsize=8.5, fontweight="bold", zorder=4)
        ax.text(lo, i - 0.36, sub, fontsize=7.4, color=GRIS, va="top")
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows], fontsize=9, fontweight="bold")
    ax.invert_yaxis()
    ax.set_xlabel("Enveloppe HT (k€)")
    ax.set_title(title)
    ax.set_ylim(len(rows) - 0.4, -0.6)
    _clean(ax)
    _save(fig, name)


def fig_tranches_a():
    rows = [
        ("Tranche basse", 4, 7, ORANGE, "reconditionné Gen10 — 128 Go, forte capacité, pérennité limitée"),
        ("Tranche cible", 8, 10, BLEU, "Gen11 neuf 64 Go — plateforme moderne, mémoire juste suffisante"),
        ("Tranche confort", 11, 14, BLEU_CLAIR, "Gen11 neuf 128 Go — la seule qui traite vraiment la contrainte RAM"),
    ]
    _tranches_chart(rows, "Trois tranches de budget, trois niveaux de service rendu", "fig_tranches_a.png")


def fig_tranches_b():
    rows = [
        ("1. Reconditionné", 3, 6, ORANGE, "DL380 Gen10 128 Go — dépannage / nœud secondaire, pas de cible 5 ans"),
        ("2. Cible coût", 8, 10, BLEU, "HPE DL325 Gen11 128 Go ou Supermicro — meilleur €/Go utile"),
        ("3. Cible recommandée", 11, 15, BLEU_CLAIR, "HPE DL325 Gen11/Gen12 128 Go équipé NVMe, garantie 3 ans"),
        ("4. Confort / croissance", 15, 19, VERT, "DL380 Gen11 ou Dell 32 cœurs — marge VM et baies"),
    ]
    _tranches_chart(rows, "Quatre tranches d'investissement pour un serveur unique", "fig_tranches_b.png")


# ---------------------------------------------------------------------------
def fig_existant_cible():
    fig, axes = plt.subplots(1, 3, figsize=(8.4, 2.9))
    data = [
        ("Mémoire vive (Go)", 64, 128, "%"),
        ("Stockage utile (To)", 0.96, 3.84, "%"),
        ("Cœurs CPU", 8, 16, "%"),
    ]
    for ax, (titre, a, b, _) in zip(axes, data):
        ax.bar([0, 1], [a, b], color=[GRIS_CLAIR, BLEU], width=0.55, zorder=3)
        for xi, v in ((0, a), (1, b)):
            lab = f"{v:g}".replace(".", ",")
            ax.text(xi, v * 1.04, lab, ha="center", va="bottom", fontsize=9, fontweight="bold")
        ax.set_xticks([0, 1])
        ax.set_xticklabels(["existant", "cible"], fontsize=8)
        ax.set_title(titre, fontsize=9)
        ax.set_ylim(0, b * 1.28)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        ax.grid(axis="y", color="#DDDDDD", linewidth=0.7)
        ax.set_axisbelow(True)
    fig.suptitle("Dimensionnement : ce que l'existant impose comme cible", fontsize=10.5,
                 fontweight="bold")
    fig.tight_layout()
    _save(fig, "fig_existant_cible.png")


# ---------------------------------------------------------------------------
def fig_bench_prix():
    cands = sorted(CANDIDATS_B, key=lambda c: c["prix"])
    fig, ax = plt.subplots(figsize=(8.2, 4.1))
    for i, c in enumerate(cands):
        ax.barh(i, c["prix"] / 1000, height=0.6, color=VENDOR_COLOR[c["vendor"]],
                hatch="//" if c["etat"] == "Reconditionné" else None,
                edgecolor="white", alpha=0.95, zorder=3)
        ax.text(c["prix"] / 1000 + 0.15, i, f'{c["prix"]/1000:,.1f} k€'.replace(".", ","),
                va="center", fontsize=8, fontweight="bold", color=GRIS)
    ax.set_yticks(range(len(cands)))
    ax.set_yticklabels([f'{c["code"]} · {c["nom"]}' for c in cands], fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("Prix HT équipé, indicatif (k€)")
    ax.set_title("Benchmark d'approvisionnement — 9 candidats, 4 constructeurs")
    ax.legend(handles=[Patch(facecolor=v, label=k) for k, v in VENDOR_COLOR.items()] +
                      [Patch(facecolor="white", edgecolor=GRIS, hatch="//", label="Reconditionné")],
              loc="lower right", frameon=False, fontsize=7.5, ncol=2)
    ax.set_xlim(0, max(c["prix"] for c in cands) / 1000 * 1.2)
    _clean(ax)
    _save(fig, "fig_bench_prix.png")


# ---------------------------------------------------------------------------
def fig_bench_perf():
    fig, ax = plt.subplots(figsize=(8.2, 4.2))
    for c in CANDIDATS_B:
        x = c["prix"] / 1000
        y = c["cores"] * c["ghz"]
        ax.scatter(x, y, s=60 + c["ram"] / 2, color=VENDOR_COLOR[c["vendor"]],
                   alpha=0.75, edgecolor="white", linewidth=1.1, zorder=4)
        ax.annotate(c["code"], (x, y), xytext=(6, -3), textcoords="offset points",
                    fontsize=8, fontweight="bold", color=VENDOR_COLOR[c["vendor"]])
    ax.set_xlabel("Prix HT équipé (k€)")
    ax.set_ylabel("Indice de calcul brut (cœurs × GHz)")
    ax.set_title("Performance brute vs prix — la taille des bulles = RAM")
    ax.legend(handles=[Patch(facecolor=v, label=k) for k, v in VENDOR_COLOR.items()],
              loc="upper left", frameon=False, fontsize=7.5)
    _clean(ax, "both")
    _save(fig, "fig_bench_perf.png")


# ---------------------------------------------------------------------------
def fig_scores_b():
    rows = []
    for c in CANDIDATS_B:
        sc = SCORES_B[c["code"]]
        tot = sum(s * p for s, (_, p) in zip(sc, POIDS_B))
        rows.append((c, sc, tot))
    rows.sort(key=lambda r: r[2])
    pal = [BLEU, BLEU_CLAIR, VERT, JAUNE, VIOLET, ORANGE, GRIS]

    fig, ax = plt.subplots(figsize=(8.2, 4.3))
    for i, (c, sc, tot) in enumerate(rows):
        left = 0
        for (lab, p), s in zip(POIDS_B, sc):
            w = s * p
            ax.barh(i, w, left=left, height=0.62, color=pal[POIDS_B.index((lab, p)) % len(pal)],
                    edgecolor="white", linewidth=0.6, zorder=3)
            left += w
        ax.text(left + 12, i, f"{tot/10:.1f}", va="center", fontsize=8.5, fontweight="bold")
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([f'{c["code"]} · {c["nom"]}' for c, _, _ in rows], fontsize=8)
    ax.set_xlim(0, 1020)
    ax.set_xlabel("Score pondéré (0–1000)")
    ax.set_title("Score global pondéré : où chaque candidat gagne ses points")
    ax.legend(handles=[Patch(facecolor=pal[i % len(pal)], label=lab)
                       for i, (lab, p) in enumerate(POIDS_B)],
              loc="upper center", bbox_to_anchor=(0.5, -0.16), frameon=False,
              fontsize=7.6, ncol=4)
    _clean(ax)
    _save(fig, "fig_scores_b.png")


# ---------------------------------------------------------------------------
def fig_tco():
    t = TCO
    n = t["duree_ans"]
    matos = t["prix_serveur"] + t["peripheriques"]
    matos_total = matos * (1 + t["fret_douane_pct"])
    local_annee = (t["proxmox_an"] + t["pbs_an"] + t["energie_eur_an"]
                   + t["sauvegarde_hors_site_an"] + t["prestation_an"])
    cloud_annee = t["cloud_mensuel"] * 12

    local_cum, cloud_cum, loc, clo = [], [], [], []
    a = b = 0
    for an in range(1, n + 1):
        a += (matos_total if an == 1 else 0) + local_annee
        b += cloud_annee
        local_cum.append(a / 1000)
        cloud_cum.append(b / 1000)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.5, 3.5),
                                   gridspec_kw={"width_ratios": [1, 1.25]})

    parts = [("Matériel + fret/douane", matos_total), ("Proxmox VE + PBS", (t["proxmox_an"] + t["pbs_an"]) * n),
             ("Énergie / onduleur", t["energie_eur_an"] * n), ("Run & maintenance", t["prestation_an"] * n),
             ("Sauvegarde hors site", t["sauvegarde_hors_site_an"] * n)]
    bottom = 0
    for i, (lab, v) in enumerate(parts):
        ax1.bar([0], [v / 1000], bottom=bottom, color=pal_parts(i), width=0.5, zorder=3,
                edgecolor="white")
        bottom += v / 1000
    ax1.bar([1], [cloud_annee * n / 1000], color=GRIS, width=0.5, zorder=3)
    ax1.text(0, bottom + 0.6, f"{bottom:.1f} k€", ha="center", fontweight="bold", fontsize=9)
    ax1.text(1, cloud_annee * n / 1000 + 0.6, f"{cloud_annee*n/1000:.1f} k€", ha="center",
             fontweight="bold", fontsize=9)
    ax1.set_xticks([0, 1])
    ax1.set_xticklabels(["Local\n(5 ans)", "Cloud\n(5 ans)"], fontsize=8.5)
    ax1.set_ylabel("Coût cumulé HT (k€)")
    ax1.set_title("Coût total sur 5 ans", fontsize=9.5)
    ax1.legend(handles=[Patch(facecolor=pal_parts(i), label=l) for i, (l, _) in enumerate(parts)],
               fontsize=6.5, frameon=False, loc="upper right")
    ax1.set_ylim(0, max(bottom, cloud_annee * n / 1000) * 1.25)
    _clean(ax1, "y")

    ax2.plot(range(1, n + 1), local_cum, marker="o", color=BLEU, linewidth=2, label="Local (capex)")
    ax2.plot(range(1, n + 1), cloud_cum, marker="s", color=ORANGE, linewidth=2,
             label=f"Cloud (hyp. {t['cloud_mensuel']} €/mois HT)")
    seuil = local_cum[-1] / n / 12 * 1000
    for an in range(1, n + 1):
        ref = seuil * 12 * an / 1000
        ax2.plot([an], [ref], marker="_", color=ROUGE, markersize=14, zorder=5)
    ax2.plot([], [], marker="_", color=ROUGE, markersize=14, linewidth=0,
             label=f"Seuil d'équilibre : {seuil:.0f} €/mois HT")
    ax2.set_xlabel("Années")
    ax2.set_ylabel("Coût cumulé (k€)")
    ax2.set_title("Point d'équilibre", fontsize=9.5)
    ax2.legend(fontsize=7.2, frameon=False, loc="upper left")
    ax2.text(2.05, seuil * 12 * 2 / 1000 - 1.9, "au-delà de cette ligne la\nlocation coûte plus cher",
             fontsize=6.8, color=ROUGE, style="italic")
    ax2.set_xticks(range(1, n + 1))
    _clean(ax2, "y")
    fig.suptitle("TCO comparé : rapatrier n'est rentabilisé que si la facture cloud actuelle dépasse le seuil",
                 fontsize=9.5, fontweight="bold")
    fig.tight_layout()
    _save(fig, "fig_tco.png")
    return matos_total, local_annee, cloud_annee * n


def pal_parts(i):
    return [BLEU, BLEU_CLAIR, JAUNE, VERT, VIOLET][i % 5]


if __name__ == "__main__":
    fig_charge()
    fig_prix_a()
    fig_valeur_a()
    fig_generations()
    fig_tranches_a()
    fig_existant_cible()
    fig_bench_prix()
    fig_bench_perf()
    fig_scores_b()
    fig_tco()
    fig_tranches_b()
    print("charts done")
