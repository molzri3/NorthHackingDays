#include <stdio.h>
#include <string.h>

// Constants for the obfuscation process
#define SHIFT1 5
#define XOR_KEY 0x4F
#define SHIFT2 3

// Obfuscated value
int obfuscated_value[] = {19, 40, 59, 125, 6, 59, 123, 55, 36, 57, 52};
#define OBFUSCATED_LEN (sizeof(obfuscated_value) / sizeof(obfuscated_value[0]))

// Function to obfuscate the input string
void obfuscate(const char *input, int *output) {
    for (int i = 0; i < OBFUSCATED_LEN; i++) {
        // First shift
        int shifted = input[i] + SHIFT1;
        // XOR operation
        int xored = shifted ^ XOR_KEY;
        // Second shift
        output[i] = xored + SHIFT2;
    }
}

int main() {
    char input[OBFUSCATED_LEN + 1];
    int obfuscated_input[OBFUSCATED_LEN];

    printf("11 chars to put so chose wisely wla ghayarha:\n");
    scanf("%11s", input);

    // Validate input length
    if (strlen(input) != OBFUSCATED_LEN) {
        printf("Wa khoya input khsa tkon fiha 11 caracters wax makatfhmx\n");
        return 1;
    }

    // Obfuscate the user input
    obfuscate(input, obfuscated_input);

    // Compare with the obfuscated value
    for (int i = 0; i < OBFUSCATED_LEN; i++) {
        if (obfuscated_input[i] != obfuscated_value[i]) {
            printf("Waaa Raaab l3ali Noooo\n");
            return 1;
        }
    }

    printf("Wa 3la slama Sir submitih Yessss\n");
    return 0;
}
