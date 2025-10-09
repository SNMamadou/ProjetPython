#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
TP Thème 2 – Analyse de logs SSH simulés (auth.log)
Objectifs :
 - Lire et parcourir un fichier de log
 - Extraire des informations pertinentes (IPs, utilisateurs, erreurs)
 - Compter et classer les tentatives de connexion suspectes
 - Afficher les 5 IPs les plus actives
"""

import re
from collections import Counter

def analyse_log():
    fichier_log = "auth.log"  # Nom du fichier dans le dossier courant

    try:
        with open(fichier_log, "r", encoding="utf-8") as f:
            lignes = f.readlines()
    except FileNotFoundError:
        print(f"[ERREUR] Le fichier '{fichier_log}' est introuvable dans le dossier courant.")
        return

    # Étape 1 : extraire les lignes contenant "Failed password"
    lignes_failed = [ligne for ligne in lignes if "Failed password" in ligne]

    # Étape 2 : extraire les adresses IP avec une expression régulière
    pattern_ip = re.compile(r'(\d{1,3}(?:\.\d{1,3}){3})')
    ips = [pattern_ip.search(ligne).group() for ligne in lignes_failed if pattern_ip.search(ligne)]

    # Étape 3 : compter le nombre d’occurrences de chaque IP
    compteur_ips = Counter(ips)

    # Étape 4 : afficher les 5 IPs ayant généré le plus d’échecs
    print("\n TOP 5 des IPs avec le plus d'échecs de connexion SSH ===")
    for ip, count in compteur_ips.most_common(5):
        print(f"{ip} -> {count} tentatives échouées")

    print("\nNombre total de tentatives échouées :", len(ips))


if __name__ == "__main__":
    analyse_log()