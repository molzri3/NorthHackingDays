//###################################################################################################################
//Compilation: gcc -fno-stack-protector -z execstack -no-pie -o challenge1 challenge1.c
//####################################################################################################################

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <fcntl.h> 

// Modified win() function to write the flag through the socket
void win(int sock) {
    // Open the flag.txt file
    int fd = open("flag.txt", O_RDONLY);
    if (fd < 0) {
        perror("open");
        const char *error_msg = "\nError: Could not open flag.txt.\n";
        write(sock, error_msg, strlen(error_msg));
        return;
    }

    // Read the flag from the file
    char flag[128]; // Adjust size as needed
    ssize_t bytes_read = read(fd, flag, sizeof(flag) - 1);
    if (bytes_read < 0) {
        perror("read");
        const char *error_msg = "\nError: Could not read flag.txt.\n";
        write(sock, error_msg, strlen(error_msg));
        close(fd);
        return;
    }
    flag[bytes_read] = '\0'; // Null-terminate the read data
    close(fd);

    // Send the flag through the socket
    const char *success_msg = "\nCongratulations! You served the perfect meal!\n"
                              "Mr. Ahmed is happy and gives you the flag: ";
    write(sock, success_msg, strlen(success_msg));
    write(sock, flag, strlen(flag));
    write(sock, "\n", 1);
}

void vuln(int sock) {
    char plate[64]; // Represents Mr. Ahmed's plate (buffer)
    char buffer[128];

    // Send welcome message with the address of win()
    char welcome_msg[256];
    snprintf(welcome_msg, sizeof(welcome_msg),
             "Welcome to the restaurant!\n"
             "Mr. Ahmed has a stomach ulcer (jortomat al ma3ida).\n"
             "He warned you: 'Don't give me more than 64 units of food, or my stomach will overflow!'\n"
             "Address of win(): %p\n"  // Include the address of win()
             "Enter the amount of food to serve (max 64 units): ",
             win);
    write(sock, welcome_msg, strlen(welcome_msg));

    // Read input from the client
    ssize_t bytes_read = read(sock, buffer, sizeof(buffer) - 1);
    if (bytes_read < 0) {
        perror("read");
        return;
    }
    buffer[bytes_read] = '\0'; // Null-terminate the input

    // Copy input to the vulnerable buffer
    strcpy(plate, buffer);

    // Send response to the client
    char response[256];
    snprintf(response, sizeof(response), "You served: %s\n", plate);
    write(sock, response, strlen(response));

    if (strlen(plate) > 64) {
        const char *overflow_msg = "\nOh no! You overfed Mr. Ahmed!\n"
                                   "His stomach overflowed, and he's in pain. The kitchen is in chaos!\n";
        write(sock, overflow_msg, strlen(overflow_msg));

        // Call win() if the buffer is overflowed
        win(sock);
    } else {
        const char *success_msg = "\nYou served the perfect amount of food!\n"
                                  "Mr. Ahmed is enjoying his meal.\n";
        write(sock, success_msg, strlen(success_msg));
    }
}

int main() {
    int server_sock, client_sock;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_len = sizeof(client_addr);

    // Create socket
    server_sock = socket(AF_INET, SOCK_STREAM, 0);
    if (server_sock < 0) {
        perror("socket");
        return 1;
    }

    // Bind socket to port
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(12345); // Use any port you like

    if (bind(server_sock, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("bind");
        close(server_sock);
        return 1;
    }

    // Listen for connections
    if (listen(server_sock, 5) < 0) {
        perror("listen");
        close(server_sock);
        return 1;
    }

    printf("Server is listening on port 12345...\n");

    // Accept connections
    while (1) {
        client_sock = accept(server_sock, (struct sockaddr *)&client_addr, &client_len);
        if (client_sock < 0) {
            perror("accept");
            continue;
        }

        printf("Client connected\n");

        // Handle client
        vuln(client_sock);

        // Close client socket
        close(client_sock);
        printf("Client disconnected\n");
    }

    // Close server socket (unreachable in this example)
    close(server_sock);
    return 0;
}

