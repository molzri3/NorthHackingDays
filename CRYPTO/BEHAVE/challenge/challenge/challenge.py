import socket
from hidden import FLAG

def repeat_to_length(data: bytes, length: int) -> bytes:
    return (data * ((length // len(data)) + 1))[:length]

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes([x ^ y for x, y in zip(a, b)])

def handle_connection(conn: socket.socket):
    count = 1  
    try:
        while True:
            conn.sendall(b"Enter your input: ")
            user_input = conn.recv(1024).strip()
            if not user_input:
                conn.sendall(b"No input received. Goodbye!\n")
                break

            xored_input = xor_bytes(user_input, bytes([count]))
            
            repeated_input = repeat_to_length(xored_input, len(FLAG))
            result = xor_bytes(repeated_input, FLAG)
            
            hex_result = result.hex()
            
            conn.sendall(hex_result.encode() + b'\n')
            count += 1
    finally:
        conn.close()

def main():
    host = "0.0.0.0"
    port = 4444

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            print(f"Connection accepted from {addr}")
            handle_connection(conn)

if __name__ == "__main__":
    main()
