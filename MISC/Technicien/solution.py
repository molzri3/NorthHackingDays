def xor(bits):
    """ XOR the bits according to the reverse logic. """
    ret = ""
    ret += str(int(bits[0]) ^ 0)  # XOR the first bit with 0
    ret += str(int(bits[1]) ^ 1)  # XOR the second bit with 1
    ret += str(int(bits[2]) ^ 0)  # XOR the third bit with 0
    ret += str(int(bits[3]) ^ 1)  # XOR the fourth bit with 1
    return ret

def decrypt(encrypted_output):
    """ Decrypt the encrypted binary output to retrieve the flag. """
    decrypted_flag = []  # Store the decrypted flag
    
    # Iterate through the encrypted output
    for i in range(0, len(encrypted_output), 2):
        # Get the 4-bit parts
        part1 = encrypted_output[i]
        part2 = encrypted_output[i+1]
        
        # XOR the 4-bit parts to get the original 8-bit value
        decrypted_byte = xor(part1) + xor(part2)
        
        # Convert the 8-bit binary back to the character
        decrypted_flag.append(chr(int(decrypted_byte, 2)))
    
    return ''.join(decrypted_flag)

# Encrypted output from the previous result
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

# Decrypt the encrypted output
decrypted_flag = decrypt(encrypted_output)

# Print the decrypted flag
print(f"Decrypted Flag: {decrypted_flag}")
