# Exemple de partage d'une variable 
 
import threading
import sys

x = 0
n = 100
# instanciation d'un objet verrou à partir de la classe Lock
verrou=threading.Lock() 

#définition des deux méthodes utilisées par les 2 threads
def add1() :
    global x,verrou        # variables globales
    for i in range(n) :
        verrou.acquire()   # acquisition de la variable x
        x+=1
        verrou.release()   # relachement de la variable x
 
def add2() :
    global x,verrou
    for i in range(n) :
        verrou.acquire()
        x+=2
        verrou.release()



#instanciantion de 2 threads 
t1=threading.Thread(target=add1)
t2=threading.Thread(target=add2)

# Lancement des threads
t1.start()   
t2.start()
 
# attente de la fin des tâches
t1.join()
t2.join()
print("Fin des opérations, la valeur finale de la variable x = ", x)
