#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

struct Data {
    char buffer[32];
    void (*func)();
};

void win() {
    printf("You win! Here's the flag: ");
    system("/bin/cat /flag.txt");
}

void default_func() {
    printf("Default function called.\n");
}

int main() {
    struct Data *data = malloc(sizeof(struct Data));
    data->func = default_func;

    printf("Enter your payload: ");
    fflush(stdout);

    // Vulnerable read - allows heap buffer overflow
    read(0, data->buffer, 64);  // Reads 64 bytes into 32-byte buffer

    data->func();
    free(data);
    return 0;
}
