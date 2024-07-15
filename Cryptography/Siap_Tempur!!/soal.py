from Paillier import Paillier
from secret import flag
from Crypto.Util.number import *

cipher=Paillier()

while True:
    print("What you want to do?")
    print("1. Encrypt a message")
    print("2. Encrypt the flag")
    print("3. exit")
    inp=int(input("> "))
    if(inp==1):
        print("Enter message")
        msg=input("> ")
        print("Enter r")
        r=int(input("> "))
        ct=cipher.encrypt(msg,r)
        print(f"encrypted : {ct}")
    elif(inp==2):
        ct=cipher.encrypt(flag,0)
        print(f"encrypted flag : {ct}")
    else:
        exit()

