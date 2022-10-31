#include <stdio.h>

int main() {
    int x, y;
    scanf("%d", &x);
    scanf("%d", &y);
    int pos = y;

    for (int i = 0; i < x; i++) {
        for (int j = 0; j < x; j++, pos++) {
            if (pos == y) {
                printf("@");
                pos = 0;
            }
            else {
                printf(".");
            }
        }
        printf("\n");
    }
}