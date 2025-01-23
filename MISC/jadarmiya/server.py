import os
import socket
import subprocess
import threading

def compile_and_run(input_file):
    compile_command = f"gcc {input_file} -o code"
    compile_result = os.system(compile_command)

    if compile_result == 0:
        print("Compilation successful.")
        print("Running the program...")
        
        # Capture the output of ./code
        try:
            result = subprocess.check_output("./code", stderr=subprocess.STDOUT, shell=True)
            return result.decode("utf-8")
        except subprocess.CalledProcessError as e:
            return f"Program execution failed: {e.output.decode('utf-8')}"
    else:
        return "Compilation failed. Please check the source code."

def handle_client(client_socket):
    try:
        # Send a prompt message to the client
        client_socket.send("Enter your code: \n".encode())

        # Receive the input code from the client
        input_code = client_socket.recv(1024).decode("utf-8").strip()

        # Open the file to write the C code
        with open("code.c", "w") as file:
            for ch in input_code:
                if ch in ['[', ']', '{', '}', '\\', '/' , '#']:
                    client_socket.send("Ma3endek zher abana !!\n".encode())
                    return
                else:
                    file.write(ch)

        # Compile and run the C code and capture the result
        result = compile_and_run("code.c")
        client_socket.send(f"{result}\n".encode())
    except Exception as e:
        client_socket.send(f"Error: {str(e)}\n".encode())
    finally:
        client_socket.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        
        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server("0.0.0.0", 9999)