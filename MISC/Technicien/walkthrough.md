## **Walkthrough:  Technicien**

This hardware-based cryptography challenge involves an encryption algorithm implemented in an embedded system, such as an **Arduino** or another microcontroller. The encryption process follows a structured approach using **bitwise XOR operations using MM74HC** to obfuscate the original message (flag). Below, we'll break down how to analyze, reverse-engineer, and decrypt the challenge step by step.

---

## **1. Understanding the Encryption Process**

From the problem statement, we know that the encryption algorithm applies **XOR transformations** to 4-bit chunks of the original data. The encryption scheme follows this pattern:

- Each **4-bit segment** is XORed against a predefined sequence:
    - **1st bit:** XOR with `0`
    - **2nd bit:** XOR with `1`
    - **3rd bit:** XOR with `0`
    - **4th bit:** XOR with `1`

This means that for each 4-bit segment, the encryption operation flips the **second** and **fourth** bits while keeping the first and third bits unchanged.

To reconstruct the original data, we must **reverse** this operation, which is done in the decryption script.

---

## **2. Analyzing the Encrypted Data**

The encrypted message is represented as a sequence of 4-bit binary strings:

```
0001 1011 0001 1101 0001 0001 0010 1110 ...
```

Each pair of 4-bit chunks represents a single **8-bit ASCII character** in the flag. Our goal is to reverse the XOR operation to restore the original ASCII values.

---

## **3. Implementing the Decryption Logic**

We use the Python script to decrypt the message. Here's how it works:

### **Step 1: Reverse the XOR Operation**

We implement the function `xor(bits)`, which takes an encrypted **4-bit segment** and reverses the encryption:

```python
def xor(bits):
    """ XOR the bits according to the reverse logic. """
    ret = ""
    ret += str(int(bits[0]) ^ 0)  # XOR the first bit with 0 (no change)
    ret += str(int(bits[1]) ^ 1)  # XOR the second bit with 1 (flip)
    ret += str(int(bits[2]) ^ 0)  # XOR the third bit with 0 (no change)
    ret += str(int(bits[3]) ^ 1)  # XOR the fourth bit with 1 (flip)
    return ret
```

This restores the original 4-bit values.

---

### **Step 2: Process Each 8-bit Character**

The function `decrypt()` takes the encrypted message and reconstructs each character:

```python
def decrypt(encrypted_output):
    """ Decrypt the encrypted binary output to retrieve the flag. """
    decrypted_flag = []  # Store the decrypted flag

    # Iterate through the encrypted output, processing two 4-bit chunks at a time
    for i in range(0, len(encrypted_output), 2):
        part1 = encrypted_output[i]  # First 4-bit part
        part2 = encrypted_output[i+1]  # Second 4-bit part

        decrypted_byte = xor(part1) + xor(part2)  # Reconstruct the 8-bit character
        decrypted_flag.append(chr(int(decrypted_byte, 2)))  # Convert to ASCII

    return ''.join(decrypted_flag
```

- The script **pairs** two decrypted 4-bit parts to form a complete **8-bit ASCII character**.
- Then, it **converts** the 8-bit binary into a character using `chr(int(binary, 2))`.
- The final decrypted characters are concatenated to reconstruct the original flag.

---

## **4. Running the Decryption Script**

Now, we execute the script to obtain the original flag:

```python
encrypted_output = [
    "0001", "1011", "0001", "1101", "0001", "0001", "0010", "1110",
    "0001", "1101", "0110", "0001", "0001", "0100", "0000", "0111",
    "0001", "0001", "0000", "0010", "0110", "0001", "0001", "0100",
    "0000", "0111", "0110", "0110", "0000", "1010", "0001", "1100",
    "0000", "0110", "0000", "1010", "0001", "1001", "0001", "1100",
    "0001", "0011", "0001", "0000", "0000", "1010", "0001", "0100",
    "0001", "1011", "0001", "0001", "0000", "1010", "0001", "1001",
    "0001", "1100", "0001", "0011", "0001", "0000", "0000", "1010",
    "0001", "1100", "0000", "0110", "0000", "1010", "0000", "1101",
    "0001", "1010", "0000", "0111", "0010", "1000"
]

decrypted_flag = decrypt(encrypted_output)

print(f"Decrypted Flag: {decrypted_flag}")
```

This will output the **original flag**. 

Check the [solution.py](http://solution.py) for the full version of code!
