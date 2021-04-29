###############################################
# Mise en place d'un client simple
# simulation d'une connexion client/serveur
#"""""""""""""""""  version basique """""""""""#

import socket, sys
  
# création d'un socket pour la connexion avec le serveur en local
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
# connexion au serveur, bloc surveillé, et gestion de l'exception
    sock.connect(('127.0.0.1',2020))

except socket.error:
   print("la connexion a échoué.......")
   sys.exit()

print(">>> Connexion établie avec le serveur...")
# Envoi et réception de messages
sock.send(b"hello serveur")
msgServer=sock.recv(1024) # taille par défaut

print(">>> S :", msgServer.decode())
 
while 1:  ## ou True
 
         if msgServer==b'FIN' or msgServer==b'':
              break   
               
         msgClient=input(">>> ")
         msgClient=msgClient.encode()
         print(">>> Envoi vers le serveur")
         sock.send(msgClient)         
         msgServer=sock.recv(100)
         print(">>> Reception du serveur")
         print(msgServer.decode())

print (">>> Connexion interrompue par le serveur!!!")
sock.close()
