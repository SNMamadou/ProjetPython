import re

def parse_ssh_log(file_path):
    """
    Analyse le fichier auth.log pour trouver les échecs de connexion SSH.
    """
    results = []
    # Regex : "Failed password" ... "from" ... IP
    regex_pattern = r"Failed password .* from (\d+\.\d+\.\d+\.\d+)"
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if "Failed password" in line:
                    match = re.search(regex_pattern, line)
                    if match:
                        ip = match.group(1)
                        results.append({'ip': ip, 'type': 'ssh_failed'})
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")
        
    return results

def parse_http_log(file_path):
    """
    Analyse le fichier access.log pour trouver les 404 et les Bots.
    Version 'Tout Terrain' pour gérer les espaces variables.
    """
    results = []
    
    # NOUVELLE REGEX EXPLIQUÉE :
    # ^(\S+)    -> L'IP au début
    # .*?       -> On ignore tout jusqu'au prochain truc important
    # ".*?"     -> La Requête (on prend tout ce qui est entre guillemets sans se poser de question)
    # \s+       -> Au moins un espace
    # (\d{3})   -> Le Code Status (ex: 404)
    # \s+       -> Au moins un espace
    # .*?       -> On ignore la taille etc
    # "(.*?)"   -> Le User-Agent (entre guillemets)
    regex_pattern = r'^(\S+).*?".*?"\s+(\d{3})\s.*?"(.*?)"'
    
    suspicious_agents = ['bot', 'crawler', 'spider', 'curl', 'wget']

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # On ignore les lignes vides ou mal formées
                if not line.strip(): continue 

                match = re.search(regex_pattern, line)
                if match:
                    ip = match.group(1)
                    status_code = match.group(2)
                    user_agent = match.group(3).lower()

                    # Cas 1 : Erreur 404
                    if status_code == '404':
                        results.append({'ip': ip, 'type': 'http_404'})

                    # Cas 2 : Détection de Bot
                    if any(bot in user_agent for bot in suspicious_agents):
                        results.append({'ip': ip, 'type': 'http_bot'})
                        
    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")

    return results
