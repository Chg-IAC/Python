###############################################
# Mise en place d'un serveur simple
# simulation d'une connexion client/serveur
#"""""""""""""""""  version basique """""""""""#

import socket,sys
  
# les paramètres du serveur en local pour le test
HOST='127.0.0.1'     # adresse IP du serveur
PORT=2020            # port d'écoute du serveur
TAILLE_BUFFER=1024   # taille max à recevoir, par défaut

# création d'un socket
Mysocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) # famille et mode

# liaison du socket à une adresse IP et un port
Mysocket.bind((HOST, PORT))
 
# boucle de traitement tant qu'il y a des clients connectés
while 1 :  ### ou while True
    print(">>> Serveur prêt, en attente d'un client...")
 
    Mysocket.listen(10)  # écoute d'une connexion

# établissement de la connexion
    connexion,adresse=Mysocket.accept()
    print(">>> Connexion client réussie, adresse IP %s, port %s \n" % (adresse[0], adresse[1]))
     
# dialogue avec le client, envoi de message
    connexion.send(b"hello client")
    print(">>> Vous étes sur les serveur, prêt à recevoir vos msg")
    print(">>> Tapez FIN ou rien si vous souhaitez interrompre la connexion") 

# réception de message du client
    msgClient=connexion.recv(TAILLE_BUFFER)  # réception de 1024 caractères
    print('>>> C:' ,msgClient.decode())

# boucle d'échange avec le client
    while 1 :
                  
             if msgClient==b"FIN" or msgClient==b"":
                    break
                                   
             msgServer=input(">>> ")
             msgServer=msgServer.encode()
             print(">>> Envoi vers le client")
             connexion.send(msgServer)             
             msgClient=connexion.recv(TAILLE_BUFFER)
             print(">>> Reception du client")
             print(msgClient.decode())

# fermeture de la connexion
    connexion.send(b"Au revoir")
    print(">>> connexion interompue par le client!!!!")
    connexion.close()
    ch=input("<R>ecommencer <T>erminer?")
    if ch==b'T':
        print('Fin des connexions.')
        break
sock.close()
  
                   
