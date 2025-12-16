import argparse
import log_parser
import data_analyzer
import network_scanner
import sys

def main():
    # 1. Configuration de la ligne de commande
    parser = argparse.ArgumentParser(description="Security Orchestrator - Mini SOAR")
    parser.add_argument("--access", required=True, help="Chemin du fichier access.log")
    parser.add_argument("--auth", required=True, help="Chemin du fichier auth.log")
    
    # Si on lance sans arguments, on aide l'utilisateur
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
        
    args = parser.parse_args()

    print("=== Démarrage de l'Analyse de Sécurité ===")

    # 2. Parsing des Logs
    print(f"[1] Analyse des fichiers...")
    http_data = log_parser.parse_http_log(args.access)
    ssh_data = log_parser.parse_ssh_log(args.auth)
    
    print(f" -> {len(http_data)} alertes HTTP trouvées.")
    print(f" -> {len(ssh_data)} alertes SSH trouvées.")

    # 3. Calcul des Scores
    print("[2] Calcul des Scores de Suspicion...")
    suspect_ips, ip_registry = data_analyzer.analyze_and_score(ssh_data, http_data)
    
    print(f" -> {len(suspect_ips)} IPs identifiées comme 'Hautement Suspectes'.")

    # 4. Scan Réseau (Action Automatisée)
    print("[3] Lancement du Scan Réseau Automatique...")
    if len(suspect_ips) > 0:
        scan_results = network_scanner.scan_hosts(suspect_ips)
    else:
        print(" -> Aucune IP n'a dépassé le seuil. Pas de scan nécessaire.")
        scan_results = {}

    # 5. Reporting
    print("[4] Génération des Rapports...")
    data_analyzer.generate_report(ip_registry, scan_results)
    data_analyzer.generate_graph(ip_registry)

    print("\n=== Analyse Terminée avec Succès ===")

if __name__ == "__main__":
    main()
