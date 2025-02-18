#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/wait.h>

#define PORT 4444
#define BUFFER_SIZE 1024

void sanitize_command(char *cmd) {
    const char *blocked_chars = "dev#%$&*()_+={}[]<>\\;|`'\"";
    
    for (size_t i = 0; i < strlen(cmd); i++) {
        if (strchr(blocked_chars, cmd[i]) != NULL) {
            strcpy(cmd, "echo 'Error: Command contains restricted characters.'");
            return;
        }
    }
}

void *handle_client(void *arg) {
    int client_socket = *((int *)arg);
    char buffer[BUFFER_SIZE];

    // Send initial prompt
    send(client_socket, "Connected to the server.\nEnter your command: ", 45, 0);

    while (1) {
        // Clear buffer
        memset(buffer, 0, BUFFER_SIZE);

        // Receive command from client
        ssize_t bytes_received = recv(client_socket, buffer, sizeof(buffer) - 1, 0);
        if (bytes_received <= 0) {
            break;  // Client disconnected
        }

        buffer[bytes_received] = '\0'; // Null-terminate the string
        sanitize_command(buffer);      // Filter the command

        // Execute command using system shell
        FILE *fp = popen(buffer, "r");
        if (fp == NULL) {
            send(client_socket, "Command execution failed\n", 25, 0);
            continue;
        }

        // Send output back to client
        char output[BUFFER_SIZE];
        while (fgets(output, sizeof(output), fp) != NULL) {
            send(client_socket, output, strlen(output), 0);
        }

        pclose(fp);

        // Send next command prompt
        send(client_socket, "\nEnter your command: ", 22, 0);
    }

    close(client_socket);
    return NULL;
}

int main() {
    int server_socket, client_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t addr_len = sizeof(client_addr);

    // Create socket
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == -1) {
        perror("Socket creation failed");
        exit(1);
    }

    // Configure server address
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    // Bind socket
    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
        perror("Bind failed");
        exit(1);
    }

    // Start listening
    if (listen(server_socket, 5) == -1) {
        perror("Listen failed");
        exit(1);
    }

    printf("Server listening on port %d...\n", PORT);

    while (1) {
        // Accept client connection
        client_socket = accept(server_socket, (struct sockaddr *)&client_addr, &addr_len);
        if (client_socket == -1) {
            perror("Accept failed");
            continue;
        }

        // Create a thread for each client
        pthread_t thread;
        if (pthread_create(&thread, NULL, handle_client, &client_socket) != 0) {
            perror("Thread creation failed");
            close(client_socket);
        }
    }

    close(server_socket);
    return 0;
}
