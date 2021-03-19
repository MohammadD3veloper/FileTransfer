#!/usr/bin/python3

import sys
import socket
import colorama
from time import sleep
from os import system
from modules.modules import get_file_size, make_path , helper

system("clear")
print(colorama.Fore.RED+helper.__doc__)

# Creating Socket Connection 
sock_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for i in colorama.Fore.LIGHTGREEN_EX+"[+] Client is searching for a connection\n":
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.2)

sock_conn.connect(("127.0.0.1",9080))

file_size = sock_conn.recv(1024).decode()

print("[!] A file with %s byte size is comming ... [!]" % file_size)
file_name = input("[?] Enter file name for saving >> ")

try:
    open(make_path() +  file_name , "x")
except FileExistsError:
    pass
file = open(make_path() + file_name, "ab")
size = get_file_size(make_path() + file_name)

while (size != file_size):
    try:
        data = sock_conn.recv(4096)
    except:
        print("[-] An error has occured in getting data [-]")
    if not data:
        break
    
    file.write(data)

    
file.close()
sock_conn.close()
print("[+] File recieved successfully [+]")