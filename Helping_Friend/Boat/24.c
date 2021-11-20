#include <stdio.h>

int main() {
    int n, m, row, column, value, chk;
    scanf("%d", &n);
    scanf("%d", &m);
    int matrix[n][m];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            scanf("%d", &matrix[i][j]);
    scanf("%d", &value);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (matrix[i][j] == value) {
                printf("[%d,%d] ", i, j);
                chk = 1;
            }
    if (chk == 0)
        printf("Not found");
}