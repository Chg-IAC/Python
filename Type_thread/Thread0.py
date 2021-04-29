import threading
import time

def loop1():
    for i in range(1, 11):
        time.sleep(1)
        print("Loop1 :",i)
def loop2():
	for i in range(12, 20):
		time.sleep(1)
		print("Loop2 :",i)
print("\nExécution séquentielle....\n")
loop1()
loop2()
print("\n Fin des appels de fonctions \n")


### Utilsation de threads
def loop1():
    for i in range(1, 11):
        time.sleep(1)
        print("Thread T1",i)
        #print(threading.current_thread())
def loop2():
	for i in range(12, 20):
		time.sleep(1)
		print("Thread T2",i)
		#print(threading.current_thread())
print("Exécution parallèle....\n")

T1=threading.Thread(target=loop1)
T2=threading.Thread(target=loop2)

### démarre les threads
T1.start()
T2.start()

### les threads s'attendent avant de continuer en séquence
## join bloquant
T1.join()
T2.join()

### Gestion de temps pas très précise
T1._stop()
T2._stop()

print("\n Fin des traitements !!!!")
