#include <stdio.h>

int main() {
    int n, m;
    scanf("%d ", &n);
    scanf("%d ", &m);
    int matrix[n][m];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            scanf("%d", &matrix[i][j]);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (matrix[i][j] != matrix[j][i]) {
                printf("Not symmetric");
                return 0;
            }
        }
    }
    printf("Symmetric");
}