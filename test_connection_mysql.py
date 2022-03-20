import mysql.connector
from mysql.connector import errorcode
"""
param_connection = {
    "host": "localhost", "user": "Soungalo", "password": "", "database": "gestionformation"
}
db_gestion_formation = mysql.connector.connect(**param_connection)
cursor = db_gestion_formation.cursor()
# cursor.execute("UPDATE tblsessionformation SET `sesFor_Continent` = 'Afrique'")
cursor.execute("SELECT * FROM tblsessionformation")
print(cursor.fetchall())
# for row in cursor:
#     print(row)

# db_gestion_formation.commit()

db_gestion_formation.close()
"""


dict_parametre = {"user": "Soungalo", "host": "localhost", "password": "", "database": "gestion_de_paie"}
connection = mysql.connector.connect(**dict_parametre)
cursor = connection.cursor()
# fin_de_contrat = ("245 264 A", "2021-12-31", "2025-12-31", "2025-08-31", 1)
# cursor.execute("""INSERT INTO tbl_fincontrat (finContrat_matricule, finContrat_date_debut, finContrat_date_fin, finContrat_date_preavis, finContrat_emetteur_preavis)
# VALUES(%s,%s,%s,%s,%s)""", fin_de_contrat)
#
# connection.commit()

cursor.execute("select * from tbl_fincontrat")
for ligne in cursor:
    print(ligne)
connection.close()

