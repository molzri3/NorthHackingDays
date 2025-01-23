from Crypto.Util.number import *
import random
from SECRET import *
import time

while (p:=getPrime(351))%4==1:continue

seed = random.randint(p // 4, p)
print(banner)
print(f"p: {p}")
print(f"seed:  {seed}")
bin_Flag=bin(bytes_to_long(FLAG))[2:]
for _  in bin_Flag:
    seed = pow(seed,2,p)
    h = 2 * random.getrandbits(351) + 1
    blue = pow(seed, h, p)
    red = pow(-seed, h, p)
    print("\nGive me red pill")
    random.shuffle(tmp := [blue, red])
    print(*tmp,sep='\n')
    init = time.time()
    answ = input(">>>")
    if time.time() - init > 60:
        print("Boboch sra3 mnk khouya hhhhh")  
        exit()
    try:
        if int(answ) != red:
            print("You don't wanna know the truth, stay in your matrix.")
            exit()
        else:
            print(_)
    except: exit()
