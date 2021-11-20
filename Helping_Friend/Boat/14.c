#include <stdio.h>

int main() {
    int h;
    scanf("%d", &h);
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < i + 1; j++) {
            if ((i + j) % 2 == 0)
                printf("0 ");
            else
                printf("1 ");
        }
        printf("\n");
    }
}