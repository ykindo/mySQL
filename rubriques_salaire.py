from datetime import date, time, datetime
import connection_bd_mysql


class CalculRubriquesSalaire:

    def __init__(self, info_matricule, info_nom="", info_prenom="", info_telephone="", info_email="",
                 info_dateNaissance="",
                 info_dateEmbauche=date.today(), info_datePaie=date.today(), info_salaireBase=0.0,
                 info_indemniteLogement=0.0,
                 info_indemniteFonction=0.0,
                 info_indemniteTransport=0.0, info_indemniteSujetion=0.0, info_indemniteTechnicite=0.0,
                 info_indemniteCaisse=0.0,
                 info_indemniteAutres=0.0, info_autresPrimes=0.0, info_avantagesNatureImmobilisation=0.0,
                 info_avantagesNatureEmploye=0.0, info_allocationFamilliale=0.0, info_montantHeuresSupplementaires=0.0,
                 info_avanceAcompte=0.0, info_oppositionSaisieArret=0.0, info_autresRetenues=0.0, info_chargeFamilial=0,
                 info_typeAbatementCadre=0, info_categorie="", info_institutionBancaire="",
                 info_numeroCompteBancaire="", info_service="", info_fonction="", info_numeroCNSS="",
                 info_ifuEmployeur="", refEmp_assujeti_PTA = 1, grilleSalaire_salaire_base= 0.0):
        self.info_matricule = info_matricule
        self.info_nom = info_nom
        self.info_prenom = info_prenom
        self.info_telephone = info_telephone
        self.info_email = info_email
        self.info_dateNaissance = info_dateNaissance
        self.info_dateEmbauche = info_dateEmbauche
        self.info_datePaie = info_datePaie
        self.grilleSalaire_salaire_base = grilleSalaire_salaire_base
        self.info_salaireBase = info_salaireBase
        if self.grilleSalaire_salaire_base == 0:
            self.info_salaireBase = info_salaireBase
        else:
            self.info_salaireBase = grilleSalaire_salaire_base
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
        self.info_typeAbatementCadre = info_typeAbatementCadre
        self.info_categorie = info_categorie
        self.info_institutionBancaire = info_institutionBancaire
        self.info_numeroCompteBancaire = info_numeroCompteBancaire
        self.info_service = info_service
        self.info_fonction = info_fonction
        self.info_numeroCNSS = info_numeroCNSS
        self.info_ifuEmployeur = info_ifuEmployeur
        self.refEmp_assujeti_PTA = refEmp_assujeti_PTA

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
        return min(75000.0, self.info_indemniteLogement, 0.2 * self.salaire_de_base_brut_imposable())

    def exoneration_fonction(self):
        return min(50000.0, self.info_indemniteFonction, 0.05 * self.salaire_de_base_brut_imposable())

    def exoneration_transport(self):
        return min(30000.0, self.info_indemniteTransport, 0.05 * self.salaire_de_base_brut_imposable())

    def exoneration_total(self):
        return int((self.exoneration_logement() + self.exoneration_fonction() + self.exoneration_transport()) / 10) * 10

    def abattement_forfaitaire(self):
        if self.info_typeAbatementCadre == 1:
            return 0.2 * self.info_salaireBase
        else:
            return 0.25 * self.info_salaireBase

    def salaire_base_imposable(self):
        return int((self.salaire_de_base_brut_imposable() - self.exoneration_total() - self.abattement_forfaitaire()) / 100) * 100

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
        if self.refEmp_assujeti_PTA == 1:
            return 0.03 * self.salaire_de_base_brut_imposable()
        else:
            return 0

    def total_retenues(self):
        return self.iuts_net() + self.cnss_employe() + self.info_oppositionSaisieArret + self.info_autresRetenues

    def salaire_a_payer(self):
        return int(
            self.salaire_brut_en_numeraire() - self.total_retenues() + self.info_allocationFamilliale) + self.info_avanceAcompte

    def charge_salariale_totale(self):
        return self.salaire_brut_en_numeraire() + self.cnss_employeur() + self.tpa() + self.info_allocationFamilliale


for i in connection_bd_mysql.employes_data:
    employe_calculate_data_dev = {
        "matricule": CalculRubriquesSalaire(*i).info_matricule,
        "nom": CalculRubriquesSalaire(*i).info_nom,
        "prenom": CalculRubriquesSalaire(*i).info_prenom,
        "telephone": CalculRubriquesSalaire(*i).info_telephone,
        "email": CalculRubriquesSalaire(*i).info_email,
        "dateNaissance": CalculRubriquesSalaire(*i).info_dateNaissance,
        "dateEmbauche": CalculRubriquesSalaire(*i).info_dateEmbauche,
        "datePaie": CalculRubriquesSalaire(*i).info_datePaie,
        "salaireBase": CalculRubriquesSalaire(*i).info_salaireBase,
        "indemniteLogement": CalculRubriquesSalaire(*i).info_indemniteLogement,
        "indemniteFonction": CalculRubriquesSalaire(*i).info_indemniteFonction,
        "indemniteTransport": CalculRubriquesSalaire(*i).info_indemniteTransport,
        "indemniteSujetion": CalculRubriquesSalaire(*i).info_indemniteSujetion,
        "indemniteTechnicite": CalculRubriquesSalaire(*i).info_indemniteTechnicite,
        "indemniteCaisse": CalculRubriquesSalaire(*i).info_indemniteCaisse,
        "indemniteAutres": CalculRubriquesSalaire(*i).info_indemniteAutres,
        "autresPrimes": CalculRubriquesSalaire(*i).info_autresPrimes,
        "avantagesNatureImmobilisation": CalculRubriquesSalaire(*i).info_avantagesNatureImmobilisation,
        "avantagesNatureEmploye": CalculRubriquesSalaire(*i).info_avantagesNatureEmploye,
        "allocationFamilliale": CalculRubriquesSalaire(*i).info_allocationFamilliale,
        "montantHeuresSupplementaires": CalculRubriquesSalaire(*i).info_montantHeuresSupplementaires,
        "avanceAcompte": CalculRubriquesSalaire(*i).info_avanceAcompte,
        "oppositionSaisieArret": CalculRubriquesSalaire(*i).info_oppositionSaisieArret,
        "autresRetenues": CalculRubriquesSalaire(*i).info_autresRetenues,
        "chargeFamilial": CalculRubriquesSalaire(*i).info_chargeFamilial,
        "typeAbatementCadre": CalculRubriquesSalaire(*i).info_typeAbatementCadre,
        "categorie": CalculRubriquesSalaire(*i).info_categorie,
        "institutionBancaire": CalculRubriquesSalaire(*i).info_institutionBancaire,
        "numeroCompteBancaire": CalculRubriquesSalaire(*i).info_numeroCompteBancaire,
        "service": CalculRubriquesSalaire(*i).info_service,
        "fonction": CalculRubriquesSalaire(*i).info_fonction,
        "numeroCNSS": CalculRubriquesSalaire(*i).info_numeroCNSS,
        "ifuEmployeur": CalculRubriquesSalaire(*i).info_ifuEmployeur,
        "prime_anciennete": CalculRubriquesSalaire(*i).prime_anciennete(),
        "salaire_brut_en_numeraire": CalculRubriquesSalaire(*i).salaire_brut_en_numeraire(),
        "taux_avantage_en_nature": CalculRubriquesSalaire(*i).taux_avantage_en_nature(),
        "salaire_brut_total": CalculRubriquesSalaire(*i).salaire_brut_total(),
        "cnss_employe": CalculRubriquesSalaire(*i).cnss_employe(),
        "salaire_de_base_brut_imposable": CalculRubriquesSalaire(*i).salaire_de_base_brut_imposable(),
        "exoneration_logement": CalculRubriquesSalaire(*i).exoneration_logement(),
        "exoneration_fonction": CalculRubriquesSalaire(*i).exoneration_fonction(),
        "exoneration_transport": CalculRubriquesSalaire(*i).exoneration_transport(),
        "exoneration_total": CalculRubriquesSalaire(*i).exoneration_total(),
        "abattement_forfaitaire": CalculRubriquesSalaire(*i).abattement_forfaitaire(),
        "salaire_base_imposable": CalculRubriquesSalaire(*i).salaire_base_imposable(),
        "iuts_brut": CalculRubriquesSalaire(*i).iuts_brut(),
        "abattement_sur_charges_familliales": CalculRubriquesSalaire(*i).abattement_sur_charges_familliales(),
        "iuts_net": CalculRubriquesSalaire(*i).iuts_net(),
        "cnss_employeur": CalculRubriquesSalaire(*i).cnss_employeur(),
        "tpa": CalculRubriquesSalaire(*i).tpa(),
        "total_retenues": CalculRubriquesSalaire(*i).total_retenues(),
        "salaire_a_payer": CalculRubriquesSalaire(*i).salaire_a_payer(),
        "charge_salariale_totale": CalculRubriquesSalaire(*i).charge_salariale_totale()
    }

    employe_calculate_data = {
        "Matricule": CalculRubriquesSalaire(*i).info_matricule,
        "Nom": CalculRubriquesSalaire(*i).info_nom,
        "Prénom": CalculRubriquesSalaire(*i).info_prenom,
        "Téléphone": CalculRubriquesSalaire(*i).info_telephone,
        "Email": CalculRubriquesSalaire(*i).info_email,
        "Date de naissance": CalculRubriquesSalaire(*i).info_dateNaissance,
        "Date embauche": CalculRubriquesSalaire(*i).info_dateEmbauche,
        "Date paie": CalculRubriquesSalaire(*i).info_datePaie,
        "Salaire de base": CalculRubriquesSalaire(*i).info_salaireBase,
        "Indemnité de logement": CalculRubriquesSalaire(*i).info_indemniteLogement,
        "Indemnité de fonction": CalculRubriquesSalaire(*i).info_indemniteFonction,
        "Indemnité de transport": CalculRubriquesSalaire(*i).info_indemniteTransport,
        "Indemnité de sujétion": CalculRubriquesSalaire(*i).info_indemniteSujetion,
        "Indemnité de technicité": CalculRubriquesSalaire(*i).info_indemniteTechnicite,
        "Indemnité de caisse": CalculRubriquesSalaire(*i).info_indemniteCaisse,
        "Autre indemnité": CalculRubriquesSalaire(*i).info_indemniteAutres,
        "Autre Prime": CalculRubriquesSalaire(*i).info_autresPrimes,
        "Avantages en nature - immobilisation": CalculRubriquesSalaire(*i).info_avantagesNatureImmobilisation,
        "Avantages en nature - employé": CalculRubriquesSalaire(*i).info_avantagesNatureEmploye,
        "Allocation familliale": CalculRubriquesSalaire(*i).info_allocationFamilliale,
        "Montant heures supplémentaires": CalculRubriquesSalaire(*i).info_montantHeuresSupplementaires,
        "Avance et Acompte": CalculRubriquesSalaire(*i).info_avanceAcompte,
        "Opposition et saisie arret": CalculRubriquesSalaire(*i).info_oppositionSaisieArret,
        "Autres retenues": CalculRubriquesSalaire(*i).info_autresRetenues,
        "Charges familliales": CalculRubriquesSalaire(*i).info_chargeFamilial,
        "Type abattement cadre": CalculRubriquesSalaire(*i).info_typeAbatementCadre,
        "Catégorie": CalculRubriquesSalaire(*i).info_categorie,
        "Institution financière": CalculRubriquesSalaire(*i).info_institutionBancaire,
        "Numéro de compte bancaire": CalculRubriquesSalaire(*i).info_numeroCompteBancaire,
        "Service": CalculRubriquesSalaire(*i).info_service,
        "Fonction": CalculRubriquesSalaire(*i).info_fonction,
        "Numéro CNSS": CalculRubriquesSalaire(*i).info_numeroCNSS,
        "ITU employeur": CalculRubriquesSalaire(*i).info_ifuEmployeur,
        "Prime ancienneté": CalculRubriquesSalaire(*i).prime_anciennete(),
        "Salaire brut en numéraire": CalculRubriquesSalaire(*i).salaire_brut_en_numeraire(),
        "Taux avantage en nature": CalculRubriquesSalaire(*i).taux_avantage_en_nature(),
        "Salaire brut total": CalculRubriquesSalaire(*i).salaire_brut_total(),
        "CNSS employé": CalculRubriquesSalaire(*i).cnss_employe(),
        "Salaire de base brut imposable": CalculRubriquesSalaire(*i).salaire_de_base_brut_imposable(),
        "Exonération sur indemnité de logement": CalculRubriquesSalaire(*i).exoneration_logement(),
        "Exonération sur indemnité de fonction": CalculRubriquesSalaire(*i).exoneration_fonction(),
        "Exonération sur indemnité de transport": CalculRubriquesSalaire(*i).exoneration_transport(),
        "Exonération total": CalculRubriquesSalaire(*i).exoneration_total(),
        "Abattement forfaitaire": CalculRubriquesSalaire(*i).abattement_forfaitaire(),
        "Salaire base imposable": CalculRubriquesSalaire(*i).salaire_base_imposable(),
        "IUTS brut": CalculRubriquesSalaire(*i).iuts_brut(),
        "Abattement sur charges familliales": CalculRubriquesSalaire(*i).abattement_sur_charges_familliales(),
        "IUTS net": CalculRubriquesSalaire(*i).iuts_net(),
        "CNSS employeur": CalculRubriquesSalaire(*i).cnss_employeur(),
        "Taxe Patronale Apprentissage": CalculRubriquesSalaire(*i).tpa(),
        "Total des retenues": CalculRubriquesSalaire(*i).total_retenues(),
        "Salaire à payer": CalculRubriquesSalaire(*i).salaire_a_payer(),
        "Charge salariale totale": CalculRubriquesSalaire(*i).charge_salariale_totale(),
    }

    # print(employe_calculate_data_dev)

    print(employe_calculate_data)
