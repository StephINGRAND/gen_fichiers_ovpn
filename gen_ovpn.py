#/usr/bin/python

import csv

def questions():


# génération d'un dictionnaire à partir du fichier csv

    with open("names.csv") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            dico = row
            with open("client.template", "r") as fichier1, open("{}.ovpn".format(row['Nom']+row['Prenom']), "w") as fichier2:
                texte = fichier1.read()
                for var1 in dico:
                    texte = texte.replace(var1, dico[var1])
                fichier2.write(texte)
                fichier2.close
                   
    

    
    


# affectation des variables du dictionnaire
    

# lecture des fichiers contenants les données à mettre à jour

##    ca_crt = (open("ca_crt2", "r")).read()
##    client_crt = (open("client_crt2", "r")).read()
##    client_key = (open("client_key2", "r")).read()
##    ta_key = (open("ta_key2", "r")).read()
##    rsa_sign = (open("rsa_sign2", "r")).read()
##
### dictionnaire
##    dico = {"<serveur_vpn>" : IP_serveur, "<port_srv>" : Port_serveur, "<ca_cert>" : ca_crt, "<cert_cert>" : client_crt, "<private_key>" : client_key, "<ta_key>" : ta_key, "<rsa_sign>" : rsa_sign}
##
### récap des informations
##
##    print("\n", "Nom : " + Nom,"\n", "Prénom : " + Prenom, "\n", "Adresse IP du serveur : " + IP_serveur, "\n", "Port du serveur : " + Port_serveur, "\n")
##    Correct = input("Est-ce correct ? O/N : ")
##
### si Oui, j'ouvre mon fichier
##    if Correct == "O" or "o":
##        with open("client.template", "r") as fichier1, open("{}.ovpn".format(Nom+Prenom), "w") as fichier2:
##            texte = fichier1.read()
##
### boucle pour piocher dans mon dictionnaire et remplacer mes variables
##
##            for var1 in dico:
##                texte = texte.replace(var1, dico[var1])
##
### écriture dans mon fichier portant le nom+prénom de la personne
##
##            fichier2.write(texte)
##            fichier2.close

# si Non, on redemande les informations
##
##    elif Correct == "N" or "n":
##        questions()

    
            
questions()
