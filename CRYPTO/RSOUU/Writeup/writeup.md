# RSOUU

## Source Code
![](../Challenge/source.py)
This challenge is a classic RSA problem with multiple random public key encryptions. 
### Factorizing `n`
The customPrime function generates the second prime `q` so close to `p` that we can try Fermat's factorization method to factorize `n`.
### Brute-forcing the Public Key
After factorizing `n`, we need to brute force the public key, which has `2^10` possibilities.
## Solution Code
![](solve.py)
