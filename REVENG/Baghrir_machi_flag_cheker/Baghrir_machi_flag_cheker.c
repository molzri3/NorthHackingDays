#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <stdint.h>
#define MAX_LEN 100


void fail() {
    printf("Mseemnaaa nooooooo 😈\n");
}

void win() {
    printf("Baghiiraaaa yeaaaayyy\n");
}

void Baghrira_chamaliya(const char *coupon) {
    int checks = 0;
    if (coupon[1]+coupon[6]+coupon[3]+coupon[5]+coupon[14]+coupon[36] == 562) checks++;
    if (coupon[35]+coupon[2]+coupon[33] == 245) checks++;
    if (coupon[34]+coupon[26]+coupon[24] == 228) checks++;
    if (coupon[28]+coupon[1]+coupon[36]+coupon[0]+coupon[21]+coupon[6]+coupon[16]+coupon[20] == 667) checks++;
    if (coupon[34]+coupon[20]+coupon[34]+coupon[2]+coupon[12]+coupon[15] == 450) checks++;
    if (coupon[23]+coupon[36]+coupon[8] == 323) checks++;
    if (coupon[15]+coupon[13]+coupon[14]+coupon[16]+coupon[31]+coupon[3]+coupon[32]+coupon[15] == 748) checks++;
    if (coupon[13]+coupon[2] == 120) checks++;
    if (coupon[6]+coupon[23]+coupon[32]+coupon[0]+coupon[19] == 467) checks++;
    if (coupon[15]+coupon[17]+coupon[36]+coupon[6]+coupon[26]+coupon[25] == 542) checks++;
    if (coupon[13]+coupon[28]+coupon[26]+coupon[8] == 304) checks++;
    if (coupon[23]+coupon[4]+coupon[19]+coupon[13]+coupon[11]+coupon[33] == 518) checks++;
    if (coupon[23]+coupon[2] == 177) checks++;
    if (coupon[21]+coupon[21]+coupon[1]+coupon[32]+coupon[6]+coupon[29]+coupon[14]+coupon[34]+coupon[34] == 780) checks++;
    if (coupon[1]+coupon[16]+coupon[5]+coupon[34] == 258) checks++;
    if (coupon[3]+coupon[17]+coupon[34]+coupon[1]+coupon[21]+coupon[36] == 616) checks++;
    if (coupon[10]+coupon[28]+coupon[13]+coupon[31]+coupon[10]+coupon[33]+coupon[21]+coupon[14] == 662) checks++;
    if (coupon[22]+coupon[27]+coupon[25]+coupon[18]+coupon[8] == 430) checks++;
    if (coupon[11]+coupon[32]+coupon[28]+coupon[8]+coupon[35]+coupon[11] == 597) checks++;
    if (coupon[24]+coupon[19]+coupon[32]+coupon[29]+coupon[15]+coupon[5]+coupon[27]+coupon[14] == 729) checks++;
    if (coupon[25]+coupon[11] == 177) checks++;
    if (coupon[31]+coupon[33]+coupon[26]+coupon[30]+coupon[14]+coupon[13]+coupon[19]+coupon[32]+coupon[11] == 797) checks++;
    if (coupon[29]+coupon[20]+coupon[14] == 213) checks++;
    if (coupon[4]+coupon[1] == 159) checks++;
    if (coupon[5]+coupon[31]+coupon[28] == 280) checks++;
    if (coupon[13]+coupon[32] == 147) checks++;
    if (coupon[11]+coupon[16] == 147) checks++;
    if (coupon[35]+coupon[1]+coupon[22]+coupon[9]+coupon[17]+coupon[12]+coupon[22]+coupon[9]+coupon[29] == 734) checks++;
    if (coupon[18]+coupon[22]+coupon[36]+coupon[22] == 318) checks++;
    if (coupon[32]+coupon[6]+coupon[8]+coupon[26]+coupon[27]+coupon[8]+coupon[26] == 566) checks++;
    if (coupon[6]+coupon[11]+coupon[11]+coupon[6]+coupon[7]+coupon[27]+coupon[29]+coupon[12]+coupon[22] == 681) checks++;
    if (coupon[7]+coupon[35]+coupon[23] == 272) checks++;
    if (coupon[6]+coupon[2]+coupon[12] == 216) checks++;
    if (coupon[19]+coupon[26]+coupon[1]+coupon[27]+coupon[0]+coupon[19]+coupon[5] == 586) checks++;
    if (coupon[28]+coupon[10]+coupon[31]+coupon[18]+coupon[21]+coupon[17] == 586) checks++;
    if (coupon[34]+coupon[30] == 181) checks++;
    if (coupon[1]+coupon[12]+coupon[14]+coupon[8]+coupon[28]+coupon[5] == 511) checks++;


    if (checks == 37) {
        win();
        return;
    }
    fail();
    return;
}

int main() {
    char wasfa_Si7riya[MAX_LEN];
    printf("Dekhel lwasfa :\n");
    scanf("%99s", wasfa_Si7riya); 

    Baghrira_chamaliya(wasfa_Si7riya);
    return 0;
}
