from sympy import *
import socket
import time
import random

def Syncronize():
    
    confirm = ""
    while confirm != "Syncronized":
        try:
            s.sendto("Syncronized".encode(), ('localhost',1070))
            confirm, addr = s.recvfrom(4096)
            confirm = confirm.decode()
        except:
            print("Waiting")
            time.sleep(1)
    
def MCD(Pn,e):
    while Pn % e != 0:
        if Pn < e:
            t = Pn
            Pn = e
            e = t
            
        Pn = Pn%e
    
    if e == 1:
        return True
    return False

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 1060))

p = Pn = q = e = d = Pub1 = Pub = 0

while not isprime(p):
    p = random.randint(10**3, 10**4-1)

while not isprime(q):
    q = random.randint(10**3, 10**4-1)
    
n = p*q
Pn = (p-1)*(q-1)

e = random.randint(10**2, 10**3-1)

while not MCD(Pn,e):
    e = random.randint(10**2, 10**3-1)

print("N = ", n)
print("e = ", e)

Syncronize()

time.sleep(0.5)
s.sendto(n.to_bytes(35,'big'), ('localhost', 1070))

Syncronize()

time.sleep(0.5)
s.sendto(e.to_bytes(35,'big'), ('localhost', 1070))

Syncronize()

while Pub == 0:
    Pub,addr = s.recvfrom(4096)
    Pub = int.from_bytes(Pub, "big")

Syncronize()

while Pub1 == 0:
    Pub1,addr = s.recvfrom(4096)
    Pub1 = int.from_bytes(Pub1, "big")

print("Pub = ", Pub)
print("Pub1 = ", Pub1)

d = random.randint(10**5, Pn-1)

while (((e*d)-1) % Pn) != 0:
    d = random.randint(10**5, Pn-1)

print(d) 

while True:
    message = int(input())
    if message == 0:
        break
    message = (message**Pub1) % Pub
    s.sendto(message.to_bytes(35,'big'), ('localhost', 1070))
    print(message)
