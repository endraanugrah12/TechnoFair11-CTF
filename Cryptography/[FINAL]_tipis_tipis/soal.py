from Crypto.Cipher import ARC4
from secret import flag,key
import random
import string

charset=string.ascii_lowercase
wordlist=[''.join(random.sample(charset,6)) for _ in range(10)]

print("Today words : ",wordlist)

while True:
    print("What you want to do?")
    print("1. take a peek")
    print("2. exit")
    inp=int(input("> "))
    if inp==1:
        random.shuffle(wordlist)
        rand_num=[random.randrange(0,len(flag)) for _ in range(10)]
        pt=flag
        for cnt,i in enumerate(rand_num):
            pt=pt[:i]+wordlist[cnt]+pt[i:]
        cipher=ARC4.new(key)
        print('ct : ',cipher.encrypt(pt.encode()).hex())
    elif inp==2:
        exit()

