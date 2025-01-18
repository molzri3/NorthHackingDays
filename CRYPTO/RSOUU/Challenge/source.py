from Crypto.Util.number import getPrime, bytes_to_long,GCD
from gmpy2 import next_prime
import random
from SECRET import FLAG,BITS

assert BITS==1024
seed=getPrime(BITS)
def  customPrime(b):
    prime=seed
    for _ in range( len(BITS*'_')):prime=next_prime(prime)
    return prime

p,q=seed,customPrime(BITS)
n=p*q
values=[0x1001,0x100f]
c=bytes_to_long(FLAG)
for _ in range(10):
    e=values[random.randint(0,1)]
    c=pow(c,e,n)

print(f"c={c}")

print(f"n={n}")

