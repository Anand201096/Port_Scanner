import sys
import socket
import os
import pyfiglet
import time
from cfonts import render
from termcolor import colored


ascii_banner = pyfiglet.figlet_format("Port Scanner")
print(ascii_banner)

cred='Coded by:--> @AnandGurav'
print(colored(cred,'red'))
lang='Works within the same network'
print(colored(lang,'green'))
print("======================================================")



time.sleep(1)

ip = input(colored('[*]  Enter IP Address:--> ','red'))


open_ports =[] 

ports = range(1, 65535)


def probe_port(ip, port, result = 1): 
  try: 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    sock.settimeout(0.5) 
    r = sock.connect_ex((ip, port))   
    if r == 0: 
      result = r 
    sock.close() 
  except Exception as e: 
    pass 
  return result


for port in ports: 
    sys.stdout.flush() 
    response = probe_port(ip, port) 
    if response == 0: 
        open_ports.append(port) 
    

if open_ports:
  
  offset = 5
  time.sleep(1)
  print("Loading:")

  #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
  animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]",   "[■■■■■■■■■■]"]

  for i in range(len(animation)):
      time.sleep(0.3)
      sys.stdout.write("\r" + animation[i % len(animation)])
      sys.stdout.flush()

  print("\n")
  
  print ("Open Port(s) is / are:", sorted(open_ports)) 


else:
 
  offset = 5
  time.sleep(1)
  print("Loading:")

  #animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
  animation = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]",   "[■■■■■■■■■■]"]

  for i in range(len(animation)):
      time.sleep(0.3)
      sys.stdout.write("\r" + animation[i % len(animation)])
      sys.stdout.flush()

  print("\n")
  
  print ("Looks like no ports are open.")




time.sleep(1)

output = render('Thankyou!', colors=['yellow', 'red'], align='center')
print(output)



def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    answer = input("\n [-] Do you want to restart this program ?(y/n) ")
    if answer.lower().strip() in "y".split():
        restart_program()




