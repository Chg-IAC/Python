# Mise en place d'un serveur multi accès avec le module select
# Cette version est un test de réception de msg de plusieurs clients
# Version à améliorer pour l'envoi aux clients en parallèle

#Ceci sont les modules nécessaires
import socket, select,threading

print ("########## Serveur de Tchat façon Module THREAD ##########")
print           ("            ##### Par Philippe et Pierre ##### ")
 
# Les paramètres du serveur
hote = '127.0.0.1'
port = 10000
nbre=1024

# Définition du socket de connexion
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Déclaration du socket connexion principale 
connexion_principale.bind((hote, port)) # Mise en place de la varibale pour l'adresse du serveur et du port associé au socket connexion principale
connexion_principale.listen(5) # Nombre maximum de 5 clients
print ("Serveur de Tchat Disponible")
print("Le serveur écoute à présent sur le port :", port)
 
serveur_lancé = True  #booléen # Condition pour lancé le serveur 


clients_connectes = [] # Liste de déclaration des clients connectés 

def serveur () :

    while serveur_lancé:  ## while True:
        # On va vérifier les nouveaux clients qui se connectent
        # Pour cela, on écoute la connexion_principale (socket)
        connexions_demandees, wlist, xlist = select.select([connexion_principale], # on a remplacer le rlist par connexions_demandees car select lit les clients en demande de connexion
            [], [], 0.06)  # 60 ms de time out
        
        for connexion in connexions_demandees:  #les clients  de rlist 
            connexion_avec_client, infos_connexion = connexion.accept() # on accepte les clients 

            # On ajoute le socket connecté à la liste des clients
            clients_connectes.append(connexion_avec_client) # génération du socket aléatoirement 
        
        # On écoute la liste des clients connectés
        # Les clients renvoyés par select sont ceux devant être lus (recv)
        # On attend là  60ms maximum
        # On encadre l'appel à select.select dans un bloc try

        clients_a_lire = [] # Déclaration d'une liste de client ayant écrit le message 
        try:
            clients_a_lire, wlist, xlist = select.select(clients_connectes, # Maintenant que les clients sont accepetés on attend le message 
                    [], [], 0.06)
        except select.error:
            pass

    #on continue en séquence si pas d'erreurs
        else:  
            # On parcourt la liste des clients à lire
            for client in clients_a_lire:
                # Client est de type socket
                msg_recu = client.recv(nbre)#recois le message
                msg_recu = msg_recu.decode() # Décode le message 
                print("Message reçu :", msg_recu) # affiche le message decodé reçu sur le serveur 
                client.send(b"\n")#message de type byte
    # On transmet maintenant le message du client à l'autre client en parcourant la liste des clients connectés 
                for envoie in clients_connectes:
                    if envoie == client: # Cette condition concerne l'emetteur du message, on ne doit pas lui envoyer le message qu'il vient d'envoyer.
                        continue
                    else:
                        msgrecu=msg_recu.encode() # Condition pour transmettre le message du client au autres clients connectés
                        envoie.send(msgrecu)
        
                if msg_recu.upper() == "FIN": # Fin du tchat si le client écrit fin ou FIN majuscule ou minuscule 
                    serveur_lance = False

                
    print("Fermeture des connexions par l'un des clients ")

    # Fermeture des connexions donc des sockets
    for client in clients_connectes:
        client.close()
    
    connexion_principale.close()  ## Fermeture du socket principal
serveur()
