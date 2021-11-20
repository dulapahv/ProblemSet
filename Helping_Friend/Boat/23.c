#include <stdio.h>

int main() {
    int n, m, row, column, value = 0;
    scanf("%d ", &n);
    scanf("%d ", &m);
    int matrix[n][m];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            scanf("%d", &matrix[i][j]);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (matrix[i][j] > value) {
                value = matrix[i][j];
                row = i;
                column = j;
            }
        }
    printf("%d %d %d", row, column, value);
}