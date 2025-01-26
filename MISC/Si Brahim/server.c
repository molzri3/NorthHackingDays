#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>
#include <fcntl.h>
#include <pthread.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PATH_MAX 1024
#define PORT 8080
#define MAX_CLIENTS 10

void *handle_client(void *arg) {
    int client_socket = *(int *)arg;
    FILE *file;
    char path[PATH_MAX];
    char buffer[1024];
    char flag[1024];
    int attempts = 3;

    // Open the flag file
    file = fopen("flag.txt", "r");
    if (file == NULL) {
        perror("Failed to open flag.txt");
        close(client_socket);
        pthread_exit(NULL);
    }

    while (attempts > 0) {
        // Prompt the user for the path
        write(client_socket, "Enter the path to the flag: \n", 29);
        if (read(client_socket, path, sizeof(path) - 1) <= 0) {
            perror("Failed to read input");
            break;
        }

        // Null-terminate the path
        path[strcspn(path, "\n")] = 0;

        // Check for forbidden characters in the path
        if (strstr(path, "flag") != NULL || strstr(path, "..") != NULL || strstr(path, ".txt") != NULL) {
            write(client_socket, "The input contains forbidden characters.\n", 41);
            attempts--;
            if (attempts > 0) {
                snprintf(buffer, sizeof(buffer), "You have %d attempts remaining.\n", attempts);
                write(client_socket, buffer, strlen(buffer));
            }
            continue;
        }

        // Open the user-provided path
        FILE *file2 = fopen(path, "r");
        if (file2 == NULL) {
            perror("Failed to open the provided path");
            write(client_socket, "Failed to open the provided path.\n", 33);
            attempts--;
            if (attempts > 0) {
                snprintf(buffer, sizeof(buffer), "You have %d attempts remaining.\n", attempts);
                write(client_socket, buffer, strlen(buffer));
            }
            continue;
        }

        // Read from the user-provided file
        if (fgets(flag, sizeof(flag), file2) == NULL) {
            perror("Failed to read from the provided path");
            write(client_socket, "Failed to read from the provided path.\n", 38);
            fclose(file2);
            attempts--;
            if (attempts > 0) {
                snprintf(buffer, sizeof(buffer), "You have %d attempts remaining.\n", attempts);
                write(client_socket, buffer, strlen(buffer));
            }
            continue;
        }
        fclose(file2);

        // Print the flag to the client
        snprintf(buffer, sizeof(buffer), "The flag is: %s", flag);
        write(client_socket, buffer, strlen(buffer));

        // Close the client socket
        close(client_socket);
        pthread_exit(NULL);
    }

    if (attempts == 0) {
        write(client_socket, "You have used all your attempts. Closing connection.\n", 53);
    }

    // Close the client socket
    close(client_socket);
    pthread_exit(NULL);
}

int main() {
    int server_socket, client_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);
    pthread_t threads[MAX_CLIENTS];
    int i = 0;

    // Ignore SIGPIPE to prevent server crash on client disconnect
    signal(SIGPIPE, SIG_IGN);

    // Create socket
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket < 0) {
        perror("Socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Bind socket
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);
    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Bind failed");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    // Listen for connections
    if (listen(server_socket, MAX_CLIENTS) < 0) {
        perror("Listen failed");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    printf("Server listening on port %d...\n", PORT);

    while (1) {
        // Accept a new connection
        client_socket = accept(server_socket, (struct sockaddr *)&client_addr, &client_len);
        if (client_socket < 0) {
            perror("Accept failed");
            continue;
        }

        printf("New client connected: %s:%d\n", inet_ntoa(client_addr.sin_addr), ntohs(client_addr.sin_port));

        // Create a new thread for the client
        if (pthread_create(&threads[i], NULL, handle_client, &client_socket) != 0) {
            perror("Thread creation failed");
            close(client_socket);
        }

        // Detach the thread to handle its own cleanup
        pthread_detach(threads[i]);

        i = (i + 1) % MAX_CLIENTS;
    }

    close(server_socket);
    return 0;
}