Pour le bon fonctionnement du projet, il faut installer la bibliothéque matplotlib avec : 
pip install matplotlib

La commande principal pour lancer le projet est : 
python3 main.py --access access.log --auth auth.log

Le script test.py va permettre de visionner les fichiers access.log et auth.log  avec la commande : 
python3 .\test.py

__________________________________________________________________________________________________________

Fichier explication 

log_parser.py : L'Extracteur 
Rôle : Transformer des données brutes (texte pas utile) en données structurées (objets exploitables)

Ce qu'il fait concrètement :

    Il ouvre les fichiers .log en lecture seule.
    Il parcourt chaque ligne une par une.
    Il applique des Regex pour "capturer" uniquement les informations qu'on veut : l'IP, le Code HTTP (404), le message d'erreur SSH.
    Il ignore le bruit (les dates, les textes inutiles, les lignes vides).


data_analyzer.py : Le Cerveau (Décision & Reporting)
Rôle : Corréler les données, appliquer la logique métier (règles de sécurité) et générer les rapports.

Ce qu'il fait concrètement :

        Fusionne : Il prend les alertes SSH et les alertes HTTP et les met dans un seul endroit (un dictionnaire ip_registry).
        Note (score) : Il applique le barème : SSH = +50, Bot = +10.
        Juge : C'est lui qui contient le if score >= 50. Il sépare les IPs "bruit de fond" des "menaces réelles".
        Visualise : Il utilise matplotlib pour dessiner le graphique et csv pour écrire le tableau Excel.


network_scanner.py : Le Bras Armé (Action Active)
Rôle : Passer d'une analyse passive (lecture) à une action active (connexion) pour vérifier la menace.

Ce qu'il fait concrètement :

        Il reçoit une liste d'IPs (les suspects identifiés par le Cerveau).
        Il tente d'ouvrir une connexion TCP sur des ports (22, 80, 443).

main.py : Le Chef d'Orchestre (Orchestrator)
Rôle : Piloter l'ensemble, gérer les arguments utilisateur et enchaîner les étapes dans le bon ordre.

    Ce qu'il fait concrètement :

        Il utilise argparse pour lire ce que tu tapes dans le terminal (--access, --auth).
        Il appelle les fonctions des autres fichiers dans l'ordre logique :
            Parser les logs (appel à log_parser).
            Calculer les scores (appel à data_analyzer).
            Si nécessaire, Scanner (appel à network_scanner).
            Générer le rapport (appel à data_analyzer).


