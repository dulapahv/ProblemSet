#include <stdio.h>

int find_min(min, input) {
    if (input < min) {
        return input;
    }
    return min;
}

int main() {
    int num[2][2], min;

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            scanf("%d", &num[i][j]);
    
    min = num[0][0];

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            min = find_min(min, num[i][j]);
    
    printf("%d\n", min);
}