# Description
9etra 9etra ye7mel lwad , if you did understand this quote you will solve this challenge .

files to upload : challenge.py

# Byte-by-Byte Filename Brute Force Exploit

## Overview

This script exploits a vulnerability where the target system reads input byte by byte, allowing a brute-force attack to determine a valid filename character by character. Once the filename is identified, the script retrieves and prints the file's content.

## How It Works

### Brute-Force Filename:

Tries all possible characters (a-z, 0-9, ._-).

If a character is valid, the system waits for the next input.

If a character is invalid, an error response is received.

This behavior allows step-by-step reconstruction of the filename.

### Retrieve File Content:

Sends the full filename to the server.

Receives and prints the file contents.
