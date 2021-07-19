#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
from datetime import datetime

def gen_fichier_csv():

# questions utiles pour générer remplir le fichier .csv
    

    nom_admin = input("Quel est le nom de l'administrateur qui génère ce fichier de configuration ? ")
    ip_serveur = input("Quelle est l'adresse IP du serveur OpenVpn ? ")
    port_serveur = input("Quel est le port d'écoute du serveur OpenVpn ? ")
    nbre_clients = int(input("Quel est le nombre de fichiers OVPN clients à générer ? "))
    
# lecture des fichiers ca.crt et ta.key

    certif1 = open('pki/ca.crt','r')
    ca_crt = certif1.read()
    certif2 = open('/etc/openvpn/ta.key', 'r')
    ta_key = certif2.read()


# récapitulatif des infos saisies

    print("\n", "Nom de l'admin : " + nom_admin, "\n", "Adresse IP du serveur : " + ip_serveur, "\n", "Port du serveur : " + port_serveur, "\n", "Nombre de clients : " + str(nbre_clients), "\n")

    reponse_question = input("Est-ce exact ? O / N : ")

# si O ou o on continue le script

    if reponse_question == str("O") or reponse_question == str("o"):

# mise en mémoire de la date et l'heure

        date = str(datetime.now())

# écriture des en-têtes dans le fichier names.csv

        with open('names.csv', 'w') as csvfile:
            fieldnames = ['Nom', '<la_date>', '<admin_sys>', '<votre_identifiant_vpn>', '<serveur_vpn>', '<port_srv>', '<ca_cert>', '<cert_cert>', '<private_key>', '<ta_key>']
            csv2file = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
            csv2file.writeheader()
                
# boucle for qui va remplir le fichier names.csv avec toutes les bonnes infos pour chaque client

            for i in range(1, (nbre_clients+1)):
                os.system(r'./easyrsa build-client-full client%s nopass'%(i))
                certif3 = open('pki/issued/client%s.crt'%(i), 'r')
                cert_crt = certif3.read()
                certif4 = open('pki/private/client%s.key'%(i), 'r')
                prv_key = certif4.read()
                csv2file.writerow({'Nom' : 'client%s'%(i), '<la_date>' : date, '<admin_sys>' : nom_admin, '<votre_identifiant_vpn>' : 'client%s'%(i), '<serveur_vpn>' : ip_serveur, '<port_srv>' : port_serveur, '<ca_cert>' : ca_crt, '<cert_cert>' : cert_crt, '<private_key>' : prv_key, '<ta_key>' : ta_key})
            
# fermeture des fichiers ouverts

        certif1.close()
        certif2.close()
        certif3.close()
        certif4.close()




# si N ou n, on repart au début du script et on répond de nouveau aux questions    
    
    elif reponse_question == str("N") or reponse_question == str("n"):
        gen_fichier_csv()




def gen_fichier_ovpn():
        

# ouverture du fichier names.csv

    with open("names.csv") as csvfile:

# lecture du fichier names.csv comme un dictionnaire

        reader = csv.DictReader(csvfile, delimiter=',')

# boucle for pour remplacer les variables du fichier client.template par les valeurs du fichier names.csv

        for row in reader:
            dico = row
            
            with open("client.template", "r") as fichier1, open("{}.ovpn".format(row['Nom']), "w") as fichier2:
                texte = fichier1.read()
                for var1 in dico:
                    texte = texte.replace(var1, dico[var1])
                fichier2.write(texte)
                fichier2.close
                fichier1.close

# fermeture du fichier

    csvfile.close
    

# execution des fontions

gen_fichier_csv()
gen_fichier_ovpn()
