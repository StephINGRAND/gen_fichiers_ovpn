#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv
from datetime import datetime

def gen_fichier_csv():
    

    nom_admin = input("Quel est le nom de l'administrateur qui génère ce fichier de configuration ? ")
    ip_serveur = input("Quelle est l'adresse IP du serveur OpenVpn ? ")
    port_serveur = input("Quel est le port d'écoute du serveur OpenVpn ? ")
    nbre_clients = int(input("Quel est le nombre de fichiers OVPN clients à générer ? "))
    
    certif1 = open('pki/ca.crt','r')
    ca_crt = certif1.read()
    certif2 = open('/etc/openvpn/ta.key', 'r')
    ta_key = certif2.read()

    print("\n", "Nom de l'admin : " + nom_admin, "\n", "Adresse IP du serveur : " + ip_serveur, "\n", "Port du serveur : " + port_serveur, "\n", "Nombre de clients : " + str(nbre_clients), "\n")

    reponse_question = input("Est-ce exact ? O / N : ")

    if reponse_question == str("O") or reponse_question == str("o"):
        date = str(datetime.now())
        with open('names.csv', 'w') as csvfile:
            fieldnames = ['Nom', '<la_date>', '<admin_sys>', '<votre_identifiant_vpn>', '<serveur_vpn>', '<port_srv>', '<ca_cert>', '<cert_cert>', '<private_key>', '<ta_key>']
            csv2file = csv.DictWriter(csvfile, delimiter=',', fieldnames=fieldnames)
            csv2file.writeheader()
                

            for i in range(1, (nbre_clients+1)):
                os.system(r'./easyrsa build-client-full client%s nopass'%(i))
                certif3 = open('pki/issued/client%s.crt'%(i), 'r')
                cert_crt = certif3.read()
                certif4 = open('pki/private/client%s.key'%(i), 'r')
                prv_key = certif4.read()
                csv2file.writerow({'Nom' : 'client%s'%(i), '<la_date>' : date, '<admin_sys>' : nom_admin, '<votre_identifiant_vpn>' : 'client%s'%(i), '<serveur_vpn>' : ip_serveur, '<port_srv>' : port_serveur, '<ca_cert>' : ca_crt, '<cert_cert>' : cert_crt, '<private_key>' : prv_key, '<ta_key>' : ta_key})
            

        certif1.close()
        certif2.close()
        certif3.close()
        certif4.close()




    
    
    elif reponse_question == str("N") or reponse_question == str("n"):
        gen_fichier_csv()




def gen_fichier_ovpn():
        


    with open("names.csv") as csvfile:

      
        reader = csv.DictReader(csvfile, delimiter=',')


        for row in reader:
            dico = row
            
            with open("client.template", "r") as fichier1, open("{}.ovpn".format(row['Nom']), "w") as fichier2:
                texte = fichier1.read()
                for var1 in dico:
                    texte = texte.replace(var1, dico[var1])
                fichier2.write(texte)
                fichier2.close
                fichier1.close

    csvfile.close
    
gen_fichier_csv()
gen_fichier_ovpn()
