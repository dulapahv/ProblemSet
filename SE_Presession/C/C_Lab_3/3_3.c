#include <stdio.h>
#include <string.h>

/* void add_txt(char *usin)
{
    int i = strlen(usin), j = 0;
    char str[] = ".txt";

    while (str[j] != '\0')
    {
        usin[i] = str[j];
        i++;
        j++;
    }
    usin[i] = '\0';
}

int main() {
    char input[20];
    gets(input);

    add_txt(input);
    
    puts(input);
} */

void add_txt(char *usin) {
    strcat (usin, ".txt");
}

int main() {
    char input[20];
    gets(input);

    add_txt(input);

    puts(input);
}