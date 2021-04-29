#scanneur de port
import socket 
import threading
import time
import datetime

hote = '127.0.0.1'
f=open ('scan.txt','w')

#  pour la date utilise ceci
now=datetime.datetime.now().date()
print("date :", now.strftime('%A %d %B %y'))

#  pour la date et le temps uitlise ceci
now1=datetime.datetime.now().time()
print("Horaire :", now1.strftime('%A %d %y, %H:%M:%S'))


##now = time.time()
##print("date=======", now)
 
##print ("L'heure et la date actuelle:", time.localtime(now))


f.write ("la date : "  +str(now) +"\n")
#  ou bien
f.write(" La date et l'heure :" +now1.strftime('%A %d %y, %H:%M:%S'))
f.write ("\n")
f.write ('+-----------+---------------+\n')
f.write ('|port       |   etat        |\n')
f.write ('+-----------+---------------+\n')

print()
print("Autre version.....")

### autre version en UDP
for port in range (125, 140):
    try :
      
        connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_principale.connect((hote, port))
         
        print(" le port est ouvert ",port)
        f.write("le port "+str (port)+ "  :ouvert \n")
       
    except: #socket.error:
        print ("le port est fermé",port)
        f.write(" le port "+str (port)+ " :fermé \n")
    connexion_principale.close()

f.close()
