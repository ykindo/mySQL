import datetime


class CalculRubriquesSalaire:

    def __init__(self, info_matricule, info_nom="", info_prenom="", info_telephone="", info_email="",
                 info_dateNaissance="",
                 info_dateEmbauche=datetime, info_datePaie=datetime, info_salaireBase=.0, info_indemniteLogement=.0,
                 info_indemniteFonction=.0,
                 info_indemniteTransport=.0, info_indemniteSujetion=.0, info_indemniteTechnicite=.0,
                 info_indemniteCaisse=.0,
                 info_indemniteAutres=.0, info_autresPrimes=.0, info_avantagesNatureImmobilisation=.0,
                 info_avantagesNatureEmploye=.0, info_allocationFamilliale=.0, info_montantHeuresSupplementaires=.0,
                 info_avanceAcompte=.0, info_oppositionSaisieArret=.0, info_autresRetenues=.0, info_chargeFamilial=0,
                 info_categorie="Cadre", info_institutionBancaire="", info_numeroCompteBancaire="", info_service="",
                 info_fonction="",
                 info_numeroCNSS="", info_ifuEmployeur=""):
        self.info_matricule = info_matricule
        self.info_nom = info_nom
        self.info_prenom = info_prenom
        self.info_telephone = info_telephone
        self.info_email = info_email
        self.info_dateNaissance = info_dateNaissance
        self.info_dateEmbauche = info_dateEmbauche
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
        if int((self.info_datePaie - self.info_dateEmbauche).days / 365.25) >= 3:
            return (0.05 + (int((
                                            self.info_datePaie - self.info_dateEmbauche).days / 365.25) - 3) * 0.01) * self.info_salaireBase
        else:
            return 0

    def salaire_brut_en_numeraire(self):
        return self.info_salaireBase + self.info_indemniteLogement + self.info_indemniteFonction + self.info_indemniteTransport + self.prime_anciennete() + self.info_indemniteSujetion + self.info_indemniteTechnicite + self.info_indemniteCaisse + self.info_indemniteAutres + self.info_autresPrimes + self.info_montantHeuresSupplementaires

    def taux_avantage_en_nature(self):
        return self.info_avantagesNatureImmobilisation / 240 + (1 + 0.03 + 0.16) * self.info_avantagesNatureEmploye

    def salaire_brut_total(self):
        return self.salaire_brut_en_numeraire() + self.taux_avantage_en_nature()

    def cnss_employe(self):
        return min(600000 * 0.055, self.salaire_brut_en_numeraire() * 0.055)

    def salaire_de_base_brut_imposable(self):
        return self.salaire_brut_total() - min(self.cnss_employe(), 0.08 * self.info_salaireBase)

    def exoneration_logement(self):
        return min(75000, self.info_indemniteLogement, 0.2 * self.salaire_de_base_brut_imposable())

    def exoneration_fonction(self):
        return min(50000, self.info_indemniteFonction, 0.05 * self.salaire_de_base_brut_imposable())

    def exoneration_transport(self):
        return min(30000, self.info_indemniteTransport, 0.05 * self.salaire_de_base_brut_imposable())

    def exoneration_total(self):
        return int((self.exoneration_logement() + self.exoneration_fonction() + self.exoneration_transport()) / 10) * 10

    def abattement_forfaitaire(self):
        if self.info_categorie == "Cadre":
            return 0.2 * self.info_salaireBase
        else:
            return 0.25 * self.info_salaireBase

    def salaire_base_imposable(self):
        return int((
                               self.salaire_de_base_brut_imposable() - self.exoneration_total() - self.abattement_forfaitaire()) / 100) * 100

    def iuts_brut(self):
        if 30000 <= self.salaire_base_imposable() < 50000:
            return (self.salaire_base_imposable() - 30000) * 0.121
        elif 50000 <= self.salaire_base_imposable() < 80000:
            return (50000 - 30000) * 0.121 + (self.salaire_base_imposable() - 50000) * 0.139
        elif 80000 <= self.salaire_base_imposable() < 120000:
            return (50000 - 30000) * 0.121 + (80000 - 50000) * 0.139 + (self.salaire_base_imposable() - 80000) * 0.157
        elif 120000 <= self.salaire_base_imposable() < 170000:
            return (50000 - 30000) * 0.121 + (80000 - 50000) * 0.139 + (120000 - 80000) * 0.157 + (
                    self.salaire_base_imposable() - 120000) * 0.184
        elif 170000 <= self.salaire_base_imposable() < 250000:
            return (50000 - 30000) * 0.121 + (80000 - 50000) * 0.139 + (120000 - 80000) * 0.157 + (
                    170000 - 120000) * 0.184 + (self.salaire_base_imposable() - 170000) * 0.217
        elif 250000 <= self.salaire_base_imposable():
            return (50000 - 30000) * 0.121 + (80000 - 50000) * 0.139 + (120000 - 80000) * 0.157 + (
                    170000 - 120000) * 0.184 + (250000 - 170000) * 0.217 + (
                           self.salaire_base_imposable() - 250000) * 0.25
        else:
            return 0

    def abattement_sur_charges_familliales(self):

        if self.info_chargeFamilial == 1:
            return self.iuts_brut() * 0.08
        elif self.info_chargeFamilial == 2:
            return self.iuts_brut() * 0.1
        elif self.info_chargeFamilial == 3:
            return self.iuts_brut() * 0.12
        elif self.info_chargeFamilial >= 4:
            return self.iuts_brut() * 0.14
        else:  # self.info_chargeFamilial == 0:
            return 0

    def iuts_net(self):
        return int(self.iuts_brut() - self.abattement_sur_charges_familliales())

    def cnss_employeur(self):
        return 0.16 * self.salaire_brut_en_numeraire()

    def tpa(self):
        return 0.03 * self.salaire_de_base_brut_imposable()

    def total_retenues(self):
        return self.iuts_net() + self.cnss_employe() + self.info_oppositionSaisieArret + self.info_autresRetenues

    def salaire_a_payer(self):
        return int(
            self.salaire_brut_en_numeraire() - self.total_retenues() + self.info_allocationFamilliale) + self.info_avanceAcompte

    def charge_salariale_totale(self):
        return self.salaire_brut_en_numeraire() + self.cnss_employeur() + self.tpa() + self.info_allocationFamilliale


donnees = CalculRubriquesSalaire("ATTCV", "DISSA", "Soungalo", "70077641", "soungdis@yahoo.fr",
                                    datetime.date(1981, 12, 31), datetime.date(2013, 11, 1),
                                    datetime.date(2021, 12, 31),
                                    478132.72, 25000, 0, 0, 20000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, "Cadre", "SGBF",
                                    "12278894466654", "DSE", "SSE", "14565566659 W", "55665 R")

donnees1 = CalculRubriquesSalaire(info_matricule="ATTCV", info_dateNaissance=datetime.date(1981, 12, 31),
                                   info_dateEmbauche=datetime.date(2013, 11, 1),
                                   info_datePaie=datetime.date(2021, 12, 31),
                                   info_salaireBase=750000, info_indemniteSujetion=100000, info_indemniteLogement=80000,
                                   info_chargeFamilial=1, info_categorie="Cadre")

valeur_sortie_info_matricule = donnees.info_matricule
valeur_sortie_info_nom = donnees.info_nom
valeur_sortie_info_prenom = donnees.info_prenom
valeur_sortie_info_telephone = donnees.info_telephone
valeur_sortie_info_email = donnees.info_email
valeur_sortie_info_dateNaissance = donnees.info_dateNaissance
valeur_sortie_info_dateEmbauche = donnees.info_dateEmbauche
valeur_sortie_info_datePaie = donnees.info_datePaie
valeur_sortie_info_salaireBase = donnees.info_salaireBase
valeur_sortie_info_indemniteLogement = donnees.info_indemniteLogement
valeur_sortie_info_indemniteFonction = donnees.info_indemniteFonction
valeur_sortie_info_indemniteTransport = donnees.info_indemniteTransport
valeur_sortie_info_indemniteSujetion = donnees.info_indemniteSujetion
valeur_sortie_info_indemniteTechnicite = donnees.info_indemniteTechnicite
valeur_sortie_info_indemniteCaisse = donnees.info_indemniteCaisse
valeur_sortie_info_indemniteAutres = donnees.info_indemniteAutres
valeur_sortie_info_autresPrimes = donnees.info_autresPrimes
valeur_sortie_info_avantagesNatureImmobilisation = donnees.info_avantagesNatureImmobilisation
valeur_sortie_info_avantagesNatureEmploye = donnees.info_avantagesNatureEmploye
valeur_sortie_info_allocationFamilliale = donnees.info_allocationFamilliale
valeur_sortie_info_montantHeuresSupplementaires = donnees.info_montantHeuresSupplementaires
valeur_sortie_info_avanceAcompte = donnees.info_avanceAcompte
valeur_sortie_info_oppositionSaisieArret = donnees.info_oppositionSaisieArret
valeur_sortie_info_autresRetenues = donnees.info_autresRetenues
valeur_sortie_info_chargeFamilial = donnees.info_chargeFamilial
valeur_sortie_info_categorie = donnees.info_categorie
valeur_sortie_info_institutionBancaire = donnees.info_institutionBancaire
valeur_sortie_info_numeroCompteBancaire = donnees.info_numeroCompteBancaire
valeur_sortie_info_service = donnees.info_service
valeur_sortie_info_fonction = donnees.info_fonction
valeur_sortie_info_numeroCNSS = donnees.info_numeroCNSS
valeur_sortie_info_ifuEmployeur = donnees.info_ifuEmployeur
valeur_sortie_prime_anciennete = donnees.prime_anciennete()
valeur_sortie_salaire_brut_en_numeraire = donnees.salaire_brut_en_numeraire()
valeur_sortie_taux_avantage_en_nature = donnees.taux_avantage_en_nature()
valeur_sortie_salaire_brut_total = donnees.salaire_brut_total()
valeur_sortie_cnss_employe = donnees.cnss_employe()
valeur_sortie_salaire_de_base_brut_imposable = donnees.salaire_de_base_brut_imposable()
valeur_sortie_exoneration_logement = donnees.exoneration_logement()
valeur_sortie_exoneration_fonction = donnees.exoneration_fonction()
valeur_sortie_exoneration_transport = donnees.exoneration_transport()
valeur_sortie_exoneration_total = donnees.exoneration_total()
valeur_sortie_abattement_forfaitaire = donnees.abattement_forfaitaire()
valeur_sortie_salaire_base_imposable = donnees.salaire_base_imposable()
valeur_sortie_iuts_brut = donnees.iuts_brut()
valeur_sortie_abattement_sur_charges_familliales = donnees.abattement_sur_charges_familliales()
valeur_sortie_iuts_net = donnees.iuts_net()
valeur_sortie_cnss_employeur = donnees.cnss_employeur()
valeur_sortie_tpa = donnees.tpa()
valeur_sortie_total_retenues = donnees.total_retenues()
valeur_sortie_salaire_a_payer = donnees.salaire_a_payer()
valeur_sortie_charge_salariale_totale = donnees.charge_salariale_totale()

print(valeur_sortie_info_matricule, valeur_sortie_info_nom, valeur_sortie_info_prenom, valeur_sortie_info_telephone,
      valeur_sortie_info_email, valeur_sortie_info_dateNaissance, valeur_sortie_info_dateEmbauche,
      valeur_sortie_info_datePaie, valeur_sortie_info_salaireBase, valeur_sortie_info_indemniteLogement,
      valeur_sortie_info_indemniteFonction, valeur_sortie_info_indemniteTransport, valeur_sortie_info_indemniteSujetion,
      valeur_sortie_info_indemniteTechnicite, valeur_sortie_info_indemniteCaisse, valeur_sortie_info_indemniteAutres,
      valeur_sortie_info_autresPrimes, valeur_sortie_info_avantagesNatureImmobilisation,
      valeur_sortie_info_avantagesNatureEmploye, valeur_sortie_info_allocationFamilliale,
      valeur_sortie_info_montantHeuresSupplementaires, valeur_sortie_info_avanceAcompte,
      valeur_sortie_info_oppositionSaisieArret, valeur_sortie_info_autresRetenues, valeur_sortie_info_chargeFamilial,
      valeur_sortie_info_categorie, valeur_sortie_info_institutionBancaire, valeur_sortie_info_numeroCompteBancaire,
      valeur_sortie_info_service, valeur_sortie_info_fonction, valeur_sortie_info_numeroCNSS,
      valeur_sortie_info_ifuEmployeur, valeur_sortie_prime_anciennete, valeur_sortie_salaire_brut_en_numeraire,
      valeur_sortie_taux_avantage_en_nature, valeur_sortie_salaire_brut_total, valeur_sortie_cnss_employe,
      valeur_sortie_salaire_de_base_brut_imposable, valeur_sortie_exoneration_logement,
      valeur_sortie_exoneration_fonction, valeur_sortie_exoneration_transport, valeur_sortie_exoneration_total,
      valeur_sortie_abattement_forfaitaire, valeur_sortie_salaire_base_imposable, valeur_sortie_iuts_brut,
      valeur_sortie_abattement_sur_charges_familliales, valeur_sortie_iuts_net, valeur_sortie_cnss_employeur,
      valeur_sortie_tpa, valeur_sortie_total_retenues, valeur_sortie_salaire_a_payer,
      valeur_sortie_charge_salariale_totale)
