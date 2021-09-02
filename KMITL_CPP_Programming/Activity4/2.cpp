#include <stdio.h>

int main() {
    int c, number[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    printf("Enter a text: ");
    while (c != '\n') {
        scanf("%c", &c);
        number[c - '0']++;
    }
    printf("Digit:       0 1 2 3 4 5 6 7 8 9\n");
    printf("Occurrences: ");
    for (int i = 0; i < 10; i++) {
        printf("%d ", number[i]);
    }
}