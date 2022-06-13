#include <stdio.h>

int main() {
    int a[3][3] = {{1,2,3},
                   {4,5,6},
                   {7,8,9}};
    int b[3][3] = {{2,4,6},
                   {8,10,12},
                   {14,16,18}};
    int sum = 0;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            sum += a[i][j] + b[i][j];
    printf("sum = %d\n", sum);
}