import csv
import matplotlib.pyplot as plt

def analyze_and_score(ssh_data, http_data):
    """
    Fusionne les logs et calcule les scores.
    Règles : SSH Fail = 50pts, Bot = 10pts, 404 = 1pt.
    Seuil de suspicion : 50 points.
    """
    ip_registry = {}

    def init_ip(ip):
        if ip not in ip_registry:
            ip_registry[ip] = {'score': 0, 'ssh_fails': 0, 'http_404': 0, 'bot_requests': 0}

    # 1. Traitement SSH
    for entry in ssh_data:
        ip = entry['ip']
        init_ip(ip)
        ip_registry[ip]['ssh_fails'] += 1
        ip_registry[ip]['score'] += 50

    # 2. Traitement HTTP
    for entry in http_data:
        ip = entry['ip']
        init_ip(ip)
        if entry['type'] == 'http_404':
            ip_registry[ip]['http_404'] += 1
            ip_registry[ip]['score'] += 1
        elif entry['type'] == 'http_bot':
            ip_registry[ip]['bot_requests'] += 1
            ip_registry[ip]['score'] += 10

    # 3. Filtrage des suspects (Score >= 50)
    suspect_ips = [ip for ip, data in ip_registry.items() if data['score'] >= 50]
    
    return suspect_ips, ip_registry

def generate_report(ip_registry, scan_results):
    """
    Génère le fichier CSV final 'rapport_securite.csv'.
    """
    file_name = "rapport_securite.csv"
    
    try:
        with open(file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # En-tête du fichier CSV
            writer.writerow(["IP", "Score Global", "Raison Principale", "Ports Ouverts"])
            
            for ip, data in ip_registry.items():
                # On ne met dans le rapport que ceux qui ont un score > 0
                if data['score'] > 0:
                    # Détermination de la raison principale
                    reason = "Activité Suspecte Diverse"
                    if data['ssh_fails'] > 0: reason = "Brute-Force SSH"
                    elif data['bot_requests'] > 0: reason = "Bot Scanning"
                    elif data['http_404'] > 10: reason = "Mass 404 Errors"
                    
                    # Récupération des ports ouverts (si scannés)
                    ports = scan_results.get(ip, "Non Scanné/Fermé")
                    
                    writer.writerow([ip, data['score'], reason, ports])
        
        print(f"[+] Rapport CSV généré : {file_name}")
    except Exception as e:
        print(f"[-] Erreur lors de la création du CSV : {e}")

def generate_graph(ip_registry):
    """
    Crée un histogramme des Top 5 IPs suspectes.
    """
    # Trier les IPs par score décroissant
    sorted_ips = sorted(ip_registry.items(), key=lambda x: x[1]['score'], reverse=True)[:5]
    
    if not sorted_ips:
        print("[-] Pas assez de données pour le graphique.")
        return

    ips = [item[0] for item in sorted_ips]
    scores = [item[1]['score'] for item in sorted_ips]

    try:
        plt.figure(figsize=(10, 6))
        plt.bar(ips, scores, color='red')
        plt.xlabel('Adresses IP')
        plt.ylabel('Score de Suspicion')
        plt.title('Top 5 des IPs les plus dangereuses')
        plt.savefig('top_5_suspects.png') # Sauvegarde l'image
        print("[+] Graphique généré : top_5_suspects.png")
    except Exception as e:
        print(f"[-] Erreur lors de la création du graphique : {e}")
