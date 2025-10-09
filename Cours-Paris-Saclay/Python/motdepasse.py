#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from collections import Counter
import matplotlib.pyplot as plt

def analyse_log(fichier_log="auth.log"):
    try:
        with open(fichier_log, "r", encoding="utf-8") as f:
            lignes = f.readlines()
    except FileNotFoundError:
        print(f"[ERREUR] Le fichier '{fichier_log}' est introuvable.")
        return None, None


    lignes_failed = [l for l in lignes if "Failed password" in l]
    lignes_success = [l for l in lignes if "Accepted password" in l]

    pattern_ip = re.compile(r'(\d{1,3}(?:\.\d{1,3}){3})')
    ips_failed = [pattern_ip.search(l).group() for l in lignes_failed if pattern_ip.search(l)]
    ips_success = [pattern_ip.search(l).group() for l in lignes_success if pattern_ip.search(l)]

    compteur_failed = Counter(ips_failed)
    compteur_success = Counter(ips_success)

    return compteur_failed, compteur_success


def visualiser_ips(compteur_failed, compteur_success):
    if not compteur_failed:
        print("[INFO] Aucun échec détecté, rien à visualiser.")
        return

    top_failed = compteur_failed.most_common(10)
    ips, valeurs = zip(*top_failed)

    plt.figure(figsize=(10, 6))
    plt.bar(ips, valeurs, color='tomato', label='Échecs de connexion')

    valeurs_success = [compteur_success.get(ip, 0) for ip in ips]
    plt.bar(ips, valeurs_success, color='limegreen', alpha=0.6, label='Connexions réussies')

    plt.title("Tentatives de connexion SSH par adresse IP")
    plt.xlabel("Adresse IP")
    plt.ylabel("Nombre de tentatives")
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.tight_layout()

    plt.show()

if __name__ == "__main__":
    fichier = "auth.log"
    compteur_failed, compteur_success = analyse_log(fichier)
    visualiser_ips(compteur_failed, compteur_success)