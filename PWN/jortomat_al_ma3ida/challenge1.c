//###################################################################################################################
//Compilation: gcc -fno-stack-protector -z execstack -no-pie -o challenge1 challenge1.c
//####################################################################################################################
#include <stdio.h>
#include <string.h>

// XOR key for encoding/decoding
const unsigned char XOR_KEY = 0xAA;

// Encoded flag using XOR key
unsigned char encoded_flag[] = {
    0xE9, 0xFE, 0xFC, 0xD1, 0xC2, 0xDB, 0xCE, 0xCE,
    0xCB, 0xC4, 0xF5, 0xCC, 0xC6, 0xCB, 0xCD, 0xD7
}; // Encoded version of "CTF{perfect_meal}"

#define FLAG_LENGTH (sizeof(encoded_flag) / sizeof(encoded_flag[0]))

void win() {
    // Decode the flag at runtime
    char flag[FLAG_LENGTH + 1];
    for (size_t i = 0; i < FLAG_LENGTH; i++) {
        flag[i] = encoded_flag[i] ^ XOR_KEY;
    }
    flag[FLAG_LENGTH] = '\0'; // Null-terminate the decoded flag

    printf("i feel like vomiting %s\n", flag);
}

void vuln() {
    char plate[64]; // Represents Mr. Ahmed's plate (buffer)
    printf("Welcome to the restaurant!\n");
    printf("Mr. Ahmed has a stomach ulcer (jortomat al ma3ida).\n");
    printf("He warned you: 'Don't give me more than 64 units of food, or my stomach will overflow!'\n");
    printf("Enter the amount of food to serve (max 64 units): ");

    gets(plate); // Vulnerable function (no bounds checking)
    printf("You served: %s\n", plate);

    if (strlen(plate) > 64) {
        printf("\nOh no! You overfed Mr. Ahmed!\n");
        printf("His stomach overflowed, and he's in pain. The kitchen is in chaos!\n");
    } else {
        printf("\nYou served the perfect amount of food!\n");
        printf("Mr. Ahmed is enjoying his meal.\n");
    }
}

int main() {
    vuln();
    return 0;
}
