#!/usr/bin/python3 

import sys
import socket
import colorama
from modules.modules import validator_path, get_file_size , helper
from time import sleep
from os import system

system("clear")
print(colorama.Fore.RED+helper.__doc__)

ip = "127.0.0.1"
port = 9080

sock_conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock_conn.bind((ip,port))
sock_conn.listen(1)
c,address = sock_conn.accept()

for i in colorama.Fore.LIGHTGREEN_EX+"[+] Server bind on {}:{} Successfully\n".format(ip,port):
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.2)

print(colorama.Fore.GREEN+"[!] An user connected with {} ipaddress&port [!]".format(address))

path_file = input(colorama.Fore.BLUE+"[?] Enter the path of file >> ")
if validator_path(path_file):
    pass
else:
    print(colorama.Fore.RED+"""[X] An Error has occured : 
    Could not find path file """)
    sys.exit(33)

file_size = get_file_size(path_file)
c.send(str(file_size).encode())

file = open(path_file,"rb")

while True:
    readed = file.read(4096)
    if not readed:
        break
    try:
        c.sendall(readed)
    except:
        print(colorama.Fore.RED+"[-] An error has occured in sending data [-]")

file.close()
c.close()
print("[+] transfering file Successfuly done [+]")