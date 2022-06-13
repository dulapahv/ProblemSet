#include <stdio.h>

int main() {
    int cases, temp, num = 0;
    scanf("%d", &cases);
    for (int i = 0; i < cases; i++) {
        scanf("%d", &temp);
        num += temp;
    }
    printf("%d", num);
}