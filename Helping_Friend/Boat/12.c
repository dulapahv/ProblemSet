#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    if (n < 2)
        printf("Unable to print the sequence.");
    else {
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0)
                printf("%d ", i);
        }
        printf("\n");
        for (int i = n; i >= 1; i--) {
            if (i % 2 == 0)
                printf("%d ", i);
        }
    }
}