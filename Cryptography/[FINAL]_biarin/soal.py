from Pailier import *
from Crypto.Util.number import *
from secret import flag

flag=bytes_to_long(flag)
cipher=pailier()
while True:
    print("What you want to do?")
    print("1. encrypt message")
    print("2. get flag")
    print("3. decrypt ciphertext")
    print("4. quit")
    inp=int(input("> "))
    if inp==1:
        print("Enter plaintext (hex)")
        inp=input("> ")
        ciphertext=cipher.encrypt(int(inp,16))
        print('ct : ','{0:x}'.format(ciphertext))
    elif inp==2:
        ciphertext=cipher.encrypt(flag)
        print('ct : ','{0:x}'.format(ciphertext))
    elif inp==3:
        print("Enter ciphertext (hex)")
        inp=input("> ")
        plaintext=cipher.decrypt(int(inp,16))
        print('pt : ','{0:x}'.format(plaintext))
    else:
        exit()
