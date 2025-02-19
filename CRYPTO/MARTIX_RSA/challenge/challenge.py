from secret_matrix import SECRET_MATRIX
import numpy as np
from Crypto.Util.number import getPrime


def encrypt_flag(flag):
    pad_len = (3 - (len(flag) % 3)) % 3
    padded = flag + '\x00' * pad_len
    matrix = np.array([ord(c) for c in padded], dtype=np.int64).reshape(-1, 3)
    secret_matrix = SECRET_MATRIX.astype(np.int64)
    encrypted = np.dot(matrix, secret_matrix) % 256  
    return encrypted.astype(np.uint8).flatten().tobytes()

def rsa_encrypt_matrix():
    p = getPrime(60)
    q = getPrime(60)
    N = p * q
    e = 65537
    
    encrypted = [pow(int(x), e, N) for x in SECRET_MATRIX.flatten()]

    return N, e, encrypted

if __name__ == "__main__":
    with open("challenge\\flag.txt", "r") as f:
        flag = f.read().strip()
    
    flag_ciphertext = encrypt_flag(flag)
    N, e, rsa_matrix = rsa_encrypt_matrix()
    
    with open("output.txt", "wb") as f:
        f.write(flag_ciphertext.hex().encode())
        f.write(f"\n\nRSA_N={N}\nRSA_e={e}\nMATRIX=".encode())
        f.write(','.join(map(str, rsa_matrix)).encode())
