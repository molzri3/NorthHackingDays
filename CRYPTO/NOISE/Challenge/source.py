from Crypto.Util.number import getPrime,bytes_to_long,GCD
import random
from SECRET import flag
m=bytes_to_long(flag)
p,q=getPrime(1024),getPrime(1024)
n=p*q
phi=(p-1)*(q-1)
e,f=0x1001,0x100f
d=pow(f,-1,phi)
print(f"D={d+random.getrandbits(8)}")
c=pow(m,e,n)
print(f"c={c}")
print(f"n={n}")



