
//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Compilation: gcc -no-pie -fno-stack-protector -o vuln vuln.c --static -z execstack ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
 
#define FLAGSIZE_MAX 64
 
char flag[FLAGSIZE_MAX];
 
void sigsegv_handler(int sig) {
    printf("**********hak0 had lflag olmra jaya kono kathalaw:");
    printf("%s", flag);
    printf("**********");
    fflush(stdout);
    exit(3);
}
 
void vuln(){
        char buf1[333];
	printf("[+]3tini_n3tik: ");
	fflush(stdout);
	gets(buf1); 
	printf("[+]ah ah ch7al z9ramin , sf ghayroha ......\n");
  

}
 
int main(int argc, char **argv){
    
    FILE *f = fopen("/flag.txt","r");
    if (f == NULL) {
        printf("%s %s", "Please create 'flag.txt' in this directory with your",
                        "own debugging flag.\n");
        exit(0);
    }
    
    fgets(flag,FLAGSIZE_MAX,f);
    signal(SIGSEGV, sigsegv_handler); // Set up signal handler
    
    
    while(1){
    	vuln();
    }
    return 0;
}
