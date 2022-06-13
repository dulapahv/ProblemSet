#include <stdio.h>
#include <string.h>

#define SIZE 21

int main() {
    char input[SIZE];
    int count[26] = {0};

    scanf("%s", input);
    for (int i = 0; i < SIZE; i++)
        count[input[i] - 'a']++;

    int max = 0;
    int index = 0;
    for (int i = 0; i < 26; i++)
        if (count[i] > max) {
            max = count[i];
            index = i;
        }

    printf("%d %c", count[index], index + 'a');
}