#include <stdio.h>

int main()
{
    int num[10];
    for (int i = 0; i < 10; i++) {
        scanf("%d", &num[i]);
    }

    int find = num[9];

    for (int i = 0; i < 10; i++) {
        for (int j = i + 1; j < 10; j++) {
            if (num[i] > num[j]) {
                int temp = num[i];
                num[i] = num[j];
                num[j] = temp;
            }
        }
    }

    for (int i = 0; i < 10; i++) {
        if (num[i] == find) {
            printf("%d", i + 1);
            break;
        }
    }
}