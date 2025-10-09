-- ==============================
-- Création des tables principales
-- ==============================
 
CREATE TABLE Menaces (
    id_menace INT PRIMARY KEY AUTO_INCREMENT,               -- Identifiant unique de la menace
    nom_menace VARCHAR(50) NOT NULL UNIQUE,                 -- Nom unique de la menace
    type_incident VARCHAR(50) NOT NULL,                     -- Type de menace obligatoire (ex : malware)
    description VARCHAR(450) NOT NULL                       -- Description obligatoire
);
 
CREATE TABLE Actifs (
    id_actif INT PRIMARY KEY AUTO_INCREMENT,               -- Identifiant unique de l'actif
    nom_actif VARCHAR(100) NOT NULL UNIQUE,                -- Nom de l'actif unique
    type_actif VARCHAR(50) NOT NULL CHECK (type_actif IN ('Serveur', 'Poste de travail', 'Application', 'Base de données', 'Réseau')),
    -- Type obligatoire avec valeurs autorisées
    localisation VARCHAR(100) NOT NULL,                    -- Localisation obligatoire
    criticité VARCHAR(50) NOT NULL CHECK (criticité IN ('Faible','Moyen','Elevé','Critique'))
    -- Criticité obligatoire et restreinte à ces valeurs
);
 
CREATE TABLE Sources_d_alerte (
    id_source INT PRIMARY KEY AUTO_INCREMENT,              -- Identifiant unique
    type_source VARCHAR(50) NOT NULL,                      -- Type de source obligatoire (SIEM, IDS…)
    outil VARCHAR(100) NOT NULL,                            -- Nom de l'outil ayant généré l'alerte
    date_alert DATE NOT NULL,                               -- Date de génération de l'alerte
    message VARCHAR(450) NOT NULL                           -- Message ou résumé de l'alerte
);
 
CREATE TABLE Equipes (
    id_equipe INT PRIMARY KEY AUTO_INCREMENT,              -- Identifiant unique
    nom_equipe VARCHAR(50) NOT NULL UNIQUE,               -- Nom de l'équipe unique
    specialite VARCHAR(50) NOT NULL,                      -- Spécialité (SOC, Réseau, Forensic…)
    contact_mail VARCHAR(100) NOT NULL UNIQUE             -- Contact mail unique
);
 
CREATE TABLE Membre (
    id_membre INT PRIMARY KEY AUTO_INCREMENT,             -- Identifiant unique
    nom VARCHAR(50) NOT NULL,                              -- Nom obligatoire
    prenom VARCHAR(50) NOT NULL,                           -- Prénom obligatoire
    mail VARCHAR(100) NOT NULL UNIQUE,                     -- Mail unique obligatoire
    telephone VARCHAR(20) NOT NULL,                        -- Téléphone obligatoire
    id_equipe INT NOT NULL,                                 -- Chaque membre appartient à une seule équipe (1..1)
    FOREIGN KEY (id_equipe) REFERENCES Equipes(id_equipe)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
 
CREATE TABLE Vulnerabilites (
    id_vulnerabilite INT PRIMARY KEY AUTO_INCREMENT,       -- Identifiant unique
    description VARCHAR(450) NOT NULL,                     -- Description obligatoire
    CVSS_Score DECIMAL(3,1) NOT NULL CHECK (CVSS_Score >= 0 AND CVSS_Score <= 10)
    -- Score CVSS obligatoire entre 0 et 10
);
 
CREATE TABLE Incident (
    id_incident INT PRIMARY KEY AUTO_INCREMENT,           -- Identifiant unique
    type_incident VARCHAR(50) NOT NULL,                   -- Type obligatoire (intrusion, malware…)
    date_detection DATE NOT NULL,                          -- Date de détection obligatoire
    niveau_gravite VARCHAR(50) NOT NULL CHECK (niveau_gravite IN ('Faible', 'Moyen', 'Elevé', 'Critique')),
    statut VARCHAR(50) NOT NULL CHECK (statut IN ('En cours','Résolu')), -- Statut obligatoire
    description VARCHAR(450) NOT NULL                      -- Description obligatoire
);
 
CREATE TABLE Actions_Correctives (
    id_action INT PRIMARY KEY AUTO_INCREMENT,             -- Identifiant unique
    description VARCHAR(450) NOT NULL,                     -- Description de l'action obligatoire
    date_action DATE NOT NULL,                             -- Date de l'action obligatoire
    statut VARCHAR(50) NOT NULL CHECK (statut IN ('Planifiée','En cours','Terminée')),
    id_incident INT NOT NULL,                              -- Chaque action est liée à exactement un incident (1..1)
    id_equipe INT NOT NULL,                                -- Chaque action est réalisée par une seule équipe (1..1)
    FOREIGN KEY (id_incident) REFERENCES Incident(id_incident)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (id_equipe) REFERENCES Equipes(id_equipe)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
 
-- ==============================
-- Tables d'associations (relations N-N)
-- ==============================
 
-- Menace -> Incident (0..N / 0..N)
CREATE TABLE Provoquer (
    id_menace INT NOT NULL,
    id_incident INT NOT NULL,
    PRIMARY KEY (id_menace, id_incident), 
    FOREIGN KEY (id_menace) REFERENCES Menaces(id_menace) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_incident) REFERENCES Incident(id_incident) ON DELETE CASCADE ON UPDATE CASCADE
);
 
-- Incident -> Actif (0..N / 0..N)
CREATE TABLE Impacter (
    id_actif INT NOT NULL,
    id_incident INT NOT NULL,
    PRIMARY KEY (id_actif, id_incident),
    FOREIGN KEY (id_actif) REFERENCES Actifs(id_actif) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_incident) REFERENCES Incident(id_incident) ON DELETE CASCADE ON UPDATE CASCADE
);
 
-- Incident -> Vulnérabilité (0..N / 0..N)
CREATE TABLE Concretiser (
    id_vulnerabilite INT NOT NULL,
    id_incident INT NOT NULL,
    PRIMARY KEY (id_vulnerabilite, id_incident),
    FOREIGN KEY (id_vulnerabilite) REFERENCES Vulnerabilites(id_vulnerabilite) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_incident) REFERENCES Incident(id_incident) ON DELETE CASCADE ON UPDATE CASCADE
);
 
-- Incident -> Source d’alerte (0..N / 0..N)
CREATE TABLE Est_signale_par (
    id_source INT NOT NULL,
    id_incident INT NOT NULL,
    PRIMARY KEY (id_source, id_incident),
    FOREIGN KEY (id_source) REFERENCES Sources_d_alerte(id_source) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_incident) REFERENCES Incident(id_incident) ON DELETE CASCADE ON UPDATE CASCADE
);
 
-- Incident -> Équipe (1..N / 0..N)
CREATE TABLE Pris_en_charge (
    id_equipe INT NOT NULL,
    id_incident INT NOT NULL,
    PRIMARY KEY (id_equipe, id_incident),
    FOREIGN KEY (id_equipe) REFERENCES Equipes(id_equipe) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_incident) REFERENCES Incident(id_incident) ON DELETE CASCADE ON UPDATE CASCADE
);
