import threading
import time


### 1ier exmeple de thread sans création de nouvelles classes
def affiche(nb, nom = ''):
   for i in range(nb):
    print (nom, i)
##
a = threading.Thread(None, affiche, None, (20,), {'nom':'thread a'})
b = threading.Thread(None, affiche, None, (20,), {'nom':'thread b'})
a.start()
b.start()

a.join()
b.join()

# a._stop()
# b._stop()



## 2 méthodes d'affichage différentes, représentées par des classes
class Affiche1(threading.Thread): # hérite de Thread du module threading
    def __init__(self, nom = ''):  # le constructeur, pour créer et initialiser les objets (ou variables du type la classe Affiche1
        threading.Thread.__init__(self)
        self.nom = nom  # initialisation du nom du thread à passer en paramètre lors de la création, voir plus bas
        self.Terminated = False  # tâche non finie initialement
        
    def run(self):  # méthode d'exécution du thread ou tâche
        i = 0
        while not self.Terminated: # tant que tâche pas finie
            print ("\n"+self.nom, i)             
            i += 1
            time.sleep(1.0)  # pause
        print( "le thread "+self.nom +" s'est termine proprement\n") # sortie de la boucle une fois la tâche finie

    def stop(self): # méthode d'arrêt de la tâche, manuellement avec stop (voir en bas)
        self.Terminated = True	
 
#### 2ième classe représentant la méthode Afficher2 différente de Affiche 1, même description
class Affiche2(threading.Thread):
    def __init__(self, nom = ''):
        threading.Thread.__init__(self)
        self.nom = nom
        self._stopevent = threading.Event( )
        
    def run(self):
        i = 0
        while not self._stopevent.isSet():
            print ("\n"+self.nom, i)
            i += 1
            self._stopevent.wait(1.0)
        print ("le thread "+self.nom +" s'est termine proprement\n")
        
    def stop(self):
        self._stopevent.set( )


##########   programme principal
# création des 3 objets thread, chacun son nom
a = Affiche1('Thread A')
b = Affiche1('Thread B')
c = Affiche2('Thread C')

# lancement des threads
a.start()
b.start()
c.start()
time.sleep(6.5)  # pause
# arrêt des threads
a.stop()
b.stop()
c.stop()
