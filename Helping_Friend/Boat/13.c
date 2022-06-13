#include <stdio.h>

int main() {
    int n = 0, count = 0;
    while (n >= 0) {
        scanf("%d", &n);
        if (n % 3 == 0)
            count++;
    }
    printf("%d", count);
}