import socket
import threading

# Ports à scanner (SSH, Web, RDP...)
TARGET_PORTS = [22, 80, 443, 3389, 8080]

def scan_port(ip, port, open_ports):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Timeout court (1 seconde)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    except:
        pass

def scan_hosts(ip_list):
    """
    Scan multithreadé des IPs fournies.
    """
    scan_results = {}
    print(f"\n--- Démarrage du Scan Réseau sur {len(ip_list)} cibles ---")
    
    for ip in ip_list:
        print(f"Scanning {ip}...")
        open_ports = []
        threads = []
        
        # Lancer un thread par port pour aller vite
        for port in TARGET_PORTS:
            thread = threading.Thread(target=scan_port, args=(ip, port, open_ports))
            threads.append(thread)
            thread.start()
        
        # Attendre la fin des threads
        for thread in threads:
            thread.join()
            
        if open_ports:
            scan_results[ip] = open_ports
            print(f" -> Ports ouverts : {open_ports}")
        else:
            scan_results[ip] = [] # Aucun port trouvé
            
    return scan_results
