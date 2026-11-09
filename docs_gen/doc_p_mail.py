"""Courriel d'accompagnement de la version C — une page, ton direct."""
import os
from render import Doc

BASE = "P_Mail_a_Jad_poste_fixe_16_Go_ou_32_Go"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "livrables")

doc = Doc(
    base=BASE,
    title="Postes fixes professionnels — 16 Go ou 32 Go",
    subtitle="Courriel d'accompagnement",
    meta=[],
    doc_ref="GED-MAIL-2026-11",
    footer="Joël MBA OYONE · GED-SERVICES — courriel d'accompagnement",
)

doc.h1_plain("Postes fixes : 16 Go, 32 Go, et ce que vaut le HP Elite Mini")

doc.table(
    ["", ""],
    [
        ["**À**", "M. Jad, directeur général — ADCHIM"],
        ["**De**", "Joël MBA OYONE — GED-SERVICES"],
        ["**Objet**", "Postes fixes : 16 Go ou 32 Go, et le prix réel du HP Elite 800 G9 Mini"],
        ["**Pièces jointes**", "Note technique — cible, marché et candidat : PDF et Word"],
    ],
    widths=[3.4, 13.7], font=8.8, header=False, aligns=["l", "l"],
)

doc.p("Jad,", small=False)

doc.p("Trois points, dans l'ordre où ils se décident.")

doc.p("**Le besoin.** Bureautique intense, 32 Go de mémoire, 512 Go de stockage, Windows 11 "
      "Professionnel, trois ans de garantie. Le processeur n'est pas le sujet : un i5 de "
      "quatorzième génération suffit largement.", small=True)

doc.p("**16 Go ou 32 Go.** Le HP Elite 800 G9 Mini est livré en 16 Go pour 1 140,18 € "
      "(747 909 FCFA). Le porter à 32 Go coûte 335,95 € avec une barrette — 593,95 € si la machine "
      "arrive en 2 × 8 Go —, soit 29 à 52 % du prix du poste. Chiffre final : **1 476,13 €** en "
      "barrette, **1 561,08 €** écran compris, **1 734,13 €** si kit. En face : Lenovo M70t "
      "**1 492,95 €**, Dell OptiPlex 7020 **1 592,95 €**, tous deux à compléter aussi.", small=True)

doc.p("**Le marché.** Cinq distributeurs, trois machines : Amazon est le seul à vendre ce HP en "
      "neuf au prix relevé ; LDLC et Materiel.net ne le référencent pas mais ont le Lenovo en "
      "stock ; Fnac et Cdiscount passent par des places de marché.")

doc.p("Les montants sont **indicatifs** : relevés le 5 novembre 2026, ils bougent chaque semaine, "
      "la mémoire surtout. Ils **n'incluent pas la livraison** — sauf le port du HP, compris dans "
      "son prix — et ne valent pas offre ferme.")

doc.callout("En une phrase",
            "Bon poste, pas un bon prix : je l'achète si le vendeur confirme 1 × 16 Go avec un "
            "emplacement libre, TPM activé et trois ans de garantie sur site ; sinon, la tour "
            "Lenovo à 899 € fait le même travail.", kind="ok")

doc.p("La note complète est jointe, en PDF et en Word.")

doc.p("Bien à toi,")
doc.p("**Joël MBA OYONE** — GED-SERVICES")

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
_cp.subject = "Courriel d'accompagnement — postes fixes"
_cp.title = "Postes fixes : 16 Go ou 32 Go, et ce que vaut le HP Elite Mini"
_d.save(_PATH)
print("saved", OUT)
