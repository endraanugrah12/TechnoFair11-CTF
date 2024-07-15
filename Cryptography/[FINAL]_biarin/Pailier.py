from Crypto.Util.number import *
from math import lcm
import random


class pailier:
    def __init__(self):
        self.primes=[getPrime(512) for _ in range(2)]
        self.phi=1
        self.n=1
        self.phi = 1
        self.mul=1
        for _ in range(2):
            self.phi*=(self.primes[_]-1)
            self.n*=self.primes[_]
        self.g = [pow(random.randrange(1,self.n**2),self.primes[i],self.n**2) for i in range(2)]
        for _ in range(2):
            self.mul*=self.g[_]
        self.miu=inverse(self.L(pow(self.mul,self.phi,self.n**2)),self.n)

    def L(self,val):
        return (val-1)//self.n
        
    def pubkey(self):
        return (self.n,self.g)

    def encrypt(self,msg):
        r1=random.randrange(0,self.n-1)
        gm=pow(self.g[random.randrange(0,2)],msg,self.n**2)
        rn=pow(r1,self.n,self.n**2)
        ct=(gm*rn)%(self.n**2)
        return ct

    def decrypt(self,ct):
        m=self.L(pow(ct,self.phi,self.n**2))%self.n
        m=(m*self.miu)%self.n
        return m
