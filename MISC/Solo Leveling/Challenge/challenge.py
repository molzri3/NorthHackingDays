import socket
import threading
import os

## the file name :     FLAG_PATH=./$(md5sum xi_l3ayba.txt | cut -c-32 | fold -w1 | shuf | head -n 20 | tr -d '\n').txt \ && mv xi_l3ayba.txt $FLAG_PATH




class FileValidationServer:
    def __init__(self, host="0.0.0.0", port=9999):
        self.host = host
        self.port = port

    def response(self, conn, message):
        """Send a message to the client."""
        conn.sendall(message + b"\n")  
    def handle_client(self, conn, addr):
        """Handle individual client connections."""
        file_name = b"xi_l3ayba.txt"

        try:
            conn.settimeout(30)  

            self.response(conn, b"Enter filename: ")
            i = 0
            while i < len(file_name):
                c = conn.recv(1)
                if not c: 
                    return
                elif c != file_name[i:i+1]:
                    self.response(conn, b"Incorrect filename.")
                    return
                i += 1

            if conn.recv(1) != b'\n': 
                self.response(conn, b"Incorrect filename.")
                return

            self.response(conn, b"Valid Filename :)")

            if not os.path.isfile(file_name.decode()):
                self.response(conn, b"File not found.")
                return
            
            self.response(conn, b"File validated successfully.")

            with open(file_name.decode(), "rb") as file:
                while chunk := file.read(1024):  
                    conn.sendall(chunk)

            self.response(conn, b"[END OF FILE]")

        except socket.timeout:
            self.response(conn, b"Timeout occurred. Connection closed.")
        except Exception as e:
            print(f"Error handling client {addr}: {e}")
        finally:
            conn.close()

    def start(self):
        """Start the multi-threaded server."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind((self.host, self.port))
            server.listen(5)
            print(f"Server listening on {self.host}:{self.port}")

            while True:
                conn, addr = server.accept()
                print(f"Connection from {addr}")
                client_thread = threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True)
                client_thread.start()

if __name__ == "__main__":
    server = FileValidationServer()
    server.start()
