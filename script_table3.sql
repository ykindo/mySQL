 CREATE DATABASE `gestion_de_paie` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

-- gestion_de_paie.tbl_info_employe definition

CREATE TABLE `tbl_info_employe` (
  `info_nom` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_prenom` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_telephone` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_email` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_dateNaissance` date DEFAULT NULL,
  `info_dateEmbaucge` date DEFAULT NULL,
  `info_datePaie` date DEFAULT NULL,
  `info_salaireBase` float DEFAULT NULL,
  `info_chargeFamilial` int DEFAULT NULL,
  `info_categorie` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_institutionBancaire` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_numeroCompteBancaire` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_service` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_fonction` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_matricule` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `info_numeroCNSS` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_ifuEmployeur` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `info_sigleEmployeur` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`info_matricule`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- gestion_de_paie.tbl_refemployeur definition

CREATE TABLE `tbl_refemployeur` (
  `refEmp_raison_sociale` varchar(100) NOT NULL COMMENT 'La raison sociale',
  `refEmp_sigle` varchar(50) NOT NULL,
  `refEmp_tel` varchar(20) NOT NULL,
  `refEmp_site_internet` varchar(50) DEFAULT NULL,
  `refEmp_email` varchar(50) DEFAULT NULL,
  `refEmp_code_postal` varchar(50) DEFAULT NULL,
  `refEmp_registre_commerce` varchar(30) NOT NULL,
  `refEmp_num_IFU` varchar(100) NOT NULL,
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
  `refEmp_assujeti_PTA` tinyint(1) NOT NULL DEFAULT '0',
  `refEmp_logo` mediumblob,
  PRIMARY KEY (`refEmp_sigle`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Les informations de la structure employeur';

-- gestion_de_paie.tbl_parametre_contrat definition

CREATE TABLE `tbl_parametre_contrat` (
  `paramContrat_id` int NOT NULL AUTO_INCREMENT,
  `paramContrat_matricule` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `paramContrat_date_debut` date NOT NULL,
  `paramContrat_date_fin` date DEFAULT NULL,
  `paramContrat_date_preavis` date DEFAULT NULL,
  `paramContrat_emetteur_preavis` tinyint(1) DEFAULT '1' COMMENT 'Préavis emis par défaut par l''employeur',
  PRIMARY KEY (`paramContrat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Enregistrement des paramètres du contrat de chaque employé';