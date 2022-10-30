import socket
import time
import threading
from queue import Queue
import pyfiglet 
import os
#ORG CCT

socket.setdefaulttimeout(0.25)
lock = threading.Lock()

baner = pyfiglet.figlet_format("SCAN PORT - CCT") 

print(baner) 
ip_address = input('\033[92m''[*] INGRESA LA IP / HOST : ')
host = socket.gethostbyname(ip_address)
print ('\033[92m''[*]SCANEANDO DIRECCION IP: ', host)

def scan(port):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = sock.connect((host, port))
      with lock:
         print(port, '--- PORT OPEN')
      con.close()
   except:
      pass

def execute():
   while True:
      worker = queue.get()
      scan(worker)
      queue.task_done()
      
queue = Queue()
start_time = time.time()
   
for x in range(100):
   thread = threading.Thread(target = execute)
   thread.daemon = True
   thread.start()
   
for worker in range(1, 500):
   queue.put(worker)
   
queue.join()

print('Tiempo De Scaneo,:', time.time() - start_time)
time.sleep(10.1) 
os.system("python3 CCT_INF.py")  

