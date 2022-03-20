class Calcul_rubriques_salaire:

    def __init__(self, info_matricule, info_nom, info_prenom, info_telephone, info_email, info_dateNaissance,
                 info_dateEmbaucge, info_datePaie, info_salaireBase, info_indemniteLogement, info_indemniteFonction,
                 info_indemniteTransport, info_indemniteSujetion, info_indemniteTechnicite, info_indemniteCaisse,
                 info_indemniteAutres, info_autresPrimes, info_avantagesNatureImmobilisation,
                 info_avantagesNatureEmploye, info_allocationFamilliale, info_montantHeuresSupplementaires,
                 info_avanceAcompte, info_oppositionSaisieArret, info_autresRetenues, info_chargeFamilial,
                 info_categorie, info_institutionBancaire, info_numeroCompteBancaire, info_service, info_fonction,
                 info_numeroCNSS, info_ifuEmployeur):
        self.info_matricule = info_matricule
        self.info_nom = info_nom
        self.info_prenom = info_prenom
        self.info_telephone = info_telephone
        self.info_email = info_email
        self.info_dateNaissance = info_dateNaissance
        self.info_dateEmbaucge = info_dateEmbaucge
        self.info_datePaie = info_datePaie
        self.info_salaireBase = info_salaireBase
        self.info_indemniteLogement = info_indemniteLogement
        self.info_indemniteFonction = info_indemniteFonction
        self.info_indemniteTransport = info_indemniteTransport
        self.info_indemniteSujetion = info_indemniteSujetion
        self.info_indemniteTechnicite = info_indemniteTechnicite
        self.info_indemniteCaisse = info_indemniteCaisse
        self.info_indemniteAutres = info_indemniteAutres
        self.info_autresPrimes = info_autresPrimes
        self.info_avantagesNatureImmobilisation = info_avantagesNatureImmobilisation
        self.info_avantagesNatureEmploye = info_avantagesNatureEmploye
        self.info_allocationFamilliale = info_allocationFamilliale
        self.info_montantHeuresSupplementaires = info_montantHeuresSupplementaires
        self.info_avanceAcompte = info_avanceAcompte
        self.info_oppositionSaisieArret = info_oppositionSaisieArret
        self.info_autresRetenues = info_autresRetenues
        self.info_chargeFamilial = info_chargeFamilial
        self.info_categorie = info_categorie
        self.info_institutionBancaire = info_institutionBancaire
        self.info_numeroCompteBancaire = info_numeroCompteBancaire
        self.info_service = info_service
        self.info_fonction = info_fonction
        self.info_numeroCNSS = info_numeroCNSS
        self.info_ifuEmployeur = info_ifuEmployeur

    def prime_anciennete(self):
        pass

    def salaire_brut_en_numeraire(self):
        pass

    def taux_avantage_en_nature(self):
        pass

    def salaire_brut_total(self):
        pass

    def cnss_employe(self):
        pass

    def salaire_de_base_brut_imposable(self):
        pass

    def exoneration_logement(self):
        pass

    def exoneration_fonction(self):
        pass

    def exoneration_transport(self):
        pass

    def exoneration_total(self):
        pass

    def abattement_forfaitaire(self):
        pass

    def salaire_base_imposable(self):
        pass

    def iuts_brut(self):
        pass

    def abattement_sur_charges_familliales(self):
        pass

    def iuts_net(self):
        pass

    def cnss_employeur(self):
        pass

    def tpa(self):
        pass

    def total_retenues(self):
        pass

    def salaire_a_payer(self):
        pass

    def charge_salariale_totale(self):
        pass
