#include <stdio.h>
#include <string.h>

#define SIZE 21

int main() {
    char input[SIZE];
    fgets(input, SIZE, stdin);
    char *pos;
    if ((pos=strchr(input, '\n')) != NULL)
    *pos = '\0';

    int count = 0;
    for (int i = 0; i < sizeof(input)/sizeof(input[0]); i++) {
        if ((input[i] < 'A' || input[i] >  'Z') && (input[i] < 'a' || input[i] > 'z') && (input[i] < 0 || input[i] > 9) && input[i] != ' ') {
            input[i] = ' ';
            count++;
        }
    }

    printf("%d %s", count, input);
}