import shutil
import os
import time
import datetime 
import logging

import sqlite3
import hashlib
import sys
import socket
import time
import logging
import threading
import datetime
import shutil
from queue import Queue
from getpass import getpass



logging.basicConfig(filename='E:/donnee/test_log.log',level=logging.DEBUG,\
      format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')

logging.info('activation du script')


srclog= "E:/donnee/test_log.log"
srcbd= "E:/donnee/dbbase.db"
semaine1= "E:/sauvegarde/semaine1"
semaine2= "E:/sauvegarde/semaine2"

bd= "C:/Users/Administrator/Desktop/sauvegarde/semaine1/dbbase.db"
log= "C:/Users/Administrator/Desktop/sauvegarde/semaine2/test_log.log"

#os.rename("C:/Users/Administrator/Desktop/frama", "C:/Users/Administrator/Desktop/paz1")
##now1=datetime.datetime.now().time()
shutil.copy(srclog, semaine1)
shutil.copy(srclog, semaine2)


shutil.copy(srcbd, semaine1)
shutil.copy(srcbd, semaine2)
##os.rename(" C:/Users/Administrator/Desktop/moi/test2.txt", "C:/Users/Administrator/Desktop/moi/test3.txt")


os.rename("E:/sauvegarde/semaine1/dbbase.db", time.strftime("E:/sauvegarde/semaine1/bdd%Y%m%d%H%M%S.txt"))
os.rename("E:/sauvegarde/semaine1/test_log.log", time.strftime("E:/sauvegarde/semaine1/log%Y%m%d%H%M%S.txt"))

os.rename("E:/sauvegarde/semaine2/dbbase.db", time.strftime("E:/sauvegarde/semaine2/bdd%Y%m%d%H%M%S.txt"))
os.rename("E:/sauvegarde/semaine2/test_log.log", time.strftime("E:/sauvegarde/semaine2/log%Y%m%d%H%M%S.txt"))

logging.info('fin de sauvegarde')


