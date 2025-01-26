from pwn import *
from Crypto.Util.number import *

context.log_level = 'debug'
FLAG = ""

while True:
    conn = remote('localhost', 5551)
    conn.recvuntil(b'p: ')
    p = int(conn.recvline().decode())

    if p % 4 == 3:
        legendre = lambda a: pow(a, (p - 1) // 2, p) == 1

        while True:
            try:
                conn.recvuntil(b'red pill')
                conn.recvline()
                r = int(conn.recvline().decode())
                b = int(conn.recvline().decode())
                conn.recv()

                if legendre(r):
                    conn.sendline(str(b).encode())
                else:
                    conn.sendline(str(r).encode())

                f = conn.recvline().decode().strip()
                FLAG += f
                # print(FLAG)

            except:
                conn.close()
                m = int(FLAG, 2)
                print(long_to_bytes(m))
                exit()
    else:
        conn.close()

