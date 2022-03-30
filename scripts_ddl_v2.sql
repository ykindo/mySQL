DROP DATABASE IF EXISTS `gestion_de_paie`;
CREATE DATABASE `gestion_de_paie` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `gestion_de_paie`;

-- gestion_de_paie.tbl_refemployeur definition

CREATE TABLE `tbl_refemployeur` (
  `refEmp_num_IFU` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `refEmp_raison_sociale` varchar(100) NOT NULL COMMENT 'La raison sociale',
  `refEmp_sigle` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `refEmp_tel` varchar(20) NOT NULL,
  `refEmp_site_internet` varchar(50) DEFAULT NULL,
  `refEmp_email` varchar(50) DEFAULT NULL,
  `refEmp_code_postal` varchar(50) DEFAULT NULL,
  `refEmp_registre_commerce` varchar(30) NOT NULL,
  `refEmp_num_CNSS` varchar(30) NOT NULL,
  `refEmp_siege_social` varchar(50) NOT NULL,
  `refEmp_prof_activite` varchar(200) DEFAULT NULL COMMENT 'Profession ou activité principale de la structure',
  `refEmp_quartier` varchar(30) DEFAULT NULL,
  `refEmp_secteur` varchar(30) DEFAULT NULL,
  `refEmp_rue` varchar(30) DEFAULT NULL,
  `refEmp_section` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `refEmp_lot` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `refEmp_parcel` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `refEmp_nom_premier_responsable` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `refEmp_premon_premier_responsable` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `refEmp_titre_premier_responsable` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `refEmp_titre_honorifique_premier_responsable` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `refEmp_nom_RAF` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `refEmp_premon_RAF` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `refEmp_titre_RAF` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `refEmp_titre_honorifique_RAF` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `refEmp_assujeti_PTA` tinyint(1) NOT NULL DEFAULT '1',
  `refEmp_logo` mediumblob,
  PRIMARY KEY (`refEmp_num_IFU`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Les informations de la structure employeur';



-- gestion_de_paie.tbl_user definition

CREATE TABLE `tbl_user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_nom` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `user_prenom` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `user_num_telephone` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `user_civilite` varchar(50) DEFAULT NULL,
  `user_email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `user_ifu_employeur` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `user_photo` mediumblob,
  PRIMARY KEY (`user_id`),
  KEY `tbl_user_FK` (`user_ifu_employeur`),
  CONSTRAINT `tbl_user_FK` FOREIGN KEY (`user_ifu_employeur`) REFERENCES `tbl_refemployeur` (`refEmp_num_IFU`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Table des utilisateurs';

-- gestion_de_paie.tbl_grillesalaire definition

CREATE TABLE `tbl_grillesalaire` (
  `grilleSalaire_categorie` varchar(20) NOT NULL,
  `grilleSalaire_salaire_base` double NOT NULL,
  PRIMARY KEY (`grilleSalaire_categorie`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='La grille salariale des employés';


-- gestion_de_paie.tbl_infoemploye definition

CREATE TABLE `tbl_infoemploye` (
  `info_matricule` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `info_nom` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_prenom` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_telephone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_email` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_dateNaissance` date NOT NULL,
  `info_dateEmbauche` date NOT NULL,
  `info_datePaie` date NOT NULL,
  `info_salaireBase` double NOT NULL DEFAULT '0',
  `info_indemniteLogement` double NOT NULL DEFAULT '0',
  `info_indemniteFonction` double NOT NULL DEFAULT '0',
  `info_indemniteTransport` double NOT NULL DEFAULT '0',
  `info_indemniteSujetion` double NOT NULL DEFAULT '0',
  `info_indemniteTechnicite` double NOT NULL DEFAULT '0' COMMENT 'Indemnité de technicité',
  `info_indemniteCaisse` double NOT NULL DEFAULT '0',
  `info_indemniteAutres` double NOT NULL DEFAULT '0',
  `info_autresPrimes` double NOT NULL DEFAULT '0',
  `info_avantagesNatureImmobilisation` double NOT NULL DEFAULT '0',
  `info_avantagesNatureEmploye` double NOT NULL DEFAULT '0' COMMENT 'Salaire de base de l''employé mis à disposition',
  `info_allocationFamilliale` double NOT NULL DEFAULT '0',
  `info_montantHeuresSupplementaires` double NOT NULL DEFAULT '0',
  `info_avanceAcompte` double NOT NULL DEFAULT '0',
  `info_oppositionSaisieArret` double NOT NULL DEFAULT '0',
  `info_autresRetenues` double NOT NULL DEFAULT '0',
  `info_chargeFamilial` smallint NOT NULL DEFAULT '0',
  `info_typeAbatementCadre` tinyint(1) NOT NULL DEFAULT '0' COMMENT 'Le type d''abattement forfaitaire applicable (Cadre : 20% et Non Cadre : 25%)',
  `info_categorie` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `info_institutionBancaire` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_numeroCompteBancaire` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_service` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_fonction` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_numeroCNSS` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_ifuEmployeur` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`info_matricule`),
  KEY `tbl_info_employe_grille_FK` (`info_categorie`),
  KEY `tbl_info_employeEmployeur_FK_1` (`info_ifuEmployeur`),
  CONSTRAINT `tbl_info_employe_FK` FOREIGN KEY (`info_categorie`) REFERENCES `tbl_grillesalaire` (`grilleSalaire_categorie`) ON UPDATE CASCADE,
  CONSTRAINT `tbl_info_employeEmployeur_FK_1` FOREIGN KEY (`info_ifuEmployeur`) REFERENCES `tbl_refemployeur` (`refEmp_num_IFU`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- gestion_de_paie.tbl_parametrecontrat definition

CREATE TABLE `tbl_parametrecontrat` (
  `paramContrat_id` int NOT NULL AUTO_INCREMENT,
  `paramContrat_date_debut` date NOT NULL,
  `paramContrat_date_fin` date DEFAULT NULL,
  `paramContrat_date_preavis` date DEFAULT NULL,
  `paramContrat_emetteur_preavis` tinyint(1) DEFAULT '1' COMMENT 'Préavis emis par défaut par l''employeur',
  `paramContrat_matricule` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`paramContrat_id`),
  KEY `tbl_parametre_contrat_FK` (`paramContrat_matricule`),
  CONSTRAINT `tbl_parametre_contrat_FK` FOREIGN KEY (`paramContrat_matricule`) REFERENCES `tbl_infoemploye` (`info_matricule`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Enregistrement des paramètres du contrat de chaque employé';



-- gestion_de_paie.tbl_conge definition

CREATE TABLE `tbl_conge` (
  `conge_id` int NOT NULL AUTO_INCREMENT,
  `conge_date_debut` date DEFAULT NULL,
  `conge_date_fin` date DEFAULT NULL,
  `conge_type` varchar(50) DEFAULT NULL,
  `conge_matricule` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`conge_id`),
  KEY `tbl_conge_FK` (`conge_matricule`),
  CONSTRAINT `tbl_conge_FK` FOREIGN KEY (`conge_matricule`) REFERENCES `tbl_infoemploye` (`info_matricule`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Les informations concernant les congés des employés';



-- gestion_de_paie.tbl_suspension definition

CREATE TABLE `tbl_suspension` (
  `suspension_id` int NOT NULL AUTO_INCREMENT,
  `suspension_dateDebut` date NOT NULL,
  `suspension_dateFin` date DEFAULT NULL,
  `suspension_type` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `suspension_matricule` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `suspension_commentaire` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`suspension_id`),
  KEY `tbl_suspension_FK` (`suspension_matricule`),
  CONSTRAINT `tbl_suspension_FK` FOREIGN KEY (`suspension_matricule`) REFERENCES `tbl_infoemploye` (`info_matricule`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Les informations concernant les suspensions de travail des employés';



-- gestion_de_paie.tbl_journalmaj definition

CREATE TABLE `tbl_journalmaj` (
  `journaldesmaj_id` int NOT NULL AUTO_INCREMENT,
  `journaldesmaj_table` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'Table qui a fait l''ojet de la modification',
  `journaldesmaj_champ` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'Elément modifié',
  `journaldesmaj_ancienne_valeur` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'Ancienne valeur de l''élément modifié',
  `journaldesmaj_nouvelle_valeur` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT 'Nouvelle valeur de l''élément modifié',
  `journaldesmaj_instant_de_modification` datetime NOT NULL COMMENT 'L''instant de la modification',
  `journaldesmaj_matricule` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`journaldesmaj_id`),
  KEY `tbl_journaldesmaj_FK` (`journaldesmaj_matricule`),
  CONSTRAINT `tbl_journaldesmaj_FK` FOREIGN KEY (`journaldesmaj_matricule`) REFERENCES `tbl_infoemploye` (`info_matricule`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



-- gestion_de_paie.tbl_fincontrat definition

CREATE TABLE `tbl_fincontrat` (
  `finContrat_id` int NOT NULL AUTO_INCREMENT,
  `finContrat_dateDebut` date NOT NULL,
  `finContrat_dateFin` date DEFAULT NULL,
  `finContrat_datePreavis` date DEFAULT NULL,
  `finContrat_emetteurPreavis` tinyint(1) DEFAULT '1' COMMENT 'Préavis emis par défaut par l''employeur',
  `finContrat_matricule` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`finContrat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Enregistrement des paramètres du contrat de chaque employé';




-- gestion_de_paie.informationemplofincontrat definition

CREATE TABLE `informationemplofincontrat` (
  `NomEmployé` varchar(25) DEFAULT NULL,
  `Prénom` varchar(50) DEFAULT NULL,
  `TéléphoneEmployé` varchar(20) DEFAULT NULL,
  `E-mail` varchar(50) DEFAULT NULL,
  `Date de naissance` datetime DEFAULT NULL,
  `Date d'embauche` datetime DEFAULT NULL,
  `DateDebut` datetime DEFAULT NULL,
  `DateFin` datetime DEFAULT NULL,
  `DatePreavis` datetime DEFAULT NULL,
  `EmetteurPreavis` varchar(25) DEFAULT NULL,
  `VariationSalaireNetDû` int DEFAULT NULL,
  `Date de paie` datetime DEFAULT NULL,
  `Salaire de base` double DEFAULT NULL,
  `Indemnité de logement` double DEFAULT NULL,
  `Indemnité de transport` double DEFAULT NULL,
  `Indemnité de fonction` double DEFAULT NULL,
  `Indemnité de sujétion` double DEFAULT NULL,
  `Indemnité de caisse` double DEFAULT NULL,
  `Autres indemnités` double DEFAULT NULL,
  `Allocation familliale` double DEFAULT NULL,
  `Autres primes` double DEFAULT NULL,
  `Avantages en nature` double DEFAULT NULL,
  `Montant heures supplémentaires` double DEFAULT NULL,
  `Avance et acompte` double DEFAULT NULL,
  `Opposition et saisie arrêt` double DEFAULT NULL,
  `Autres retenues` double DEFAULT NULL,
  `Charges familiales` smallint DEFAULT NULL,
  `Catégories` varchar(255) DEFAULT NULL,
  `Institution bancaire` varchar(255) DEFAULT NULL,
  `Numéro bancaire` varchar(255) DEFAULT NULL,
  `Service` varchar(255) DEFAULT NULL,
  `Fonction` varchar(255) DEFAULT NULL,
  `Matricule` varchar(255) DEFAULT NULL,
  `Numéro CNSS` varchar(255) DEFAULT NULL,
  `AssujettiTPA` bit(1) DEFAULT NULL,
  `Moyenne des salaires nets des six derniers mois` int DEFAULT NULL,
  `Sigle employeur` varchar(50) DEFAULT NULL,
  `TauxSalaireJournalier` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



-- gestion_de_paie.salairebaseheure definition

CREATE TABLE `salairebaseheure` (
  `ID` int DEFAULT NULL,
  `Téléphone` double DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  `Taux horaire normale` double DEFAULT NULL,
  `Nombre d'heures normales semaine 1` double DEFAULT NULL,
  `Nombre d'heures normales semaine 2` double DEFAULT NULL,
  `Nombre d'heures normales semaine 3` double DEFAULT NULL,
  `Nombre d'heures normales semaine 4` double DEFAULT NULL,
  `Nombre d'heures de nuit pendant les jours ouvrés 1` double DEFAULT NULL,
  `Nombre d'heures de nuit pendant les jours ouvrés 2` double DEFAULT NULL,
  `Nombre d'heures de nuit pendant les jours ouvrés 3` double DEFAULT NULL,
  `Nombre d'heures de nuit pendant les jours ouvrés 4` double DEFAULT NULL,
  `Nombre d'heures de jour pendant les jours non ouvrés 1` double DEFAULT NULL,
  `Nombre d'heures de jour pendant les jours non ouvrés 2` double DEFAULT NULL,
  `Nombre d'heures de jour pendant les jours non ouvrés 3` double DEFAULT NULL,
  `Nombre d'heures de jour pendant les jours non ouvrés 4` double DEFAULT NULL,
  `Nombre d'heures de nuit pendant les jours non ouvrés 1` double DEFAULT NULL,
  `Nombre d'heures de nuit pendant les jours non ouvrés 2` double DEFAULT NULL,
  `Nombre d'heures de nuit pendant les jours non ouvrés 3` double DEFAULT NULL,
  `Nombre d'heures de nuit pendant les jours non ouvrés 4` double DEFAULT NULL,
  `Montant pour heures normales S1 Sup0` double DEFAULT NULL,
  `Montant pour heures normales S1 Sup1` double DEFAULT NULL,
  `Montant pour heures normales S1 Sup2` double DEFAULT NULL,
  `Montant pour heures normales S1` double DEFAULT NULL,
  `Montant pour heures normales S2 Sup0` double DEFAULT NULL,
  `Montant pour heures normales S2 Sup1` double DEFAULT NULL,
  `Montant pour heures normales S2 Sup2` double DEFAULT NULL,
  `Montant pour heures normales S2` double DEFAULT NULL,
  `Montant pour heures normales S3 Sup0` double DEFAULT NULL,
  `Montant pour heures normales S3 Sup1` double DEFAULT NULL,
  `Montant pour heures normales S3 Sup2` double DEFAULT NULL,
  `Montant pour heures normales S3` double DEFAULT NULL,
  `Montant pour heures normales S4 Sup0` double DEFAULT NULL,
  `Montant pour heures normales S4 Sup1` double DEFAULT NULL,
  `Montant pour heures normales S4 Sup2` double DEFAULT NULL,
  `Montant pour heures normales S4` double DEFAULT NULL,
  `Montant pour heures normales` double DEFAULT NULL,
  `Montant supplémentaire pour heures normales S1 Sup1` double DEFAULT NULL,
  `Montant supplémentaire pour heures normales S1 Sup2` double DEFAULT NULL,
  `Montant supplémentaire pour heures normales S2 Sup1` double DEFAULT NULL,
  `Montant supplémentaire pour heures normales S2 Sup2` double DEFAULT NULL,
  `Montant supplémentaire pour heures normales S3 Sup1` double DEFAULT NULL,
  `Montant supplémentaire pour heures normales S3 Sup2` double DEFAULT NULL,
  `Montant supplémentaire pour heures normales S4 Sup1` double DEFAULT NULL,
  `Montant supplémentaire pour heures normales S4 Sup2` double DEFAULT NULL,
  `Montant pour heures supplémentaires normales` double DEFAULT NULL,
  `Montant pour heures supplémentaires non ouvrées` double DEFAULT NULL,
  `Montant total pour heures supplémentaires` double DEFAULT NULL,
  `Salaire de base` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


