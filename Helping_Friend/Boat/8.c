#include <stdio.h>
#include <string.h>

#define SIZE 21

int main() {
    char input[SIZE];
    fgets(input, SIZE, stdin);
    char *pos;
    if ((pos=strchr(input, '\n')) != NULL)
    *pos = '\0';

    char result[SIZE] = {};
    int count = 0, index = 0;
    for (int i = 0; i < strlen(input); i++) {
        if ((input[i] >= 'A' && input[i] <= 'Z') || (input[i] >= 'a' && input[i] <= 'z') || (input[i] >= '0' && input[i] <= '9') || (input[i] == ' ')) {
            result[index] = input[i];
            index++;
        }
        else
            count++;
    }

    printf("%d %s", count, result);
}