#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

// Define 10 sentences
const char *sentences[] = {
    "Hala lala w hala lala Hala lala w hala lala \nTbghi tjini b survet    ttt w fo9 x3ar lcaskit",

    "W Ghansetefkom kamlin mn fo9 Chewaya ooooo mn fo9 chewaya eyyyy",

    "2inta m3alim w 7na menak nt3alim \n nskot w 2inta mawjod manerda ntkalem ",

    "Halib Hal Halib   Halib halib Hal Halib \n Khoutibi khouya sghir bghiy kimi   Tlaqite bih  khouya koulou   coussou coussou salam hala bouyé \n Khouya hek lilinifi   Khouya hek lilinifi Khouya hek lilinifi   Khouya khoud lbanana",

    "Cessssst fini bye bye Yal medrassa   w 2akhiiir 3am ya naja7 yalmeknasa \n s7****** SI M3A fwaasa    ila s9et n3ich f bergasa ",

    "Chaftni ghadi mkabri b Tmax, Galt hada 7alali    Khayagat okhayf f3angi, vraiment kanban mericani\n Jbedt l iPhone 6 bhal chi amir Qatari   Khdit 06 bel khaf smatni hayati",

    "3andouu ziin 3ando l7mam dayro fi daro   wana l7ub w ana lghmar jabli taldaro",

    "Ma3andi zhar m3a l'amour   Zahri ana bar mano   Ma3andi 9alb y3rf yhab   Ila hab yawil mano \n yaaw Hasta Luego, la 9lieb ola kbida    Ghadi na3tiom lfuego, ghadi n3ich otra vida",

    "Dkhelti 7yati x3al fiha daw goli why why     mn lakhar\n Nti li kayna w makyna ma7sen makayna ma7sen makaynsa ma7sen ",

    "Sif seyef khaso ghi chi sriyif    Ajiw 9rbo l7dana hzo ydikoum m3ana\nFo9ach jito chkoun ana?     Qu'est-ce qui ce passe f magana? mal sa3a zerbana?\nOw owh owh     Ana 3yet ana 3yet l7fada (baraka)"
};

// Hidden flag (not named "flag")
const char *hidden_flag = "Sp0t1f1_d_jUMI4";

int main() {
    // Seed the random number generator
    srand(time(0));

    // Randomly choose between 1 and 10
    int choice = rand() % 10 + 1;

    // Print the corresponding sentence
    printf("%s\n", sentences[choice - 1]);

    // Store the hidden flag in memory (not printed)
    char buffer[50];
    strcpy(buffer, hidden_flag);

    return 0;
}