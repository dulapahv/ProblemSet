#include <stdio.h>

int main() {
    int c, number[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    printf("Enter a text: ");
    while (c != '\n') {
        scanf("%c", &c);
        number[c - '0']++;
    }
    printf("Repeated digit(s): ");
    for (int i = 0; i < 10; i++)
        if (number[i] > 1)
            printf("%d ", i);
}