import numpy as np
from Crypto.Util.number import inverse

def decrypt_flag(ciphertext, matrix):
    matrix = matrix.astype(np.int64)
    det = int(np.round(np.linalg.det(matrix)))
    print(f"[Debug] Determinant: {det}, mod 256: {det % 256}")
    
    try:
        det_inv = pow(det % 256, -1, 256)
    except ValueError:
        raise Exception("Matrix is not invertible modulo 256 (determinant has no inverse)")
    
    adjugate = np.round(np.linalg.inv(matrix) * det).astype(np.int64)
    
    matrix_inv = (adjugate * det_inv) % 256
    print("[Debug] Inverse Matrix:\n", matrix_inv)
    
    ciphertext_matrix = np.frombuffer(ciphertext, dtype=np.uint8).reshape(-1, 3)
    decrypted = np.dot(ciphertext_matrix, matrix_inv) % 256
    decrypted_bytes = decrypted.astype(np.uint8).flatten().tobytes()
    
    print("[Debug] Decrypted bytes (hex):", decrypted_bytes.hex())
    
    clean_bytes = decrypted_bytes.rstrip(b'\x00')
    return clean_bytes.decode('latin-1')

def main():
    with open("output.txt", "rb") as f:
        data = f.read().split(b"\n\nRSA_N=")
    
    ciphertext = data[0]
    params = data[1].decode().split('\n')
    
    N = int(params[0])
    e = int(params[1].split('=')[1])
    rsa_matrix = list(map(int, params[2].split('=')[1].split(',')))

    # prime factors (player should factor N)
    p = 123456789101112167
    q = 123456789101112109
    phi = (p-1) * (q-1)
    d = inverse(e, phi)
    secret_values = [pow(c, d, N) % 256 for c in rsa_matrix]
    secret_matrix = np.array(secret_values, dtype=np.uint8).reshape(3, 3)
    print("[Debug] Decrypted Secret Matrix:\n", secret_matrix)
    
    flag = decrypt_flag(ciphertext, secret_matrix)
    print("\nFlag:", flag)

if __name__ == "__main__":
    main()