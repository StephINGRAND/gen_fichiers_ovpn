# gen_fichiers_ovpn
 Générateur de fichiers clients .ovpn en masse


Ce script permet de generer en masse des fichiers .ovpn pour un deploiement en urgence de connexions vpn.



Prerequis:

Les certificats sur le serveur OpenVpn doivent etre generes avec l'option nopass. Le fichier ta.key doit rester a son emplacement d'origine dans /etc/openvpn.

Le script doit etre place dans le dossier easy-rsa avec le fichier modele client.template.

Ce script ne fonctionne qu'avec python 3.

Dans le fichier de configuration du serveur, la compression lzo doit etre activee.



Fonctionnement:

1. Lancer le script via la commande:

python3 generateur_ovpn.py


2. Repondre aux differentes questions.

3. Un fichier names.csv contenant toutes les informations sera genere automatiquement puis les variables du client.template seront remplacees par les valeurs contenues dans ce fichier.

4. Dans le dossier easy-rsa, vous trouverez autant de fichiers clientxxx.ovpn que demande.

5. Il suffira ensuite de distribuer vos fichiers de configuration .ovpn a chaque personne de votre entreprise en respectant les mesures de securite et de confidentialite, le fichier de configuration etant confidentiel et unique pour chaque personne.

6. Ce fichier doit �tre copie dans le dossier config de votre client OpenVpn. Une fois copie, il n'y a plus qu'e lancer la connexion.

