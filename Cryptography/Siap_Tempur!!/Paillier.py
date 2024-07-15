from Crypto.Util.number import *
from math import lcm
import random

class Paillier :
    def __init__(self):
        self.cnt=1
        while True:
            p, q = getPrime(512), getPrime(512)
            if GCD(p*q, (p-1)*(q-1)) == 1:
                break
        self.phi=lcm(p-1,q-1)
        self.n = p * q
        self.r= { r+1 : random.randint(2, self.n-1) for r in range(128) }

    def encrypt(self,msg,r):
        msg_len=len(msg)
        msg=bytes_to_long(msg.encode())
        gm=pow(self.n+1,msg,self.n**2)
        if r==0:
            rn=pow(self.r[msg_len],self.n+self.cnt,self.n**2)
        else:
            rn=pow(r,self.n+self.cnt,self.n**2)
        ct=(gm*rn)%(self.n**2)
        self.cnt+=1
        return ct
