# gen_fichiers_ovpn
 Générateur de fichiers clients .ovpn en masse


Ce script permet de générer en masse des fichiers .ovpn pour un déploiement en urgence de connexions vpn vers un serveur OpenVpn.



## Préréquis:

Les certificats sur le serveur OpenVpn doivent être générés avec l'option nopass. Le fichier ta.key doit rester à son emplacement d'origine dans /etc/openvpn.

Le script doit être placé dans le dossier easy-rsa avec le fichier modèle client.template.

Ce script ne fonctionne qu'avec python 3.

Dans le fichier de configuration du serveur, la compression lzo doit être activée.



## Fonctionnement:

1. Lancer le script via la commande:

```
python3 generateur_ovpn.py
```

2. Répondre aux différentes questions.

3. Un fichier names.csv contenant toutes les informations sera generé automatiquement puis les variables du client.template seront remplacées par les valeurs contenues dans ce fichier.

4. Dans le dossier easy-rsa, vous trouverez autant de fichiers clientxxx.ovpn que demande.

5. Il suffira ensuite de distribuer vos fichiers de configuration .ovpn a chaque personne de votre entreprise en respectant les mesures de sécurité et de confidentialité, le fichier de configuration étant confidentiel et unique pour chaque personne.

6. Ce fichier doit être copié dans le dossier config de votre client OpenVpn. Une fois copié, il n'y a plus qu'à lancer la connexion.

## Démarche du script:

Démarrage par la fonction gen_fichier_csv:

1. Le script génère un certificat et une clé client avec easy-rsa (sans mot de passe) qu'il nomme `clientXXX.crt` et `clientXXX.key` ( les XXX représentant le numéro du client ). 
2. Les fichiers suivants `ca.crt`, `ta.key`, `clientXXX.crt` et `clientXXX.key` sont lus.
3. Des en-têtes sont créées dans un fichier nommé `names.csv`.
4. Chaque en-tête du fichier `names.csv` est alimentée par l'information correspondante.
5. Une fois le fichier `names.csv` rempli, 

La fonction //gen_fichier_ovpn// se lance :

6. Le fichier `names.csv` est lu comme un dictionnaire
7. Les variables du fichier `client.template` sont remplacées par les valeurs lues dans le dictionnaire
8. Les fichiers `clientXXX.ovpn` sont générés dans le dossier `easy-rsa`
 
