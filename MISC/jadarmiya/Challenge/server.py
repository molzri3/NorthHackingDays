import os
import socket
import subprocess
import threading
import random
import string

def generate_random_filename():
    return os.path.join(os.getcwd(), "code_" + ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + ".c")

def compile_and_run(input_file):
    output_file = input_file.replace(".c", "")
    compile_command = f"gcc {input_file} -o {output_file}"
    compile_result = os.system(compile_command)

    if compile_result == 0:
        print(f"Compilation successful: {output_file}")
        try:
            result = subprocess.check_output(output_file, stderr=subprocess.STDOUT, shell=True)
            return result.decode("utf-8")
        except subprocess.CalledProcessError as e:
            return f"Program execution failed: {e.output.decode('utf-8')}"
    else:
        return "Compilation failed. Please call the owner of the challenge."

def handle_client(client_socket):
    try:
        client_socket.send("Enter your code: \n".encode())
        input_code = client_socket.recv(1024).decode("utf-8").strip()
        
        file_name = generate_random_filename()
        print(file_name)
        
        with open(file_name, "w") as file:
            for ch in input_code:
                if ch in ['[', ']', '{', '}', '\\', '/' , '#']:
                    client_socket.send("Ma3endek zher abana !!\n".encode())
                    return
                else:
                    file.write(ch)
        
        result = compile_and_run(file_name)
        client_socket.send(f"{result}\n".encode())
        
        os.remove(file_name)
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
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server("0.0.0.0", 9999)
