#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import csv

def demande():
    
    nbre_clients = input("Quel est le nombre de certificats clients à générer ? ")

    print(nbre_clients)

    Reponse = input("Est-ce exact ? 1 oui / 2 non : ")
    
    print(Reponse)
    
    if Reponse == 1:
        for i in range(1, (nbre_clients+1)):
            print(i)
            os.system(r'./easyrsa build-client-full cle%s nopass'%(i))
            with open('names.csv', 'w') as csvfile, open("/pki/issued/cle%s"%(i), 'r') as cle:
		texte = cle.read()
            	fieldnames = ['Nom', 'Prenom', '<prv_key>']
    		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
    		writer.writerow({'Nom': 'Baked', 'Prenom': 'Beans', '<prv_key>' : prv})

    
    
 
  

    elif Reponse == 2:
        demande()

demande()
