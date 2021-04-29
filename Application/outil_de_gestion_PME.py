
import sqlite3
import hashlib
import sys
import socket
import time
import logging
import threading
import datetime
import shutil
import os
import sys
import random
import fileinput
import logging
import string
from ftplib import FTP
import ftplib
from queue import Queue
from getpass import getpass
#########################################
from ftplib import FTP
import ftplib
from getpass import getpass
import hashlib
import os
import sys
import re
import string
import random
import fileinput
import logging
########################################################################
####Si non crée, il le crée affiche 4 colonnes ( l'heure, le nom , l'info (info warning erreur ect) et le message a afficher )
logging.basicConfig(filename='Z:/donnee/test_log.log',level=logging.DEBUG,\
      format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
#######################################################################################################################
###connection a la bdd dbbase.db si non crée, il le crée automatiquement
connection = sqlite3.connect('Z:/donnee/dbbase.db') #creation de connexion, cree un fichier .db
#connection = sqlite3.connect('dbbase.db') #creation de connexion, cree un fichier .db
print("Connecté à la base")

############################################################
##Création de la table utilisateur
cursor = connection.cursor() #Connecte la bdd à la requete
cursor.execute("""
CREATE TABLE IF NOT EXISTS utilisateur(
     id_user INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     login CHAR[40],
     mdp CHAR[4],
     nom CHAR[40],
     prenom CHAR[40],
     region CHAR[40],
     adresse CHAR[20],
     cp INTEGER,
     age INTEGER,
     id_permission INTERGER

)
""")

#############################################################
######Ajout des éléments dans une base de donnée
def add():
        firstname = input("prenom: ") # taper le prenom
        name = input("nom: ") # taper le nom
        age = input("Age: ") # taper le nom
        region = input("region: ") # taper le nom
        adresse = input("adresse: ") # taper le nom
        cp = input("Code Postale: ") # taper le nom
        permission = input ("Niveau de permissions de 1 à 3 sachant que 1 etant la plus élevé")
        name=name.lower()
        global mdpuser
        mdpuser = firstname[0] + name[:3] # recupere la premiere lettre du prenom + 4 lettres du prenom
        print ("votre mot de passe est :",mdpuser) #affiche le mot de passe en dur
        hash_key = hashlib.md5(mdpuser.encode()).hexdigest() #chiffre le mot de passe
        cursor.execute("""
        INSERT INTO utilisateur (login,nom,mdp,prenom,region,adresse,cp,age,id_permission) VALUES (?,?,?,?,?,?,?,?,?) """,(firstname,name,hash_key,firstname,region,adresse,cp,age,permission) )
        connection.commit() #Valider la modification pour que sa s'enregistre sur la BDD
        print("enregistre")
        logging.info('Ajout user !!!!!!!')
        return mdpuser

###############################################################################
###################Lister les utilisateur de la base de donné utilisteur en montrant login,nom,mdp,prenom,region,adresse,cp,age,id_permission
## et on affiche toute les lignes avec fetchone
def listeuser():

        print("id,login,mdp,nom,prenom,region,adresse,cp,age,id_permission")
        cursor.execute("""SELECT * FROM Utilisateur""")#liste tout les champs de la table utilisateur et de la table who

        insertion = cursor.fetchall() # recuppere les donnés de la requete
        for lign in insertion: # permet d'fficher ligne par lignes les utilisateurs
            print(lign)
        test = cursor.fetchone()
        logging.info('listing utilisateur !!!!!!!')# affiche listing utilisagteur dans le fichier log

def listeuseradmin():# meme chose que le dessus, permet d'afficher seulement les éléments
        print("login,nom,prenom,id_permission")
        cursor.execute("""SELECT login,nom,prenom,id_permission FROM Utilisateur""")#liste tout les champs de la table utilisateur et de la table who

        insertion = cursor.fetchall() # recuppere les donnés de la requete
        for lign in insertion: # permet d'fficher ligne par lignes les utilisateurs
            print(lign)
        test = cursor.fetchone()
        logging.info('listing utilisateur !!!!!!!')# affiche listing utilisagteur dans le fichier log
####################################################################################################################
######Permet de supprimer une ligne de la bdd
def delete():
        cursor.execute("""SELECT  login FROM Utilisateur  """)# Selectionne les utilisateurs de ta table utilisateur
        insertion = cursor.fetchall()# recupere les champs d'un coup au lieu de 1 par 1 ( fetone()) toute les lignes
        identifiant = input("supprimer la ligne") # entrer le numero de la ligne à supprimer
        cursor.execute("DELETE FROM utilisateur WHERE login = \'%s\' "%(identifiant)) # requete suppressions qui le fait selon l'id
        #cursor.execute("DELETE FROM utilisateur WHERE login = ? ",identifiant)
        print("supprimer")
        if connection.commit():# valide la requette et sauvegarde la suppression sur la BDD
            print("enregistre")
        logging.warning('suppression user !!!!!!!')####affiche supression user en warning dans le fichier log

#########################################################################################################
######permet de mettre a jour les éléments de la bdd

def update():
        cursor.execute("""SELECT * FROM utilisateur""") # Selectionne les utilisateurs de la table utilisateur
        insertion = cursor.fetchall()# recupere les champs d'un coup au lieu de 1 par 1 ( fetone()) toute les lignes
        print(insertion) # affiche les lignes
        firstname = input("New firstname : ")
        name = input("New lastname : ")
        region = input("region")
        adresse = input("adresse")
        cp = input("code postale")
        age = input("age")
        permission = input("permission")
        modification = input("modifié la ligne")
        cursor.execute("UPDATE utilisateur set login = ? ,nom = ?,region = ?, adresse = ?, cp = ?, age = ?, id_permission = ? WHERE id_user = ?", (firstname, name, region, adresse,cp, age, permission, modification)) # requete modification taper un nouveau prenom, nom et taper la ligne a modifié
        print("the line has been updated")
        cursor.execute("""SELECT * FROM utilisateur""") # affiche les lignes pour voir la modification
        insertion = cursor.fetchall() # Recupere les champs d'un coup au lieu de 1 par 1 ( fetone()) toute les lignes
        print(insertion)##affiche la nouvelle ligne modifié
        connection.commit()# valide la requette et sauvegarde la suppression sur la BDD
        logging.warning('modification utilisateur !!!!!!!')##envoie les info dans le fichier log

#################################################################################################################################
############################""
def bruteforce():##permet de forcé un mot de passe en essayé toute les combinaisons possible

        logging.warning('brute force commencement')#envoie u fichier log que la fonctionne commence
        liste=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        print ("Vous avez choisi de brute forcer un mot de passe !!!!!")
        #brute=input("Choisissez maintenant l'utilisateur que vous voulez brute forcer:")
        #brute=input("Entrez le chiffre de l'utilisateur que vous voulez brute forcer : ")
        input("utilisateur")

        for i in liste :
                #for j in range (0,4):
                if i != mdpuser [0]:
                    print(i)
                else :
                    print (i,"est la premiere lettre du mot de passe ")
                if i != mdpuser [1]:
                    print(i)
                else :
                    print (i,"est la deuxième lettre du mot de passe ")
                if i != mdpuser [2]:
                    print(i)
                else :
                    print (i,"est la troisième lettre du mot de passe ")
                if i != mdpuser [3]:
                    print(i)
                else :
                    print (i,"est la quatrième lettre du mot de passe ")
        logging.warning('brute force fin')

###############################################################################################################
def lecturelog():#### fonction qui permet d'afficher dans le terminal les info recensé dans le fichier
    with open("Z:/donnee/test_log.log", "r") as log_file:
        for line in log_file.readlines():
            tmp = line.split("--")
            print("time: %s, user: %s, level: %s, message: %s" % (tmp[0], tmp[1], tmp[2], tmp[3]))

##################################################################################################################
def mort():# Cette fonction permet de faire un scan de port
    logging.info('scan de port commencement')
    socket.setdefaulttimeout(0.25)
    print_lock = threading.Lock()
    target = 'paris'
    f=open ('Z:/donnee/scan.txt','w')#### ecirs dans le fichier les éléments ecris avec f.write
    now1=datetime.datetime.now().time()
    print("Horaire :", now1.strftime('%A %d %y, %H:%M:%S'))
    f.write(" La date et l'heure :" +now1.strftime('%A %d %y, %H:%M:%S'))
    f.write ("\n")
    f.write ('+-----------+---------------+\n')
    f.write ('|port       |   etat        |\n')
    f.write ('+-----------+---------------+\n')

    def portscan(port):

        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = connexion_principale.connect((target, port))

            print('Port', port, 'is open!')
            f.write("le port " +str (port)+ "  :ouvert \n")
            logging.info('ports ouvert :')
            logging.info(port)
            connexion_principale.close()

        except:
            pass
    def threader():
        while True:
            worker = q.get()
            portscan(worker)
            q.task_done()

    q = Queue()
    startTime = time.time()

    for x in range(100):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    for worker in range(1, 10000):###port de 1 a 10000
        q.put(worker)
    q.join()
    print('Time taken:', time.time() - startTime)
    logging.info('scan de port terminé')
    f.close()
###########################################################"FTP"##############################################
def client():
    def fenetre():
        choix=input("1 - Afficher le contenu du répertoire courant \n2 - Changer de répertoire \n3 - Renommer un fichier \n4 - Supprimer un fichier  \n5 - Télécharger un fichier \n6 - Créer un répertoire  \n7 - client vers serveur\n8 - suppression dossier \n0 - Quitter \nRentrez le numéro de l'action désirée : ") #pour le choix de quitter revenir au gros menu d'avant ou il choisis les Gestion
        if choix == "1":     # Chaque choix renvoi sur la fonction Contenu()
            os.system('cls')
            Contenu()
        elif choix == "2":     # Chaque choix renvoi sur la fonctionChanger()
            os.system('cls')
            Changer()
        elif choix == "3":     # Chaque choix renvoi sur la fonction Rename()
            os.system('cls')
            Rename()
        elif choix == "4":     # Chaque choix renvoi sur la fonction Deletefile()
            os.system('cls')
            Deletefile()

        elif choix == "5":     # Chaque choix renvoi sur la fonction Download()
            os.system('cls')
            Download()
        elif choix == "6":     # Chaque choix renvoi sur la fonction adddirectory()
            os.system('cls')
            adddirectory()

        elif choix == "7":     # Chaque choix renvoi sur la fonction cts()
            os.system('cls')
            cts()

        elif choix == "8":     # Chaque choix renvoi sur la fonction supdossier()
            os.system('cls')
            supdossier()

        elif choix == "0":
            os.system('cls')
            Deco()
        else:
            os.system('cls')
            print("Ce choix n'existe pas")
            fenetre()

    def supdossier():#Supression de dossier
        print(ftp.dir())
        directory= input("Rentrez le nom du dossier à supprimer : \n")
        try:
            ftp.rmd(directory)##commande supression de la lib ftp
            print ("Dossier supprimé")
            print(ftp.dir())
            fenetre()
        except ftplib.all_errors:
            print ("Le dossier spécifié n'existe pas")

    def cts(): #dll du client vers le serveur
        print(ftp.dir())
        chemin= "C:/Users/chg/Desktop/download/"
        fichier = input ("Rentrez le nom du fichier : \n")
        cheminfichier = (chemin + fichier)
        print(fichier)
        print(cheminfichier)
        try:
            file = open(cheminfichier, 'rb') # le fichier qu'on a selectionné s'ouvre avec open
            ftp.storbinary('STOR '+fichier, file) # cette commande permet de stocker le fichier pour ensuite l'envoyé
            file.close() # on ferme le fichier
            print ("Fichier uploadé :", ftp.nlst(fichier))
            print(ftp.dir())
            fenetre()
        except FileNotFoundError:
            print ("Le fichier spécifié n'existe pas")
            fenetre()

    #Télécharger un fichier
    def Download():##dll du serveur vers client
        print(ftp.dir())
        filename= input("Rentrez le nom de fichier à télécharger : \n")
        path ='C:/Users/chg/Desktop/download/'
        try:
            handle = open(path.rstrip("/") + "/" + filename.lstrip("/"), 'wb')
            if ftp.retrbinary('RETR %s' % filename, handle.write) == True:
                print ("Fichier téléchargé :", ftp.nlst(filename))
                fenetre()
        except ftplib.error_perm:
            print ("Echec du téléchargement")
            fenetre()
    #Créer un dossier
    def adddirectory(): ##cree un dossier
        print(ftp.dir())
        directory= input("Rentrez le nom du nouveau dossier : \n")
        ftp.mkd(directory)##commande ajout de ftp
        print ("Dossier créé")
        print(ftp.dir())
        fenetre()

        try:
            file = open(cheminfichier, 'rb') # ici, j'ouvre le fichier ftp.py
            ftp.storbinary('STOR '+ fichier, file) # ici (où connect est encore la variable de la connexion), j'indique le fichier à envoyer
            file.close() # on ferme le fichier
            print ("Fichier uploadé :", ftp.nlst(fichier))
            print(ftp.dir())
            fenetre()
        except FileNotFoundError:
            print ("Le fichier spécifié n'existe pas")
            fenetre()

    #Supprimer un fichier
    def Deletefile(): #suppression file
        print(ftp.dir())
        filetodelete= input("Entrez le nom du fichier à supprimer dans le répertoire courant: \n")
        try:
            ftp.delete(filetodelete)
            print("Fichier", filetodelete, "supprimé")
            print(ftp.dir())
            fenetre()
        except ftplib.all_errors:
            print ("Le fichier spécifié n'existe pas")
            fenetre()

    #Renomer un fichier
    def Rename(): #renommé
        print(ftp.dir())
        filetorename= input("Entrez le nom du fichier à renommer dans le répertoire courant : \n")
        logging.warning('fichier à renommer' +str(filetorename))
        into= input ("Saisir le nouveau nom : \n")
        logging.warning('le nouveau nom est : ' +str(into))
        try:
            ftp.rename(filetorename, into)
            print('Nouveu nom : ', ftp.nlst(into))
            print(ftp.dir())
            fenetre()
        except ftplib.all_errors:
            print ("Le fichier n'existe pas")
            fenetre()

    #Changer de répertoire de travail
    def Changer(): #changer de repertoire
        print(ftp.dir())
        dossier= input("Nom du dossier : \n")
        logging.warning('Changement de repertoire : '+str(dossier))
        try:
            ftp.cwd(dossier)
            print(ftp.dir())
            fenetre()
        except ftplib.all_errors:
            print ("Le dossier n'existe pas")
            fenetre()

    #Afficher le contenu du répertoir on l'on se trouve
    def Contenu(): #lister
        print(ftp.dir())
        logging.warning('Afficher le contenue du répertoire ')
        fenetre()

    #Déconnexion du serveur FTP avec retour à l'accueil du progame
    def Deco():
        logging.warning('Deconnexion')
        print(ftp.quit())


    ftp_host ='paris'
    ftp_login = input('Login :  \n') ##philippe
    ftp_password = getpass ('Mot de passe:  \n') ##philippe
    hashey = hashlib.md5(ftp_password.encode()).hexdigest()
    ftp = FTP(ftp_host, ftp_login, ftp_password)
    print(ftp.getwelcome())
    logging.warning('Connexion ftp' +str(ftp_login) +str(hashey))
    fenetre()    #Connexion au serveur FTP




#################################Insertion####################################################################
###### page principale ou l'on fait nos choix pour le superadmin
def authentificationsuper():
        run = True
        while run:
                print("press 0 to quit")
                print("press 1 to add a user")
                print("press 2 to show all user")
                print("press 3 to delete")
                print("press 4 for update")
                print("press 5 for port scan")
                print("press 6 for test brut force")
                print("press 7 for test lecturelog")

                val = input ()
                print("")
                #try:

                val = int(val)
                if val == 0:
                            #return identifiant()
                            break

                elif val == 1:
                        add()

                elif val == 2:
                        listeuser()

                elif val == 3:
                        delete()

                elif val == 4:
                        update()

                elif val == 5:
                        mort()

                elif val == 6:
                        bruteforce()

                elif val == 7:
                        lecturelog()
                        print("wrong command")
                print("")
        print("end")


##########################################################
def authentificationadmin(): #Page principale avec les fonctionnalité d'un admin
        run = True
        while run:
                print("press 0 to quit")
                print("press 1 to add a user")
                print("press 2 to show all user")
                print("press 3 to delete")
                print("press 4 for update")

                val = input ()
                print("")
                #try:

                val = int(val)
                if val == 0:
                            #return identifiant()
                            break

                elif val == 1:
                        add()
                elif val == 2:
                        listeuseradmin()
                elif val == 3:
                        delete()
                elif val == 4:
                        update()

##########################################################
def infirm():
        run = True
        while run:
                print("press 0 to quit")
                print("press 1 to show all user")
                print("press 2 to go on ftp's client")


                val = input ()
                print("")
                #try:

                val = int(val)
                if val == 0:
                            #return identifiant()
                            break

                elif val == 1:
                        listeuser()

                elif val == 2:
                        client()






                print("")
        print("end")
##########################################################################

login = 'esgi' # touche espace pour login et mdp
passd = 'esgi' # Le Superutilisateur va devoir crée son propre login et mot de passe, ensuite il va devoir modifier les paramettre de login et passe
def superadmin():# page de connection superadmin
    print("bonjour superadmin")
    user = input('User: ')
    passw = getpass('Mot de passe: ')
    hashey = hashlib.md5(passw.encode()).hexdigest()
    cursor.execute("""
    SELECT * FROM Utilisateur WHERE login = ? AND mdp = ? AND id_permission = 1""", (user,hashey))## si l'id_permission est egale a 1 alors il se connect sinon ca ne fonctionne pas

    if cursor.fetchall() or user == login and passw == passd :
        logging.info('supertulisateur connecté' +str(hashey) +str(user))

        print('Bienvenue sur lapps')
        authentificationsuper()### apres authentification, va sur la page principale en tant que superadmin


    else: ######si il se trompe de mdp ou de login, son id permission va en 4 ce qui ban son compte
        ban = 4
        cursor.execute("UPDATE utilisateur set  id_permission = ? WHERE login = ?", (ban,user)) # requete modification taper un nouveau prenom, nom et taper la ligne a modifié
        connection.commit()# valide la requette et sauvegarde la suppression sur la BDD
        print("login ou mot de passe incorrect, compte désactivé, contacté votre superviseur")
        logging.warning('tentative de connection superutilisateur échouer' +str(hashey) +str(user))


def admin():
    print("bonjour admin")
    user = input('User: ')
    passw = getpass('Mot de passe: ')
    hashey = hashlib.md5(passw.encode()).hexdigest()
    cursor.execute("""
    SELECT * FROM Utilisateur WHERE  login = ? AND mdp = ? AND id_permission = 2
    """, (user,hashey))

    if cursor.fetchall() or user == login and passw == passd :
        logging.info('admin connecté ' +str(hashey) +str(user))
        print('Bienvenue sur lapps')
        authentificationadmin()### apres authentification, va sur la page principale en tant que admin


    else:
        ban = 4 ######si il se trompe de mdp ou de login, son id permission va en 4 ce qui ban son compte
        cursor.execute("UPDATE utilisateur set  id_permission = ? WHERE login = ?", (ban,user)) # requete modification taper un nouveau prenom, nom et taper la ligne a modifié
        connection.commit()# valide la requette et sauvegarde la suppression sur la BDD
        print("login ou mot de passe incorrect, compte désactivé, contacté votre superviseur")
        logging.warning('tentative de connection admin' +str(hashey) +str(user))

def identifiant():##### avant la fenetre d'identifiant il faut selectionner la permission que nous avons
        while True:
                print("1 pour superadmin")
                print("2 pour admin")
                print("3 pour medecin")
                val = input ("qui etes vous ?")
                print("")
                #try:

                val = int(val)

                if val == 1:
                    superadmin()

                elif val == 2:
                    admin()
                elif val == 3:
                    infirmier()

#logging voir les mdp hash

def infirmier():# page de connection superadmin
    print("bonjour medecin")
    user = input('User: ')
    passw = getpass('Mot de passe: ')
    hashey = hashlib.md5(passw.encode()).hexdigest()
    cursor.execute("""
    SELECT * FROM Utilisateur WHERE login = ? AND mdp = ? AND id_permission = 3""", (user,hashey))## si l'id_permission est egale a 1 alors il se connect sinon ca ne fonctionne pas

    if cursor.fetchall() or user == login and passw == passd :
        logging.info('supertulisateur connecté' +str(hashey) +str(user))

        print('Bienvenue sur lapps')
        infirm()### apres authentification, va sur la page principale en tant que admin


    else: ######si il se trompe de mdp ou de login, son id permission va en 4 ce qui ban son compte
        ban = 4
        cursor.execute("UPDATE utilisateur set  id_permission = ? WHERE login = ?", (ban,user)) # requete modification taper un nouveau prenom, nom et taper la ligne a modifié
        connection.commit()# valide la requette et sauvegarde la suppression sur la BDD
        print("login ou mot de passe incorrect, compte désactivé, contacté votre superviseur")
        logging.warning('tentative de connection superutilisateur échouer' +str(hashey) +str(user))

identifiant()#execute cette fonction en premier
