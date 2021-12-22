#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    // char buffer[255];
    // gets(buffer);
    // puts(buffer);
    // printf("%d", strlen(buffer));
    char c, index = 0, usin[255];
    while ((c = getchar()) != EOF) {
        usin[index++] = c;
    }

    puts(usin);
    printf("%d", strlen(usin));
}