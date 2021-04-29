
# Mise en place d'un client simple en mode SELECT

import socket,sys,threading # Importation des différents modules
nbre=1024 # variable par défaut 
  
# création d'un socket pour la connexion avec le serveur en local
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print  ("Mise en place d'un client simple en mode SELECT & Connexion Client 1")
print                          ("Par Philippe et Pierre")
try:
# connexion au serveur, bloc surveillé, et gestion de l'exception
    sock.connect(('127.0.0.1',10000)) # Ceci est l'adresse localhost ainsi que le port d'écoute du serveur pour la connexion du client

except socket.error:
   print("la connexion a échoué.......")
   sys.exit()
   
def envoie():
    msgServer=sock.recv(nbre)#recevoir le message
    print("Message du client 2 :\n",msgServer.decode(),"\n") # A cette étape le message est décodé.
    
def envoierecep():

    print(">>> Connexion établie avec le serveur...") # Lorsque la connexion est faite on affiche le message suivant 
    sock.send(b"hello serveur, je suis le client 1 ")
    msgServer=sock.recv(nbre) # Ceci est la taille par défaut 
    print(">>> Connecter au Serveur")

    msgClient=b"" #type byte
    while msgClient.upper()!=b"FIN": # Quand le client écrit fin ou FIN majuscule ou minuscule le tchat s'arrête
            
            if msgServer.upper()=='FIN':
                break   
            msgClient=input(">>> ") # Demande à l'utilisateur d'entrée un message avec la variable input !
            print(">>> Envoi vers le serveur")
            msgClient=msgClient.encode() # Le message est encodé en bit sous forme de 0 et de 1          
            sock.send(msgClient) # le message est ensuite envoyé
            envoie()

    

    print (" Fermeture de ma connexion ")
    sock.close()

envoierecep()



