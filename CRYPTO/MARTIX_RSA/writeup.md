# CTF Challenge Writeup: Matrix RSA

**Challenge Name**: Matrix RSA  
**Category**: Cryptography  
**Difficulty**: Medium  
**Provided Files**:  
- `challenge.py` (encryption script)  
- `output.txt` (encrypted flag + RSA parameters)  

---

## Challenge Overview

This challenge combines **matrix-based encryption** with **RSA** to protect the secret transformation . The flag is encrypted using modular matrix multiplication, and the secret matrix is further protected by RSA encryption. Players must:

1. Factor the RSA modulus `N` to recover the secret matrix  
2. Compute the modular inverse of the matrix  
3. Reverse the encryption process to reveal the flag  

---

## Solution Walkthrough

### Step 1: Analyze the Encryption Scheme

The encryption process in `challenge.py` works as follows:  
1. **Pad the Flag**: The input flag is padded with null bytes (`\x00`) to make its length divisible by 3.  
2. **Matrix Conversion**: ASCII values are arranged into a matrix with 3 columns.  
3. **Matrix Multiplication**: The plaintext matrix is multiplied by a secret 3×3 matrix modulo 256.  
4. **RSA Protection**: The secret matrix elements are individually encrypted using RSA.  

### Step 2: Extract RSA Parameters

From `output.txt`:  
- Encrypted flag (bytes)  
- RSA modulus `N`  
- Public exponent `e=65537`  
- RSA-encrypted matrix values  


### Step 3: Factor the RSA Modulus

**Key Insight**: The primes are consecutive numbers:  

    p = 123456789101112167
    q = 123456789101112109


### Step 4: Decrypt the Secret Matrix

1. **Compute RSA Private Key**: claculates phi and d.  
2. **Decrypt Matrix Elements**: Each element of the secret matrix should be decrypted
```
rsa_matrix = [123456789, 987654321, ...]  # From output.txt
secret_values = [pow(c, d, N) % 256 for c in rsa_matrix]
secret_matrix = np.array(secret_values, dtype=np.uint8).reshape(3, 3)
```
### Step 6: Invert the Matrix and Decrypt the Flag

1. **Matrix Inversion Modulo 256**:

```
matrix = secret_matrix.astype(np.int64)
det = int(np.round(np.linalg.det(matrix))) % 256
det_inv = pow(det, -1, 256)  # Modular inverse

adjugate = np.round(np.linalg.inv(matrix) * det).astype(np.int64)
matrix_inv = (adjugate * det_inv) % 256
```

2. **Decrypt the Flag**:

```
ciphertext = ...  # From output.txt
ciphertext_matrix = np.frombuffer(ciphertext, dtype=np.uint8).reshape(-1, 3)
decrypted = np.dot(ciphertext_matrix, matrix_inv) % 256
flag_bytes = bytes(decrypted.flatten()).rstrip(b'\x00')
flag = flag_bytes.decode('latin-1')  # Supports all 256 bytes
```

## FINAL FLAG 

CTF{linear_algebra_meets_rsa}


