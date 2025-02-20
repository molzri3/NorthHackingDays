//###################################################################################################################
//Compilation: gcc -fno-stack-protector -z execstack -no-pie -o challenge1 challenge1.c --static
//####################################################################################################################

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

#define BUFSIZE 100
#define FLAGSIZE 64

void win(unsigned int arg1, unsigned int arg2) {
    char buf[FLAGSIZE];
    FILE *f = fopen("flag.txt", "r");
    if (f == NULL) {
        printf("Please create 'flag.txt' in this directory with your flag.\n");
        exit(0);
    }
    fgets(buf, FLAGSIZE, f);
    if (arg1 != 0xCAFEF00D)
        return;
    if (arg2 != 0xF00DF00D)
        return;
    printf("[+] Emm hadchi bnin lay3tik saha, hahowa lflag :%s", buf);
}

void vuln(){
    char buf[BUFSIZE];
    /* Vulnerable: no bounds checking */
    gets(buf);
    printf("[!] Ach had lhala ,Fin t3alemti tyab ?!\n");
}

int main(int argc, char **argv){
    setvbuf(stdout, NULL, _IONBF, 0);
    
    gid_t gid = getegid();
    setresgid(gid, gid, gid);
    
    puts("[+] Fiya jou3, kayn maytkal ?");
    vuln();
    return 0;
}
