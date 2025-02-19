# Description 
you have two steps to see the flag :) 

# Flag
NHD{#endek_M3a_HAdxi_Dyal_Misc}

# XOR Cipher Brute Force Solution

## Overview

This project demonstrates the decryption of an encoded message using a two-step process:

Base62 Decoding - The input string is first decoded from Base62 encoding.

XOR Brute Force Attack - A brute-force attack is performed to find the correct XOR key used to encrypt the message.

## Tools Used

CyberChef: A powerful online tool for encoding, decoding, and cryptanalysis.

XOR Brute Force: Used to attempt decryption with all possible single-byte XOR keys.

## Steps to Decrypt

### Decode from Base62:

The input string is first decoded using the Base62 algorithm.

### XOR Brute Force Attack:

The decoded result is XOR-ed against all possible single-byte keys (0x00 to 0xFF).

The output is analyzed to determine the correct key by identifying human-readable text.
