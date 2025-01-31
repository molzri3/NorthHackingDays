import socket
import threading
import os

class FileValidationServer:
    def __init__(self, host="0.0.0.0", port=9999):
        self.host = host
        self.port = port

    def response(self, conn, message):
        """Send a message to the client."""
        conn.sendall(message + b"\n")  # Ensure newline for proper display in netcat

    def handle_client(self, conn, addr):
        """Handle individual client connections."""
        file_name = b"480d38fd77e72471580a.txt"

        try:
            conn.settimeout(30)  # ✅ Replaces `signal.alarm(30)`

            self.response(conn, b"Enter filename: ")
            i = 0
            while i < len(file_name):
                c = conn.recv(1)
                if not c:  # Client disconnected
                    return
                elif c != file_name[i:i+1]:
                    self.response(conn, b"Incorrect filename.")
                    return
                i += 1

            if conn.recv(1) != b'\n':  # Ensure proper newline
                self.response(conn, b"Incorrect filename.")
                return

            self.response(conn, b"Valid Filename :)")

            # Check if file exists
            if not os.path.isfile(file_name.decode()):
                self.response(conn, b"File not found.")
                return
            
            self.response(conn, b"File validated successfully.")

            # Send file content in chunks
            with open(file_name.decode(), "rb") as file:
                while chunk := file.read(1024):  # Read in 1KB chunks
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
