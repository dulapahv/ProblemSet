#include <stdio.h>

int main() {
    int h;
    scanf("%d", &h);
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < i + 1; j++)
            printf("1 ");
        for (int j = h - i - 2; j >= 0; j--)
            printf("0 ");
        printf("\n");
    }
    for (int i = 1; i < h; i++) {
        for (int j = h - i - 1; j >= 0; j--)
            printf("1 ");
        for (int j = 0; j < i; j++)
            printf("0 ");
        printf("\n");
    }
}