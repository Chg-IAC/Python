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

logging.info('activation du script de suppression semaine 2')

test= "E:/sauvegarde/semaine2" 
shutil.rmtree(test) 

os.makedirs("E:/sauvegarde/semaine2/")


logging.info('fin du script semaine2 ')
